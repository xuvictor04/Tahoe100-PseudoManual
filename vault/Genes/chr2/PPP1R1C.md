---
symbol: "PPP1R1C"
type: "gene"
col: 7455
ensembl_id: "ENSG00000150722"
name: "protein phosphatase 1 regulatory inhibitor subunit 1C"
location: "2q31.3-q32.1"
module: 80
arm: "+"
pooled_cpm: 12.0
n_lines_expressing: 37
n_dd_up: 39
n_dd_down: 13
n_dd_up_clean: 30
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 14
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# PPP1R1C

*protein phosphatase 1 regulatory inhibitor subunit 1C* — 2q31.3-q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.45× (z +35.7, q 0e+00, up in 28 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.621× (z -6.2, q 4e-07, down in 12 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NANOS3]] (+0.69, fdr 7e-06), [[ADGRL4]] (+0.68, fdr 7e-06), [[CDK6-AS1]] (+0.67, fdr 1e-05); moves opposite to [[UBAC1]] (-0.62, fdr 3e-05), [[INTS10]] (-0.61, fdr 1e-05), [[SLC35A3]] (-0.61, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PRKG2-AS1]] → it (grade B ⚠); 14 go from it, the strongest it → [[PRKG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7455.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.45×** | +35.7 | 0e+00 | 28/31 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.33×** | +25.0 | 0e+00 | 33/33 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +21.1 | 0e+00 | 25/33 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.66×** | +20.0 | 0e+00 | 29/34 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.54×** | +12.6 | 3e-34 | 26/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +11.1 | 1e-26 | 22/35 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +11.0 | 4e-26 | 26/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +10.1 | 3e-22 | 20/34 (AsPC-1, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.02×** | +8.5 | 9e-16 | 21/34 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +7.6 | 2e-12 | 16/34 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.7 | 1e-09 | 5/20 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.2 | 3e-08 | 3/15 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.61×** | +6.0 | 6e-08 | 15/34 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.55×** | +5.9 | 1e-07 | 17/34 (AsPC-1, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.3 | 4e-06 | 4/26 (HT-29, SW 900, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +5.3 | 4e-06 | 9/34 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 9e-06 | 9/34 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 7e-04 | 11/34 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.621×** | -6.2 | 4e-07 | 12/33 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.748×** | -5.6 | 5e-06 | 15/34 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.670×** | -5.5 | 8e-06 | 14/34 (LOX-IMVI, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -4.8 | 2e-04 | 16/34 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.773×** | -3.9 | 0.011 | 12/34 (AsPC-1, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.075 | 9/33 (LOX-IMVI, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.832×** | -3.3 | 0.075 | 12/34 (AsPC-1, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.769×** | -3.3 | 0.075 | 8/34 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.791×** | -3.2 | 0.075 | 12/34 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.852× | -3.2 | 0.085 | 3/34 (Panc 03.27, A549, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.799×** | -3.1 | 0.085 | 10/34 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.789×** | -3.1 | 0.085 | 10/34 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.855× | -3.1 | 0.085 | 3/34 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.825×** | -3.0 | 0.093 | 10/34 (AsPC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.804×** | -3.0 | 0.098 | 15/34 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 48.7 | 3 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 56.1 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +17.2) | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -15.1) |
| [[SW480 (line)]] | alt | 37.9 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.195× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 18.9 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 9.14 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +12.0) | — |
| [[A498 (line)]] | wt | 3.94 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +14.7) | — |
| [[NCI-H2030 (line)]] | alt | 43.6 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -10.5) |
| [[A-172 (line)]] | wt | 4.11 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 81.4× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.164× (z -9.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.209× (z -8.8) |
| [[A549 (line)]] | wt | 7.22 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +11.5) | [[Cobimetinib (drug)]] 0.05 µM 0.0848× (z -8.7) |
| [[C32 (line)]] | wt | 8.86 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +15.6) | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -11.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 5.35 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +9.5) | [[Ferulic acid (drug)]] 5 µM 0.0594× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 9.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +12.1) | — |
| [[LoVo (line)]] | wt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 7.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +13.8) | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0666× (z -10.1) |
| [[COLO 205 (line)]] | alt | 5.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +12.7) | — |
| [[KATO III (line)]] | alt | 7.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 4.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 3.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +11.7) | — |
| [[A-427 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NANOS3]] | +0.69 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ADGRL4]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CDK6-AS1]] | +0.67 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TRIM59]] | +0.66 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MMRN2]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ANGPT2]] | +0.65 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[ICAM2]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SSUH2]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[LPXN]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBAC1]] | -0.62 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[INTS10]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[SLC35A3]] | -0.61 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[INPP5B]] | -0.60 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[MYPOP]] | -0.60 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SNTA1]] | -0.59 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[ABHD12]] | -0.59 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CALCOCO2]] | -0.59 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.59 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[OXNAD1]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[YIPF1]] | -0.58 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[TMEM183A]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG2-AS1]] | B | PRKG2-AS1 activity raises PPP1R1C's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without PRKG2-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[LINC01322]] | B | LINC01322 activity raises PPP1R1C's level | lines that do not express LINC01322 (35) vs lines expressing it (15) | 2.31× lower at baseline in the lines without LINC01322 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, TM4SF4, TIMD4 |
| [[GOLT1A]] | B | GOLT1A activity raises PPP1R1C's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without GOLT1A | 0.056 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PPP1R1C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLRC4-KLRK1]], [[KLRK1]] | B | KLRC4-KLRK1, KLRK1 activity raises PPP1R1C's level | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (21) | 1.72× lower at baseline in the lines without KLRC4-KLRK1, KLRK1 | 0.068 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG2]] | B | PPP1R1C activity raises PRKG2's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without PPP1R1C | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[MTNR1A]] | B | PPP1R1C activity raises MTNR1A's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without PPP1R1C | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[GPR39]] | B | PPP1R1C activity raises GPR39's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 2.74× lower at baseline in the lines without PPP1R1C | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[BCAN-AS1]] | B | PPP1R1C activity raises BCAN-AS1's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 2.19× lower at baseline in the lines without PPP1R1C | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[CASC8]] | B | PPP1R1C activity strengthens CASC8's drug response | lines that do not express PPP1R1C (6) vs lines expressing it (20) | the lines without PPP1R1C respond 0.54× as strongly (z diff +1.15); strongest at Idarubicin (hydrochloride) 5 µM: 0.82x vs 3.49x (z diff +7.1) | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ZNF518A]] | B | PPP1R1C activity raises ZNF518A's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without PPP1R1C | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[HDAC9]] | B | PPP1R1C activity lowers HDAC9's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.44× higher at baseline in the lines without PPP1R1C | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[TMEM183A]] | B | PPP1R1C activity lowers TMEM183A's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.26× higher at baseline in the lines without PPP1R1C | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[SNTA1]] | B | PPP1R1C activity lowers SNTA1's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.67× higher at baseline in the lines without PPP1R1C | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[LRRC37A3]] | B | PPP1R1C activity raises LRRC37A3's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.31× lower at baseline in the lines without PPP1R1C | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[LINC01776]] | B | PPP1R1C activity lowers LINC01776's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 2.20× higher at baseline in the lines without PPP1R1C | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[LINC01592]] | B | PPP1R1C activity lowers LINC01592's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.85× higher at baseline in the lines without PPP1R1C | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.0, 5.9); signed map (26.7, 6.4). **Vector** length 94.0, 21.7% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +35.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +25.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +11.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory inhibitor subunit 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.3-q32.1 — chr2:181,954,241-182,131,398 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Inhibitor-1-like |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVI7](https://www.uniprot.org/uniprotkb/Q8WVI7) (Protein phosphatase 1 regulatory subunit 1C):

> May increase cell susceptibility to TNF-induced apoptosis.

**Summary**, from NCBI Gene [151242](https://www.ncbi.nlm.nih.gov/gene/151242):

> Protein phosphatase-1 (PP1) is a major serine/threonine phosphatase that regulates a variety of cellular functions. PP1 consists of a catalytic subunit (see PPP1CA; MIM 176875) and regulatory subunits that determine the subcellular localization of PP1 or regulate its function. PPP1R1C belongs to a group of PP1 inhibitory subunits that are themselves regulated by phosphorylation (Wang et al., 2008 [PubMed 18310074]).[supplied by OMIM, Feb 2010]

**Accessions** — [HGNC:14940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14940) · Entrez [151242](https://www.ncbi.nlm.nih.gov/gene/151242) · UniProt [Q8WVI7](https://www.uniprot.org/uniprotkb/Q8WVI7) · Ensembl [ENSG00000150722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150722)

## Data

Gene col 7455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7455); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7455]; `tensor/DDL_lfc|DDL_z.npy` [7455]; `embed/gene_vectors.npy` [7455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7455 or target_col == 7455). Every well: [[PPP1R1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
