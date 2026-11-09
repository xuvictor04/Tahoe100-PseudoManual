---
symbol: "COL13A1"
type: "gene"
col: 12403
ensembl_id: "ENSG00000197467"
name: "collagen type XIII alpha 1 chain"
location: "10q22.1"
module: 84
arm: "+"
pooled_cpm: 25.54
n_lines_expressing: 39
n_dd_up: 1
n_dd_down: 55
n_dd_up_clean: 1
n_dd_down_clean: 48
in_vector_space: true
direction_upstream: 30
direction_downstream: 28
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# COL13A1

*collagen type XIII alpha 1 chain* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +4.8, q 0.001, up in 21 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 3.51×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 2.47×).
> Pooled over the cell lines (median), lowered significantly by 55 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.182× (z -23.8, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA3]] (+0.72, fdr 7e-06), [[SHC4]] (+0.68, fdr 7e-06), [[RASA3]] (+0.67, fdr 7e-06); moves opposite to [[RAB32]] (-0.56, fdr 1e-05), [[SETD2]] (-0.56, fdr 1e-05), [[SLC3A2]] (-0.55, fdr 2e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[ITGB3]] → it (grade B ⚠); 28 go from it, the strongest it → [[FXYD5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12403.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 3.51×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 2.47×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.8 | 0.001 | 21/37 (SW480, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.41× | +3.4 | 0.14 | 13/37 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 1.40× | +3.4 | 0.14 | 16/37 (HOP62, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 1.37× | +3.2 | 0.21 | 9/36 (A-172, HOP62, …) | two highest doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.23 | 8/37 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.23 | 11/37 (H4, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 55 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.182×** | -23.8 | 0e+00 | 36/36 (C32, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.165×** | -17.1 | 0e+00 | 36/37 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.220×** | -15.0 | 0e+00 | 34/36 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.297×** | -12.0 | 5e-31 | 33/37 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.325×** | -11.1 | 1e-26 | 30/37 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.372×** | -9.8 | 2e-20 | 29/36 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.500×** | -9.7 | 3e-20 | 28/37 (C32, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.389×** | -8.9 | 4e-17 | 30/37 (C32, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.424×** | -8.5 | 2e-15 | 30/37 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.411×** | -8.4 | 2e-15 | 29/36 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.499×** | -8.3 | 5e-15 | 28/37 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -8.3 | 7e-15 | 28/35 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.440×** | -8.1 | 2e-14 | 26/37 (C32, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.482×** | -6.8 | 4e-10 | 27/36 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.525×** | -6.3 | 8e-09 | 23/36 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.605×** | -6.0 | 6e-08 | 22/37 (C32, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 120 | 0 | 33 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0162× (z -34.1) |
| [[NCI-H460 (line)]] | wt | 27.5 | 0 | 22 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -17.2) |
| [[H4 (line)]] | wt | 117 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -17.9) |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0731× (z -20.5) |
| [[HOP62 (line)]] | alt | 95.8 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -21.1) |
| [[Hs 766T (line)]] | wt | 45.5 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.0245× (z -31.3) |
| [[RPMI-7951 (line)]] | alt | 96.7 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0656× (z -21.2) |
| [[BT-474 (line)]] | alt | 45.4 | 0 | 9 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0164× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 35.9 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -19.6) |
| [[HS-578T (line)]] | alt | 44.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0639× (z -20.9) |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -21.6) |
| [[A-172 (line)]] | wt | 35.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -23.6) |
| [[J82 (line)]] | alt | 13.3 | 0 | 6 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0751× (z -11.1) |
| [[LoVo (line)]] | wt | 10.7 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.7) | [[Belumosudil (drug)]] 5 µM 0.116× (z -12.4) |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 8.76 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 53.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.2) |
| [[RKO (line)]] | wt | 11.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -10.9) |
| [[SNU-423 (line)]] | alt | 74.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0705× (z -21.3) |
| [[SW480 (line)]] | alt | 19.2 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.47× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.185× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 39.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -12.1) |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.1) |
| [[A549 (line)]] | wt | 8.62 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0822× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 7.80 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0759× (z -9.5) |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0736× (z -8.9) |
| [[HCT15 (line)]] | alt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.8) |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0607× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.5) |
| [[A-427 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA3]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SHC4]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[RASA3]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TRIB2]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ITGB3]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SPRED2]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[PHC2]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 | pathway: Extracellular matrix organization |
| [[CPNE5]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ARPC2]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[IL1RAP]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB32]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SETD2]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SLC3A2]] | -0.55 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TLK1]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[RNF115]] | -0.53 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 28, C 2. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB3]] | B | ITGB3 activity raises COL13A1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.40× lower at baseline in the lines without ITGB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[FN1]] | B | FN1 activity raises COL13A1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 3.74× lower at baseline in the lines without FN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[COL4A2]] | B | COL4A2 activity raises COL13A1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 2.71× lower at baseline in the lines without COL4A2 | 0.017 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1 |
| [[SETBP1]] | B | SETBP1 activity raises COL13A1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.75× lower at baseline in the lines without SETBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[PLAT]] | B | PLAT activity raises COL13A1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 3.42× lower at baseline in the lines without PLAT | 0.024 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[UBASH3B]] | B | UBASH3B activity raises COL13A1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without UBASH3B | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[ZNF215]] | B | ZNF215 activity raises COL13A1's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 2.76× lower at baseline in the lines without ZNF215 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[HTR7]] | B | HTR7 activity raises COL13A1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.94× lower at baseline in the lines without HTR7 | 0.033 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[COL15A1]] | B | COL15A1 activity raises COL13A1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 3.63× lower at baseline in the lines without COL15A1 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[APLN]] | B | APLN activity raises COL13A1's level | lines that do not express APLN (13) vs lines expressing it (37) | 2.42× lower at baseline in the lines without APLN | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[C12orf75-AS1]] | B | C12orf75-AS1 activity raises COL13A1's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without C12orf75-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[INSYN2B]] | B | INSYN2B activity raises COL13A1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.52× lower at baseline in the lines without INSYN2B | 0.052 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 27, C 1. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FXYD5]] | B | COL13A1 activity raises FXYD5's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without COL13A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[STAMBPL1]] | B | COL13A1 activity raises STAMBPL1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without COL13A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[S100A16]] | B | COL13A1 activity raises S100A16's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.62× lower at baseline in the lines without COL13A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[EHBP1L1]] | B | COL13A1 activity raises EHBP1L1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without COL13A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[SSH1]] | B | COL13A1 activity raises SSH1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without COL13A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[WWTR1]] | B | COL13A1 activity raises WWTR1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.74× lower at baseline in the lines without COL13A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[PDLIM7]] | B | COL13A1 activity raises PDLIM7's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without COL13A1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[TRIOBP]] | B | COL13A1 activity raises TRIOBP's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without COL13A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[KCNN4]] | B | COL13A1 activity raises KCNN4's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.19× lower at baseline in the lines without COL13A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[AMOTL1]] | B | COL13A1 activity raises AMOTL1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 4.02× lower at baseline in the lines without COL13A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[LINC03009-1]] | B | COL13A1 activity raises LINC03009-1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without COL13A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[PCDHGC3]] | B | COL13A1 activity raises PCDHGC3's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.92× lower at baseline in the lines without COL13A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 6.2); signed map (6.3, 50.4). **Vector** length 129, 43.3% of its response variance represented; |z| ≥ 3 in 1,501 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.1 | -8.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.1 | -8.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.3 | -8.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.1 | -8.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.6 | -5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.5 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XIII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,801,880-69,964,275 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Membrane associated collagens with interrupted triple helices |
| Reactome | 7 pathways, smallest: Collagen chain trimerization; Collagen degradation; Collagen biosynthesis and modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TAT6](https://www.uniprot.org/uniprotkb/Q5TAT6) (Collagen alpha-1(XIII) chain):

> Involved in cell-matrix and cell-cell adhesion interactions that are required for normal development. May participate in the linkage between muscle fiber and basement membrane. May play a role in endochondral ossification of bone and branching morphogenesis of lung. Binds heparin. At neuromuscular junctions, may play a role in acetylcholine receptor clustering.

**Summary**, from NCBI Gene [1305](https://www.ncbi.nlm.nih.gov/gene/1305):

> This gene encodes the alpha chain of one of the nonfibrillar collagens. The function of this gene product is not known, however, it has been detected at low levels in all connective tissue-producing cells so it may serve a general function in connective tissues. Unlike most of the collagens, which are secreted into the extracellular matrix, collagen XIII contains a transmembrane domain and the protein has been localized to the plasma membrane. The transcripts for this gene undergo complex and …

**Accessions** — [HGNC:2190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2190) · Entrez [1305](https://www.ncbi.nlm.nih.gov/gene/1305) · UniProt [Q5TAT6](https://www.uniprot.org/uniprotkb/Q5TAT6) · Ensembl [ENSG00000197467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197467)

## Data

Gene col 12403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12403); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12403]; `tensor/DDL_lfc|DDL_z.npy` [12403]; `embed/gene_vectors.npy` [12403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12403 or target_col == 12403). Every well: [[COL13A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL13A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
