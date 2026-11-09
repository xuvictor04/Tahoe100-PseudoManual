---
symbol: "DDHD2"
type: "gene"
col: 1440
ensembl_id: "ENSG00000085788"
name: "DDHD domain containing 2"
location: "8p11.23"
module: 175
arm: "+"
pooled_cpm: 50.08
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# DDHD2

*DDHD domain containing 2* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.42× (z +6.8, q 5e-09, up in 21 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 2.10×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -17.2, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB10]] (+0.63, fdr 7e-06), [[FAM234B]] (+0.63, fdr 1e-05), [[EXD2]] (+0.62, fdr 1e-05); moves opposite to [[NFE2L2]] (-0.61, fdr 1e-05), [[ADNP2]] (-0.59, fdr 1e-05), [[TUT7]] (-0.57, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CERCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 2.10×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.8 | 5e-09 | 21/40 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.9 | 0.031 | 18/48 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.14 | 0/48 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -17.2 | 0e+00 | 38/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.555×** | -11.8 | 1e-29 | 43/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -9.1 | 2e-17 | 37/48 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.637×** | -9.0 | 2e-17 | 38/48 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.664×** | -8.2 | 3e-14 | 35/48 (SNU-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -8.1 | 4e-14 | 36/48 (J82, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -7.8 | 7e-13 | 33/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.675×** | -7.6 | 2e-12 | 35/48 (NCI-H1792, HOP62, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -7.1 | 9e-11 | 34/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.722×** | -6.3 | 2e-08 | 29/47 (NCI-H460, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -5.6 | 9e-07 | 32/48 (HOP62, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.756×** | -5.6 | 1e-06 | 22/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -5.6 | 1e-06 | 28/48 (HS-578T, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.758×** | -5.6 | 1e-06 | 27/48 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.770×** | -5.2 | 6e-06 | 24/48 (A-427, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -4.9 | 3e-05 | 25/48 (J82, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.876× | -3.7 | 0.005 | 9/49 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.900× | -3.0 | 0.064 | 3/48 (H4, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -12.7) |
| [[H4 (line)]] | wt | 67.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 79.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 48.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -18.1) |
| [[A-172 (line)]] | wt | 106 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -12.6) |
| [[AN3 CA (line)]] | alt | 68.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.4) |
| [[HS-578T (line)]] | alt | 80.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -20.3) |
| [[J82 (line)]] | alt | 73.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 23.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 59.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.3) |
| [[SNU-1 (line)]] | wt | 91.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0879× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.7) |
| [[A-427 (line)]] | wt | 70.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.1) |
| [[C-33 A (line)]] | alt | 107 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.381× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 44.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.1) |
| [[HCT15 (line)]] | alt | 79.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -9.1) |
| [[HOP62 (line)]] | alt | 56.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -19.1) |
| [[Hs 766T (line)]] | wt | 75.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.2) |
| [[KATO III (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.51× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 41.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 79.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 62.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.377× (z -9.5) |
| [[PANC-1 (line)]] | alt | 26.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -9.9) |
| [[RKO (line)]] | wt | 41.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -15.0) |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.3) |
| [[SW480 (line)]] | alt | 44.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.521× (z -8.7) |
| [[A498 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.63 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[EXD2]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A30]] | +0.62 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ANKRD36B]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[IARS2]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF25]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[MYH10]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MAN1B1]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[PGM2]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[AKTIP]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[HACE1]] | +0.59 | +0.73 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFE2L2]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ADNP2]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[TUT7]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TAF7]] | -0.56 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[SON]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[JAGN1]] | -0.53 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RBBP6]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DNTTIP2]] | -0.52 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.51 | -0.32 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | CERCAM activity raises DDHD2's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without CERCAM | 0.040 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[FKBP10]] | B | FKBP10 activity raises DDHD2's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without FKBP10 | 0.091 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.3, -12.0); signed map (-36.1, -15.8). **Vector** length 102, 25.0% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.4 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +3.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.1 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Tomivosertib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.2 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -3.2 | -6.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | DDHD domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,225,218-38,275,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0725, SPG54, p125B, iPLA1gamma, iPLA1γ; previously SAMWD1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O94830](https://www.uniprot.org/uniprotkb/O94830) (Triacylglycerol hydrolase DDHD2):

> Diacylglycerol (DAG) and triacylglycerol (TAG) lipase required for proper lipid homeostasis in the central nervous system. It cooperates with PNPLA2/ATGL in neuronal TAG catabolism and hydrolyzes sn-1,3 DAG downstream of PNPLA2/ATGL (By similarity). In vitro, it also acts as a phospholipase that hydrolyzes preferentially phosphatidic acids, including 1,2-dioleoyl-sn-phosphatidic acid, phosphatidylcholine and phosphatidylethanolamine. Specifically binds to phosphatidylinositol 3-phosphate …

**Summary**, from NCBI Gene [23259](https://www.ncbi.nlm.nih.gov/gene/23259):

> This gene encodes a phospholipase enzyme containing sterile-alpha-motif (SAM), WWE, and DDHD domains. This protein participates in membrane trafficking between the endoplastic reticulum and the Golgi body. Mutations in this gene can cause autosomal recessive spastic paraplegia 54. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:29106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29106) · Entrez [23259](https://www.ncbi.nlm.nih.gov/gene/23259) · UniProt [O94830](https://www.uniprot.org/uniprotkb/O94830) · Ensembl [ENSG00000085788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085788)

## Data

Gene col 1440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1440); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1440]; `tensor/DDL_lfc|DDL_z.npy` [1440]; `embed/gene_vectors.npy` [1440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1440 or target_col == 1440). Every well: [[DDHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
