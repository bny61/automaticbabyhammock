#!/usr/bin/env python3
"""Simulate a tap-started, ECU-sustained hammock and render a plot and animation.

    ../../.venv/bin/python tap_and_sustain.py

Produces `tap-and-sustain.png` and `tap-and-sustain.gif` alongside this file.

WHAT IS MODELLED
    A damped mass-spring oscillator that a parent excites with a tap. The ECU
    detects the resulting motion, phase-locks to it, and injects a short impulse
    once per cycle at maximum velocity to hold a target amplitude set by the dial.

    This is the tap-to-start architecture described in
    brainstorming/ideas/IDEA-005-tap-to-start-user-excites-unit-sustains.md and
    the operating modes in docs/02-architecture/operating-modes.md.

WHAT IS ASSUMED, NOT MEASURED
    - Damping ratio. IF-005 is unmeasured; DAMPING_RATIO below is a guess and it
      dominates both the decay curve and the energy the actuator must supply.
    - Detection and lock time.
    - Impulse magnitude, the proportional control gain, and the actuator's impulse limit.

    The natural frequency is NOT a guess: it follows from the droop relation
    f = (1/2pi)*sqrt(g/x), derived in ../spring-mass-dynamics/static-droop-sets-frequency.md.

    This figure illustrates a hypothesis. It is not evidence. Run the experiments in
    the validation plan before treating any number here as real.
"""

from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from pathlib import Path

# --- physical parameters -----------------------------------------------------
G = 9.81
STATIC_DROOP_M = 0.22        # 22 cm - benchmark spring pack, loaded minus free
DAMPING_RATIO = 0.03         # ASSUMED - IF-005 is unmeasured

OMEGA = np.sqrt(G / STATIC_DROOP_M)          # rad/s, from the droop relation
FREQ = OMEGA / (2 * np.pi)                   # Hz
PERIOD = 1.0 / FREQ

# --- scenario ----------------------------------------------------------------
TAP_AMPLITUDE_MM = 9.0       # how hard the parent taps
TARGET_AMPLITUDE_MM = 25.0   # dial setting (~90%)
LOCK_TIME_S = 2.0            # ECU watches for this long before driving
IMPULSE_GAIN = 30.0          # impulse scales with amplitude error;
                             # high enough that steady-state droop is <1 mm
IMPULSE_DV_MAX = 0.045       # m/s, largest impulse the actuator can deliver
T_END = 22.0
DT = 0.002

# --- palette (validated: see dataviz skill, all six checks pass) -------------
C_WITH = "#2a78d6"           # categorical slot 1 - with ECU
C_WITHOUT = "#eb6834"        # categorical slot 2 - without ECU
INK = "#0b0b0b"
INK_2 = "#52514e"
INK_MUTED = "#8a8983"
SURFACE = "#fcfcfb"
GRID = "#e6e5e1"


def simulate(drive: bool):
    """Integrate the oscillator. Returns time, displacement, and pulse times."""
    n = int(T_END / DT)
    t = np.linspace(0.0, T_END, n)
    x = np.zeros(n)
    v = np.zeros(n)
    pulses: list[float] = []

    v[0] = (TAP_AMPLITUDE_MM / 1000.0) * OMEGA   # the tap: an impulse of velocity
    locked = False

    for i in range(n - 1):
        # RK4 on  x'' = -2*zeta*omega*x' - omega^2 * x
        def deriv(xx, vv):
            return vv, -2 * DAMPING_RATIO * OMEGA * vv - OMEGA**2 * xx

        k1x, k1v = deriv(x[i], v[i])
        k2x, k2v = deriv(x[i] + 0.5 * DT * k1x, v[i] + 0.5 * DT * k1v)
        k3x, k3v = deriv(x[i] + 0.5 * DT * k2x, v[i] + 0.5 * DT * k2v)
        k4x, k4v = deriv(x[i] + DT * k3x, v[i] + DT * k3v)

        x[i + 1] = x[i] + DT / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        v[i + 1] = v[i] + DT / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)

        if not drive:
            continue

        # Energy is injected at maximum velocity, i.e. as displacement crosses
        # zero going positive - the phase at which a given impulse does the most
        # work. The impulse is proportional to amplitude error, so the motor runs
        # once every cycle and merely does less work as the target is approached.
        # That matches the observed "soft whir once per bounce cycle": a fixed
        # impulse with cycle-skipping would be audibly irregular.
        crossing = x[i] <= 0.0 < x[i + 1]
        if crossing and t[i] >= LOCK_TIME_S:
            locked = True
            amplitude = np.hypot(x[i + 1], v[i + 1] / OMEGA)
            error = TARGET_AMPLITUDE_MM / 1000.0 - amplitude
            dv = float(np.clip(IMPULSE_GAIN * error, 0.0, IMPULSE_DV_MAX))
            if dv > 0.0:
                v[i + 1] += dv
                pulses.append(t[i + 1])

    return t, x * 1000.0, pulses, locked


def envelope(x_mm, t):
    """Instantaneous amplitude A = sqrt(x^2 + (v/omega)^2), from the signal itself."""
    v = np.gradient(x_mm, t)
    return np.hypot(x_mm, v / OMEGA)


def annotate_phases(ax, ymax, labels=True):
    """Shade the ECU operating modes behind the trace."""
    bands = [
        (0.0, LOCK_TIME_S, "Acquire", "#f2f1ed"),
        (LOCK_TIME_S, T_END, "Soothe", "#fcfcfb"),
    ]
    for t0, t1, label, colour in bands:
        ax.axvspan(t0, t1, color=colour, zorder=0, lw=0)
        if labels:
            ax.text((t0 + t1) / 2 if label == "Acquire" else t0 + 1.4, ymax * 0.93,
                    label, ha="center" if label == "Acquire" else "left",
                    fontsize=8, color=INK_MUTED, style="italic", zorder=5)
    ax.axvline(LOCK_TIME_S, color=INK_MUTED, lw=0.8, ls=(0, (4, 3)), zorder=2)


def make_plot(out: Path):
    t, x_on, pulses, _ = simulate(drive=True)
    _, x_off, _, _ = simulate(drive=False)

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(10, 6.4), sharex=True,
        gridspec_kw={"height_ratios": [2.0, 1.0], "hspace": 0.18},
    )
    fig.patch.set_facecolor(SURFACE)

    # --- displacement --------------------------------------------------------
    ax1.set_facecolor(SURFACE)
    annotate_phases(ax1, 32)
    ax1.axhline(0, color=GRID, lw=1, zorder=1)
    ax1.plot(t, x_off, color=C_WITHOUT, lw=1.4, alpha=0.85, zorder=3)
    ax1.plot(t, x_on, color=C_WITH, lw=1.6, zorder=4)

    ax1.scatter([0.02], [0], s=54, color=INK, zorder=8, marker="v", clip_on=False)
    ax1.annotate("parent taps", xy=(0.05, 1.5), xytext=(1.15, 20.5),
                 fontsize=9.5, color=INK, zorder=8,
                 arrowprops=dict(arrowstyle="->", color=INK_2, lw=0.9,
                                 shrinkA=2, shrinkB=2))

    if pulses:
        ax1.scatter(pulses, np.full(len(pulses), -30.8), marker="^", s=17,
                    color=C_WITH, zorder=6, clip_on=False)
        ax1.text(pulses[0] + 0.3, -27.2, "motor pulse — one per cycle, sized to the amplitude error",
                 fontsize=8.2, color=C_WITH, va="center")

    ax1.set_ylim(-32, 32)
    ax1.set_ylabel("Displacement  (mm)", fontsize=9.5, color=INK_2)
    ax1.set_title("Tap to start: the parent excites, the ECU sustains",
                  fontsize=13.5, color=INK, pad=14, loc="left", weight="medium")

    # --- amplitude envelope --------------------------------------------------
    ax2.set_facecolor(SURFACE)
    annotate_phases(ax2, 29, labels=False)
    ax2.axhline(TARGET_AMPLITUDE_MM, color=INK_MUTED, lw=0.9, ls=(0, (2, 3)), zorder=2)
    ax2.text(LOCK_TIME_S + 0.3, TARGET_AMPLITUDE_MM + 1.5, "dial setting",
             fontsize=8.4, color=INK_MUTED)

    env_on, env_off = envelope(x_on, t), envelope(x_off, t)
    ax2.plot(t, env_off, color=C_WITHOUT, lw=1.8, zorder=3)
    ax2.plot(t, env_on, color=C_WITH, lw=2.0, zorder=4)

    ax2.text(T_END - 0.4, env_on[-1] - 4.5, "with ECU — held at the setting",
             color=C_WITH, fontsize=10, ha="right", weight="medium", va="top")
    ax2.text(T_END - 0.4, 3.6, "without ECU — decays away",
             color=C_WITHOUT, fontsize=10, ha="right", weight="medium")

    ax2.set_ylim(0, 31)
    ax2.set_ylabel("Amplitude  (mm)", fontsize=9.5, color=INK_2)
    ax2.set_xlabel("Time  (s)", fontsize=9.5, color=INK_2)

    for ax in (ax1, ax2):
        ax.grid(True, color=GRID, lw=0.7, zorder=0)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
        ax.tick_params(colors=INK_2, labelsize=8.5, length=3)
        ax.set_xlim(0, T_END)

    fig.text(0.008, 0.012,
             f"Natural frequency {FREQ:.2f} Hz derived from {STATIC_DROOP_M*100:.0f} cm static droop "
             f"(f = 1/2π · √(g/x)).   "
             f"Damping ratio ζ = {DAMPING_RATIO} is ASSUMED — IF-005 is unmeasured.   "
             "Illustrates a hypothesis; not evidence.",
             fontsize=7.4, color=INK_MUTED)

    fig.savefig(out, dpi=170, bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out.name}  ({FREQ:.3f} Hz, {len(pulses)} pulses)")


def make_gif(out: Path):
    t, x_on, pulses, _ = simulate(drive=True)
    _, x_off, _, _ = simulate(drive=False)

    fps, span = 20, 16.0
    step = max(1, int((1 / fps) / DT))
    idx = np.arange(0, int(span / DT), step)

    fig, (axh, axt) = plt.subplots(
        1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1, 2.5], "wspace": 0.22})
    fig.patch.set_facecolor(SURFACE)

    # --- left: the hammock itself -------------------------------------------
    axh.set_facecolor(SURFACE)
    axh.set_xlim(-1, 1); axh.set_ylim(-48, 28); axh.axis("off")
    axh.set_title("Hammock", fontsize=10, color=INK_2, pad=8)
    axh.plot([0, 0], [24, 20], color=INK_2, lw=2)
    axh.text(0, 25.5, "suspension", ha="center", fontsize=7.5, color=INK_MUTED)
    spring, = axh.plot([], [], color=INK_2, lw=1.4, solid_joinstyle="round")
    cradle, = axh.plot([], [], color=C_WITH, lw=8, solid_capstyle="round")
    axh.axhline(-24, color=GRID, lw=1, ls=(0, (3, 3)))
    axh.text(0.94, -22.6, "rest", fontsize=7, color=INK_MUTED, ha="right")


    def spring_xy(y_top, y_bot, coils=8, width=0.19):
        """Zigzag between two heights, so the pack reads as a spring not a rod."""
        ys = np.linspace(y_top, y_bot, coils * 2 + 3)
        xs = np.zeros_like(ys)
        xs[1:-1] = np.resize([-width, width], len(ys) - 2)
        return xs, ys

    # --- right: the trace ----------------------------------------------------
    axt.set_facecolor(SURFACE)
    axt.set_xlim(0, span); axt.set_ylim(-34, 34)
    axt.axhline(0, color=GRID, lw=1)
    axt.grid(True, color=GRID, lw=0.7); axt.set_axisbelow(True)
    for side in ("top", "right"):
        axt.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        axt.spines[side].set_color(GRID)
    axt.tick_params(colors=INK_2, labelsize=8.5, length=3)
    axt.set_xlabel("Time  (s)", fontsize=9, color=INK_2)
    axt.set_ylabel("Displacement  (mm)", fontsize=9, color=INK_2)
    axt.axvline(LOCK_TIME_S, color=INK_MUTED, lw=0.8, ls=(0, (4, 3)))
    axt.text(LOCK_TIME_S + 0.2, 30, "ECU locks on", fontsize=8, color=INK_MUTED)
    line_off, = axt.plot([], [], color=C_WITHOUT, lw=1.3, alpha=0.85)
    line_on, = axt.plot([], [], color=C_WITH, lw=1.6)
    dot, = axt.plot([], [], "o", color=C_WITH, ms=5)
    axt.text(span - 0.2, -31, "without ECU", color=C_WITHOUT, fontsize=9,
             ha="right", weight="medium")
    axt.text(span - 0.2, 24.5, "with ECU", color=C_WITH, fontsize=9,
             ha="right", weight="medium")
    state = axt.text(0.2, -30.5, "", fontsize=9.5, color=INK, weight="medium")

    pulse_arr = np.array(pulses)

    def frame(k):
        i = idx[k]
        now, disp = t[i], x_on[i]
        y = -24 + disp * 0.62
        spring.set_data(*spring_xy(20, y + 3.5))
        cradle.set_data([-0.55, 0.55], [y, y])
        line_on.set_data(t[:i], x_on[:i])
        line_off.set_data(t[:i], x_off[:i])
        dot.set_data([now], [disp])
        if now < 0.15:
            state.set_text("tap")
        elif now < LOCK_TIME_S:
            state.set_text("Acquire — watching, not driving")
        else:
            recent = pulse_arr[(pulse_arr > now - 0.18) & (pulse_arr <= now)]
            state.set_text("Soothe — pulse" if len(recent) else "Soothe")
        state.set_color(C_WITH if now >= LOCK_TIME_S else INK_2)
        return spring, cradle, line_on, line_off, dot, state

    anim = FuncAnimation(fig, frame, frames=len(idx), interval=1000 / fps, blit=True)
    anim.save(out, writer=PillowWriter(fps=fps), dpi=78,
              savefig_kwargs={"facecolor": SURFACE})
    plt.close(fig)
    print(f"wrote {out.name}  ({len(idx)} frames at {fps} fps)")


if __name__ == "__main__":
    here = Path(__file__).parent
    print(f"f = {FREQ:.3f} Hz   period {PERIOD:.3f} s   droop {STATIC_DROOP_M*100:.0f} cm   zeta {DAMPING_RATIO}")
    make_plot(here / "tap-and-sustain.png")
    make_gif(here / "tap-and-sustain.gif")
