---
symbol: "PHC2"
type: "gene"
col: 5588
ensembl_id: "ENSG00000134686"
name: "polyhomeotic homolog 2"
location: "1p35.1"
module: 174
arm: "+"
pooled_cpm: 109.17
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 46
n_dd_up_clean: 6
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# PHC2

*polyhomeotic homolog 2* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.56× (z +6.9, q 2e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -12.7, q 3e-34, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4]] (+0.84, fdr 7e-06), [[PTPN12]] (+0.79, fdr 7e-06), [[ITGB5]] (+0.79, fdr 7e-06); moves opposite to [[GIPC2]] (-0.64, fdr 3e-05), [[MATN2]] (-0.61, fdr 3e-05), [[RAB21]] (-0.56, fdr 6e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[LINC01812]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.9 | 2e-09 | 33/48 (SW48, SW1417, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +6.9 | 2e-09 | 29/48 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +6.5 | 1e-08 | 33/48 (SW480, SW48, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.0 | 7e-05 | 34/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.35×** | +4.7 | 3e-04 | 24/48 (SW48, SW1417, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.0 | 0.005 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.062 | 20/48 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.077 | 23/49 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LB-100 (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.10 | 16/48 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.14 | 16/48 (A549, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -12.7 | 3e-34 | 35/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.479×** | -12.0 | 1e-30 | 43/50 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.560×** | -11.3 | 2e-27 | 42/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.486×** | -11.2 | 4e-27 | 41/49 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.526×** | -10.5 | 1e-23 | 43/49 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -10.2 | 2e-22 | 33/49 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.516×** | -9.9 | 3e-21 | 40/47 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.524×** | -9.7 | 3e-20 | 38/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -9.4 | 3e-19 | 33/43 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.609×** | -9.2 | 1e-18 | 38/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.583×** | -8.4 | 2e-15 | 37/47 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.606×** | -7.8 | 3e-13 | 36/49 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.595×** | -7.5 | 3e-12 | 39/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.711×** | -7.4 | 4e-12 | 36/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.713×** | -7.3 | 1e-11 | 37/49 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.636×** | -7.1 | 6e-11 | 34/48 (H4, C32, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.736×** | -6.7 | 6e-10 | 36/48 (C32, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 530 | 0 | 28 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -21.5) |
| [[SK-MEL-2 (line)]] | alt | 190 | 0 | 23 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -20.8) |
| [[NCI-H460 (line)]] | wt | 78.7 | 0 | 19 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.2) |
| [[HOP62 (line)]] | alt | 246 | 0 | 18 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.551× (z -16.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.1) |
| [[RKO (line)]] | wt | 598 | 0 | 12 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -19.5) |
| [[RPMI-7951 (line)]] | alt | 247 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 145 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.338× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 6 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.539× (z -16.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.0) |
| [[H4 (line)]] | wt | 137 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 116 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.368× (z -27.2) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 78.6 | 0 | 5 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.357× (z -9.3) |
| [[SW 900 (line)]] | alt | 178 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -11.8) |
| [[SW48 (line)]] | wt | 68.8 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.96× (z +9.2) | — |
| [[SW480 (line)]] | alt | 120 | 2 | 3 | [[Tucidinostat (drug)]] 5 µM 1.73× (z +10.0) | [[Trametinib (drug)]] 0.5 µM 0.554× (z -9.5) |
| [[A-172 (line)]] | wt | 72.8 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.212× (z -12.7) |
| [[A549 (line)]] | wt | 84.1 | 0 | 4 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.297× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 65.4 | 1 | 1 | [[Belinostat (drug)]] 5 µM 2.87× (z +8.8) | [[Binimetinib (drug)]] 0.5 µM 0.409× (z -8.7) |
| [[C-33 A (line)]] | alt | 55.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0827× (z -21.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 97.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 87.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 91.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.5) |
| [[SNU-423 (line)]] | alt | 133 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -14.2) |
| [[SW 1271 (line)]] | alt | 142 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0603× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -8.5) |
| [[AN3 CA (line)]] | alt | 82.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -11.7) |
| [[CHP-212 (line)]] | wt | 95.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 80.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 97.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.9) |
| [[HS-578T (line)]] | alt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 195 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -11.3) |
| [[PANC-1 (line)]] | alt | 94.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -8.7) |
| [[A-427 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4]] | +0.84 | +0.86 / +0.88 | both halves | 7e-06 |  |
| [[PTPN12]] | +0.79 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[STX1A]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[RGS17]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[NPAS2]] | +0.72 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.71 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ETV5]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SPRED2]] | +0.70 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[ST3GAL1]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIPC2]] | -0.64 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[MATN2]] | -0.61 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[RAB21]] | -0.56 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[ZCCHC8]] | -0.56 | -0.59 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01812]] | B | LINC01812 activity raises PHC2's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.00× lower at baseline in the lines without LINC01812 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[HTR7]] | B | HTR7 activity raises PHC2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without HTR7 | 0.027 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[ITPRIP]] | B | ITPRIP activity raises PHC2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without ITPRIP | 0.028 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[SERPINE1]] | B | SERPINE1 activity raises PHC2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without SERPINE1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[DUSP5]] | B | DUSP5 activity raises PHC2's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.36× lower at baseline in the lines without DUSP5 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[ITPRIP]] | B | ITPRIP activity strengthens PHC2's drug response | lines that do not express ITPRIP (10) vs lines expressing it (40) | the lines without ITPRIP respond 0.54× as strongly (z diff +2.46); strongest at Dinaciclib 5 µM: 0.82x vs 0.45x (z diff +3.4) | 0.049 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent; artifact flags |
| [[NPAS2]] | B | NPAS2 activity raises PHC2's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without NPAS2 | 0.052 | ⚠ within organs, on part of the lines |
| [[STC1]] | B | STC1 activity raises PHC2's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without STC1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[ITGB3]] | B | ITGB3 activity raises PHC2's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 1.47× lower at baseline in the lines without ITGB3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[C13orf46]] | B | C13orf46 activity raises PHC2's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without C13orf46 | 0.057 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PHC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PHC2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.883). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.1, 5.5); signed map (7.1, 48.5). **Vector** length 160, 57.7% of its response variance represented; |z| ≥ 3 in 1,674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +9.1 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.4 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +7.5 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.8 | +6.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +4.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.4 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +1.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -14.3 | -12.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -13.4 | -11.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -12.9 | -10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -12.3 | -9.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -11.8 | -11.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -11.6 | -9.2 |

## What is on record

|  |  |
|---|---|
| Name | polyhomeotic homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:33,323,623-33,431,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPH2; previously EDR2 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; MicroRNA protein coding host genes |
| Reactome | 19 pathways, smallest: SUMOylation of DNA methylation proteins; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXK0](https://www.uniprot.org/uniprotkb/Q8IXK0) (Polyhomeotic-like protein 2):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility.

**Summary**, from NCBI Gene [1912](https://www.ncbi.nlm.nih.gov/gene/1912):

> In Drosophila melanogaster, the 'Polycomb' group (PcG) of genes are part of a cellular memory system that is responsible for the stable inheritance of gene activity. PcG proteins form a large multimeric, chromatin-associated protein complex. The protein encoded by this gene has homology to the Drosophila PcG protein 'polyhomeotic' (Ph) and is known to heterodimerize with EDR1 and colocalize with BMI1 in interphase nuclei of human cells. The specific function in human cells has not yet been …

**Accessions** — [HGNC:3183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3183) · Entrez [1912](https://www.ncbi.nlm.nih.gov/gene/1912) · UniProt [Q8IXK0](https://www.uniprot.org/uniprotkb/Q8IXK0) · Ensembl [ENSG00000134686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134686)

## Data

Gene col 5588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5588); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5588]; `tensor/DDL_lfc|DDL_z.npy` [5588]; `embed/gene_vectors.npy` [5588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5588 or target_col == 5588). Every well: [[PHC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
