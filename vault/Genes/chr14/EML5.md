---
symbol: "EML5"
type: "gene"
col: 9138
ensembl_id: "ENSG00000165521"
name: "EMAP like 5"
location: "14q31.3"
module: 125
arm: "+"
pooled_cpm: 18.21
n_lines_expressing: 32
n_dd_up: 37
n_dd_down: 6
n_dd_up_clean: 30
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# EML5

*EMAP like 5* — 14q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.72× (z +20.2, q 0e+00, up in 24 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.563× (z -8.2, q 2e-13, down in 19 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.666× (z -5.8, q 2e-06, down in 16 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NGF]] (+0.58, fdr 1e-05), [[RPLP0P2]] (+0.58, fdr 1e-05), [[ROR1-AS1]] (+0.57, fdr 1e-05); moves opposite to [[PIGS]] (-0.50, fdr 7e-05), [[SMARCD2]] (-0.49, fdr 1e-04), [[NUP133]] (-0.47, fdr 1e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NPFFR2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NGF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.72×** | +20.2 | 0e+00 | 24/30 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +15.6 | 0e+00 | 18/29 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.39×** | +12.4 | 4e-33 | 23/28 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +11.0 | 7e-26 | 20/30 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +8.1 | 9e-14 | 3/14 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +8.0 | 9e-14 | 13/28 (A498, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +7.5 | 5e-12 | 17/29 (A498, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.1 | 7e-11 | 15/28 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +6.8 | 5e-10 | 14/29 (SK-MEL-2, A549, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +6.6 | 2e-09 | 12/29 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +5.9 | 2e-07 | 13/29 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +5.9 | 2e-07 | 11/29 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 2e-07 | 8/30 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +5.6 | 7e-07 | 9/30 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +5.5 | 2e-06 | 13/28 (NCI-H1573, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 3e-05 | 11/28 (LoVo, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.43×** | +4.9 | 3e-05 | 6/30 (SK-MEL-2, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -8.2 | 2e-13 | 19/27 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.597×** | -7.3 | 7e-11 | 19/30 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -5.8 | 2e-06 | 16/29 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.722×** | -4.6 | 6e-04 | 15/29 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.746×** | -4.2 | 0.004 | 8/29 (RPMI-7951, HS-578T, …) | two highest doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.099 | 3/30 (SW 1271, NCI-H2030, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 363 | 0 | 27 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -23.4) |
| [[LoVo (line)]] | wt | 47.7 | 3 (2 ⚠) | 5 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.96× (z +10.4) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.40× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.119× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.306× (z -9.0) |
| [[SW480 (line)]] | alt | 20.2 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.230× (z -11.6) |
| [[A-427 (line)]] | wt | 29.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -12.3) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A498 (line)]] | wt | 25.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.3) | — |
| [[COLO 205 (line)]] | alt | 5.53 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0799× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 21.4 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.22× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.45× (z +8.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0751× (z -13.3) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 63.7 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.49× (z +9.3) ⚠ unreliable plate only | [[Digitoxin (drug)]] 0.5 µM 0.214× (z -8.5) |
| [[J82 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.30 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.08× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 4.74 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0759× (z -8.9) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.5) | — |
| [[A-172 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGF]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.58 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ROR1-AS1]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NIBAN1]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ENTHD1]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[OSGIN1]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CRYM]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[KCNIP4]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[LINC01060]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ADAMTS16]] | +0.51 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[CREB5]] | +0.51 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ABCA13]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGS]] | -0.50 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[SMARCD2]] | -0.49 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[NUP133]] | -0.47 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[PIH1D1]] | -0.46 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[CDIPT]] | -0.46 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[KLHDC3]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PPP2R5C]] | -0.45 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[ZDHHC7]] | -0.43 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[FBXL20]] | -0.43 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[TPCN1]] | -0.42 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[ZBTB44]] | -0.42 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[MARF1]] | -0.41 | -0.43 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPFFR2]] | B | NPFFR2 activity raises EML5's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 1.74× lower at baseline in the lines without NPFFR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[NPL]] | B | NPL activity raises EML5's level | lines that do not express NPL (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without NPL | 0.060 | ⚠ within organs, on part of the lines; also absent: IQCJ-SCHIP1, NPR2, CAPS2; maybe low, not absent; its own permutation p |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises EML5's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without APCDD1L-DT | 0.099 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGF]] | B | EML5 activity raises NGF's level | lines that do not express EML5 (18) vs lines expressing it (32) | 1.39× lower at baseline in the lines without EML5 | 0.069 | ⚠ within organs, on part of the lines; also absent: HOXA7, DOCK3, ENPP4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, 20.7); signed map (36.1, 21.5). **Vector** length 72.7, 15.3% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +20.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +12.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +4.9 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | EMAP like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3 — chr14:88,612,431-88,792,953 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HuEMAP-2, EMAP-2, FAP16 |
| Gene groups (HGNC) | WD repeat domain containing; EMAP like |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05BV3](https://www.uniprot.org/uniprotkb/Q05BV3) (Echinoderm microtubule-associated protein-like 5):

> May modify the assembly dynamics of microtubules, such that microtubules are slightly longer, but more dynamic.

**Summary**, from NCBI Gene [161436](https://www.ncbi.nlm.nih.gov/gene/161436):

> Predicted to enable microtubule binding activity. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18197) · Entrez [161436](https://www.ncbi.nlm.nih.gov/gene/161436) · UniProt [Q05BV3](https://www.uniprot.org/uniprotkb/Q05BV3) · Ensembl [ENSG00000165521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165521)

## Data

Gene col 9138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9138); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9138]; `tensor/DDL_lfc|DDL_z.npy` [9138]; `embed/gene_vectors.npy` [9138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9138 or target_col == 9138). Every well: [[EML5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EML5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
