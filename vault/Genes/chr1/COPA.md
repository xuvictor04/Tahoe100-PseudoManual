---
symbol: "COPA"
type: "gene"
col: 4325
ensembl_id: "ENSG00000122218"
name: "coat protein complex I subunit alpha"
location: "1q23.2"
module: 56
arm: "+"
pooled_cpm: 363.66
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# COPA

*coat protein complex I subunit alpha* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.73× (z +4.6, q 0.001, up in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.36×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SK-MEL-2 3.84×); [[Auranofin (drug)]] 5 µM in 1 line (C32 2.69×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -14.2, q 9e-43, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC24D]] (+0.88, fdr 7e-06), [[SEC23A]] (+0.86, fdr 7e-06), [[TMEM39A]] (+0.85, fdr 7e-06); moves opposite to [[CMTR2]] (-0.65, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SEC13]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.36×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SK-MEL-2 3.84×); [[Auranofin (drug)]] 5 µM in 1 line (C32 2.69×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +4.6 | 0.001 | 36/49 (SK-MEL-2, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +4.6 | 0.001 | 37/48 (hTERT-HPNE, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.25× | +3.4 | 0.11 | 33/48 (A498, SK-MEL-2, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -14.2 | 9e-43 | 45/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -10.3 | 2e-22 | 41/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -10.1 | 1e-21 | 42/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.537×** | -9.7 | 7e-20 | 44/47 (hTERT-HPNE, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.571×** | -8.7 | 4e-16 | 37/44 (C-33 A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.591×** | -8.5 | 2e-15 | 37/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.602×** | -8.2 | 2e-14 | 36/48 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -7.9 | 2e-13 | 39/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.620×** | -7.7 | 8e-13 | 39/49 (RKO, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.605×** | -7.5 | 4e-12 | 39/45 (NCI-H2347, H4, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.646×** | -7.1 | 9e-11 | 33/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -6.9 | 3e-10 | 40/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.657×** | -6.8 | 6e-10 | 44/48 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.752×** | -6.5 | 4e-09 | 40/48 (J82, A549, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.664×** | -6.4 | 8e-09 | 39/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -5.6 | 7e-07 | 36/48 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.727×** | -5.1 | 9e-06 | 42/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -4.7 | 8e-05 | 31/48 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -3.7 | 0.005 | 21/48 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.795×** | -3.7 | 0.005 | 29/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.014 | 28/48 (NCI-H1792, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 491 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.4) |
| [[NCI-H1792 (line)]] | alt | 452 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -22.0) |
| [[A-172 (line)]] | wt | 546 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -24.1) |
| [[AsPC-1 (line)]] | alt | 424 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 413 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -19.7) |
| [[H4 (line)]] | wt | 544 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 477 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -14.9) |
| [[SW 900 (line)]] | alt | 603 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 558 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -22.4) |
| [[HOP62 (line)]] | alt | 449 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -21.5) |
| [[HS-578T (line)]] | alt | 409 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -16.2) |
| [[J82 (line)]] | alt | 357 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -23.4) |
| [[A549 (line)]] | wt | 354 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -18.0) |
| [[A498 (line)]] | wt | 487 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -14.6) |
| [[Hs 766T (line)]] | wt | 485 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.519× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 338 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 327 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.84× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -12.5) |
| [[SNU-423 (line)]] | alt | 324 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -21.3) |
| [[KATO III (line)]] | alt | 283 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -13.7) |
| [[LoVo (line)]] | wt | 333 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 278 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.9) |
| [[BT-474 (line)]] | alt | 264 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.0) |
| [[C32 (line)]] | wt | 681 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.69× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.5) |
| [[COLO 205 (line)]] | alt | 366 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.285× (z -13.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.389× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 220 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 563 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -9.9) |
| [[RKO (line)]] | wt | 238 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 235 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -13.3) |
| [[A-427 (line)]] | wt | 193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -12.3) |
| [[C-33 A (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0740× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 254 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -12.5) |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -9.3) |
| [[PANC-1 (line)]] | alt | 253 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 298 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.8) |
| [[SW 1088 (line)]] | alt | 480 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -8.8) |
| [[SW480 (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.434× (z -10.0) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 236 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 417 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 420 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 214 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 225 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 269 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 516 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 402 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 280 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24D]] | +0.88 | +0.90 / +0.83 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC23A]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 688 |
| [[TMEM39A]] | +0.85 | +0.89 / +0.82 | both halves | 7e-06 |  |
| [[COPB1]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 999 |
| [[SEC13]] | +0.82 | +0.87 / +0.75 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 657 |
| [[COG6]] | +0.82 | +0.85 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC31A]] | +0.82 | +0.83 / +0.79 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 704 |
| [[SAR1A]] | +0.81 | +0.85 / +0.76 | both halves | 7e-06 | STRING 451 |
| [[SEC61A1]] | +0.80 | +0.85 / +0.76 | both halves | 7e-06 | STRING 412 |
| [[SRP54]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.79 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 670 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTR2]] | -0.65 | -0.74 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC13]] | C | SEC13's natural level strengthens COPA's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.08; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.897). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -32.5); signed map (-50.9, 9.8). **Vector** length 123, 55.5% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.72 to 10); *COPII-mediated vesicle transport* (reactome, mean cos +0.77 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.68 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +8.0 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +7.7 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.2 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.0 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.9 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -14.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:160,288,594-160,343,566 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HEP-COP, alpha-COP |
| Gene groups (HGNC) | WD repeat domain containing; Receptor ligands; Coat protein complex I |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P53621](https://www.uniprot.org/uniprotkb/P53621) (Coatomer subunit alpha):

> The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. Coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. In mammals, the coatomer can only be recruited by membranes associated to ADP-ribosylation …

**Summary**, from NCBI Gene [1314](https://www.ncbi.nlm.nih.gov/gene/1314):

> In eukaryotic cells, protein transport between the endoplasmic reticulum and Golgi compartments is mediated in part by non-clathrin-coated vesicular coat proteins (COPs). Seven coat proteins have been identified, and they represent subunits of a complex known as coatomer. The subunits are designated alpha-COP, beta-COP, beta-prime-COP, gamma-COP, delta-COP, epsilon-COP, and zeta-COP. The alpha-COP, encoded by COPA, shares high sequence similarity with RET1P, the alpha subunit of the coatomer …

**Accessions** — [HGNC:2230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2230) · Entrez [1314](https://www.ncbi.nlm.nih.gov/gene/1314) · UniProt [P53621](https://www.uniprot.org/uniprotkb/P53621) · Ensembl [ENSG00000122218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122218)

## Data

Gene col 4325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4325); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4325]; `tensor/DDL_lfc|DDL_z.npy` [4325]; `embed/gene_vectors.npy` [4325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4325 or target_col == 4325). Every well: [[COPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
