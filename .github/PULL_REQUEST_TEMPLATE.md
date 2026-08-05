## What and why

<!-- What changes, and what problem it solves. -->

## Requirement IDs

<!-- REQUIRED for changes to hardware/, firmware/ or mechanical/.
     A PR that implements no requirement needs an explanation of why. -->

**Implements:**
**Changes:**
**Verified by:**

## Checklist

- [ ] `python tools/check_requirements.py` passes
- [ ] `python tools/gen_traceability.py` re-run and the matrix committed with this change
- [ ] `mkdocs build --strict` passes

### If this touches requirements

- [ ] Every new requirement has a parent that resolves, and a verification method
- [ ] Every new `SAF-xxx` names the `HAZ-xxx` it mitigates
- [ ] Every new `IF-xxx` has a tolerance band
- [ ] No `TBD` in any requirement set to `approved`

### If this touches hardware, firmware or mechanical

- [ ] Every new part has a row in the part selection matrix
- [ ] No mains-side circuitry added (ADR-0002)
- [ ] No radio added (ADR-0003)
- [ ] No assumption about the stand or hammock hardcoded — it is an `IF-xxx` in the ICD
- [ ] No hardware platform assumed before the relevant ADR exists

### If this touches safety

- [ ] Hazard analysis reviewed for impact
- [ ] Independence claims are testable by injecting the fault they claim to survive
- [ ] No accepted ADR was edited (supersede instead)
