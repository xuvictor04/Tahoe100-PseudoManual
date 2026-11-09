---
symbol: "DSC2"
type: "gene"
col: 5597
ensembl_id: "ENSG00000134755"
name: "desmocollin 2"
location: "18q12.1"
module: 31
arm: "+"
pooled_cpm: 53.79
n_lines_expressing: 28
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 35
direction_downstream: 45
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# DSC2

*desmocollin 2* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.72× (z +19.7, q 0e+00, up in 19 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.28× (z +6.8, q 1e-09, up in 16 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.228× (z -29.1, q 0e+00, down in 26 of 26 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSG2]] (+0.69, fdr 7e-06), [[KLK11]] (+0.61, fdr 7e-06), [[MAP7]] (+0.61, fdr 1e-05); moves opposite to [[SNU13]] (-0.48, fdr 1e-04), [[CHEK2]] (-0.46, fdr 3e-04), [[CCDC107]] (-0.46, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[IL1RN]] → it (grade B ⚠); 45 go from it, the strongest it → [[PFKFB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +19.7 | 0e+00 | 19/26 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +15.2 | 0e+00 | 17/22 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +13.6 | 1e-39 | 14/23 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.8 | 1e-09 | 16/26 (J82, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 1e-07 | 15/26 (LS 180, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +6.1 | 1e-07 | 16/26 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +6.0 | 2e-07 | 14/27 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +5.9 | 2e-07 | 13/26 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +5.3 | 8e-06 | 12/26 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +5.0 | 3e-05 | 8/26 (SW 900, A-427, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +5.0 | 3e-05 | 15/26 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +4.6 | 2e-04 | 13/26 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 13/26 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.7 | 0.007 | 5/20 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.018 | 11/26 (NCI-H460, HCT15, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.019 | 12/25 (CFPAC-1, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.034 | 13/26 (KATO III, HEC-1-A, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.034 | 11/26 (LS 180, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.034 | 9/26 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.040 | 10/26 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.046 | 9/26 (CFPAC-1, COLO 205, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.065 | 3/26 (COLO 205, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, none with an alert; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.228×** | -29.1 | 0e+00 | 26/26 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.233×** | -28.7 | 0e+00 | 25/26 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.269×** | -25.8 | 0e+00 | 26/26 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.446×** | -15.9 | 0e+00 | 24/26 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.566×** | -11.2 | 4e-27 | 23/26 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.389×** | -9.7 | 2e-20 | 23/27 (AsPC-1, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.753×** | -7.9 | 3e-13 | 15/26 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.550×** | -6.2 | 5e-08 | 20/26 (KATO III, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.748×** | -5.7 | 7e-07 | 12/26 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.790×** | -4.6 | 2e-04 | 15/27 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.797×** | -4.4 | 5e-04 | 13/26 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.802×** | -4.3 | 7e-04 | 6/26 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.798×** | -4.3 | 9e-04 | 18/27 (KATO III, LoVo, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.808×** | -4.2 | 0.001 | 9/25 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.808×** | -4.2 | 0.001 | 9/26 (NCI-H1573, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 114 | 4 (1 ⚠) | 8 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.0998× (z -23.3) |
| [[NCI-H1573 (line)]] | alt | 82.1 | 4 (3 ⚠) | 8 | [[Dinaciclib (drug)]] 0.05 µM 3.22× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -21.2) |
| [[KATO III (line)]] | alt | 76.6 | 6 (6 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.0751× (z -24.5) |
| [[LS 180 (line)]] | wt | 175 | 1 | 7 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.46× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.0583× (z -29.3) |
| [[AsPC-1 (line)]] | alt | 286 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0442× (z -28.6) |
| [[NCI-H460 (line)]] | wt | 31.4 | 1 | 6 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.74× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 201 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0860× (z -25.5) |
| [[HEC-1-A (line)]] | alt | 42.6 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -17.5) |
| [[COLO 205 (line)]] | alt | 42.5 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0399× (z -21.4) |
| [[HepG2_C3A (line)]] | wt | 71.1 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0664× (z -20.2) |
| [[HT-29 (line)]] | alt | 83.5 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +8.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.120× (z -18.7) |
| [[SW48 (line)]] | wt | 218 | 2 | 3 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.62× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.105× (z -16.3) |
| [[A-427 (line)]] | wt | 36.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.215× (z -13.7) |
| [[Hs 766T (line)]] | wt | 34.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -15.9) |
| [[LoVo (line)]] | wt | 259 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0745× (z -22.5) |
| [[NCI-H2347 (line)]] | alt | 129 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -19.6) |
| [[SW1417 (line)]] | alt | 98.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0980× (z -25.9) |
| [[BT-474 (line)]] | alt | 127 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -15.1) |
| [[SW 900 (line)]] | alt | 46.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.232× (z -10.5) |
| [[HCT15 (line)]] | alt | 77.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -12.8) |
| [[J82 (line)]] | alt | 15.6 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.69× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -8.9) |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -10.5) |
| [[A-172 (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.73 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSG2]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | same gene group; pathway: Formation of the cornified envelope; STRING 999 |
| [[KLK11]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MAP7]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[MYO5B]] | +0.60 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[DHRS9]] | +0.55 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TACSTD2]] | +0.55 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[TMEM30B]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DAPP1]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PDCD6IP-DT]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[LINC00857]] | +0.52 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[KPNA7]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[COL17A1]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNU13]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CHEK2]] | -0.46 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[CCDC107]] | -0.46 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[ZHX3]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[NAT9]] | -0.44 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[TM2D3]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MMS19]] | -0.43 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[MNX1]] | -0.43 | -0.18 / -0.53 | ⚠ one half (not replicated) | 1e-03 |  |
| [[PHKA2]] | -0.43 | -0.25 / -0.31 | both halves | 4e-04 | pathway: HALLMARK_GLYCOLYSIS |
| [[MGAT1]] | -0.43 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[MT2A]] | -0.42 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[HDHD5]] | -0.42 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[SLC25A32]] | -0.42 | -0.32 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 9, C 26. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RN]] | B | IL1RN activity raises DSC2's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 3.29× lower at baseline in the lines without IL1RN | 0.011 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[F2RL1]] | B | F2RL1 activity raises DSC2's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 4.11× lower at baseline in the lines without F2RL1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[HTR1D]] | B | HTR1D activity raises DSC2's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.55× lower at baseline in the lines without HTR1D | 0.018 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises DSC2's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.00× lower at baseline in the lines without LMO7 | 0.052 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[DSG2]] | B | DSG2 activity raises DSC2's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 4.80× lower at baseline in the lines without DSG2 | 0.067 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[DHRS9]] | B | DHRS9 activity raises DSC2's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 3.07× lower at baseline in the lines without DHRS9 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[C6orf141]] | B | C6orf141 activity raises DSC2's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 2.71× lower at baseline in the lines without C6orf141 | 0.083 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[ACSL5]] | B | ACSL5 activity raises DSC2's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.94× lower at baseline in the lines without ACSL5 | 0.087 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[MT2A]] | B | MT2A activity lowers DSC2's level | lines that do not express MT2A (9) vs lines expressing it (41) | 3.39× higher at baseline in the lines without MT2A | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[LAD1]] | C | LAD1 activity raises DSC2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 7.10× lower at baseline in the lines without LAD1 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises DSC2's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 8.58× lower at baseline in the lines without EPCAM | 1e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises DSC2's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 7.90× lower at baseline in the lines without C1orf116 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 23, C 22. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PFKFB2]] | B | DSC2 activity raises PFKFB2's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without DSC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[DSG2]] | B | DSC2 activity raises DSG2's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.62× lower at baseline in the lines without DSC2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[PKP3]] | B | DSC2 activity raises PKP3's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.04× lower at baseline in the lines without DSC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[EPS8L1]] | B | DSC2 activity raises EPS8L1's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.50× lower at baseline in the lines without DSC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[LMO7DN]] | B | DSC2 activity raises LMO7DN's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without DSC2 | 0.022 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[ATP9A]] | B | DSC2 activity raises ATP9A's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without DSC2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[LMO7]] | B | DSC2 activity raises LMO7's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.02× lower at baseline in the lines without DSC2 | 0.024 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[YOD1]] | B | DSC2 activity raises YOD1's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 1.85× lower at baseline in the lines without DSC2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[PKP3]] | B | DSC2 activity strengthens PKP3's drug response | lines that do not express DSC2 (11) vs lines expressing it (22) | the lines without DSC2 respond 0.82× as strongly (z diff +1.42); strongest at Idarubicin (hydrochloride) 5 µM: 0.59x vs 0.44x (z diff +3.5) | 0.035 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT; target measured in part of the lines; artifact flags |
| [[ACSL5]] | B | DSC2 activity raises ACSL5's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without DSC2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[FAM83H]] | B | DSC2 activity raises FAM83H's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.09× lower at baseline in the lines without DSC2 | 0.045 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[KPNA7]] | B | DSC2 activity raises KPNA7's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without DSC2 | 0.047 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.367). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, 57.8); signed map (54.3, 7.5). **Vector** length 105, 32.0% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +19.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +4.1 |
| fall | [[Budesonide (drug)]] 5 µM |  | -2.0 | -5.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.9 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | desmocollin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:31,058,545-31,102,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDHF2; previously DSC3 |
| Gene groups (HGNC) | Desmosomal cadherins |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02487](https://www.uniprot.org/uniprotkb/Q02487) (Desmocollin-2):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion. Promotes timely incorporation of DSG2 into desmosome intercellular junctions and promotes interaction of desmosome cell junctions with intermediate filament cytokeratin, via modulation of DSP phosphorylation. Plays an important role in desmosome-mediated maintenance of intestinal epithelial cell intercellular adhesion strength and barrier function. Positively regulates wound healing of …

**Summary**, from NCBI Gene [1824](https://www.ncbi.nlm.nih.gov/gene/1824):

> This gene encodes a member of the desmocollin protein subfamily. Desmocollins, along with desmogleins, are cadherin-like transmembrane glycoproteins that are major components of the desmosome. Desmosomes are cell-cell junctions that help resist shearing forces and are found in high concentrations in cells subject to mechanical stress. This gene is found in a cluster with other desmocollin family members on chromosome 18. Mutations in this gene are associated with arrhythmogenic right …

**Accessions** — [HGNC:3036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3036) · Entrez [1824](https://www.ncbi.nlm.nih.gov/gene/1824) · UniProt [Q02487](https://www.uniprot.org/uniprotkb/Q02487) · Ensembl [ENSG00000134755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134755)

## Data

Gene col 5597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5597); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5597]; `tensor/DDL_lfc|DDL_z.npy` [5597]; `embed/gene_vectors.npy` [5597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5597 or target_col == 5597). Every well: [[DSC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
