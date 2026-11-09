---
symbol: "ABLIM3"
type: "gene"
col: 10354
ensembl_id: "ENSG00000173210"
name: "actin binding LIM protein family member 3"
location: "5q32"
module: 97
arm: "+"
pooled_cpm: 79.8
n_lines_expressing: 35
n_dd_up: 23
n_dd_down: 38
n_dd_up_clean: 21
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 12
direction_downstream: 15
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ABLIM3

*actin binding LIM protein family member 3* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 2.39× (z +12.5, q 3e-33, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.317× (z -23.4, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3RF3]] (+0.67, fdr 7e-06), [[ERGIC1]] (+0.66, fdr 7e-06), [[AKAP12]] (+0.65, fdr 7e-06); moves opposite to [[BCL2L14]] (-0.52, fdr 2e-05), [[TNFSF10]] (-0.49, fdr 3e-05), [[MTUS1-DT]] (-0.49, fdr 5e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); 15 go from it, the strongest it → [[RGS17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **2.39×** | +12.5 | 3e-33 | 22/33 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **2.31×** | +12.0 | 7e-31 | 23/33 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **2.20×** | +11.3 | 2e-27 | 22/33 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **2.17×** | +11.1 | 2e-26 | 22/33 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.17×** | +11.1 | 2e-26 | 23/33 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.13×** | +10.8 | 2e-25 | 23/33 (HOP62, SK-MEL-2, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.12×** | +10.8 | 2e-25 | 21/33 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.05×** | +10.3 | 4e-23 | 23/33 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.1 | 8e-18 | 22/33 (HOP62, NCI-H1792, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.95×** | +8.9 | 3e-17 | 22/33 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.92×** | +8.6 | 3e-16 | 21/32 (HOP62, SK-MEL-2, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.79×** | +8.4 | 3e-15 | 22/33 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.51×** | +8.4 | 3e-15 | 19/33 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.76×** | +8.1 | 2e-14 | 21/33 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.69×** | +7.5 | 2e-12 | 19/33 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.317×** | -23.4 | 0e+00 | 33/34 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.408×** | -18.3 | 0e+00 | 28/33 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.458×** | -11.3 | 4e-27 | 27/33 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.456×** | -10.5 | 2e-23 | 21/30 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.495×** | -9.7 | 2e-20 | 29/33 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.498×** | -9.7 | 3e-20 | 23/31 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -8.9 | 5e-17 | 27/35 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -8.2 | 1e-14 | 23/33 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.546×** | -8.1 | 3e-14 | 25/33 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.571×** | -7.8 | 4e-13 | 22/33 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.611×** | -7.1 | 6e-11 | 23/33 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.684×** | -6.8 | 4e-10 | 21/33 (AsPC-1, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.684×** | -6.5 | 5e-09 | 19/34 (AsPC-1, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -6.1 | 3e-08 | 19/32 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.644×** | -6.1 | 3e-08 | 21/32 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.709×** | -5.8 | 3e-07 | 22/35 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.757×** | -5.7 | 4e-07 | 17/33 (PANC-1, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -5.5 | 1e-06 | 16/33 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.673×** | -5.3 | 3e-06 | 21/34 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 236 | 18 | 14 (7 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.93× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -21.6) |
| [[AsPC-1 (line)]] | alt | 109 | 8 | 18 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 4.05× (z +10.5) | [[Trametinib (drug)]] 5 µM 0.138× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 108 | 16 | 6 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.81× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -22.7) |
| [[A-172 (line)]] | wt | 131 | 7 | 13 (3 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 3.34× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -27.3) |
| [[PANC-1 (line)]] | alt | 188 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -31.6) |
| [[NCI-H1792 (line)]] | alt | 103 | 15 | 2 | [[Clobetasol propionate (drug)]] 0.5 µM 3.43× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 179 | 9 | 7 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.73× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -21.8) |
| [[Hs 766T (line)]] | wt | 129 | 9 | 3 | [[Dexamethasone (drug)]] 0.5 µM 4.67× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -15.6) |
| [[SNU-423 (line)]] | alt | 195 | 4 | 7 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.55× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -16.7) |
| [[HS-578T (line)]] | alt | 189 | 2 | 7 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.98× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -21.5) |
| [[J82 (line)]] | alt | 120 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -16.5) |
| [[A498 (line)]] | wt | 159 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -18.1) |
| [[SW480 (line)]] | alt | 45.7 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -14.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.5) |
| [[HT-29 (line)]] | alt | 83.9 | 4 (3 ⚠) | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 4.43× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -17.1) |
| [[KATO III (line)]] | alt | 106 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -18.1) |
| [[COLO 205 (line)]] | alt | 37.7 | 5 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 8.70× (z +10.5) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 9.28× (z +10.4) | — |
| [[H4 (line)]] | wt | 82.2 | 2 | 2 | [[Triamcinolone (drug)]] 5 µM 2.91× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -9.2) |
| [[SW 900 (line)]] | alt | 81.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -20.4) |
| [[A549 (line)]] | wt | 59.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 76.8 | 1 | 2 | [[Clobetasol propionate (drug)]] 0.5 µM 2.72× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -15.3) |
| [[LoVo (line)]] | wt | 23.8 | 1 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.00× (z +8.5) ⚠ cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -8.9) |
| [[SHP-77 (line)]] | alt | 82.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.2) |
| [[C32 (line)]] | wt | 65.4 | 0 | 1 | — | [[Binimetinib (drug)]] 5 µM 0.315× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 89.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 93.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -11.4) |
| [[SW 1088 (line)]] | alt | 334 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -12.0) |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.4) |
| [[SW48 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3RF3]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ERGIC1]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[AKAP12]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TANC2]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ITGA5]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FOXL1]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TOX2]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[HIPK2]] | +0.59 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GAB3]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PTPN1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MT1X]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[JCAD]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L14]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TNFSF10]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MTUS1-DT]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TFAP2A-AS1]] | -0.49 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[LINC02068]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[LINC02384]] | -0.47 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[CASP10]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RARRES1]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[LIPC]] | -0.46 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[DDR1]] | -0.45 | -0.45 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises ABLIM3's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.43× lower at baseline in the lines without TBC1D8 | 0.012 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[LOX]] | B | LOX activity raises ABLIM3's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.94× lower at baseline in the lines without LOX | 0.030 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[NR3C1]] | B | NR3C1 activity raises ABLIM3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[TBXAS1]] | B | TBXAS1 activity raises ABLIM3's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 2.54× lower at baseline in the lines without TBXAS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[RGS17]] | B | RGS17 activity raises ABLIM3's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without RGS17 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[B3GNT5]] | B | B3GNT5 activity raises ABLIM3's level | lines that do not express B3GNT5 (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without B3GNT5 | 0.048 | ⚠ within organs, on part of the lines; also absent: MCF2L2, SOX4, RND3 |
| [[RARRES1]] | B | RARRES1 activity raises ABLIM3's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without RARRES1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[FOXL1]] | B | FOXL1 activity raises ABLIM3's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 3.06× lower at baseline in the lines without FOXL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[HIPK2]] | B | HIPK2 activity raises ABLIM3's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 3.37× lower at baseline in the lines without HIPK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[TMTC1]] | B | TMTC1 activity strengthens ABLIM3's drug response | lines that do not express TMTC1 (16) vs lines expressing it (18) | the lines without TMTC1 respond 0.58× as strongly (z diff +1.97); strongest at Budesonide 5 µM: 1.37x vs 2.57x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000255983, CNRIP1, ADAM23; target measured in part of the lines; the reference differs |
| [[HSD11B1]] | B | HSD11B1 activity raises ABLIM3's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without HSD11B1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[SNAI2]] | C | SNAI2 activity raises ABLIM3's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 4.19× lower at baseline in the lines without SNAI2 | 0.006 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS17]] | B | ABLIM3 activity raises RGS17's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 3.06× lower at baseline in the lines without ABLIM3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[AKAP13]] | B | ABLIM3 activity raises AKAP13's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without ABLIM3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[DUSP1]] | B | ABLIM3 activity raises DUSP1's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 2.43× lower at baseline in the lines without ABLIM3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[LINC02068]] | B | ABLIM3 activity raises LINC02068's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.32× lower at baseline in the lines without ABLIM3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[RBMS1]] | B | ABLIM3 activity raises RBMS1's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without ABLIM3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | B | ABLIM3 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express ABLIM3 (15) vs lines expressing it (33) | the lines without ABLIM3: 0.89× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[TBC1D8]] | B | ABLIM3 activity raises TBC1D8's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.91× lower at baseline in the lines without ABLIM3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[LOX]] | B | ABLIM3 activity raises LOX's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 5.28× lower at baseline in the lines without ABLIM3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[RPS6KA2]] | B | ABLIM3 activity raises RPS6KA2's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.80× lower at baseline in the lines without ABLIM3 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[AFAP1L1]] | B | ABLIM3 activity raises AFAP1L1's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without ABLIM3 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[NIBAN2]] | B | ABLIM3 activity raises NIBAN2's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without ABLIM3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[PALM2AKAP2]] | B | ABLIM3 activity strengthens PALM2AKAP2's drug response | lines that do not express ABLIM3 (11) vs lines expressing it (29) | the lines without ABLIM3 respond 0.50× as strongly (z diff +2.55); rises at some drug-doses, falls at others (73% from rises): Idarubicin (hydrochloride) 5 µM: 1.04x vs 0.59x (z diff +6.0); Harringtonine 0.5 µM: 1.21x vs 2.07x (z diff +4.8); Harringtonine 5 µM: 1.06x vs 1.86x (z diff +4.1) | 0.089 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 12.8); signed map (15.7, 35.6). **Vector** length 137, 45.6% of its response variance represented; |z| ≥ 3 in 1,665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +7.1 | +11.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +6.6 | +10.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +6.6 | +10.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +6.3 | +11.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +6.3 | +12.0 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -6.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.1 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.8 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.4 | -7.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | actin binding LIM protein family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,141,483-149,260,542 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0843 |
| Gene groups (HGNC) | LIM domain containing |
| Reactome | 4 pathways, smallest: DCC mediated attractive signaling; Netrin-1 signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O94929](https://www.uniprot.org/uniprotkb/O94929) (Actin-binding LIM protein 3):

> May act as scaffold protein. May stimulate ABRA activity and ABRA-dependent SRF transcriptional activity.

**Summary**, from NCBI Gene [22885](https://www.ncbi.nlm.nih.gov/gene/22885):

> This gene encodes a member of the actin-binding LIM (abLIM) family of proteins. These proteins are characterized by an N-terminal LIM domain and a C-terminal dematin-like domain. The encoded protein interacts with actin filaments and may be a component of adherens junctions in several cell types. A variant of this gene may be associated with pain sensitivity in male human patients. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:29132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29132) · Entrez [22885](https://www.ncbi.nlm.nih.gov/gene/22885) · UniProt [O94929](https://www.uniprot.org/uniprotkb/O94929) · Ensembl [ENSG00000173210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173210)

## Data

Gene col 10354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10354); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10354]; `tensor/DDL_lfc|DDL_z.npy` [10354]; `embed/gene_vectors.npy` [10354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10354 or target_col == 10354). Every well: [[ABLIM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABLIM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
