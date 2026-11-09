---
symbol: "MTSS1"
type: "gene"
col: 10016
ensembl_id: "ENSG00000170873"
name: "MTSS I-BAR domain containing 1"
location: "8q24.13"
module: 84
arm: "+"
pooled_cpm: 128.5
n_lines_expressing: 30
n_dd_up: 2
n_dd_down: 41
n_dd_up_clean: 2
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 14
direction_downstream: 24
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# MTSS1

*MTSS I-BAR domain containing 1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +6.7, q 1e-08, up in 9 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 5.09×); [[Econazole (drug)]] 5 µM in 1 line (NCI-H1573 5.06×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 5.01×).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.609× (z -12.8, q 5e-35, down in 19 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB3]] (+0.63, fdr 7e-06), [[MARCHF3]] (+0.61, fdr 1e-05), [[TMEM255B]] (+0.60, fdr 1e-05); moves opposite to [[ABCC2]] (-0.48, fdr 4e-05), [[FIGN]] (-0.47, fdr 4e-05), [[ZSCAN31]] (-0.47, fdr 9e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TNS1]] → it (grade B ⚠); 24 go from it, the strongest it → [[SMOX]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10016.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 5.09×); [[Econazole (drug)]] 5 µM in 1 line (NCI-H1573 5.06×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 5.01×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.7 | 1e-08 | 9/28 (HT-29, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +5.4 | 2e-05 | 9/29 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 18 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.609×** | -12.8 | 5e-35 | 19/28 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -9.6 | 3e-19 | 19/28 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.698×** | -9.3 | 3e-18 | 21/28 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -8.6 | 1e-15 | 23/28 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.641×** | -7.5 | 5e-12 | 16/28 (CFPAC-1, SW 900, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -7.5 | 5e-12 | 22/28 (C32, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -7.1 | 1e-10 | 20/28 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -6.6 | 4e-09 | 21/26 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.693×** | -6.5 | 7e-09 | 18/24 (HS-578T, Hs 766T, …) | inconsistent across doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -6.0 | 9e-08 | 19/28 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.724×** | -5.7 | 7e-07 | 17/28 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.771×** | -5.6 | 1e-06 | 16/28 (CFPAC-1, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.802×** | -5.5 | 1e-06 | 16/29 (CFPAC-1, SW 900, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.752×** | -5.2 | 8e-06 | 17/28 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.755×** | -5.1 | 1e-05 | 15/27 (SW 900, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.821×** | -4.3 | 3e-04 | 17/28 (CFPAC-1, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.793×** | -4.2 | 6e-04 | 18/29 (A-172, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 162 | 0 | 20 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -26.8) |
| [[RPMI-7951 (line)]] | alt | 458 | 0 | 20 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0936× (z -29.5) |
| [[HOP62 (line)]] | alt | 213 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -22.1) |
| [[C32 (line)]] | wt | 123 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -23.0) |
| [[Hs 766T (line)]] | wt | 1,942 | 0 | 17 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -26.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -18.1) |
| [[A-172 (line)]] | wt | 143 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -18.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -16.2) |
| [[HS-578T (line)]] | alt | 571 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -25.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 344 | 0 | 14 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -24.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 53.8 | 10 | 2 | [[Dexamethasone (drug)]] 0.05 µM 5.09× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 141 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 276 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -16.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.205× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 439 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -27.8) |
| [[SW 900 (line)]] | alt | 165 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -16.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.4) |
| [[J82 (line)]] | alt | 118 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -15.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.6) |
| [[PANC-1 (line)]] | alt | 65.1 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -18.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.1) |
| [[BT-474 (line)]] | alt | 148 | 0 | 6 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.272× (z -10.4) ⚠ cell-cycle shift, explains ~73% of this change |
| [[KATO III (line)]] | alt | 66.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -10.8) |
| [[HT-29 (line)]] | alt | 39.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 74.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-427 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 24.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 30.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB3]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MARCHF3]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TMEM255B]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RAC2]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ITPR1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TREM1]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[STX1A]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RGS17]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[FLT1]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ST3GAL1]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[WDFY2]] | +0.55 | +0.60 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC2]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[FIGN]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZSCAN31]] | -0.47 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[SEMA3E]] | -0.46 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ACTR3C]] | -0.46 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[NFIB]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[BLTP3A]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS1]] | B | TNS1 activity raises MTSS1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.92× lower at baseline in the lines without TNS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[CSPG4]] | B | CSPG4 activity raises MTSS1's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.86× lower at baseline in the lines without CSPG4 | 0.018 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[NAV2]] | B | NAV2 activity raises MTSS1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.36× lower at baseline in the lines without NAV2 | 0.039 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[MAP2K1]] | B | MAP2K1 activity raises MTSS1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.1% of all compounds | 0.042 | ⚠ off-target possible; 4 compounds |
| [[GNA15]] | B | GNA15 activity raises MTSS1's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without GNA15 | 0.067 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[TMEM255B]] | B | TMEM255B activity raises MTSS1's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without TMEM255B | 0.077 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[IL1B]] | B | IL1B activity raises MTSS1's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.75× lower at baseline in the lines without IL1B | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[ABTB3]] | B | ABTB3 activity raises MTSS1's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.34× lower at baseline in the lines without ABTB3 | 0.088 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises MTSS1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.57× lower at baseline in the lines without ST3GAL1 | 0.090 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[ZNF385D]] | B | ZNF385D activity raises MTSS1's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.30× lower at baseline in the lines without ZNF385D | 0.091 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[SPOCK1]] | B | SPOCK1 activity raises MTSS1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 2.32× lower at baseline in the lines without SPOCK1 | 0.095 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[CREG2]] | B | CREG2 activity raises MTSS1's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without CREG2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 21, C 3. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMOX]] | B | MTSS1 activity raises SMOX's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without MTSS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[CD82]] | B | MTSS1 activity raises CD82's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without MTSS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[RGS17]] | B | MTSS1 activity raises RGS17's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without MTSS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[ADGRE2]] | B | MTSS1 activity strengthens ADGRE2's drug response | lines that do not express MTSS1 (10) vs lines expressing it (13) | the lines without MTSS1 respond 0.95× as strongly (z diff +0.74); strongest at Trametinib 5 µM: 0.40x vs 0.23x (z diff +3.7) | 0.014 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1; target measured in part of the lines; artifact flags |
| [[TMEM255B]] | B | MTSS1 activity raises TMEM255B's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without MTSS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[IRAK2]] | B | MTSS1 activity raises IRAK2's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without MTSS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[CSPG4]] | B | MTSS1 activity raises CSPG4's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without MTSS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[EID3]] | B | MTSS1 activity lowers EID3's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.53× higher at baseline in the lines without MTSS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[GNA15]] | B | MTSS1 activity raises GNA15's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without MTSS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[BLTP3A]] | B | MTSS1 activity lowers BLTP3A's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.37× higher at baseline in the lines without MTSS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[RAC2]] | B | MTSS1 activity raises RAC2's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.66× lower at baseline in the lines without MTSS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[NAV1]] | B | MTSS1 activity raises NAV1's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without MTSS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.4, 3.5); signed map (2.4, 49.7). **Vector** length 123, 38.1% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.9 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.6 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.3 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.2 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[AT7519 (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.2 | -4.0 |
|  | [[NG25 (drug)]] 5 µM |  | -4.9 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | MTSS I-BAR domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:124,550,784-124,728,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0429, MIMA, MIMB, MIM |
| Gene groups (HGNC) | I-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43312](https://www.uniprot.org/uniprotkb/O43312) (Protein MTSS 1):

> May be related to cancer progression or tumor metastasis in a variety of organ sites, most likely through an interaction with the actin cytoskeleton.

**Summary**, from NCBI Gene [9788](https://www.ncbi.nlm.nih.gov/gene/9788):

> Enables actin monomer binding activity; identical protein binding activity; and signaling receptor binding activity. Predicted to be involved in several processes, including adherens junction maintenance; positive regulation of actin filament bundle assembly; and renal tubule development. Predicted to act upstream of or within several processes, including actin filament polymerization; bone mineralization; and magnesium ion homeostasis. Located in actin cytoskeleton. [provided by Alliance of …

**Accessions** — [HGNC:20443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20443) · Entrez [9788](https://www.ncbi.nlm.nih.gov/gene/9788) · UniProt [O43312](https://www.uniprot.org/uniprotkb/O43312) · Ensembl [ENSG00000170873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170873)

## Data

Gene col 10016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10016); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10016]; `tensor/DDL_lfc|DDL_z.npy` [10016]; `embed/gene_vectors.npy` [10016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10016 or target_col == 10016). Every well: [[MTSS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTSS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
