# LEADERBOARD.md — The Superhero Feast Leaderboard

> **Design Brief:** A live, real-time leaderboard for the Avengers-themed superhero builder game. Theme: playful, celebratory, Duolingo-inspired with vibrant colors and delightful micro-interactions. Powered by Supabase Realtime.

---

## 1. Overall Layout & Information Architecture

```
┌─────────────────────────────────────────────────────────┐
│  🏆 CHITAURI LEADERBOARD                    LIVE UPDATE  │  ← Header
├─────────────────────────────────────────────────────────┤
│                                                           │
│          🥇 PODIUM (Rank 1, 2, 3)                        │  ← Podium Section
│      [2nd]    [1st]    [3rd]                             │
│       ║        ║        ║                                 │
│      165px    200px    140px (heights)                    │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  📋 LEADERBOARD GRID (Rank 4–20)                         │  ← Scrolling List
│   [4] Name | Hero | Score | Gates Passed                 │
│   [5] ...                                                 │
│   [6] ...                                                 │
│   ...                                                     │
│  [20] ...                                                 │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Color & Typography Locked

| Element | Color | Font | Size | Weight |
|---|---|---|---|---|
| Page background | `#FFFFFF` | — | — | — |
| Text (primary) | `#14141A` | Manrope | 16px body, 32px heading | 400/600 |
| Accent (badges, gates) | `#E23636` | Manrope | var | 600 |
| Blue highlight (podium) | `#1560D4` | Manrope | var | 600 |
| Gate pass (✓) | `#10B981` | — | — | — |
| Gate fail (✗) | `#EF4444` | — | — | — |
| Borders | `#E5E7EB` | — | — | — |
| Medal background (podium) | `#FCD34D` (gold), `#C7D2FE` (silver), `#FED7AA` (bronze) | — | — | — |

---

## 3. Podium Section — Top 3 Heroes

### 3.1 Structure

Three vertical "medals" displayed at different heights, arranged left-center-right:

| Position | Height | Offset | Rank |
|---|---|---|---|
| **Left (2nd place)** | 165px | 0 | Silver medal `#C7D2FE` |
| **Center (1st place)** | 200px | Top: -20px (lifts above line) | Gold medal `#FCD34D` |
| **Right (3rd place)** | 140px | 0 | Bronze medal `#FED7AA` |

> **As shipped:** these heights apply to a colored riser/pedestal *beneath*
> each card (with the rank number on it, like an Olympic podium block), not
> to the whole card. The rich content in §3.2 (medal + name + score + 5 gate
> lines + player name) genuinely needs more than 140-200px — forcing it into
> a fixed box of that height caused real overflow/overlap (worst on mobile).
> Card content is consistent height across all three ranks; the riser below
> it carries the 200:165:140 step effect instead. Rank 1's `-20px` lift is
> applied to the whole card+riser unit via a small negative top margin.

### 3.2 Each Medal Card Contains

```
┌────────────────────┐
│   [Medal Icon]     │  ← Circular, 60px, gold/silver/bronze
│   (🥇/🥈/🥉)        │
│                    │
│  Hero Name         │  ← Manrope, 20px, bold, #14141A
│  "Ironclad Surge"  │
│                    │
│  Score: 2,450      │  ← Manrope, 16px, #E23636 (red)
│                    │
│  Gates: 5/5 ✓      │  ← Checkmarks green, Manrope 14px
│  ✓ Reach portal    │     Stacked vertically (abbreviated)
│  ✓ Survive ...     │
│  ✓ Find weakness   │
│  ✓ Crack ...       │
│  ✓ Survive swarm   │
│                    │
│  Player: Alex      │  ← Manrope, 12px gray, #6B7280
└────────────────────┘
```

### 3.3 Podium Styling Details

- **Shape:** Rounded rectangle, `rounded-xl` (12px)
- **Shadow:** `shadow-lg` (realistic depth)
- **Background:** Off-white `#F8F9FA`
- **Border:** `1px solid #E5E7EB`
- **Padding:** `p-6`
- **Width:** Each card ~140–160px (responsive)
- **Medal circle:** 60px diameter, centered at top of card, color-coded
- **Text alignment:** Center

### 3.4 Animations on Podium

1. **Entrance:** Cards slide up from below with a spring bounce (Framer Motion: `type: "spring", stiffness: 100, damping: 20`), staggered by 100ms each
2. **Medal spin:** The medal icon rotates 360° on load, then settles with a gentle wobble every 3 seconds (infinite loop)
3. **Score counter:** The score number animates from 0 to final value on first load (e.g., 0 → 2,450 over 1.5s)
4. **Gate indicators:** Each checkmark and icon fades in sequentially (stagger delay 150ms between each)

---

## 4. Leaderboard List — Ranks 4–20

### 4.1 List Structure (Grid Layout)

**Desktop (≥768px):**
```
┌────┬──────────────┬─────────────────┬────────────┬──────────────┐
│ #  │ Hero Name    │ Player Name      │ Score      │ Gates Passed │
├────┼──────────────┼─────────────────┼────────────┼──────────────┤
│ 4  │ Ironclad Surge │ Alex           │ 2,380      │ 5/5 ✓✓✓✓✓   │
│ 5  │ Void Dancer  │ Morgan          │ 2,310      │ 4/5 ✓✓✓✓    │
│ 6  │ Thought Weaver │ Casey          │ 2,200      │ 3/5 ✓✓✓     │
│ ... │               │                 │            │              │
└────┴──────────────┴─────────────────┴────────────┴──────────────┘
```

**Mobile (<768px):**
```
┌──────────────────────────────────┐
│ #4 — Ironclad Surge              │
│ Alex | Score: 2,380              │
│ Gates: ✓ ✓ ✓ ✓ ✓ (5/5)           │
└──────────────────────────────────┘
┌──────────────────────────────────┐
│ #5 — Void Dancer                 │
│ Morgan | Score: 2,310            │
│ Gates: ✓ ✓ ✓ ✓ (4/5)             │
└──────────────────────────────────┘
```

### 4.2 Row Styling

- **Background:** White `#FFFFFF`
- **Border:** `border-b 1px solid #E5E7EB` (divider between rows)
- **Padding:** `p-4` (desktop), `p-3` (mobile)
- **Hover state:** Background shifts to light gray `#F9FAFB` on desktop only

### 4.3 Column Details

| Column | Content | Style |
|---|---|---|
| **Rank** | `#4`, `#5`, etc. | Manrope 18px bold `#14141A`, 40px wide |
| **Hero Name** | "Ironclad Surge" | Manrope 16px bold `#14141A` |
| **Player Name** | "Alex" | Manrope 14px gray `#6B7280` |
| **Score** | `2,380` | Manrope 18px bold `#E23636` (red accent) |
| **Gates Passed** | `5/5 ✓✓✓✓✓` | Green icons (✓ = `#10B981`), Red icons (✗ = `#EF4444`), 5 inline icons |

### 4.4 Animations on List

1. **Row entrance:** Rows fade in and slide right with a small translateX, staggered by 80ms each (using CSS `animation-delay: calc(var(--index) * 80ms)`)
2. **Hover highlight:** On desktop, row background animates to `#F9FAFB` with a smooth transition (100ms)
3. **Score pulse:** Score number has a subtle pulse animation (opacity: 1 → 0.8 → 1) that loops every 2 seconds on new entries (first 5 seconds after render)
4. **Gate icons:** Each gate icon fades in with a bounce (spring physics) when score is first rendered

---

## 5. Header Section

```
┌──────────────────────────────────────────────────────────┐
│                                                            │
│   🏆 CHITAURI LEADERBOARD                 🔄 LIVE UPDATE  │
│                                                            │
│   20 heroes. 5 gates. One mothership to save the city.   │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

- **Title:** Manrope 40px bold, `#14141A`, centered
- **Subtitle:** Manrope 14px gray `#6B7280`, centered, max-width 600px
- **Live indicator:** Small green dot that pulses, next to text "LIVE UPDATE" (Manrope 12px)
- **Padding:** `py-8 px-4` on mobile, `py-12 px-8` on desktop
- **Background:** White with subtle border-bottom `#E5E7EB`

### 5.1 Live Update Badge

- **Appearance:** Green dot + "LIVE UPDATE" text, Manrope 11px gray
- **Pulse animation:** Green dot opacity loops: 1 → 0.4 → 1, every 2s (infinite)
- **Position:** Top right, `p-4` from edge

---

## 6. Real-time Updates (Supabase Realtime)

### 6.1 Mechanism

- Subscribe to `leaderboard` table via Supabase Realtime
- On INSERT/UPDATE, the component re-renders and animates the new/updated row
- The podium updates with a smooth transition if rank 1, 2, or 3 changes

### 6.2 Update Animation

When a new score lands and the leaderboard re-sorts:

1. **Affected rows:** Animate their rank badge with a "bounce" effect (scale: 0.8 → 1.1 → 1)
2. **Score animation:** New score counts up from previous score to new score
3. **Position shift:** If a row moves up/down, use Framer Motion `layoutId` to animate the position smoothly

---

## 7. Interactive States

### 7.1 Hover (Desktop Only)

- **Row hover:** Background `#F9FAFB`, subtle shadow lift
- **Score hover:** Text color brightens to `#DC2626` (darker red)
- **Cursor:** Standard pointer

### 7.2 Loading State

Before Realtime connects:

- **Skeleton loaders:** 5 skeleton rows (gray shimmer placeholders, same height as real rows)
- **Header:** Visible immediately
- **Podium:** Skeleton 3-cards with shimmer pulse

### 7.3 Empty State (No Submissions Yet)

```
┌────────────────────────────────────────┐
│                                        │
│   🏆 No heroes yet. Be the first! 🚀  │
│                                        │
│   Leaderboard updates live as scores  │
│   are tallied. Check back soon.        │
│                                        │
└────────────────────────────────────────┘
```

- Manrope 20px bold, centered, `#14141A`
- Subtitle: 14px gray `#6B7280`
- Padding: `py-16 px-4`

---

## 8. Responsive Breakpoints

| Breakpoint | Layout | Changes |
|---|---|---|
| **Mobile** (`<640px`) | Single column | Rows stack vertically, podium medals arrange in a "winner's circle" (small, tight) |
| **Tablet** (`640px–1024px`) | Single column | Podium medals slightly larger, rows use card-style containers |
| **Desktop** (`≥1024px`) | Full grid | Standard grid layout, podium medals at full size |

> **As shipped:** "small, tight" on mobile also means the podium card's
> per-gate breakdown list (5 lines) is hidden below the `sm:` breakpoint —
> only the "Gates: X/5" summary line shows. With it visible at mobile width,
> three cards' worth of content genuinely didn't fit without overlap;
> hiding it there and keeping the fraction was the fix.

---

## 9. Tech Stack & Interactivity

### 9.1 Framework & Libraries — as actually shipped

Built as `leaderboard/index.html`, a single static file with **zero npm
install and zero bundler**, matching CLAUDE.md's Stage 4 deploy constraint
(see its "Revision note (framework choice)" in §2):

- **React 18 + Framer Motion + Phosphor Icons + Supabase JS** loaded as ESM
  directly from `esm.sh`, wired together with a `<script type="importmap">`
  so every package resolves to one shared React instance
- **JSX authored normally**, transformed in the browser via **Babel
  Standalone** (`data-type="module"` so `import`/`export` still work) —
  this is what makes "no build step" and "real JSX" both true at once
- **Tailwind CSS** via the `cdn.tailwindcss.com` play build (JIT, no
  PostCSS step)
- Drag-and-drop deploy: point Cloudflare Pages at the `leaderboard/` folder

### 9.2 Key Components (as actually shipped)

All in the one file, not separate component files (see §16):
`Header`/`LiveBadge`, `PodiumSection`/`PodiumCard`/`GateRow`,
`LeaderboardList`/`ListRow`/`GateIcons`, `useLeaderboardData` (the Realtime
hook — debounces to one refetch per DB change burst, since Stage 3 replaces
the whole table on every scoring run), `useCountUp`, `ConfettiBurst`.

### 9.3 Data Structure (from Supabase leaderboard table)

`gate_detail`'s keys are **not** the shorthand originally sketched here —
they're the real gate keys from `scoring/data.py`'s `GATES` list, since
that's what Stage 3 actually writes:

```json
{
  "id": "uuid",
  "rank": 1,
  "player_name": "Alex",
  "hero_name": "Ironclad Surge",
  "total_score": 2450,
  "gates_passed": 5,
  "gate_detail": {
    "reach_portal": true,
    "survive_crossing": true,
    "find_weakness": true,
    "crack_leviathan": true,
    "survive_swarm": true
  },
  "scored_at": "2026-09-15T18:45:00Z"
}
```

---

## 10. Design Tokens (Tailwind CSS Variables)

```css
/* Colors */
--color-accent: #E23636;
--color-blue: #1560D4;
--color-text-primary: #14141A;
--color-text-secondary: #6B7280;
--color-bg-primary: #FFFFFF;
--color-bg-secondary: #F8F9FA;
--color-success: #10B981;
--color-error: #EF4444;
--color-border: #E5E7EB;

/* Gold/Silver/Bronze */
--color-gold: #FCD34D;
--color-silver: #C7D2FE;
--color-bronze: #FED7AA;

/* Shadows */
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);

/* Typography */
--font-family: 'Manrope', sans-serif;
--font-size-heading: clamp(28px, 8vw, 40px);
--font-size-body: 16px;
--line-height-tight: 1.2;
--line-height-relaxed: 1.6;
```

---

## 11. Animation Reference

| Animation | Duration | Easing | Use Case |
|---|---|---|---|
| **Spring (default)** | Automatic | `stiffness: 100, damping: 20` | Card entrance, podium updates |
| **Fade-in** | 300ms | ease-in-out | Row entrance, loading states |
| **Slide-right** | 400ms | ease-out | Row entrance offset |
| **Score counter** | 1.5s | ease-out | Score number animation |
| **Pulse** | 2s | linear | Infinite loop (gates, live indicator) |
| **Bounce** | 600ms | cubic-bezier | Medal spin, rank badge update |

---

## 12. Accessibility & Performance

- **ARIA labels:** All interactive elements have descriptive labels
- **Keyboard nav:** Rows are focusable (`:focus-visible` ring `#E23636`)
- **Color contrast:** All text meets WCAG AA (4.5:1 minimum)
- **Animations:** Respect `prefers-reduced-motion` — disable infinite loops for users with motion sensitivity
- **Performance:** Memoize list rows to prevent unnecessary re-renders; use `React.memo` on podium cards
- **Mobile optimization:** Debounce Realtime updates to max 1 re-render per second

---

## 13. Deployment Notes

- **Host:** Cloudflare Pages (static, no build step)
- **Environment:** Single HTML file with inline React/Tailwind (or JSX compiled to a single bundle)
- **API keys:** Supabase anon key baked into the frontend (read-only on `leaderboard` table, safe to expose)
- **Realtime:** Native Supabase Realtime WebSocket, no polling

---

## 14. Playfulness & Brand Voice

- **Tone:** Celebratory, encouraging, Marvel-inspired
- **Confetti moments:** When podium updates or new rank 1 achieved, optional CSS animation of falling confetti (subtle, performance-conscious)
- **Mascot/Icon:** Consider a small "Chitauri eye" icon that blinks occasionally in the header (optional micro-interaction)
- **Color energy:** Red (#E23636) is the hero accent; blue (#1560D4) is the enemy; gold/silver/bronze are victory
- **Typography bounce:** Headings use Manrope's full weight range (700 for boldness, 400 for lightness) to create visual rhythm

---

## 15. Success Criteria

Checked = actually verified in headless Chromium against production Supabase
data, not just implemented. See CLAUDE.md §9 test log for how.

- [x] Podium renders with correct rank heights — as a riser below the card,
  not the card itself (see §3.1 note); screenshotted at desktop + mobile
- [x] Top 3 medals display with spring entrance, staggered by 100ms (code:
  `delay: index * 0.1`; visually confirmed, not frame-measured)
- [ ] Leaderboard list scrolls smoothly with row entrance animations
  (staggered entrance implemented and rendered with zero console errors;
  scroll smoothness itself wasn't separately profiled)
- [x] Score numbers animate from 0 to final on load, and old → new on
  update — confirmed live: DB score change propagated and counted up with
  no reload
- [x] Gate icons render correctly (✓ green, ✗ red) — confirmed via
  screenshot; sequential fade-in implemented, not frame-isolated
- [x] Supabase Realtime subscription updates podium and list live —
  confirmed with a real Postgres UPDATE while the page was open
- [x] Mobile layout collapses to single column, podium adapts — this is
  where the height-overflow bug was actually caught; fixed and re-verified
- [ ] Hover states work on desktop, no janky repaints (implemented via
  Tailwind `hover:`; not interactively tested with a real pointer)
- [x] Loading skeleton appears before data loads
- [x] Empty state displays if no submissions (verified before the retune
  session added test data; not re-verified after, but nothing touched that
  code path)
- [x] Animations respect `prefers-reduced-motion` — tested with motion
  emulated to `reduce`, zero console errors
- [ ] Accessibility: ARIA labels and keyboard-focusable rows are in the
  code (`role`, `tabIndex`, `focus-visible:ring-accent`); not verified with
  an actual screen reader or a contrast-ratio tool

---

## 16. File Structure — as actually shipped

```
leaderboard/
└── index.html   # everything: markup, Tailwind config, keyframes, all
                  # components, the Realtime hook -- inline in one file
```

Not split into `components/`/`hooks/`/`utils/` as originally sketched here.
With Babel Standalone doing the JSX transform in-browser (no bundler), there
was no import graph to speak of — separate files would have meant either a
handful of extra `<script type="text/babel">` tags evaluated in sequence
(fragile load-order dependencies) or reaching for a bundler, which defeats
the "no build step, drag-and-drop deploy" point in the first place. One file
was the simpler choice that actually satisfies CLAUDE.md's Stage 4 intent.

---

## END OF SPEC

**Next step:** Paste this LEADERBOARD.md into Claude Code with the following prompt:

```
Read LEADERBOARD.md fully. This is the design spec for the Cloudflare Pages 
leaderboard. Build a single-file React component (or HTML+JSX bundle) that 
implements this design exactly. Use Tailwind CSS for styling, Framer Motion 
for animations, Supabase Realtime for live updates, and Phosphor Icons for 
icon elements (no emojis). The component must subscribe to the `leaderboard` 
table and render the podium + list in real-time. Make it production-ready and 
playful.
```