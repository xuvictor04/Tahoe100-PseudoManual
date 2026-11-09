---
symbol: "DNAH17"
type: "gene"
col: 11947
ensembl_id: "ENSG00000187775"
name: "dynein axonemal heavy chain 17"
location: "17q25.3"
module: 228
arm: "+"
pooled_cpm: 12.49
n_lines_expressing: 37
n_dd_up: 17
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# DNAH17

*dynein axonemal heavy chain 17* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.0× (z +43.9, q 0e+00, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.632× (z -5.9, q 2e-06, down in 14 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAT1]] (+0.70, fdr 7e-06, ⚠ same locus), [[CPAMD8]] (+0.65, fdr 7e-06), [[SSUH2]] (+0.65, fdr 7e-06), [[MAP3K20-AS1]] (+0.64, fdr 7e-06); moves opposite to [[WHAMMP1]] (-0.61, fdr 1e-05), [[RPA1]] (-0.55, fdr 2e-05), [[ABCB10]] (-0.55, fdr 1e-05).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TNFSF14]] → it (grade B ⚠); 11 go from it, the strongest it → [[SCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.0×** | +43.9 | 0e+00 | 30/31 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.55×** | +19.6 | 0e+00 | 23/31 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.79×** | +19.5 | 0e+00 | 26/32 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.70×** | +16.9 | 0e+00 | 21/32 (PANC-1, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +11.9 | 9e-31 | 3/12 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +11.7 | 1e-29 | 24/34 (SW480, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +10.7 | 1e-24 | 13/29 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +9.3 | 1e-18 | 5/16 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +7.3 | 2e-11 | 18/32 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.2 | 4e-08 | 9/22 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +6.1 | 6e-08 | 13/31 (NCI-H460, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 7e-04 | 12/33 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.3 | 9e-04 | 5/25 (BT-474, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.064 | 3/30 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.086 | 2/27 (AsPC-1, J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.57×** | +3.0 | 0.087 | 0/26 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.632×** | -5.9 | 2e-06 | 14/30 (KATO III, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.645×** | -5.5 | 1e-05 | 12/30 (NCI-H1573, HEC-1-A, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -4.6 | 1e-03 | 15/28 (A549, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.519×** | -4.4 | 0.001 | 12/27 (HepG2/C3A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.734×** | -4.3 | 0.002 | 9/34 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.799×** | -4.1 | 0.004 | 6/34 (NCI-H1573, RPMI-7951, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.765×** | -4.1 | 0.004 | 12/33 (A549, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.004 | 13/34 (CFPAC-1, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.804×** | -4.0 | 0.004 | 8/34 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.559×** | -3.9 | 0.005 | 10/33 (HOP62, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.742×** | -3.9 | 0.006 | 13/32 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.728×** | -3.8 | 0.007 | 7/34 (Panc 03.27, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.014 | 8/34 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.767×** | -3.4 | 0.023 | 15/34 (HepG2/C3A, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.768×** | -3.4 | 0.023 | 11/33 (HepG2/C3A, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.782×** | -3.2 | 0.052 | 10/34 (HepG2/C3A, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 428 | 0 | 16 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.00447× (z -33.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -19.8) |
| [[A549 (line)]] | wt | 42.4 | 1 | 11 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.0104× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0957× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 23.2 | 0 | 11 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0933× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 15.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +28.7) | — |
| [[A-172 (line)]] | wt | 3.78 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.2× (z +17.0) | — |
| [[SNU-423 (line)]] | alt | 13.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +11.2) | [[Selinexor (drug)]] 5 µM 0.118× (z -15.7) |
| [[A498 (line)]] | wt | 3.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 3.61 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +11.7) | [[Fenofibrate (drug)]] 5 µM 0.0664× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 4.60 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +15.6) | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 3.34 | 2 | 0 | [[Auranofin (drug)]] 5 µM 11.9× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 5.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.8× (z +15.3) | — |
| [[BT-474 (line)]] | alt | 4.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 8.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +18.1) | — |
| [[hTERT-HPNE (line)]] | wt | 3.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +9.8) | — |
| [[J82 (line)]] | alt | 4.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +16.9) | — |
| [[KATO III (line)]] | alt | 4.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0858× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 9.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 3.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 4.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +8.9) | — |
| [[SW48 (line)]] | wt | 3.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +9.8) | — |
| [[A-427 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAT1]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 | ⚠ same locus (27.8 kb, same strand: neighbours can correlate without regulation) |
| [[CPAMD8]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SSUH2]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MAP3K20-AS1]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PLB1]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[BMP2]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[HMGN2P46]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NOS1]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SMCO2]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MSANTD3-TMEFF1]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[COL22A1]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMMP1]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[RPA1]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ABCB10]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.54 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PXMP4]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NDC1]] | -0.53 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[IARS2]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF14]] | B | TNFSF14 activity raises DNAH17's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without TNFSF14 | 0.005 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[SCAT1]] | B | SCAT1 activity raises DNAH17's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without SCAT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[COL22A1]] | B | COL22A1 activity raises DNAH17's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 1.62× lower at baseline in the lines without COL22A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[FAM43A]] | B | FAM43A activity raises DNAH17's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without FAM43A | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTAFR]] | B | PTAFR activity raises DNAH17's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.77× lower at baseline in the lines without PTAFR | 0.064 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[MAST4]] | B | MAST4 activity raises DNAH17's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without MAST4 | 0.072 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[IL2RG]] | B | IL2RG activity raises DNAH17's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.81× lower at baseline in the lines without IL2RG | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[TRPV3]] | B | TRPV3 activity raises DNAH17's level | lines that do not express TRPV3 (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without TRPV3 | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC03042]] | C | LINC03042 activity raises DNAH17's level | lines that do not express LINC03042 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LINC03042 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC00960, CORO2B, DNAH17; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAT1]] | B | DNAH17 activity raises SCAT1's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without DNAH17 | 0.004 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[CD163L1]] | B | DNAH17 activity raises CD163L1's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 3.34× lower at baseline in the lines without DNAH17 | 0.016 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[ADAMTSL4-AS2]] | B | DNAH17 activity raises ADAMTSL4-AS2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without DNAH17 | 0.017 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[ERI2]] | B | DNAH17 activity raises ERI2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without DNAH17 | 0.022 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[LAT2]] | B | DNAH17 activity raises LAT2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without DNAH17 | 0.036 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[IARS2]] | B | DNAH17 activity lowers IARS2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.13× higher at baseline in the lines without DNAH17 | 0.070 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[KIAA1217]] | B | DNAH17 activity raises KIAA1217's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without DNAH17 | 0.073 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[IER3]] | B | DNAH17 activity raises IER3's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without DNAH17 | 0.087 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[ADAM7-AS1]] | B | DNAH17 activity raises ADAM7-AS1's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without DNAH17 | 0.089 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[MFSD14A]] | B | DNAH17 activity lowers MFSD14A's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.32× higher at baseline in the lines without DNAH17 | 0.089 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[MCL1]] | B | DNAH17 activity raises MCL1's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without DNAH17 | 0.091 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.4, -2.5); signed map (39.3, 11.5). **Vector** length 93.5, 20.8% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +43.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +16.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.8 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,423,697-78,577,396 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNEL2, FLJ40457; previously DNAHL1 |
| Gene groups (HGNC) | Dyneins, axonemal outer arm complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UFH2](https://www.uniprot.org/uniprotkb/Q9UFH2) (Dynein axonemal heavy chain 17):

> Force generating protein component of the outer dynein arms (ODAs) in the sperm flagellum (By similarity). Produces force towards the minus ends of microtubules (By similarity). Key component of dynein, a family of motor proteins essential for movement along microtubules (By similarity). Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP (By similarity). Required for structural and functional integrity of cilia (By similarity). Plays a major role …

**Summary**, from NCBI Gene [8632](https://www.ncbi.nlm.nih.gov/gene/8632):

> Dyneins are microtubule-associated motor protein complexes composed of several heavy, light, and intermediate chains. DNAH17 is a heavy chain associated with axonemal dynein (Milisav and Affara, 1998 [PubMed 9545504]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2946) · Entrez [8632](https://www.ncbi.nlm.nih.gov/gene/8632) · UniProt [Q9UFH2](https://www.uniprot.org/uniprotkb/Q9UFH2) · Ensembl [ENSG00000187775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187775)

## Data

Gene col 11947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11947); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11947]; `tensor/DDL_lfc|DDL_z.npy` [11947]; `embed/gene_vectors.npy` [11947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11947 or target_col == 11947). Every well: [[DNAH17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
