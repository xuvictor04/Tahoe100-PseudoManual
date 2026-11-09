---
symbol: "CROT"
type: "gene"
col: 83
ensembl_id: "ENSG00000005469"
name: "carnitine O-octanoyltransferase"
location: "7q21.12"
module: 57
arm: "+"
pooled_cpm: 11.5
n_lines_expressing: 48
n_dd_up: 36
n_dd_down: 17
n_dd_up_clean: 25
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# CROT

*carnitine O-octanoyltransferase* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.35× (z +18.6, q 0e+00, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.493× (z -15.5, q 0e+00, down in 37 of 45 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.412× (z -13.7, q 3e-40, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB4A]] (+0.71, fdr 7e-06), [[TMEM185A]] (+0.68, fdr 1e-05), [[ATP5F1C]] (+0.67, fdr 1e-05); moves opposite to [[DPH1-AS1]] (-0.60, fdr 1e-05), [[KDSR]] (-0.58, fdr 4e-05), [[LETM2]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GJC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 83.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.35×** | +18.6 | 0e+00 | 40/46 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.20×** | +17.9 | 0e+00 | 41/46 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.60×** | +14.7 | 0e+00 | 37/45 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.86×** | +9.6 | 1e-19 | 36/46 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +8.6 | 7e-16 | 30/46 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +7.9 | 3e-13 | 23/46 (C32, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.7 | 1e-09 | 12/20 (Hs 766T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.57×** | +6.7 | 1e-09 | 23/39 (LS 180, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +6.2 | 3e-08 | 22/44 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.48×** | +6.1 | 7e-08 | 20/45 (C32, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.0 | 1e-07 | 17/36 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 1e-06 | 21/43 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +5.1 | 1e-05 | 15/46 (Hs 766T, PANC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 17/46 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.38×** | +4.8 | 7e-05 | 16/44 (A498, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +4.7 | 8e-05 | 15/46 (A498, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 1e-04 | 12/46 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 4e-04 | 15/45 (C32, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.33×** | +4.3 | 5e-04 | 9/45 (SW 900, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.2 | 7e-04 | 10/45 (HT-29, NCI-H2347, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.001 | 9/40 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 83.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.493×** | -15.5 | 0e+00 | 37/45 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.412×** | -13.7 | 3e-40 | 37/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -13.6 | 6e-40 | 36/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -11.8 | 4e-30 | 32/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.503×** | -10.2 | 2e-22 | 29/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.520×** | -10.1 | 5e-22 | 31/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.579×** | -8.5 | 2e-15 | 25/43 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -6.9 | 5e-10 | 23/41 (C-33 A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -6.5 | 5e-09 | 24/46 (SK-MEL-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.722×** | -5.0 | 3e-05 | 16/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.737×** | -4.7 | 1e-04 | 16/45 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -3.9 | 0.005 | 16/45 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.782×** | -3.8 | 0.006 | 17/45 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.4 | 0.024 | 18/44 (C32, SK-MEL-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.036 | 12/45 (RKO, NCI-H661, …) | two highest doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.861× | -3.3 | 0.036 | 10/46 (Hs 766T, SW 1088, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.040 | 7/46 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.678×** | -3.1 | 0.053 | 13/42 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.825×** | -3.0 | 0.085 | 14/45 (NCI-H2030, AN3 CA, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 83. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.0 | 1 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.0127× (z -33.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.168× (z -13.5) |
| [[C32 (line)]] | wt | 41.8 | 2 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.78× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0897× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -18.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -12.2) |
| [[A498 (line)]] | wt | 21.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.24× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 10.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.48× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -12.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 9.27 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -8.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +8.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0421× (z -8.5) |
| [[HOP62 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0825× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 12.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +8.9) | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -16.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 83), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB4A]] | +0.71 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.68 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.67 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SNX4]] | +0.67 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.66 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[RHOT1]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[REPS1]] | +0.65 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SKP2]] | +0.65 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[METTL17]] | +0.64 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[TM7SF3]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SDHB]] | +0.64 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[UBAC1]] | +0.63 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH1-AS1]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[KDSR]] | -0.58 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[LETM2]] | -0.58 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[KDM6B]] | -0.58 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[HIVEP2-DT]] | -0.57 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[EPHA1-AS1]] | -0.57 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[ZNF597]] | -0.57 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[EPOP]] | -0.57 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[LINC01033]] | -0.57 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[GGPS1]] | -0.57 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MMP25]] | -0.56 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TGIF2-RAB5IF]] | -0.56 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GJC1]] | B | GJC1 activity strengthens CROT's drug response | lines that do not express GJC1 (11) vs lines expressing it (35) | the lines without GJC1 respond 0.62× as strongly (z diff +1.82); strongest at Homoharringtonine 5 µM: 0.74x vs 0.39x (z diff +4.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.3, -8.9); signed map (-32.6, -12.4). **Vector** length 68.9, 12.5% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +9.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[NG25 (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.4 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.1 | +7.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +4.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.8 | -15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.7 | -8.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.7 | -10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.6 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -3.3 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.2 | +0.5 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.0 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | carnitine O-octanoyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:87,345,664-87,399,794 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COT |
| Gene groups (HGNC) | Carnitine acyltransferases |
| Hallmark sets | BILE_ACID_METABOLISM, XENOBIOTIC_METABOLISM, KRAS_SIGNALING_UP |
| Reactome | 6 pathways, smallest: Beta-oxidation of pristanoyl-CoA; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKG9](https://www.uniprot.org/uniprotkb/Q9UKG9) (Peroxisomal carnitine O-octanoyltransferase):

> Beta-oxidation of fatty acids. The highest activity concerns the C6 to C10 chain length substrate. Converts the end product of pristanic acid beta oxidation, 4,8-dimethylnonanoyl-CoA, to its corresponding carnitine ester.

**Summary**, from NCBI Gene [54677](https://www.ncbi.nlm.nih.gov/gene/54677):

> This gene encodes a member of the carnitine/choline acetyltransferase family. The encoded protein converts 4,8-dimethylnonanoyl-CoA to its corresponding carnitine ester. This transesterification occurs in the peroxisome and is necessary for transport of medium- and long- chain acyl-CoA molecules out of the peroxisome to the cytosol and mitochondria. The protein thus plays a role in lipid metabolism and fatty acid beta-oxidation. Alternatively spliced transcript variants have been …

**Accessions** — [HGNC:2366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2366) · Entrez [54677](https://www.ncbi.nlm.nih.gov/gene/54677) · UniProt [Q9UKG9](https://www.uniprot.org/uniprotkb/Q9UKG9) · Ensembl [ENSG00000005469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005469)

## Data

Gene col 83: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 83); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 83, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 83]; `tensor/DDL_lfc|DDL_z.npy` [83]; `embed/gene_vectors.npy` [83]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 83 or target_col == 83). Every well: [[CROT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CROT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
