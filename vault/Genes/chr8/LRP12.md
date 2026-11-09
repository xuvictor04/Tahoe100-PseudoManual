---
symbol: "LRP12"
type: "gene"
col: 7210
ensembl_id: "ENSG00000147650"
name: "LDL receptor related protein 12"
location: "8q22.3"
module: 57
arm: "+"
pooled_cpm: 55.2
n_lines_expressing: 42
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# LRP12

*LDL receptor related protein 12* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.22× (z +8.9, q 3e-16, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.500× (z -14.8, q 0e+00, down in 28 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.695× (z -7.7, q 2e-12, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXPE3]] (+0.58, fdr 1e-05), [[CDYL]] (+0.57, fdr 3e-05), [[RNF2]] (+0.56, fdr 1e-05); moves opposite to [[UBAP1L]] (-0.53, fdr 2e-05), [[SLC35F5]] (-0.49, fdr 5e-05), [[CEP95]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[AKT3]] → it (grade B ⚠); 4 go from it, the strongest it → [[KCTD6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +8.9 | 3e-16 | 25/41 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +8.3 | 2e-14 | 26/40 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.3 | 6e-11 | 25/40 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +7.1 | 2e-10 | 24/40 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.7 | 2e-09 | 30/40 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +6.4 | 1e-08 | 23/39 (SNU-423, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +6.3 | 3e-08 | 21/40 (LS 180, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +6.2 | 5e-08 | 23/40 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +5.0 | 3e-05 | 21/40 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 5e-04 | 15/40 (HOP62, NCI-H1792, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.011 | 11/40 (HOP62, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.012 | 14/40 (HEC-1-A, RKO, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.5 | 0.019 | 13/40 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.17× | +3.4 | 0.024 | 8/40 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.12× | +3.4 | 0.026 | 8/40 (hTERT-HPNE, C-33 A, …) | top dose only | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.037 | 10/40 (HOP62, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.040 | 11/40 (NCI-H2347, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.068 | 5/40 (C32, HOP62, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.083 | 10/40 (A498, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.500×** | -14.8 | 0e+00 | 28/39 (RKO, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.531×** | -13.0 | 6e-36 | 26/36 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -10.7 | 1e-24 | 25/38 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -7.7 | 2e-12 | 24/40 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.790×** | -7.0 | 2e-10 | 21/40 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -6.0 | 2e-07 | 19/40 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.766×** | -5.7 | 1e-06 | 21/39 (SW1417, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.796×** | -4.8 | 9e-05 | 18/40 (HS-578T, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.819×** | -4.2 | 0.001 | 16/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.6 | 0.015 | 16/40 (C32, NCI-H460, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.832×** | -3.6 | 0.017 | 11/40 (SW 900, J82, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.733×** | -3.5 | 0.020 | 13/38 (BT-474, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.859× | -3.2 | 0.051 | 15/40 (C32, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.753×** | -3.2 | 0.051 | 13/39 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.051 | 8/40 (A498, A-172, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.900× | -3.1 | 0.061 | 5/40 (A498, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 184 | 2 | 8 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 10.6× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 90.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -15.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 88.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -18.7) |
| [[A498 (line)]] | wt | 169 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.94× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.01× (z +9.5) | — |
| [[J82 (line)]] | alt | 70.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 39.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.293× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -9.5) |
| [[A549 (line)]] | wt | 42.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.79× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -13.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.175× (z -9.5) |
| [[HOP62 (line)]] | alt | 74.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -11.3) |
| [[Hs 766T (line)]] | wt | 46.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.58× (z +9.1) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 58.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 66.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 43.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 83.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -10.1) |
| [[SW1417 (line)]] | alt | 47.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -19.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -15.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 99.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0981× (z -24.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -19.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.79× (z +9.2) ⚠ toxic | — |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 5 µM 0.0711× (z -8.5) |
| [[SW 900 (line)]] | alt | 96.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 19.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.94× (z +9.4) | — |
| [[A-172 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 109 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXPE3]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CDYL]] | +0.57 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[RNF2]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SMIM13]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MINPP1]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[BCL9]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CSNK1G3]] | +0.54 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[MTMR8]] | +0.51 | +0.53 / +0.36 | both halves | 9e-05 |  |
| [[ZNF280B]] | +0.50 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[HSF2]] | +0.50 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[BLMH]] | +0.50 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[AKIP1]] | +0.50 | +0.45 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBAP1L]] | -0.53 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[SLC35F5]] | -0.49 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[CEP95]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ACAD9]] | -0.47 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ATG12]] | -0.46 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[PSORS1C1]] | -0.44 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[PPP1R13L]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TRPV1]] | -0.44 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TMEM91]] | -0.44 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[USP20]] | -0.44 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[SAFB2]] | -0.44 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[KIAA0319L]] | -0.43 | -0.52 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT3]] | B | AKT3 activity raises LRP12's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 3.16× lower at baseline in the lines without AKT3 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[DENND5A]] | C | DENND5A activity raises LRP12's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 8.15× lower at baseline in the lines without DENND5A | 0.016 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[PKIG]] | C | PKIG activity raises LRP12's level | lines that do not express PKIG (6) vs lines expressing it (44) | 5.07× lower at baseline in the lines without PKIG | 0.066 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1; co-absent with the target |
| [[CIBAR1]] | C | CIBAR1 activity raises LRP12's level | lines that do not express CIBAR1 (4) vs lines expressing it (46) | 6.92× lower at baseline in the lines without CIBAR1 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: CLTCL1, SPIRE1, ZNF480; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD6]] | B | LRP12 activity raises KCTD6's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without LRP12 | 0.085 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1 |
| [[GNPDA2]] | B | LRP12 activity raises GNPDA2's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without LRP12 | 0.096 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1 |
| [[PKIG]] | C | LRP12 activity raises PKIG's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 3.46× lower at baseline in the lines without LRP12 | 0.040 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1; co-absent with the target |
| [[CIBAR1]] | C | LRP12 activity raises CIBAR1's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 2.52× lower at baseline in the lines without LRP12 | 0.047 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.290). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.7, -3.4); signed map (-36.8, -18.8). **Vector** length 101, 26.2% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.0 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.1 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.6 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:104,489,231-104,589,258 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST7, FLJ12929 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Reactome | 5 pathways, smallest: Retinoid metabolism and transport; Metabolism of fat-soluble vitamins; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y561](https://www.uniprot.org/uniprotkb/Q9Y561) (Low-density lipoprotein receptor-related protein 12):

> Probable receptor, which may be involved in the internalization of lipophilic molecules and/or signal transduction. May act as a tumor suppressor.

**Summary**, from NCBI Gene [29967](https://www.ncbi.nlm.nih.gov/gene/29967):

> This gene encodes a member of the low-density lipoprotein receptor related protein family. The product of this gene is a transmembrane protein that is differentially expressed in many cancer cells. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:31708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31708) · Entrez [29967](https://www.ncbi.nlm.nih.gov/gene/29967) · UniProt [Q9Y561](https://www.uniprot.org/uniprotkb/Q9Y561) · Ensembl [ENSG00000147650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147650)

## Data

Gene col 7210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7210); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7210]; `tensor/DDL_lfc|DDL_z.npy` [7210]; `embed/gene_vectors.npy` [7210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7210 or target_col == 7210). Every well: [[LRP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
