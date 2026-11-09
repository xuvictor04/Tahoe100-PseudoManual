---
symbol: "GNAL"
type: "gene"
col: 6513
ensembl_id: "ENSG00000141404"
name: "G protein subunit alpha L"
location: "18p11.21"
module: 102
arm: "+"
pooled_cpm: 19.68
n_lines_expressing: 46
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# GNAL

*G protein subunit alpha L* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +29.1, q 0e+00, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.914× (z -5.4, q 3e-05, down in 7 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.805× (z -3.9, q 0.023, down in 16 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAIN1]] (+0.66, fdr 7e-06), [[ATP6V1E2]] (+0.65, fdr 1e-05), [[CDH23]] (+0.62, fdr 1e-05); moves opposite to [[CBY1]] (-0.55, fdr 6e-05), [[ZBTB48]] (-0.54, fdr 7e-05), [[HAUS3]] (-0.53, fdr 4e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[PAX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +29.1 | 0e+00 | 34/41 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +17.4 | 0e+00 | 34/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +16.5 | 0e+00 | 21/29 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +11.7 | 1e-29 | 25/41 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +11.7 | 1e-29 | 30/41 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +11.6 | 5e-29 | 23/37 (AsPC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +11.5 | 1e-28 | 32/43 (PANC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +10.7 | 5e-25 | 15/22 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +9.7 | 1e-20 | 20/41 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +6.6 | 2e-09 | 14/43 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.1 | 7e-08 | 21/39 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +6.0 | 9e-08 | 15/43 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.7 | 4e-07 | 13/43 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.7 | 5e-07 | 15/44 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.4 | 2e-06 | 12/36 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +5.4 | 2e-06 | 12/42 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.2 | 5e-06 | 15/41 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.003 | 14/39 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.050 | 5/44 (NCI-H2030, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -5.4 | 3e-05 | 7/44 (HepG2/C3A, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.023 | 16/43 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.810×** | -3.8 | 0.024 | 5/41 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.054 | 14/42 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.4 | 0.072 | 7/39 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.704×** | -3.3 | 0.072 | 12/39 (NCI-H23, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.072 | 12/38 (H4, AsPC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.881× | -3.2 | 0.085 | 6/44 (HCT15, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 148 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 94.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0860× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -13.6) |
| [[RKO (line)]] | wt | 52.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0656× (z -28.1) |
| [[SNU-1 (line)]] | wt | 65.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 13.3 | 3 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.28× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.0) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.236× (z -10.2) |
| [[PANC-1 (line)]] | alt | 8.29 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.95× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 9.91 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +14.2) | — |
| [[HS-578T (line)]] | alt | 7.41 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +10.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -9.1) |
| [[LoVo (line)]] | wt | 40.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.336× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 22.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +15.0) | — |
| [[A-172 (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +8.8) | — |
| [[A498 (line)]] | wt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.9) | — |
| [[A549 (line)]] | wt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 5.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 8.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 8.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +8.7) | — |
| [[J82 (line)]] | alt | 5.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 6.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.38× (z +9.4) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 33.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 8.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 7.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 8.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 5.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAIN1]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ATP6V1E2]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[CDH23]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 | pathway: Sensory Perception |
| [[ASIC2]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MEGF11]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[GRID1]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[FAM184A]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[LINC01122]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[DLGAP1]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 | pathway: Neuronal System |
| [[BCL2]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[BEND3]] | +0.56 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[SDK2]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBY1]] | -0.55 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[ZBTB48]] | -0.54 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[HAUS3]] | -0.53 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[GPATCH11]] | -0.51 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[TMEM175]] | -0.51 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[SENP2]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[DNAL4]] | -0.49 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[KIAA0319L]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[NPHP1]] | -0.47 | -0.21 / -0.38 | both halves | 7e-04 |  |
| [[C6orf89]] | -0.47 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[KRBOX4]] | -0.47 | -0.55 / -0.43 | both halves | 4e-05 |  |
| [[ISCA2]] | -0.47 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX2]] | B | PAX2 activity raises GNAL's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without PAX2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[KCND3]] | B | KCND3 activity raises GNAL's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without KCND3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[HRK]] | B | HRK activity raises GNAL's level | lines that do not express HRK (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without HRK | 0.011 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |
| [[MSI1]] | B | MSI1 activity raises GNAL's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without MSI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[TOP2A]] | B | TOP2A activity lowers GNAL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BTNL9]] | B | BTNL9 activity raises GNAL's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.18× lower at baseline in the lines without BTNL9 | 0.047 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[FTCDNL1]] | B | FTCDNL1 activity raises GNAL's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 2.40× lower at baseline in the lines without FTCDNL1 | 0.049 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[CACNG2]] | B | CACNG2 activity lowers GNAL's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 2.50× higher at baseline in the lines without CACNG2 | 0.079 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[PRDM6]] | B | PRDM6 activity raises GNAL's level | lines that do not express PRDM6 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without PRDM6 | 0.081 | ⚠ within organs, on part of the lines; also absent: GALNT8, RHBDL3, ASGR1; maybe low, not absent |
| [[EMID1]] | B | EMID1 activity raises GNAL's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without EMID1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[LRRN2]] | B | LRRN2 activity raises GNAL's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without LRRN2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[MED12L]] | B | MED12L activity raises GNAL's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without MED12L | 0.091 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.0, 34.1); signed map (38.0, -0.1). **Vector** length 82.6, 15.6% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +17.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +29.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +5.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.4 | +3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.9 | +6.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:11,689,264-11,885,685 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits alpha, group s |
| Reactome | 15 pathways, smallest: Adenylate cyclase activating pathway; Adenylate cyclase inhibitory pathway; Olfactory Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P38405](https://www.uniprot.org/uniprotkb/P38405) (Guanine nucleotide-binding protein G(olf) subunit alpha):

> Guanine nucleotide-binding protein (G protein) involved as transducer in olfactory signal transduction controlled by G protein-coupled receptors (GPCRs) (By similarity). Contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state (By similarity). Signaling by an activated GPCR promotes GDP release and GTP binding (By similarity). The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby terminating the …

**Summary**, from NCBI Gene [2774](https://www.ncbi.nlm.nih.gov/gene/2774):

> This gene encodes a stimulatory G protein alpha subunit which mediates odorant signaling in the olfactory epithelium. This protein couples dopamine type 1 receptors and adenosine A2A receptors and is widely expressed in the central nervous system. Mutations in this gene have been associated with dystonia 25 and this gene is located in a susceptibility region for bipolar disorder and schizophrenia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:4388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4388) · Entrez [2774](https://www.ncbi.nlm.nih.gov/gene/2774) · UniProt [P38405](https://www.uniprot.org/uniprotkb/P38405) · Ensembl [ENSG00000141404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141404)

## Data

Gene col 6513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6513); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6513]; `tensor/DDL_lfc|DDL_z.npy` [6513]; `embed/gene_vectors.npy` [6513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6513 or target_col == 6513). Every well: [[GNAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
