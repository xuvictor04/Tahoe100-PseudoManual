---
symbol: "EPHB2"
type: "gene"
col: 5430
ensembl_id: "ENSG00000133216"
name: "EPH receptor B2"
location: "1p36.12"
module: 228
arm: "+"
pooled_cpm: 60.88
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# EPHB2

*EPH receptor B2* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +17.0, q 0e+00, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.435× (z -9.2, q 3e-17, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL8]] (+0.62, fdr 7e-06), [[ABR]] (+0.61, fdr 1e-05), [[LIF]] (+0.61, fdr 1e-05); moves opposite to [[ANAPC10]] (-0.56, fdr 2e-05), [[SMAD4]] (-0.53, fdr 3e-05), [[FPGT]] (-0.51, fdr 3e-05).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IL31RA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +17.0 | 0e+00 | 30/41 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +11.6 | 7e-29 | 30/41 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.5 | 3e-28 | 28/41 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +9.7 | 3e-20 | 20/40 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +8.7 | 4e-16 | 26/41 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +7.5 | 5e-12 | 19/41 (HOP62, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +6.3 | 2e-08 | 19/41 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +6.2 | 3e-08 | 22/41 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.5 | 2e-06 | 17/41 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.7 | 1e-04 | 14/41 (HOP62, J82, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +4.7 | 1e-04 | 14/41 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.7 | 1e-04 | 16/41 (NCI-H1573, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +4.6 | 2e-04 | 20/41 (LoVo, HOP62, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +4.5 | 3e-04 | 17/41 (J82, SNU-423, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 4e-04 | 14/41 (HEC-1-A, NCI-H1573, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.002 | 14/41 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.007 | 4/41 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.031 | 11/40 (HEC-1-A, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -9.2 | 3e-17 | 31/42 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -7.8 | 1e-12 | 24/41 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -5.7 | 2e-06 | 21/41 (COLO 205, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -4.9 | 1e-04 | 20/41 (LS 180, PANC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.790×** | -4.8 | 2e-04 | 19/40 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.656×** | -4.7 | 3e-04 | 17/40 (PANC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.846× | -4.4 | 9e-04 | 18/42 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.680×** | -4.3 | 0.001 | 12/28 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.820×** | -4.2 | 0.002 | 15/41 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.817×** | -4.1 | 0.002 | 17/40 (PANC-1, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | **0.827×** | -4.0 | 0.003 | 16/40 (LoVo, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.879× | -3.4 | 0.030 | 15/41 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.852× | -3.4 | 0.030 | 12/41 (SNU-423, SW 900, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.850× | -3.3 | 0.037 | 15/39 (PANC-1, COLO 205, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.2 | 0.049 | 2/42 (NCI-H2030, NCI-H23) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.857× | -3.1 | 0.062 | 11/40 (PANC-1, A-172, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.091 | 14/42 (PANC-1, A549, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.765×** | -3.0 | 0.092 | 7/40 (NCI-H1573, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.871× | -2.9 | 0.100 | 8/41 (A549, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 46.8 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +33.1) | — |
| [[COLO 205 (line)]] | alt | 486 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -12.6) |
| [[LoVo (line)]] | wt | 47.9 | 4 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +20.0) | [[TAK-901 (drug)]] 5 µM 0.162× (z -10.4) |
| [[A-172 (line)]] | wt | 66.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +22.9) | [[Dinaciclib (drug)]] 5 µM 0.0636× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 54.7 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 89.2 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +12.1) | [[TAK-901 (drug)]] 5 µM 0.155× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 69.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[PANC-1 (line)]] | alt | 87.3 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 126 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.8) | — |
| [[LS 180 (line)]] | wt | 199 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 37.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[AsPC-1 (line)]] | alt | 51.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 54.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +24.3) | — |
| [[J82 (line)]] | alt | 36.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +21.7) | — |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 70.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.71× (z +11.2) | — |
| [[A498 (line)]] | wt | 64.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +9.0) | — |
| [[A549 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +12.6) | — |
| [[H4 (line)]] | wt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 80.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 77.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL8]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ABR]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 | same gene group |
| [[LIF]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[TFPI2]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[IRAK2]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[MAMLD1]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PHLDA2]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SLC4A7]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RASGRF2]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[PRKCA]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC10]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SMAD4]] | -0.53 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[FPGT]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[HMBOX1]] | -0.51 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[OXNAD1]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TTC9C]] | -0.49 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[LRIG2]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[DERL1]] | -0.48 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[ATPAF2]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CRYZL1]] | -0.48 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[CLASP1]] | -0.47 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[VDAC3]] | -0.47 | -0.60 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL31RA]] | B | IL31RA activity raises EPHB2's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.54× lower at baseline in the lines without IL31RA | 0.046 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[PHLDA1]] | B | PHLDA1 activity raises EPHB2's level | lines that do not express PHLDA1 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without PHLDA1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DPYSL2, PARP3, C1RL; maybe low, not absent |
| [[G0S2]] | B | G0S2 activity raises EPHB2's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without G0S2 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[CARD10]] | B | CARD10 activity raises EPHB2's level | lines that do not express CARD10 (8) vs lines expressing it (42) | 3.05× lower at baseline in the lines without CARD10 | 0.089 | ⚠ within organs, on part of the lines; also absent: MFNG, LRP5, SDC1; maybe low, not absent; its own permutation p |
| [[SYNJ2]] | C | SYNJ2 activity raises EPHB2's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.29× lower at baseline in the lines without SYNJ2 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.1, -0.3); signed map (2.2, 42.9). **Vector** length 108, 26.2% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +17.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.9 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:22,710,839-22,921,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hek5, Tyro5; previously DRT, ERK, EPHT3 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors; MicroRNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 7 pathways, smallest: Ephrin signaling; EPHB-mediated forward signaling; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P29323](https://www.uniprot.org/uniprotkb/P29323) (Ephrin type-B receptor 2):

> Receptor tyrosine kinase which binds promiscuously transmembrane ephrin-B family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Functions in axon guidance during development. Involved in the guidance of commissural axons, that form a major …

**Summary**, from NCBI Gene [2048](https://www.ncbi.nlm.nih.gov/gene/2048):

> This gene encodes a member of the Eph receptor family of receptor tyrosine kinase transmembrane glycoproteins. These receptors are composed of an N-terminal glycosylated ligand-binding domain, a transmembrane region and an intracellular kinase domain. They bind ligands called ephrins and are involved in diverse cellular processes including motility, division, and differentiation. A distinguishing characteristic of Eph-ephrin signaling is that both receptors and ligands are competent to …

**Accessions** — [HGNC:3393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3393) · Entrez [2048](https://www.ncbi.nlm.nih.gov/gene/2048) · UniProt [P29323](https://www.uniprot.org/uniprotkb/P29323) · Ensembl [ENSG00000133216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133216)

## Data

Gene col 5430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5430); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5430]; `tensor/DDL_lfc|DDL_z.npy` [5430]; `embed/gene_vectors.npy` [5430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5430 or target_col == 5430). Every well: [[EPHB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
