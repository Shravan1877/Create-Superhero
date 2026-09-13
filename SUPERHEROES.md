# SUPERHEROES.md — Framework & Canonical Hero Dataset

> Companion to `CLAUDE.md`. That file owns the *system*; this file owns the
> *framework* and the *data*. Ratings here are the calibration reference for the
> whole game — if these are wrong, every player score is wrong.

---

# PART I — THE FRAMEWORK

## 1. Scale philosophy

Every axis is **0–100** and the scale is **roster-relative**, not absolute-conceivable.

> **100 = the best in this roster. Not "the strongest thing imaginable."**

Rationale: on an absolute cosmic scale every human lands between 5 and 15 and the
entire table collapses into noise. Roster-relative keeps the spread usable.

**Anchors are fixed before any hero is rated.** Every other rating is placed
*relative to the anchors*, never judged in a vacuum. This is the single biggest
defence against "why is Falcon a 40, that's random" arguments at the event.

### 1.1 Master anchors

| Axis | 100 | ~50 | ~10 |
|---|---|---|---|
| Raw Power | Hulk | Captain America | Untrained adult |
| Durability | Hulk | Scarlet Witch | Untrained adult |
| Speed & Agility | Quicksilver | Falcon | Untrained adult |
| Mobility & Flight | Iron Man / Vision | Quicksilver | Any ground-only human |
| Ranged Projection | War Machine | Hawkeye | Sidearm |
| Crowd Clearing | Thor | Captain America | Single-target fighter |
| Stamina | Vision | Iron Man | Untrained adult |
| Exotic Survivability | Vision | — | Unprotected human |
| Tactical Intelligence | Captain America | Black Widow (85) / Ant-Man (45) | Hulk (15) |
| Technical Intelligence | Iron Man | Black Widow | Quicksilver (25) |
| Leadership | Captain America | Black Widow | Hulk (8) |
| Improvisation | Iron Man | Vision | Hulk (35) |

---

## 2. Block A — Physical & Combat (8 axes)

All Block A axes use **optimum = 100** (more is genuinely better).

| # | Axis | Definition | Weight |
|---|---|---|---|
| A1 | **Raw Power** | Peak force delivered in a single strike | 7 |
| A2 | **Durability** | Damage absorbed before being taken out | 8 |
| A3 | **Speed & Agility** | Reaction time, evasion, close-quarters movement | 6 |
| A4 | **Mobility & Flight** | Independent battlefield traversal and altitude | 10 |
| A5 | **Ranged Projection** | Damage delivered at distance | 6 |
| A6 | **Crowd Clearing** | Targets neutralised **per action** — one-to-many | 10 |
| A7 | **Stamina** | Sustained output over a multi-hour engagement | 7 |
| A8 | **Exotic Survivability** | Vacuum, radiation, extreme cold, no oxygen | 9 |

**Two deliberate separations:**

- **Crowd Clearing is not Raw Power.** Hulk hits hardest; Thor clears more. Against
  an army with infinite reinforcement, the second matters more than the first.
- **Exotic Survivability is its own axis.** The mothership run means leaving
  atmosphere. Most heroes simply cannot.

---

## 3. Block B — Mind & Command (4 axes)

All Block B axes use **optimum = 100**.

| # | Axis | Definition | Weight |
|---|---|---|---|
| B1 | **Tactical Intelligence** | Reading a live battlefield, allocating force | 8 |
| B2 | **Technical Intelligence** | Analysis, engineering, deducing *how a thing works* | 10 |
| B3 | **Leadership** | Force multiplication — how much better everyone else gets | 6 |
| B4 | **Improvisation** | Effectiveness once the plan is already dead | 7 |

**Technical Intelligence carries the heaviest Block B weight** because the hive-mind
weakness had to be *discovered*, not punched. The Avengers won partly by luck.

---

## 4. Block C — Personality (10 axes)

**Polarity is expressed as a number, never a category.** Every trait scores through
the same formula as Blocks A and B — see `CLAUDE.md` §4.2.

| # | Trait | Definition | Optimum | Weight |
|---|---|---|---|---|
| C1 | **Emotional Resilience** | Recovery from loss and trauma | 100 | 8 |
| C2 | **Emotional Intelligence** | Reading and handling other people | 100 | 5 |
| C3 | **Capacity for Attachment** | Depth of love and bonds | **70** | 6 |
| C4 | **Self-Sacrifice Drive** | Willingness to pay the final cost | **75** | 10 |
| C5 | **Impulse Control** | Restraint under provocation | **90** | 7 |
| C6 | **Guilt Burden** | Weight of the past carried into the present | **15** | 4 |
| C7 | **Trust & Openness** | Letting others in | **65** | 6 |
| C8 | **Moral Rigidity** | Unwillingness to bend the rules | **55** | 5 |
| C9 | **Ego & Need for Validation** | Need to be seen winning | **25** | 4 |
| C10 | **Courage Under Terror** | Functioning while genuinely afraid | 100 | 10 |

### 4.1 Why the non-100 optimums are what they are

Each is derived from the Chitauri mission, not chosen aesthetically.

| Trait | Optimum | Reasoning |
|---|---|---|
| Self-Sacrifice | **75** | The mothership run is one-way, so you need this high. But 100 means throwing your life away on turn one against infantry that don't matter. |
| Courage Under Terror | **100**, weight 10 | Flying a nuke into an unknown portal is the hardest single ask in the mission. |
| Moral Rigidity | **55** | You must be willing to make the ugly call. Someone who won't nuke *anything* loses. |
| Ego | **25**, not 0 | Zero self-belief never attempts the impossible shot either. |
| Impulse Control | **90**, not 100 | Total restraint never unleashes when unleashing is correct. |
| Capacity for Attachment | **70** | Motivation — but at 95+ it is a hostage-shaped hole in your defence. |
| Trust & Openness | **65** | Below 30 = zero team synergy. Above 85 = trivially manipulated (Loki's whole method). |
| Guilt Burden | **15** | Some accountability is function. Heavy guilt is hesitation at the wrong moment. |

---

## 5. Vulnerability schema

Vulnerabilities are **not** scalar axes. Separate structure, **max 3 per hero**.

| Field | Values |
|---|---|
| `name` | Free text |
| `type` | Physical / Psychological / Dependency / Situational |
| `severity` | 0–100 — how bad when it triggers |
| `exploitability` | 0–100 — how easily an enemy can *cause* it |

**Two numbers, not one**, because *"catastrophic but nearly impossible to trigger"*
and *"mild but trivially triggered"* are completely different risks.
Threat weight = `severity × exploitability`.

---

## 6. Interrogation protocol

Before any hero is rated, these six questions must be answered. **Ratings written
without this step are invalid.** This is what stops "Thor feels strong, give him 90."

1. **What is the source of the power?** Innate, tech, chemical, mystical, trained?
   → Determines whether it can be *removed*, which drives Dependency vulnerabilities.
2. **What is the hardest on-screen feat, and the most embarrassing failure?**
   → Brackets the true range instead of rating the highlight reel.
3. **Does the power scale with numbers, or only against one target?**
   → Separates Crowd Clearing from Raw Power.
4. **What happens when the equipment/substance/emotion is taken away?**
   → Reveals the real floor.
5. **Is the intellect available at the same time as the strength?**
   → Critical for Banner/Hulk. A genius who can't think while fighting scores differently.
6. **What has actually broken this character on screen — psychologically?**
   → Personality ratings must come from depicted failure, not vibes.

---

# PART II — THE ROSTER

17 heroes across *The Avengers* (2012), *Age of Ultron* (2015), and *Civil War* (2016).
Ratings reflect each character **as of Civil War** — their most developed state
within scope.

---

## AVENGERS (2012) — The founding six + Fury

### 1. Iron Man — Tony Stark

**Interrogation**
- *Source:* Entirely tech. Removable, and that is the whole point of him.
- *Best feat:* Flew a nuclear missile through the portal and destroyed the command
  ship. He is the literal solution to this exact scenario.
- *Worst failure:* Blacked out and fell back through the portal. He did not survive
  it on merit — Hulk caught him.
- *Scaling:* Repulsors are one-to-few. Crowd clearing is good, not elite.
- *Without the suit:* Baseline human. Total dependency.
- *Intellect during combat:* Yes — full access. This is his decisive advantage.
- *What breaks him:* Panic attacks, PTSD from the portal, obsessive need to be
  the one who fixes it.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Total suit dependency | Dependency | 95 | 45 |
| Post-portal panic/PTSD | Psychological | 70 | 60 |
| Compulsive need for control | Psychological | 60 | 70 |

---

### 2. Captain America — Steve Rogers

**Interrogation**
- *Source:* Serum (permanent) + shield (removable) + genuine tactical training.
- *Best feat:* The New York command sequence — assigning every Avenger their role
  and multiplying the whole team. This is the canonical Leadership 100.
- *Worst failure:* Cannot fly, cannot reach the portal, cannot clear crowds fast.
  Against an army he is a *bottleneck holder*, not a war-winner.
- *Scaling:* One-to-few. He holds ground; he does not sweep it.
- *Intellect:* Tactical, not technical. He would never deduce the hive link.
- *What breaks him:* Bucky. The entire Civil War plot is Steve's attachment
  overriding his judgement.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Loyalty to Barnes overrides judgement | Psychological | 85 | 75 |
| No flight / no altitude | Physical | 80 | 90 |
| Inflexible moral code | Psychological | 55 | 50 |

---

### 3. Thor

**Interrogation**
- *Source:* Innate Asgardian physiology + Mjolnir. Partially removable.
- *Best feat:* Parked on the Chrysler Building and channelled lightning into the
  portal, killing many Chitauri at once and turning Leviathans back. **This is the
  single best crowd-clearing feat in the film — hence Crowd Clearing = 100.**
- *Worst failure:* Could not solve anything. Every problem got a hammer.
- *Scaling:* Lightning is genuinely one-to-many. Exceptional here.
- *Intellect:* Low technical. Would never find the keystone weakness alone.
- *What breaks him:* Ego, and Loki. He is consistently manipulated by family.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Manipulable via Loki/family | Psychological | 70 | 65 |
| Mjolnir dependency (this era) | Dependency | 60 | 40 |
| Arrogance → tactical blindness | Psychological | 55 | 60 |

---

### 4. Hulk / Bruce Banner

**Interrogation**
- *Source:* Gamma accident. Not removable — but also not reliably *summonable*.
- *Best feat:* Killed a Leviathan with a single punch. Highest Raw Power in scope.
- *Worst failure:* Scarlet Witch put him into full berserker mode and turned him
  into a weapon against his own side. He is *hijackable*.
- *Scaling:* Good crowd clearing by sheer area of destruction, but indiscriminate.
- **Q5 is decisive here:** Banner's intellect is ~95, but **it is not available
  while Hulk is out.** Rated at 90 with an explicit vulnerability capturing the
  trade-off. This is exactly why Q5 exists in the protocol.
- *What breaks him:* Fear of himself. Guilt. Zero impulse control in Hulk form.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Intellect unavailable while transformed | Situational | 90 | 80 |
| Susceptible to mental manipulation | Psychological | 95 | 55 |
| Cannot distinguish friend from foe in rage | Psychological | 85 | 70 |

---

### 5. Black Widow — Natasha Romanoff

**Interrogation**
- *Source:* Pure training. Nothing removable, nothing enhanced.
- *Best feat:* Closed the portal. Also the only one who reliably manages other
  people's psychology — including talking Banner down.
- *Worst failure:* Physically outclassed by literally every enhanced combatant.
- *Scaling:* Strictly one-to-one.
- *Intellect:* High tactical, moderate technical.
- *What breaks her:* The ledger. Guilt is her defining internal conflict.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Baseline human durability | Physical | 90 | 85 |
| Guilt over past ("red in my ledger") | Psychological | 65 | 55 |
| Compartmentalised, struggles to trust | Psychological | 50 | 40 |

---

### 6. Hawkeye — Clint Barton

**Interrogation**
- *Source:* Training + equipment. Fully removable.
- *Best feat:* Overwatch — calling out patterns and strays from elevation. His real
  contribution is *information*, not damage. Also: **he is the only one who resisted
  Wanda's mental attack.**
- *Worst failure:* Mind-controlled by Loki's sceptre for most of the first film.
- *Scaling:* One arrow, one target. Worst crowd clearing among the six.
- *What breaks him:* His family. It is his anchor and his exposure.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Baseline human durability | Physical | 88 | 85 |
| Finite ammunition | Dependency | 70 | 60 |
| Family as leverage | Psychological | 75 | 45 |

---

### 7. Nick Fury

**Interrogation**
- *Source:* Position, information, and nerve. No powers at all.
- *Why include him:* He is the **calibration anchor proving Leadership and Tactical
  can be elite while physical stats are near-baseline.** Without him the table looks
  like "strong = good at everything."
- *Best feat:* Assembled the team; manipulated them into cohesion.
- *What breaks him:* Nothing emotional. He is the roster's low outlier on Trust (10)
  and on Capacity for Attachment (25).

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Baseline human, no combat enhancement | Physical | 92 | 88 |
| Trusts no one — poor team synergy | Psychological | 55 | 30 |
| Authority depends on institution | Dependency | 60 | 50 |

---

## AGE OF ULTRON (2015) — Five additions

### 8. Vision

**Interrogation**
- *Source:* Vibranium synthezoid body + Mind Stone. Not removable by conventional means.
- *Best feat:* **Density manipulation → phasing.** He can lower density to fly, or
  increase it mid-phase to destroy an object from the inside. He tore apart Ultron
  sentries and phased his fingers through Ultron's vibranium shell.
- *Why this matters enormously here:* phasing is the *ideal* Leviathan counter.
  Stark had to fly inside one to kill it. Vision can simply phase in and re-densify.
- *Worst failure:* Corvus Glaive's weapon negated his phasing, and Wanda could
  manipulate the Mind Stone to control his density **against his will.**
- *Intellect:* Processes enormous data volumes. Second only to Stark, arguably equal.
- *What breaks him:* Literal-mindedness. He is the roster's Improvisation outlier
  (45) despite being near-genius — rules-bound, not creative.

> **Vision is the strongest mothership-run candidate in the entire roster.**
> Flight, vacuum tolerance, technical intelligence, and a hard counter to Leviathans.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Mind Stone can be externally manipulated | Physical | 95 | 35 |
| Rigid, literal thinking | Psychological | 50 | 55 |
| Emotionally naive — new to existence | Psychological | 45 | 50 |

---

### 9. Scarlet Witch — Wanda Maximoff

**Interrogation**
- *Source:* Mind Stone exposure via HYDRA experimentation. Innate, not removable.
- *Best feat:* Neuro-electric interfacing — she read minds, inflicted waking
  nightmares on Thor, Cap and Widow, forced Banner into berserker mode, and
  overrode the Mind Stone's control over Dr. Cho. She is the only character who can
  *disable* opponents without touching them.
- **Critical limitation for this mission:** the Chitauri are a **hive mind of
  cybernetic drones with no fear and no morale.** Her single best weapon —
  psychological manipulation — is *nearly useless against them.* This is the most
  interesting hero/enemy mismatch in the roster and should be preserved in scoring.
- *Worst failure:* Froze completely during the first Sokovia engagement.
- *Notable:* when Pietro died she unleashed a massive power surge — a direct link
  between her emotional state and her output. Attachment is fuel *and* liability.
- *What breaks her:* Grief, guilt, lack of control.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Mental powers useless vs. hive-mind drones | Situational | 85 | 90 |
| Emotional state destabilises output | Psychological | 80 | 70 |
| Freezes under first contact | Psychological | 70 | 60 |

---

### 10. Quicksilver — Pietro Maximoff

**Interrogation**
- *Source:* Mind Stone exposure. Innate.
- *Best feat:* Speed sufficient to evacuate civilians and intercept fire.
- *Worst failure:* **Died to conventional gunfire.** The ceiling on his durability is
  brutally established — speed is not protection once you commit to a stationary act.
- *Scaling:* Speed gives moderate crowd clearing, but ground-only. He cannot reach
  a portal in the sky. Hard fail on the mission's first gate.
- *What breaks him:* Wanda. Total attachment (95), and it is what kills him.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Durability does not scale with speed | Physical | 95 | 80 |
| Ground-bound — cannot gain altitude | Physical | 85 | 90 |
| Recklessness / no impulse control | Psychological | 70 | 65 |

---

### 11. War Machine — James Rhodes

**Interrogation**
- *Source:* Tech, same platform as Stark but military-spec.
- *Distinction from Iron Man:* **heavier ordnance, better pilot, lower innovation.**
  Rhodes gets the roster's Ranged Projection 100 anchor. He does not get Stark's
  Technical Intelligence or Improvisation.
- *Worst failure:* Shot down by friendly fire in Civil War — armour does not make
  you unhittable.
- *Intellect:* MIT-trained engineer, genuinely capable — but an operator, not an inventor.
- *What breaks him:* Institutional loyalty. He follows orders past the point of doubt.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Total suit dependency | Dependency | 95 | 45 |
| Defers to chain of command | Psychological | 60 | 65 |
| Less adaptive than Stark's platform | Situational | 45 | 50 |

---

### 12. Falcon — Sam Wilson

**Interrogation**
- *Source:* EXO-7 wingsuit. Fully removable — and the Winter Soldier literally
  ripped it apart.
- *Best feat:* Aerial recon and Redwing. He is an *enabler*, not a heavy hitter.
- *Worst failure:* Ant-Man beat him at normal size using a suit Scott had barely
  trained with.
- *Ceiling:* Glide plus limited jets. He is mobile, **not orbital.** He would reach
  the portal's altitude and then have nothing.
- *Intellect:* Practical. Notably, he was a VA counsellor — the roster's second-highest
  Emotional Intelligence (85), behind only Widow.
- *What breaks him:* Nothing much. He is the roster's most psychologically stable
  non-enhanced member, which makes him a useful mid-anchor.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Wingsuit destroyable | Dependency | 85 | 70 |
| Baseline human durability | Physical | 85 | 80 |
| Limited operational altitude | Physical | 70 | 75 |

---

## CIVIL WAR (2016) — Four additions

### 13. Black Panther — T'Challa

**Interrogation**
- *Source:* **Two separate systems — this matters.** The Heart-Shaped Herb grants
  permanent super-soldier-level strength, speed, durability and senses. The Panther
  Habit is separate: vibranium microweave that absorbs kinetic energy, plus claws
  that scratched Cap's vibranium shield.
- *Consequence:* he is the roster's **most robust "gear removed" case** — strip the
  suit and he is still enhanced. Compare Iron Man, who becomes baseline.
- *Best feat:* Fought Cap and the Winter Soldier simultaneously and held his own;
  pushed back Bucky's bionic arm by force.
- *Worst failure:* Ground-bound. No answer to an aerial invasion.
- *What breaks him:* Vengeance — the entire Civil War arc — though he resolves it.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| No flight capability | Physical | 80 | 85 |
| Vengeance clouds judgement | Psychological | 70 | 60 |
| Duty to Wakanda constrains action | Situational | 50 | 40 |

---

### 14. Spider-Man — Peter Parker

**Interrogation**
- *Source:* Innate (bite). Webshooters are self-made tech — semi-removable.
- *Best feat:* **Caught and bent back the Winter Soldier's bionic arm with one hand.**
  Multiple sources note Bucky's arm was *casually overpowered.* This places Peter's
  raw strength clearly above Bucky's and above Cap's — a genuinely counterintuitive
  result that the interrogation protocol surfaced and the "vibes" method would miss.
- *Worst failure:* Wildly inexperienced. Talks through fights. Gets knocked out by a
  thrown jetway.
- *Mobility caveat:* web-swinging **requires anchor points.** In open sky he has
  nothing. He is agile, not aerial.
- *What breaks him:* Desperate need for Stark's approval (Ego 70 — high for a 15-year-old
  in a roster of adults).

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Severe inexperience | Psychological | 75 | 80 |
| Web-swinging needs anchor points | Situational | 70 | 75 |
| Needs approval / easily led | Psychological | 65 | 70 |

---

### 15. Ant-Man — Scott Lang

**Interrogation**
- *Source:* Pym Particles. **Consumable** — this is a genuine, canon-flagged
  resource limit, not a headcanon.
- *Best feat:* Giant-Man at roughly 20 m in Civil War, forcing Stark, Rhodes and
  Peter to stop and rethink. Also: shrank inside Yellowjacket's suit to destroy it
  from within — *the exact tactic Stark used on a Leviathan.*
- *Worst failure:* Reverted to normal size from a single hard punch by Falcon.
  Giant form is powerful and **unstable**.
- *Scaling:* Both directions. Giant = crowd clearing; tiny = infiltration.
- *Why he is interesting here:* the shrink-and-destroy-from-inside tactic is a
  legitimate Leviathan answer that does not require raw power. This is exactly the
  kind of lateral solution the gate design should reward.
- *What breaks him:* Cassie. Highest Attachment on the roster after Wanda.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| Finite Pym Particle supply | Dependency | 90 | 55 |
| Giant form unstable / reverts on impact | Physical | 75 | 70 |
| Daughter as leverage | Psychological | 80 | 45 |

---

### 16. Winter Soldier — Bucky Barnes

**Interrogation**
- *Source:* HYDRA's serum variant (innate) + bionic arm (removable).
- *Best feat:* Overpowered Captain America in direct combat using the arm.
- *Worst failure:* Two of them, and both are severe. Stark destroyed the arm with a
  single arc-reactor blast. And **Zemo activated him with spoken trigger words** —
  ten words turn him into a weapon against his own allies.
- *Ceiling correction:* the arm is strong but **not flexible**, and Spider-Man
  countered it with ease. Bucky is *super-soldier tier*, not *super-strength tier*.
- *What breaks him:* The trigger words. This is the highest exploitability-weighted
  vulnerability in the entire roster and should be modelled as such.

**Vulnerabilities**

| Name | Type | Sev | Exp |
|---|---|---|---|
| HYDRA trigger words | Psychological | 100 | 85 |
| Arm destroyable by energy weapons | Dependency | 70 | 55 |
| Crushing guilt over past kills | Psychological | 85 | 60 |

---

# PART III — MASTER MATRIX

## Block A — Physical & Combat

| Hero | A1 Power | A2 Dura | A3 Speed | A4 Mobility | A5 Ranged | A6 Crowd | A7 Stamina | A8 Exotic |
|---|---|---|---|---|---|---|---|---|
| Hulk | **100** | **100** | 50 | 45 | 12 | 85 | 88 | 60 |
| Thor | 95 | 92 | 68 | 90 | 88 | **100** | 90 | 85 |
| Vision | 85 | 88 | 70 | **95** | 85 | 80 | **98** | **95** |
| Scarlet Witch | 80 | 45 | 45 | 40 | 82 | 88 | 50 | 30 |
| Iron Man | 78 | 75 | 60 | **95** | 90 | 72 | 55 | 70 |
| Ant-Man | 75 | 55 | 55 | 35 | 15 | 60 | 45 | 22 |
| War Machine | 70 | 72 | 55 | 92 | **100** | 75 | 55 | 68 |
| Spider-Man | 65 | 50 | 85 | 40 | 30 | 40 | 65 | 20 |
| Black Panther | 60 | 68 | 78 | 30 | 20 | 35 | 72 | 20 |
| Winter Soldier | 55 | 52 | 62 | 18 | 40 | 30 | 70 | 25 |
| Captain America | **50** | 55 | 65 | 20 | 28 | 38 | 85 | 25 |
| Quicksilver | 32 | 25 | **100** | 50 | 10 | 65 | 45 | 10 |
| Falcon | 25 | 22 | 50 | 70 | 45 | 35 | 50 | 15 |
| Hawkeye | 18 | 18 | 45 | 15 | 55 | 30 | 50 | 10 |
| Black Widow | 16 | 18 | 60 | 18 | 30 | 25 | 55 | 10 |
| Nick Fury | 12 | 15 | 30 | 12 | 25 | 18 | 40 | 10 |

## Block B — Mind & Command

| Hero | B1 Tactical | B2 Technical | B3 Leadership | B4 Improvisation |
|---|---|---|---|---|
| Captain America | **100** | 40 | **100** | 80 |
| Vision | 82 | 98 | 50 | 45 |
| Iron Man | 78 | **100** | 60 | **95** |
| Nick Fury | 92 | 55 | 90 | 80 |
| Black Widow | 85 | 50 | 55 | 85 |
| Black Panther | 80 | 78 | 82 | 72 |
| Hulk / Banner | 15 | 90 | 8 | 35 |
| Winter Soldier | 75 | 38 | 35 | 70 |
| War Machine | 72 | 60 | 55 | 60 |
| Hawkeye | 70 | 30 | 45 | 75 |
| Falcon | 65 | 45 | 48 | 70 |
| Thor | 55 | 35 | 58 | 55 |
| Ant-Man | 45 | 65 | 30 | 85 |
| Scarlet Witch | 45 | 40 | 25 | 50 |
| Spider-Man | 40 | 72 | 25 | 88 |
| Quicksilver | 35 | 25 | 25 | 60 |

## Block C — Personality

Optimum row shown for reference — **closeness to optimum is what scores**, not height.

| Hero | C1 Resil | C2 EQ | C3 Attach | C4 Sacrifice | C5 Impulse | C6 Guilt | C7 Trust | C8 Moral | C9 Ego | C10 Courage |
|---|---|---|---|---|---|---|---|---|---|---|
| *OPTIMUM* | *100* | *100* | *70* | *75* | *90* | *15* | *65* | *55* | *25* | *100* |
| Captain America | 88 | 78 | 88 | 98 | 75 | 55 | 70 | 95 | 30 | 98 |
| Iron Man | 35 | 45 | 75 | 95 | 35 | 90 | 35 | 45 | 95 | 88 |
| Thor | 65 | 40 | 62 | 75 | 40 | 60 | 68 | 65 | 80 | 85 |
| Hulk / Banner | 32 | 60 | 65 | 55 | 30 | 92 | 45 | 55 | 15 | 65 |
| Black Widow | 82 | 92 | 60 | 80 | 88 | 85 | 28 | 30 | 20 | 92 |
| Hawkeye | 80 | 75 | 90 | 60 | 72 | 35 | 65 | 50 | 25 | 85 |
| Nick Fury | 90 | 75 | 25 | 50 | 85 | 30 | 10 | 15 | 30 | 85 |
| Vision | 70 | 55 | 55 | 85 | 95 | 25 | 72 | 80 | 10 | 75 |
| Scarlet Witch | 28 | 45 | 98 | 60 | 35 | 88 | 40 | 40 | 40 | 55 |
| Quicksilver | 45 | 40 | 95 | 92 | 30 | 35 | 60 | 35 | 72 | 78 |
| War Machine | 78 | 65 | 72 | 70 | 70 | 35 | 62 | 68 | 45 | 80 |
| Falcon | 75 | 85 | 70 | 68 | 65 | 30 | 75 | 60 | 35 | 80 |
| Black Panther | 75 | 70 | 78 | 60 | 50 | 50 | 45 | 70 | 45 | 82 |
| Spider-Man | 55 | 50 | 82 | 70 | 45 | 60 | 80 | 75 | 70 | 68 |
| Ant-Man | 60 | 55 | 92 | 65 | 50 | 40 | 70 | 40 | 40 | 70 |
| Winter Soldier | 30 | 35 | 80 | 65 | 40 | 98 | 20 | 45 | 15 | 75 |

---

# PART IV — CALIBRATION

## 7. Gate validation — does the framework produce canon-correct results?

Gates from `CLAUDE.md` §6.1 applied to the dataset:

| Hero | Reach portal (Mob≥70) | Survive crossing (Exo≥70) | Find weakness (Tech≥75) | Crack Leviathan (Pow≥85 / Tech≥80) | Survive swarm (Crowd≥60) | **Passed** |
|---|---|---|---|---|---|---|
| **Vision** | ✅ 95 | ✅ 95 | ✅ 98 | ✅ 98 | ✅ 80 | **5/5** |
| **Iron Man** | ✅ 95 | ✅ 70 | ✅ 100 | ✅ 100 | ✅ 72 | **5/5** |
| War Machine | ✅ 92 | ❌ 68 | ❌ 60 | ❌ | ✅ 75 | 2/5 |
| Thor | ✅ 90 | ✅ 85 | ❌ 35 | ✅ 95 | ✅ 100 | 4/5 |
| Hulk | ❌ 45 | ❌ 60 | ✅ 90 | ✅ 100 | ✅ 85 | 3/5 |
| Scarlet Witch | ❌ 40 | ❌ 30 | ❌ 40 | ❌ | ✅ 88 | 1/5 |
| Falcon | ✅ 70 | ❌ 15 | ❌ 45 | ❌ | ❌ 35 | 1/5 |
| Captain America | ❌ 20 | ❌ 25 | ❌ 40 | ❌ | ❌ 38 | **0/5** |
| Black Widow | ❌ | ❌ | ❌ | ❌ | ❌ | 0/5 |

### Verdict: the framework works.

- **Iron Man passes all five** — and he is the character who *canonically performed
  this exact mission.* Strongest possible validation signal.
- **Vision also passes all five**, which is correct: phasing plus vacuum tolerance
  plus near-Stark intellect makes him the ideal candidate.
- **Thor fails on Technical Intelligence only** — exactly right. He has the raw
  capability and cannot find the weakness alone.
- **Captain America scores 0/5** — correct and important. He is the roster's best
  leader and tactician and he still cannot do the mothership run. He stayed on the
  ground in the film. **The framework is not rewarding "generally impressive."**
- **Hulk 3/5** despite maximum Power and Durability — proves raw strength alone
  does not win this.

> **The flat-build test:** a normalised flat build sits near 62 on every axis and
> passes **exactly one gate** (Crowd Clearing). It fails the mothership run entirely.
> This is the intended behaviour and confirms the anti-max design.

---

## 8. Resolved tensions (decided this session)

1. **Banner/Hulk duality — kept as one row.** Splitting into two rows would only
   help reference-table tidiness; it changes nothing about the player-facing game,
   since players build original heroes rather than picking from this roster. The
   existing vulnerability (`Intellect unavailable while transformed`) already
   carries the trade-off. Closed, no change.
2. **Scarlet Witch's low score — intentional, not a bug.** Called out explicitly
   rather than patched: her signature power is close to useless against the
   Chitauri specifically (no fear, no morale, no mind to manipulate — see
   ENEMY.md §8.1), which is thematically correct even though she's one of the
   most powerful characters against a different kind of enemy. This is the
   roster's clearest illustration of "mission fit beats raw power" and should be
   used as the example when explaining the framework, not quietly smoothed over.
3. **War Machine vs. Iron Man — confirmed correct.** The separation resting on
   Technical Intelligence and Improvisation matches canon: Rhodes is a highly
   capable pilot and engineer, but an operator on Stark's platform, not its
   inventor. No change.
4. **Exotic Survivability thresholds — kept at 70, on purpose.** Only 4 of 16
   heroes clearing it isn't a flaw, it's the point: a hard, rare-specialist gate,
   matching canon — leaving atmosphere nearly killed Stark. A gate everyone
   clears isn't a gate. No change.
5. **Ant-Man's interior-attack tactic — no new gate needed.** It's already
   covered by the existing `Technical Int ≥ 80` branch of the Leviathan gate,
   since finding a Leviathan's interior weak point is itself a technical
   solution. Ant-Man individually not clearing that threshold (Technical Int 65)
   is roster-accurate — he executed that tactic with Pym's guidance, not solo
   genius. No change.
