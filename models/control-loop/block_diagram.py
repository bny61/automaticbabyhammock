#!/usr/bin/env python3
"""Render a Simulink-style signal-flow diagram of the tap-and-sustain loop.

    ../../.venv/bin/python block_diagram.py

Produces `control-loop-block-diagram.png` alongside this file.

WHAT THIS DIAGRAM IS
    The block-by-block form of exactly what `tap_and_sustain.py` integrates:
    a damped mass-spring plant as a chain of two integrators with velocity and
    position feedback, and an ECU path that estimates amplitude, compares it to
    the dial setpoint, and injects one velocity impulse per cycle at the zero
    crossing. Every gain and limit shown is read from that script, not retyped.

WHAT IS NOT DECIDED
    Blocks drawn with a dashed amber border are placeholders for decisions the
    project has not made: how motion is sensed (TS-004), how the impulse is
    produced (TS-001, TS-003) and whether tap-to-start is adopted at all
    (OP-021). They are drawn because the loop cannot be explained without a box
    in those positions - not because a choice has been made.

    The diagram illustrates a hypothesis. It is not evidence.
"""

from __future__ import annotations

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon
from pathlib import Path

# Parameters are imported so the drawing cannot drift from the simulation.
from tap_and_sustain import (
    DAMPING_RATIO,
    FREQ,
    IMPULSE_DV_MAX,
    IMPULSE_GAIN,
    LOCK_TIME_S,
    STATIC_DROOP_M,
    TARGET_AMPLITUDE_MM,
    C_WITH,
    C_WITHOUT,
    INK,
    INK_2,
    INK_MUTED,
    SURFACE,
    GRID,
)

PLANT = INK_2          # decided physics
ECU = C_WITH           # the control path
OPEN = C_WITHOUT       # not yet decided


# --- drawing primitives ------------------------------------------------------

def box(ax, cx, cy, w, h, lines, *, colour=PLANT, dashed=False, fs=8.6, weight=None):
    """A block. `lines` is a list of (text, fontsize-delta, italic) or plain strings."""
    ax.add_patch(FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0,rounding_size=0.9",
        linewidth=1.4, edgecolor=colour, facecolor=SURFACE,
        linestyle=(0, (4, 2.5)) if dashed else "solid", zorder=4))
    n = len(lines)
    for i, entry in enumerate(lines):
        text, dfs, italic = entry if isinstance(entry, tuple) else (entry, 0, False)
        y = cy + (n - 1) * 1.55 / 2 - i * 1.55
        ax.text(cx, y, text, ha="center", va="center", zorder=5,
                fontsize=fs + dfs, color=colour if i == 0 else INK_MUTED,
                style="italic" if italic else "normal",
                weight=weight if i == 0 else None)


def summing(ax, cx, cy, signs, *, colour=PLANT, r=2.4):
    """A summing junction. `signs` maps 'l','r','t','b' to '+' or '-'."""
    ax.add_patch(Circle((cx, cy), r, linewidth=1.4, edgecolor=colour,
                        facecolor=SURFACE, zorder=4))
    off = r + 1.9
    place = {"l": (cx - off, cy + 1.6), "r": (cx + off, cy + 1.6),
             "t": (cx - 1.9, cy + off), "b": (cx - 1.9, cy - off)}
    for port, sign in signs.items():
        x, y = place[port]
        ax.text(x, y, sign, ha="center", va="center", fontsize=10,
                color=colour, zorder=6)


def gain(ax, cx, cy, label, *, colour=PLANT, w=6.0, h=6.4, facing="left"):
    """A gain triangle, apex pointing in the direction of signal flow."""
    s = -1 if facing == "left" else 1
    pts = [(cx - s * w / 2, cy + h / 2), (cx - s * w / 2, cy - h / 2), (cx + s * w / 2, cy)]
    ax.add_patch(Polygon(pts, closed=True, linewidth=1.4, edgecolor=colour,
                         facecolor=SURFACE, zorder=4))
    ax.text(cx - s * w * 0.12, cy, label, ha="center", va="center",
            fontsize=8.4, color=colour, zorder=5)


def arrow(ax, p0, p1, *, colour=PLANT, dashed=False, lw=1.3):
    ax.annotate("", xy=p1, xytext=p0, zorder=3, annotation_clip=False,
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=11,
                                linestyle=(0, (4, 2.5)) if dashed else "solid"))


def hline(ax, y, x0, x1, *, colour=PLANT, hops=(), lw=1.3, r=1.15):
    """Horizontal wire with semicircular hops over the crossings in `hops`."""
    hops = sorted(h for h in hops if min(x0, x1) + r < h < max(x0, x1) - r)
    cursor = x0
    step = 1 if x1 > x0 else -1
    for h in hops if step > 0 else reversed(hops):
        ax.plot([cursor, h - step * r], [y, y], color=colour, lw=lw, zorder=3,
                solid_capstyle="butt")
        th = np.linspace(np.pi, 0, 40) if step > 0 else np.linspace(0, np.pi, 40)
        ax.plot(h + r * np.cos(th), y + r * np.sin(th), color=colour, lw=lw, zorder=3)
        cursor = h + step * r
    ax.plot([cursor, x1], [y, y], color=colour, lw=lw, zorder=3, solid_capstyle="butt")


def vline(ax, x, y0, y1, *, colour=PLANT, lw=1.3):
    ax.plot([x, x], [y0, y1], color=colour, lw=lw, zorder=3, solid_capstyle="butt")


def label(ax, x, y, text, *, colour=INK_MUTED, fs=8.2, ha="center", va="center",
          italic=False):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs, color=colour, zorder=6,
            style="italic" if italic else "normal")


def dot(ax, x, y, *, colour=PLANT):
    ax.add_patch(Circle((x, y), 0.65, facecolor=colour, edgecolor="none", zorder=6))


# --- the diagram -------------------------------------------------------------

def draw(out: Path):
    fig, ax = plt.subplots(figsize=(13.0, 10.6))
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0, 100)
    ax.set_ylim(7, 90)
    ax.set_aspect("equal")
    ax.axis("off")

    # geometry
    Y_TAP, Y_PLANT, Y_RET = 79.0, 70.0, 62.0
    Y_VFB, Y_PFB = 54.0, 48.0
    Y_ECU, Y_TRIG = 38.0, 16.0
    X_SA, X_SV, X_NODE = 20.0, 48.0, 78.0
    X_VPICK, X_PRET, X_SATRET, X_ZC = 44.5, 13.0, 6.0, 86.0

    # ---------------------------------------------------------------- title
    ax.text(0, 89.0, "Tap and sustain — signal-flow form of the loop in "
            "tap_and_sustain.py", fontsize=14.5, color=INK, weight="medium",
            ha="left", va="top")
    ax.text(0, 86.4, "The parent injects the energy. The ECU only replaces what "
            "damping removes.", fontsize=10, color=INK_MUTED, ha="left", va="top")

    # ---------------------------------------------------------------- plant
    label(ax, 99, 85.0, "PLANT — hammock, spring pack, infant", colour=INK_MUTED,
          fs=8.6, ha="right")
    label(ax, 99, 82.4, "properties assumed via IF-xxx; ζ is unmeasured (IF-005)",
          colour=INK_MUTED, fs=7.8, ha="right", italic=True)

    box(ax, X_TAP := 48.0, Y_TAP, 34, 8,
        [("Parent's tap", 0.6, False),
         "impulse into velocity   v₀ = A_tap · ω",
         "the only source of start-up energy"], colour=INK, weight="medium")
    arrow(ax, (X_TAP, Y_TAP - 4), (X_SV, Y_PLANT + 2.4), colour=INK)

    summing(ax, X_SA, Y_PLANT, {"l": "−", "b": "−"})
    box(ax, 33, Y_PLANT, 14, 7, [("1/s", 3.0, False), "integrate"])
    summing(ax, X_SV, Y_PLANT, {"t": "+", "b": "+"})
    box(ax, 61, Y_PLANT, 14, 7, [("1/s", 3.0, False), "integrate"])

    arrow(ax, (X_SA + 2.4, Y_PLANT), (26, Y_PLANT))
    label(ax, 24.2, Y_PLANT + 2.2, "ẍ", fs=9.5, colour=PLANT)
    arrow(ax, (40, Y_PLANT), (X_SV - 2.4, Y_PLANT))
    label(ax, 41.6, Y_PLANT + 2.2, "ẋ", fs=9.5, colour=PLANT)
    arrow(ax, (X_SV + 2.4, Y_PLANT), (54, Y_PLANT))
    arrow(ax, (68, Y_PLANT), (95, Y_PLANT))
    label(ax, 71.5, Y_PLANT + 2.0, "x", fs=9.5, colour=PLANT)
    label(ax, 95, Y_PLANT - 3.0, "displacement x(t)\nthe blue trace", fs=8.2,
          ha="right")
    dot(ax, X_NODE, Y_PLANT)
    dot(ax, X_VPICK, Y_PLANT)

    # velocity feedback  −2ζω
    vline(ax, X_VPICK, Y_PLANT, Y_VFB)
    hline(ax, Y_VFB, X_VPICK, 33)
    gain(ax, 30, Y_VFB, f"−2ζω", colour=PLANT)
    hline(ax, Y_VFB, 27, X_SA)
    arrow(ax, (X_SA, Y_VFB), (X_SA, Y_PLANT - 2.4))
    label(ax, 33.5, Y_VFB - 3.4, f"damping   ζ = {DAMPING_RATIO}  (assumed)", fs=7.6)

    # position feedback  −ω²
    vline(ax, X_NODE, Y_PLANT, Y_PFB)
    hline(ax, Y_PFB, X_NODE, 49)
    gain(ax, 46, Y_PFB, "−ω²", colour=PLANT)
    hline(ax, Y_PFB, 43, X_PRET)
    vline(ax, X_PRET, Y_PFB, Y_PLANT)
    arrow(ax, (X_PRET, Y_PLANT), (X_SA - 2.4, Y_PLANT))
    label(ax, 44, Y_PFB - 3.4, f"stiffness   ω = √(g/x_droop) → f = {FREQ:.2f} Hz "
          f"from {STATIC_DROOP_M * 100:.0f} cm droop  (derived)", fs=7.6)

    # ---------------------------------------------------------- ECU boundary
    ax.add_patch(FancyBboxPatch(
        (2.0, 9.5), 90.0, 34.0, boxstyle="round,pad=0,rounding_size=1.4",
        linewidth=1.1, edgecolor=GRID, facecolor="#f7f7f5",
        linestyle=(0, (6, 4)), zorder=1))
    label(ax, 4.0, 12.0, "ECU — in scope", colour=INK_MUTED, fs=8.6, ha="left")

    # sensing → amplitude → error → gain → saturate
    vline(ax, X_NODE, Y_PFB, Y_ECU + 4.5, colour=ECU)
    arrow(ax, (X_NODE, Y_ECU + 6.0), (X_NODE, Y_ECU + 4.5), colour=ECU)
    box(ax, 79, Y_ECU, 22, 9,
        [("Motion sensing", 0.4, False), "method undecided", "TS-004"],
        colour=OPEN, dashed=True, weight="medium")
    box(ax, 54, Y_ECU, 22, 9,
        [("Amplitude estimate", 0.4, False), "A = √(x² + (ẋ/ω)²)"],
        colour=ECU, weight="medium")
    arrow(ax, (68, Y_ECU), (65, Y_ECU), colour=ECU)
    hline(ax, Y_ECU, 68, 65.4, colour=ECU)

    summing(ax, 34, Y_ECU, {"r": "−", "b": "+"}, colour=ECU)
    arrow(ax, (43, Y_ECU), (36.4, Y_ECU), colour=ECU)
    box(ax, 34, 26, 26, 8,
        [("Dial setpoint", 0.4, False), f"A_target = {TARGET_AMPLITUDE_MM:.0f} mm",
         "the user's only control"], colour=ECU, weight="medium")
    arrow(ax, (34, 30), (34, Y_ECU - 2.4), colour=ECU)

    gain(ax, 24, Y_ECU, f"K = {IMPULSE_GAIN:.0f}", colour=ECU)
    arrow(ax, (31.6, Y_ECU), (27.2, Y_ECU), colour=ECU)
    label(ax, 29.5, Y_ECU + 4.4, "error", fs=7.8, colour=ECU)
    box(ax, 11, Y_ECU, 13, 9,
        [("Saturate", 0.4, False), "0 … Δv_max", f"{IMPULSE_DV_MAX} m/s"],
        colour=ECU, weight="medium")
    arrow(ax, (21, Y_ECU), (17.6, Y_ECU), colour=ECU)

    # trigger path
    box(ax, 79, Y_TRIG, 22, 9,
        [("Zero-cross detect", 0.4, False), "x : − → +", "peak velocity — most work"],
        colour=ECU, weight="medium")
    vline(ax, X_ZC, Y_ECU - 4.5, Y_TRIG + 4.5, colour=ECU)
    arrow(ax, (X_ZC, Y_TRIG + 6.0), (X_ZC, Y_TRIG + 4.5), colour=ECU)
    box(ax, 50, Y_TRIG, 24, 9,
        [("Mode gate", 0.4, False), f"Acquire {LOCK_TIME_S:.0f} s, then Soothe",
         "adoption undecided — OP-021"], colour=OPEN, dashed=True, weight="medium")
    arrow(ax, (68, Y_TRIG), (62.2, Y_TRIG), colour=ECU)
    hline(ax, Y_TRIG, 38, 11, colour=ECU, lw=1.1)
    arrow(ax, (11, Y_TRIG), (11, Y_ECU - 4.5), colour=ECU, dashed=True, lw=1.1)
    label(ax, 15.5, 26, "enable\none pulse\nper cycle", fs=7.6, colour=ECU)

    # ------------------------------------------------- impulse back to plant
    hline(ax, Y_ECU, 4.5, X_SATRET, colour=ECU)
    vline(ax, X_SATRET, Y_ECU, Y_RET, colour=ECU)
    hline(ax, Y_RET, X_SATRET, 21, colour=ECU, hops=(X_PRET, X_SA))
    box(ax, 30, Y_RET, 18, 6,
        [("Actuator", 0.4, False), "undecided — TS-001/003"],
        colour=OPEN, dashed=True, fs=7.8, weight="medium")
    hline(ax, Y_RET, 39, X_SV, colour=ECU, hops=(X_VPICK,))
    arrow(ax, (X_SV, Y_RET), (X_SV, Y_PLANT - 2.4), colour=ECU)
    label(ax, 52.4, 66.0, "Δv", fs=8.6, colour=ECU, ha="left")

    # ---------------------------------------------------------------- legend
    ax.add_patch(FancyBboxPatch((57.0, 21.0), 26.0, 11.0,
                                boxstyle="round,pad=0,rounding_size=1.0",
                                linewidth=1.0, edgecolor=GRID,
                                facecolor=SURFACE, zorder=4))
    for dy, colour, ls, text in (
            (8.2, PLANT, "solid", "plant — physics, derived"),
            (5.0, ECU, "solid", "ECU control path"),
            (1.8, OPEN, (0, (4, 2.5)), "not yet decided")):
        ax.plot([59.5, 64.5], [21 + dy, 21 + dy], color=colour, lw=1.4, ls=ls, zorder=5)
        label(ax, 66, 21 + dy, text, ha="left", fs=8.0, colour=INK_2)

    # ---------------------------------------------------------------- footer
    fig.text(0.012, 0.018,
             "Gains, limits and frequencies are imported from tap_and_sustain.py — "
             "this drawing cannot drift from the simulation.   "
             f"ζ = {DAMPING_RATIO} is ASSUMED (IF-005 unmeasured); it sets both the decay "
             "window and the actuator energy.\n"
             "Three blocks are placeholders for open decisions, not choices: sensing "
             "(TS-004), actuation (TS-001, TS-003), tap-to-start itself (OP-021).   "
             "Illustrates a hypothesis; not evidence.",
             fontsize=7.6, color=INK_MUTED, linespacing=1.6)

    fig.savefig(out, dpi=170, bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out.name}")


if __name__ == "__main__":
    draw(Path(__file__).parent / "control-loop-block-diagram.png")
