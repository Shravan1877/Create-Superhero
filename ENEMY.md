# ENEMY.md — Chitauri Invasion Force: Full Dossier

> Companion to `CLAUDE.md` and `SUPERHEROES.md`.
> This file is the **complete threat model**. Every gate, weight, and optimum in the
> scoring framework traces back to something in this document. If a game mechanic
> can't be justified from here, it's invented and should be removed.
>
> **Scope:** The Chitauri as deployed at the Battle of New York, 4 May 2012.
> Later appearances (Endgame) are noted but are *out of scope* for scoring.

---

# PART I — IDENTITY

## 1. Who they are

| Field | Detail |
|---|---|
| **Species** | Sentient six-fingered reptilian humanoids, cybernetically enhanced |
| **Homeworld** | Chitauri Prime — described as polluted and hive-like |
| **Biology** | Born fully organic; bodies composed of silicon dioxide and boron trioxide |
| **Status** | Subjugated slave-army, not a free civilisation |
| **Master** | Thanos |
| **Loaned to** | Loki, in exchange for the Tesseract |
| **Name origin** | "Chi Tauri" — a binary star in the constellation Taurus |
| **Comics analogue** | Closest to the Phalanx (cybernetic hive-mind race), not the Ultimate-universe shapeshifters |

**Critical framing:** they are not an invading civilisation with goals of their own.
They are a **disposable instrument**. Thanos conquered and transformed the entire
species into a slave army connected by collective consciousness. Every individual
was cybernetically altered — this was done *to* them.

### 1.1 Prior operations

They were Thanos's infantry at **Zen-Whoberi**, where they massacred half the
Zehoberei population — Gamora's homeworld. They are veterans of planetary
genocide, not first-timers. New York was not their first invasion; it was just
their first failure.

---

## 2. Chain of command

```
THANOS
  └─ The Other          (intermediary; met Loki at the Sanctuary)
      └─ LOKI            (field commander, via the Scepter)
          └─ COMMAND SHIP / MOTHERSHIP   ← the actual control node
              └─ every soldier, chariot, and Leviathan
```

**Loki commands, but the Command Ship *controls*.** This distinction is the entire
battle. Killing or capturing Loki does not stop the army — Hulk beat Loki into
submission and the invasion continued. Killing the Command Ship stops everything
instantly.

---

# PART II — FORCE COMPOSITION

Four tiers. Each is a separate tactical problem.

## 3. Tier 1 — Infantry

| Attribute | Assessment |
|---|---|
| **Numbers** | Thousands, with continuous reinforcement |
| **Durability** | Roughly human-level — conventional firearms kill them |
| **Strength** | Contested Captain America in pure strength; tanked his elbow strike |
| **Armour** | Fused directly to the body; withstands a few hits from their own plasma weapons before burning through |
| **Mobility** | Can cling to and climb building walls (surface scaling) |
| **Deployment** | Dropped from Leviathan underside pods, or arrive by chariot |

### 3.1 Cybernetic enhancement package

- Electronic neural networks installed at an early age
- Armour physically fused to the body — not removable equipment
- **Chemical stimulants** enhancing strength and agility
- **Internal reactors** powering the cybernetic implants

> **Exploitable detail:** infantry are *dependent* on the stimulants and reactors.
> This is a supply-chain and power dependency, not innate biology.

### 3.2 The durability paradox

This is the most debated aspect of the Chitauri and it matters for design.

Individually they are **weak** — sidearms are effective, National Guard weapons
were never the problem. What defeated Earth's conventional response was not
toughness but **deployment speed**. The Guard could not move troops fast enough,
and the Chitauri established superiority over Manhattan before any meaningful
military force arrived.

**Design consequence:** rating them as "tough" is wrong. Rate them as **fast,
numerous, and continuously reinforced.** The threat is the rate, not the unit.

---

## 4. Tier 2 — Chariots

| Attribute | Assessment |
|---|---|
| **Role** | Air support, rapid assault, scouting, patrol |
| **Crew** | Pilot + up to 3 |
| **Escort** | Typically accompanied by two soldiers with energy rifles |
| **Armament** | Front-mounted pulse cannon |
| **Propulsion** | Antigravity technology enabling atmospheric flight |
| **Armour** | **None. Exposed crew.** |
| **Capability** | Can fire accurately while moving at high speed |

### 4.1 Threat profile

Individually trivial. **In mass, genuinely dangerous** — roughly two dozen chariots
were able to pin the Hulk under sustained fire he could not escape, and hundreds of
them eventually drew blood from him.

> **The lesson:** the Chitauri's real weapon is *accumulation*. Nothing they field
> beats a top-tier hero alone. Enough of it beats anyone.

### 4.2 Counter-profile

Zero armour and exposed crew make chariots the softest target in the force.
Hawkeye picked them off from elevation with arrows. Black Widow and Thor boarded
them mid-flight and killed the riders. The Ancient One one-shotted them with magic.

---

## 5. Tier 3 — Leviathans

The centrepiece of the invasion and the hardest conventional problem.

| Attribute | Assessment |
|---|---|
| **Nature** | Colossal bio-mechanical creatures, cybernetically augmented |
| **Size** | Comparable to a high-rise building |
| **Role** | Troop transport **and** siege weapon **and** wrecking crew |
| **Capacity** | Up to 24 soldiers in pods along the underside |
| **Propulsion** | Antigravity systems for atmospheric flight |
| **Armament** | Some carry energy guns comparable or superior to infantry rifles |
| **Speed** | Slow. Easy to hit. |

### 5.1 Armour — the hard number

This is the single most important defensive stat in the force.

- **Iron Man's firepower could not penetrate it from the outside.** JARVIS assessed
  that Stark would run out of power before he got through.
- A tank moving at full speed through a building failed to damage it.
- A direct Hulk punch stripped metal off the skin, but the metal itself remained
  largely intact — the *impact* killed it, not the penetration.
- Only **Hulk and Thor** could crack the armour and kill one in a single blow.

### 5.2 Documented weak points

1. **Unarmoured regions.** They are substantially weaker anywhere the plating
   doesn't cover.
2. **The interior.** Stark's solution was to fly *inside* one and destroy it from
   within — bypassing the armour entirely. This is the canonical proof that
   **lateral tactics beat raw force here.**
3. **Speed.** They are slow enough to be reliably targeted.
4. **The hive link** — like everything else, they die when the Command Ship does.

### 5.3 Tactical function — underrated

Leviathans are not just heavy units. They are a **dispersal system**: they carry
soldiers high onto buildings and spread them across the city in a pattern that
prevents them from being killed in concentrated groups. Killing a Leviathan is
also a crowd-control action.

---

## 6. Tier 4 — Command Ship / Mothership

| Attribute | Assessment |
|---|---|
| **Location** | Beyond the portal, in Chitauri space |
| **Function** | Hive-mind control node for every unit |
| **Combat stats** | Unknown — never engaged conventionally |
| **Defences** | Unknown |
| **Destroyed by** | A single nuclear warhead, delivered by hand |

**This is the only target that matters.** Everything else is noise.

---

# PART III — SYSTEMS

## 7. Weapons and equipment

| System | Notes |
|---|---|
| **Energy rifles** | Standard issue. Harmed Captain America with direct hits. Staggered and threw back Iron Man in armour. |
| **Plasma weapons** | Can burn through Chitauri armour itself after a few hits |
| **Handheld grenades** | Roughly room-clearing yield |
| **Chariot pulse cannon** | Destroyed cars, tore through streets, engulfed a rooftop in one blast |
| **Leviathan guns** | Comparable to or better than infantry rifles |
| **Melee** | Proficient. Not just shooters — they contest in close quarters. |

## 8. The hive mind — mechanics

**Type:** Multi-minded hive (Type 2). Individuals may retain base sentience, but
their actions are governed entirely by the command signal.

### 8.1 What it grants

| Benefit | Effect |
|---|---|
| **Massive-scale coordination** | Army-wide tactical sync with no communication lag |
| **No fear** | Will not break, will not flinch |
| **No morale requirement** | Cannot be demoralised, cannot be routed |
| **Fight until deactivated** | No surrender, no retreat, no self-preservation |

> This makes them a **perfect drone army.** Every psychological weapon in the human
> or superhuman arsenal is worthless against them.

### 8.2 What it costs

Every unit is neurally linked to the Command Ship via their implants. Sever the
signal and the entire force **instantly deactivates — collapsing like puppets with
the strings cut.** Not disorganised. Not demoralised. *Dead.*

This is a textbook **Keystone Army**: an overwhelming force with a single fragile,
well-protected point of failure.

### 8.3 Production note worth knowing

Joss Whedon acknowledged in DVD commentary that he disliked resorting to this
device, but used it so the heroes could achieve a clean victory rather than
seventeen more hours of mopping up. Useful to know: **the weakness is a narrative
convenience, which is exactly why it's so absolute.** There's no partial version.

### 8.4 The intelligence failure

A deleted Endgame scene has Rocket asking why they didn't simply destroy the
Command Center immediately, then laughing when he learns they didn't know that was
the weakness — it's common knowledge in his galaxy.

> **This is the most important fact in this entire document for game design.**
> The Avengers didn't win by being strong. They won by being *lucky enough* to
> stumble onto a solution the rest of the galaxy already knew.
> **Knowledge was the decisive weapon. Not power.**

---

# PART IV — THE BATTLE

## 9. Timeline

| Phase | Events |
|---|---|
| **Portal opens** | Selvig's Tesseract-powered generator, atop Stark Tower. Loki triggers it. |
| **First wave** | Thousands of infantry, chariots, and the first Leviathan pour through |
| **Collapse of conventional defence** | Buildings destroyed, civilians gunned down in the streets. National Guard cannot deploy fast enough. Superiority established before any real military response. |
| **Avengers engage** | Initially the Chitauri are *overwhelmed* — they did not expect resistance |
| **Escalation** | Portal throughput increases until containment becomes impossible |
| **Command established** | Captain America takes command of the Avengers *and* local police |
| **Sustained fight** | Roughly two to three hours |
| **Nuclear order** | World Security Council launches a warhead at Manhattan, against Fury's and Hill's explicit orders |
| **Decapitation** | Stark diverts the warhead through the portal into the Command Ship |
| **Instant collapse** | Every Chitauri and Leviathan dies and falls |
| **Portal closed** | Romanoff, using Loki's Scepter, per Selvig's information |

## 10. Force disposition — what the Avengers actually did

Captain America's assignment of roles is the canonical demonstration of leadership
as force multiplication:

| Hero | Assigned role |
|---|---|
| **Hawkeye** | High vantage point (120 Park Ave) — call out attack patterns and strays |
| **Iron Man** | Maintain air superiority; 3-block perimeter |
| **Thor** | Bottleneck the portal with lightning |
| **Cap + Black Widow** | Ground-level containment |
| **Hulk** | Smash. Targets of opportunity. |
| **NYPD / SWAT** | Held 39th Street against a Chitauri platoon, stalling the advance and enabling civilian evacuation |

**Note the SWAT/NYPD entry.** Ordinary officers with conventional weapons
successfully held a street against a Chitauri platoon. Further evidence the
infantry are not individually formidable.

## 11. Proven countermeasures

Every one of these is on-screen verified:

| Method | Effect | Used by |
|---|---|---|
| **Destroy the Command Ship** | Total instant army death | Iron Man (nuke) |
| **Close the portal** | Cuts reinforcement | Black Widow (Scepter) |
| **Bottleneck the portal** | Lightning at the chokepoint killed many at once and turned back the 4th and 5th Leviathans | Thor |
| **Attack Leviathan interior** | Bypasses armour entirely | Iron Man |
| **Single overwhelming impact** | One punch killed a Leviathan | Hulk |
| **Conventional firearms** | Effective on infantry | NYPD, SWAT, National Guard |
| **Elevated overwatch** | Pattern-calling multiplied the whole team | Hawkeye |
| **Precision anti-air** | Chariots have no armour | Hawkeye |
| **Magic** | One-shot chariots near the New York Sanctum | The Ancient One |

---

# PART V — ASSESSMENT

## 12. Strengths, ranked by actual danger

1. **Continuous reinforcement.** The portal is a faucet. No attrition strategy works.
2. **Deployment speed.** They took the city before anyone could respond.
3. **Immunity to psychological warfare.** No fear, no morale, no surrender.
4. **Leviathan armour.** Only two beings in the roster can crack it head-on.
5. **Mass coordination.** No comms lag, no confusion, no friendly fire.
6. **Accumulation.** Nothing they field beats a top hero alone; enough of it beats anyone.
7. **Air mobility.** Antigravity across two vehicle classes.
8. **Surface scaling.** Vertical terrain doesn't slow them down.

## 13. Weaknesses, ranked by exploitability

1. **THE KEYSTONE — Command Ship link.** One strike ends everything. Absolute, no partial effect.
2. **Portal dependency.** Close it, no reinforcements, fight becomes finite.
3. **The portal is a chokepoint.** Everything must funnel through one point in the sky.
4. **Infantry fragility.** Human-level durability. Sidearms work.
5. **Chariots are unarmoured** with exposed crew.
6. **Leviathans are slow** and have unarmoured regions.
7. **Leviathans are hollow.** Interior attack bypasses the armour problem completely.
8. **Zero adaptability.** Puppets don't improvise. No fallback plan when the signal cuts.
9. **Stimulant and reactor dependency** in infantry.
10. **Loki is a single point of *command* failure** — though not of control.

## 14. Threat matrix

| Tier | Individual threat | Massed threat | Counter difficulty | Kills the war? |
|---|---|---|---|---|
| Infantry | Low | High | Low | No |
| Chariots | Low | High | Low | No |
| Leviathans | Very high | Extreme | Very high | No |
| **Command Ship** | Unknown | N/A | **Access, not combat** | **YES** |

**Read the last column.** Three of the four tiers are irrelevant to victory. You can
kill Chitauri for seventeen hours and win nothing. The only tier that ends the war is
the one that was never even defended — because reaching it was assumed impossible.

---

# PART VI — DESIGN IMPLICATIONS

## 15. What this enemy demands of a hero

This section is the bridge from lore to game mechanics.

| Mission step | Requirement | Framework axis |
|---|---|---|
| Survive first contact | Withstand energy rifle fire | Durability |
| Don't drown in numbers | Neutralise many per action | **Crowd Clearing** |
| Handle a Leviathan | Extreme force **or** interior access | Raw Power **or** Technical Int |
| Reach the portal | Independent altitude | **Mobility & Flight** |
| Cross the portal | Vacuum, no oxygen | **Exotic Survivability** |
| Know where to strike | Deduce the hive link | **Technical Intelligence** |
| Actually go through with it | One-way trip into the unknown | **Courage / Self-Sacrifice** |
| Last the distance | Two to three hours minimum | Stamina |

## 16. Rules this enemy imposes on the game

1. **Raw strength alone must not win.** Punching is unbounded work against an
   unbounded enemy. Hulk had maximum power and could not have ended it.
2. **Intelligence must be weighted heavily.** The weakness had to be *discovered*.
   Rocket's laugh is the thesis of the whole design.
3. **Flight and vacuum tolerance must be gates, not bonuses.** Without both, the
   win condition is physically unreachable. Most heroes simply cannot attempt it.
4. **Psychological powers must be near-worthless.** The enemy has no fear, no morale,
   no mind to attack. *(This is why Scarlet Witch scores poorly — intended, not a bug.)*
5. **Lateral tactics must be rewarded.** Stark killing a Leviathan from inside is
   canon proof that cleverness substitutes for power. The gate design reflects this
   via the `Raw Power ≥ 85 OR Technical Int ≥ 80` branch.
6. **Generalists must lose.** The mission has a *shape*, not a threshold. A build
   that's good at everything clears none of the specific requirements.

## 17. Deliberate simplifications

Declared honestly so nobody "discovers" them later and thinks they're bugs:

- **Loki is excluded** as a combatant. He's a command element, not a scoring target.
- **The Scepter / Mind Stone** is excluded. Portal-closing is treated as achieved.
- **Civilian evacuation** is not scored, despite being a major on-screen concern.
- **Team-ups are not modelled.** Every player build is evaluated solo, even though
  the actual victory was a group effort. This is a known abstraction.
- **The nuke is not an available resource.** Players must solve it with the hero
  they build.

---

# PART VII — REFERENCE

## 18. Canon gaps — things genuinely unknown

- Command Ship combat capability, armament, and defences. Never engaged.
- Total invasion force size. "Thousands" is the only figure; the full force was
  intended to take the planet, not just Manhattan.
- Number of Leviathans held in reserve — many more were staged when the army died.
- Whether the hive link has any range limit.
- Whether a partial or degraded signal is possible. All evidence says no — it is
  binary.

## 19. Out-of-scope appearances

Noted only so they don't contaminate the ratings:

- **Endgame (2023 Battle of Earth):** 2014-Thanos deployed Chitauri alongside
  Outriders, Sakaarans, the Black Order and **Chitauri Gorillas** — a heavier
  variant not present in 2012. All disintegrated by Stark's Gauntlet snap.
- **Doctor Strange tie-in:** the New York Sanctum was within the 2012 attack radius;
  the Ancient One destroyed approaching Chitauri with Mystic Arts.
- **Aftermath:** Chitauri technology entered the black market during the NYC cleanup,
  which drives several later MCU plots. Irrelevant to scoring.

## 20. Sources consulted

Marvel Cinematic Universe Wiki (Chitauri, Leviathans, Battle of New York, Chitauri
Invasion) · Marvel Movies Wiki · VS Battles Wiki (MCU Chitauri profile and revision
threads) · Villains Wiki · Outlier Battles Wiki · Marvel.com character pages ·
Marvel Codex · GameRant · TV Tropes (Keystone Army) · Comic Vine MCU Chitauri
Respect Thread · Savage Worlds MCU conversion (Chitauri statblocks) · RetroZap
Battle of New York location breakdown · SpaceBattles analysis threads · NamuWiki

> **Source-reliability note:** wiki and fan-analysis sources vary in rigour.
> Anything load-bearing in this document — the hive-mind keystone, Leviathan armour
> performance, infantry durability, the Rocket intelligence-failure gag — appears
> consistently across multiple independent sources and is directly supported by
> on-screen events. Power-scaling tier numbers (9-A, 8-C, 7-A) are *fan-derived* and
> were used only as directional hints, never as inputs to any rating.
