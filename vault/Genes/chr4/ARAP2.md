---
symbol: "ARAP2"
type: "gene"
col: 514
ensembl_id: "ENSG00000047365"
name: "ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 2"
location: "4p14"
module: 143
arm: "+"
pooled_cpm: 41.86
n_lines_expressing: 40
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 12
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ARAP2

*ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 2* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.29× (z +32.6, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.616× (z -7.7, q 8e-12, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRK]] (+0.70, fdr 1e-05), [[LINC00857]] (+0.64, fdr 3e-05), [[BTC]] (+0.64, fdr 3e-05); moves opposite to [[SNAPC3]] (-0.69, fdr 7e-06), [[MMS19]] (-0.68, fdr 1e-05), [[UNC45A]] (-0.66, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RASEF]] → it (grade B ⚠); 12 go from it, the strongest it → [[PTPRK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.29×** | +32.6 | 0e+00 | 36/38 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.09×** | +22.3 | 0e+00 | 36/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.10×** | +21.5 | 0e+00 | 36/38 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.14×** | +18.1 | 0e+00 | 36/38 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +15.1 | 0e+00 | 33/38 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.17×** | +12.2 | 2e-32 | 30/38 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.14×** | +12.0 | 3e-31 | 31/38 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.09×** | +11.6 | 2e-29 | 30/38 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +11.2 | 2e-27 | 28/38 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +8.7 | 3e-16 | 28/37 (NCI-H1792, SW 900, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +8.6 | 5e-16 | 18/32 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.2 | 3e-11 | 24/35 (NCI-H1792, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.8 | 3e-07 | 19/38 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +5.5 | 2e-06 | 21/39 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 4e-06 | 18/38 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.1 | 1e-05 | 18/38 (SW 900, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +4.9 | 3e-05 | 17/38 (BT-474, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.1 | 0.001 | 17/38 (C32, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.004 | 17/38 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.616×** | -7.7 | 8e-12 | 23/38 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -7.3 | 7e-11 | 25/38 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.730×** | -5.0 | 1e-04 | 20/38 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.856× | -3.5 | 0.068 | 10/38 (hTERT-HPNE, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 65.2 | 8 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 7.67× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 27.8 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +30.0) | — |
| [[SW 900 (line)]] | alt | 56.4 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +20.3) | — |
| [[NCI-H1573 (line)]] | alt | 154 | 7 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +28.0) | [[Panobinostat (drug)]] 5 µM 0.373× (z -11.0) |
| [[KATO III (line)]] | alt | 43.4 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.347× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 83.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +21.4) | — |
| [[COLO 205 (line)]] | alt | 33.7 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.215× (z -9.4) |
| [[HT-29 (line)]] | alt | 120 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.199× (z -17.2) |
| [[A-427 (line)]] | wt | 60.5 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.362× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 58.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +22.2) | — |
| [[HepG2_C3A (line)]] | wt | 37.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 103 | 2 | 3 | [[Harringtonine (drug)]] 5 µM 2.87× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.401× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 71.7 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.0) |
| [[SW480 (line)]] | alt | 34.4 | 4 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.79× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.390× (z -8.5) |
| [[A-172 (line)]] | wt | 12.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 95.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +25.8) | — |
| [[HEC-1-A (line)]] | alt | 78.4 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 2.83× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +15.6) | — |
| [[J82 (line)]] | alt | 16.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +14.7) | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +20.4) | — |
| [[SNU-423 (line)]] | alt | 14.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +20.6) | — |
| [[A549 (line)]] | wt | 10.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +12.8) | — |
| [[C32 (line)]] | wt | 12.2 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 12.6× (z +10.4) | — |
| [[H4 (line)]] | wt | 27.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +12.2) | — |
| [[LoVo (line)]] | wt | 52.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.359× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 14.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.3× (z +32.8) | — |
| [[PANC-1 (line)]] | alt | 11.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +28.2) | — |
| [[RKO (line)]] | wt | 95.0 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +8.9) | [[Selinexor (drug)]] 5 µM 0.411× (z -10.1) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.323× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 42.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +18.7) | — |
| [[A498 (line)]] | wt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.2) | — |
| [[SW48 (line)]] | wt | 95.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -9.1) |
| [[HCT15 (line)]] | alt | 61.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.08× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | +0.70 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[LINC00857]] | +0.64 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[BTC]] | +0.64 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SH3D19]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | +0.63 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[LINC02977]] | +0.63 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[NANOS3]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[BMPR1B]] | +0.61 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MSRA]] | +0.61 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZNF702P]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD18B]] | +0.60 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ATE1]] | +0.60 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC3]] | -0.69 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[MMS19]] | -0.68 | -0.71 / -0.50 | both halves | 1e-05 |  |
| [[UNC45A]] | -0.66 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.66 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[CNOT8]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[MED23]] | -0.64 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.63 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.63 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SDHAP1]] | -0.63 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[HACE1]] | -0.63 | -0.60 / -0.34 | both halves | 1e-04 | same gene group |
| [[MOSPD3]] | -0.63 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[INPP5B]] | -0.62 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASEF]] | B | RASEF activity raises ARAP2's level | lines that do not express RASEF (20) vs lines expressing it (30) | 3.25× lower at baseline in the lines without RASEF | 0.002 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[MAP7]] | B | MAP7 activity raises ARAP2's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 3.53× lower at baseline in the lines without MAP7 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[PTPRK]] | B | PTPRK activity raises ARAP2's level | lines that do not express PTPRK (6) vs lines expressing it (44) | 4.15× lower at baseline in the lines without PTPRK | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000246225, EPS8, ASPH |
| [[HDAC6]] | B | HDAC6 activity raises ARAP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BTC]] | B | BTC activity raises ARAP2's level | lines that do not express BTC (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without BTC | 0.053 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[ADGRG6]] | B | ADGRG6 activity raises ARAP2's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without ADGRG6 | 0.063 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[LMO7]] | B | LMO7 activity raises ARAP2's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.92× lower at baseline in the lines without LMO7 | 0.071 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[COBL]] | B | COBL activity raises ARAP2's level | lines that do not express COBL (23) vs lines expressing it (27) | 3.11× lower at baseline in the lines without COBL | 0.071 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[DSC2]] | B | DSC2 activity raises ARAP2's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.71× lower at baseline in the lines without DSC2 | 0.073 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[PLEKHA6]] | B | PLEKHA6 activity raises ARAP2's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 2.89× lower at baseline in the lines without PLEKHA6 | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[PLEKHA5]] | C | PLEKHA5 activity raises ARAP2's level | lines that do not express PLEKHA5 (4) vs lines expressing it (46) | 6.34× lower at baseline in the lines without PLEKHA5 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRK]] | B | ARAP2 activity raises PTPRK's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 2.68× lower at baseline in the lines without ARAP2 | 0.016 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[QPCTL]] | B | ARAP2 activity lowers QPCTL's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.49× higher at baseline in the lines without ARAP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[RASEF]] | B | ARAP2 activity raises RASEF's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 4.14× lower at baseline in the lines without ARAP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[MAP7]] | B | ARAP2 activity raises MAP7's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 3.48× lower at baseline in the lines without ARAP2 | 0.057 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[OSBPL7]] | B | ARAP2 activity raises OSBPL7's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without ARAP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[TMEM39B]] | B | ARAP2 activity lowers TMEM39B's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.55× higher at baseline in the lines without ARAP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[PEX3]] | B | ARAP2 activity lowers PEX3's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.48× higher at baseline in the lines without ARAP2 | 0.084 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[SEC14L2]] | B | ARAP2 activity lowers SEC14L2's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 2.12× higher at baseline in the lines without ARAP2 | 0.085 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[MRGBP]] | B | ARAP2 activity lowers MRGBP's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.25× higher at baseline in the lines without ARAP2 | 0.086 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[PKD1P6]] | B | ARAP2 activity lowers PKD1P6's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.40× higher at baseline in the lines without ARAP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[VDAC3]] | B | ARAP2 activity lowers VDAC3's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.42× higher at baseline in the lines without ARAP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[ABLIM1]] | B | ARAP2 activity raises ABLIM1's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without ARAP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.7, -13.6); signed map (25.6, 5.0). **Vector** length 126, 37.4% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.7 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +22.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +21.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | -3.3 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.0 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:35,948,221-36,244,514 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PARX; previously CENTD1 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; Pleckstrin homology domain containing; Sterile alpha motif domain containing |
| Reactome | 7 pathways, smallest: RAC3 GTPase cycle; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ64](https://www.uniprot.org/uniprotkb/Q8WZ64) (Arf-GAP with Rho-GAP domain, ANK repeat and PH domain-containing protein 2):

> Phosphatidylinositol 3,4,5-trisphosphate-dependent GTPase-activating protein that modulates actin cytoskeleton remodeling by regulating ARF and RHO family members. Is activated by phosphatidylinositol 3,4,5-trisphosphate (PtdIns(3,4,5)P3) binding. Can be activated by phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4,5)P2) binding, albeit with lower efficiency (By similarity).

**Summary**, from NCBI Gene [116984](https://www.ncbi.nlm.nih.gov/gene/116984):

> The protein encoded by this gene contains ARF-GAP, RHO-GAP, ankyrin repeat, RAS-associating, and pleckstrin homology domains. The protein is a phosphatidylinositol (3,4,5)-trisphosphate-dependent Arf6 GAP that binds RhoA-GTP, but it lacks the predicted catalytic arginine in the RHO-GAP domain and does not have RHO-GAP activity. The protein associates with focal adhesions and functions downstream of RhoA to regulate focal adhesion dynamics. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:16924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16924) · Entrez [116984](https://www.ncbi.nlm.nih.gov/gene/116984) · UniProt [Q8WZ64](https://www.uniprot.org/uniprotkb/Q8WZ64) · Ensembl [ENSG00000047365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047365)

## Data

Gene col 514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 514); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 514]; `tensor/DDL_lfc|DDL_z.npy` [514]; `embed/gene_vectors.npy` [514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 514 or target_col == 514). Every well: [[ARAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
