# Question bank

Questions organised by topic, each tied to a gap that actually exists in the repository. **Draw
from this; do not read it out.** Two or three questions at a time, following whatever the user
finds interesting.

Priority order is roughly top to bottom: the first three sections unblock work that is currently
stuck.

---

## 1. Grounding — ask these first, once

Establishes what the user actually knows first-hand, which determines how much weight to give
everything else they say.

- Have you owned, used or handled any of these products — Competitor A, Competitor B, Competitor C,
  another entrant, another entrant? Which, and for how long?
- Do you have one you can take apart, or photograph, or weigh?
- Is there a prototype or mechanism already built, or is this still on paper?
- What made you start this project? What was wrong with what you could buy?
- Are you doing this alone, or is there a team, a workshop, a supplier?
- Who is the buyer you have in mind — and is it the same person as the user?

## 2. The blocking gaps

These are stopping work right now. If the user can answer even roughly, it unblocks a phase.

**Cost — blocks TS-001, the keystone decision**
- What should this sell for? What do the competitors charge?
- What BOM cost would make the business work at, say, a thousand units?
- Is this a premium product or an affordable alternative to the German incumbents?

**Positioning — ADR-0001, blocks all requirements**
- Do you intend to sell this as something a baby *sleeps* in, or as a soothing device for when
  they are awake and watched?
- Do you know how the German competitors word this in their manuals?
- Would you put your own newborn in it unattended overnight?

**Scope of sale**
- Do you want to sell just the motor unit, like Competitor A and Competitor B do, or a complete set
  with stand and hammock?
- If just the motor: whose stands must it work on? Have you seen it fail on one?

## 3. What the benchmark does not tell us

`competitive-benchmark.md` lists these as unknown. The user may simply know.

- Do you know what kind of motor is inside any of these units? Have you heard one up close?
- What does one *sound* like? A hum, a click, a whir? Once per bounce or continuous?
- Can you hear it from the next room? Over a baby monitor?
- How far does the hammock actually move — a few centimetres, ten, more?
- How fast does it bounce? Can you tap the rhythm?
- Competitor C advertises a "self-learning" motor. Any idea what it actually does?
- What does a spring pack cost, and where would you buy springs like that?

## 4. The motion itself

The core of the product, and where the user's physical intuition is worth more than any datasheet.

- When you rock a baby by hand, what are you actually doing — pushing at the bottom, lifting,
  something else?
- Does the motion need to be perfectly regular, or does slight irregularity soothe better?
- Should it stop by itself once the baby is asleep, or run all night?
- Should intensity change over a session — start stronger, ease off?
- Does a newborn need different motion from a one-year-old? How?
- What would tell you the motion is wrong — too much, too little, wrong rhythm?

## 5. Safety — ask directly, and listen for stories

The repository's hazard analysis is a Phase 0 seed. The user may know real failure modes.

- What is the worst thing you can imagine going wrong with this?
- Have you heard of one failing? Dropping? Making a noise it should not?
- What would you want it to do if a spring broke at three in the morning?
- Should it restart by itself after a power cut, or stay off until someone touches it?
  *(This is genuinely open — SAF-008.)*
- Where would a baby's fingers go if they explored the unit?
- How does the power cable run? Could it ever form a loop a baby could reach?
- What would make you personally distrust one of these?

## 6. The parent's experience

Feeds user needs, personas and the interface design.

- Walk me through 3 a.m. What exactly does the parent do?
- What do they touch, and can they find it without light?
- What should it look like from the bed — any light at all, or none?
- What happens when they lift the baby out?
- What would make a tired parent give up and rock by hand instead?
- What would make them recommend it to a friend?
- What would make them return it in the first week?

## 7. Installation and compatibility

Feeds the interface control document, which is where this project is most exposed.

- Where do people actually hang these — ceiling hook, stand, door frame?
- How do they decide their ceiling can take it? Do they get that wrong?
- What is the first-time setup like? What goes wrong?
- Have you seen a stand that wobbles or bounces on its own?
  *(Competitor A publishes a compatibility warning about exactly this.)*
- If someone's stand were unsuitable, how would you want them to find out — a label, or the unit
  refusing to run?

## 8. Manufacturing and business

Usually later, but cheap to ask and it constrains everything.

- Where would this be made? Do you have a manufacturer in mind?
- How many in the first year?
- Which countries first?
- Is there anything you *want* to be proud of in it — materials, repairability, longevity?
- What would you never compromise on?

## 9. Idea generation

When the interview shifts from extraction to invention.

- What would you add that none of the competitors have?
- If cost were no object, what would you change?
- If you had to halve the cost, what would go first?
- What is the stupidest idea you have had about this? *(Often the most productive question here.)*
- What annoys you most about the existing products?
- What have you thought about and rejected? Why?

---

## Following up

Whatever the topic, these earn their keep:

- "How do you know that?" — separates observation from assumption
- "Can you put a number on it?" — turns opinion into something testable
- "Has that actually happened?" — separates real failure modes from imagined ones
- "What would change your mind?" — finds the real uncertainty
- "Show me" — a sketch, a photo, a gesture described in words
