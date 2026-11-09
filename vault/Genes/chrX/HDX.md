---
symbol: "HDX"
type: "gene"
col: 9095
ensembl_id: "ENSG00000165259"
name: "highly divergent homeobox"
location: "Xq21.1"
module: 32
arm: "+"
pooled_cpm: 25.93
n_lines_expressing: 34
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 14
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# HDX

*highly divergent homeobox* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.30× (z +27.2, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.517× (z -8.7, q 2e-15, down in 22 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.600× (z -6.5, q 2e-08, down in 20 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD9]] (+0.66, fdr 7e-06), [[RASGRP3]] (+0.66, fdr 7e-06), [[GBP5]] (+0.65, fdr 7e-06); moves opposite to [[SETD3]] (-0.64, fdr 7e-06), [[GMCL1]] (-0.58, fdr 1e-05), [[MMS19]] (-0.57, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAJC18]] → it (grade C ⚠); 2 go from it, the strongest it → [[IGSF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.30×** | +27.2 | 0e+00 | 30/32 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.74×** | +16.7 | 0e+00 | 32/32 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +11.4 | 7e-28 | 28/32 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +9.1 | 1e-17 | 25/31 (CFPAC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +7.4 | 1e-11 | 25/32 (HOP62, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.8 | 6e-07 | 24/31 (HOP62, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +5.6 | 1e-06 | 16/32 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.6 | 1e-06 | 15/32 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +4.9 | 5e-05 | 18/32 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 16/32 (SW1417, PANC-1, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.6 | 3e-04 | 18/32 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +4.1 | 0.002 | 17/31 (SW480, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.008 | 12/32 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.009 | 12/32 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.31×** | +3.5 | 0.017 | 13/32 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.023 | 16/32 (SW1417, Hs 766T, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.031 | 10/31 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.037 | 11/32 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.080 | 5/31 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.0 | 0.082 | 7/32 (MIA PaCa-2, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.517×** | -8.7 | 2e-15 | 22/29 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -8.0 | 3e-13 | 19/28 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -6.5 | 2e-08 | 20/32 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -5.6 | 3e-06 | 17/32 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.747×** | -5.5 | 5e-06 | 20/32 (PANC-1, BT-474, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.748×** | -5.4 | 5e-06 | 18/32 (A549, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.678×** | -4.7 | 2e-04 | 14/29 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -4.7 | 2e-04 | 16/31 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.805×** | -4.1 | 0.003 | 16/32 (A549, A498, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.811×** | -3.9 | 0.005 | 14/32 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.008 | 14/32 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.752×** | -3.8 | 0.008 | 12/32 (A549, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.754×** | -3.7 | 0.008 | 17/32 (A549, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.756×** | -3.7 | 0.009 | 15/32 (CHP-212, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.753×** | -3.5 | 0.015 | 15/32 (NCI-H661, LOX-IMVI, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.780×** | -3.3 | 0.035 | 13/32 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.783×** | -3.2 | 0.040 | 12/32 (CHP-212, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.780×** | -3.2 | 0.050 | 10/32 (A549, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 64.9 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -12.6) |
| [[A-172 (line)]] | wt | 54.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 57.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -16.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.8 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +16.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -8.6) |
| [[BT-474 (line)]] | alt | 52.4 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 43.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +27.5) | — |
| [[HOP62 (line)]] | alt | 22.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +18.0) | — |
| [[Panc 03.27 (line)]] | alt | 40.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 50.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.8) | [[Docetaxel (drug)]] 0.05 µM 0.283× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~89% of this change |
| [[SK-MEL-2 (line)]] | alt | 64.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +13.6) | — |
| [[A549 (line)]] | wt | 44.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -10.1) |
| [[C32 (line)]] | wt | 10.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +11.7) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0752× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +17.9) | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -12.0) |
| [[SNU-423 (line)]] | alt | 70.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 44.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +15.6) | — |
| [[SW480 (line)]] | alt | 23.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +15.8) | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -8.7) ⚠ cell-cycle shift, explains ~2% of this change |
| [[H4 (line)]] | wt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.2) | — |
| [[J82 (line)]] | alt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 8.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 9.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +14.1) | — |
| [[A-427 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD9]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RASGRP3]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GBP5]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[KCNT2]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[IFIT5]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TNIP3]] | +0.63 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[RIPK2-DT]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.63 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[IFI16]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CARD6]] | +0.62 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[ZNFX1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PATL2]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.64 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[MMS19]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[RPA1]] | -0.57 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[GLG1]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SMARCD2]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[USP48]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[VPS26B]] | -0.54 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC7]] | -0.54 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[TSC2]] | -0.54 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC18]] | C | DNAJC18 activity raises HDX's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 5.74× lower at baseline in the lines without DNAJC18 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGSF1]] | B | HDX activity lowers IGSF1's level | lines that do not express HDX (16) vs lines expressing it (34) | 1.03× higher at baseline in the lines without HDX | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: LOXL2, SDK2, WIPF1 |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | B | HDX activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express HDX (16) vs lines expressing it (32) | the lines without HDX: 0.70× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: LOXL2, SDK2, WIPF1 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, 24.4); signed map (46.3, 24.7). **Vector** length 108, 31.0% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.53 to 23); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.52 to 21); *IFIT antiviral response* (reactome, mean cos +0.55 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +16.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +27.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.6 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.2 | -5.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.8 | -2.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | highly divergent homeobox |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:84,317,874-84,502,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30678; previously CXorf43 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

UniProt [Q7Z353](https://www.uniprot.org/uniprotkb/Q7Z353) carries no function annotation.

**Summary**, from NCBI Gene [139324](https://www.ncbi.nlm.nih.gov/gene/139324):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26411) · Entrez [139324](https://www.ncbi.nlm.nih.gov/gene/139324) · UniProt [Q7Z353](https://www.uniprot.org/uniprotkb/Q7Z353) · Ensembl [ENSG00000165259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165259)

## Data

Gene col 9095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9095); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9095]; `tensor/DDL_lfc|DDL_z.npy` [9095]; `embed/gene_vectors.npy` [9095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9095 or target_col == 9095). Every well: [[HDX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
