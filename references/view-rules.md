# View rules (园丁规则 — every weed you pull becomes a rule)

Each rule came from a real failure (or a known failure of the original engine). Rules marked
**[lint]** are enforced by `scripts/verify_view.py`; the rest are enforced by review.
Append new rules at the bottom with the failure that produced them.

R1 [lint] Determinism: no Math.random / Date / performance.now / CSS animation or transition / requestAnimationFrame in a view. Seeded `ctx.hash` only.
R2 [lint] Never create or remove DOM nodes in `seek`; create everything in `build`, then toggle styles.
R3 [lint] Every text node is `mark`ed 'text' and stays inside its 'box'/'frame' and the canvas; use `ctx.fit` for every label (CJK labels are ~2x wider than Latin).
R4 [lint] Contrast ≥ 4.5 (≥ 3 for ≥20px). `dim` text on an accent fill usually fails — use `fg`.
R5 [lint] Connectors (`mark` 'edge') end on card borders and never cross another card.
R6 [lint] No toggle faster than 0.4 s; highlights last ≥ 0.8 s.
R7 [lint] Content fills ≥70% of rect width and ≥60% of height, balanced left/right margins.
R8 Derive every size from rect (`u = Math.min(w,h)/100`); a constant tuned on 4:5 breaks 1:1.
R9 Only theme colour names (acc1..6, accf1..6, fg, dim, panel, grid, ok, warn, bad, bg, line); no hex in view code.
R10 Numbers shown twice come from one variable (one truth); simulated numbers are labelled illustrative in `credit`.
