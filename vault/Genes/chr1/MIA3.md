---
symbol: "MIA3"
type: "gene"
col: 7796
ensembl_id: "ENSG00000154305"
name: "MIA SH3 domain ER export factor 3"
location: "1q41"
module: 35
arm: "-"
pooled_cpm: 117.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MIA3

*MIA SH3 domain ER export factor 3* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.53× (z +25.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.751× (z -10.9, q 4e-25, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN7]] (+0.61, fdr 2e-05), [[GPATCH11]] (+0.61, fdr 1e-05), [[CCDC112]] (+0.57, fdr 4e-05); moves opposite to [[MED28-DT]] (-0.57, fdr 4e-04), [[SIAH2-AS1]] (-0.56, fdr 2e-04), [[CCDC26]] (-0.55, fdr 1e-04).
> It sits in the **-** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +25.1 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +24.9 | 0e+00 | 48/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +20.7 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +11.6 | 8e-29 | 42/48 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +8.1 | 8e-14 | 42/49 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +7.7 | 9e-13 | 35/48 (AsPC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.20× | +6.9 | 4e-10 | 24/48 (LS 180, HEC-1-A, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +5.6 | 1e-06 | 25/48 (SNU-423, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +5.3 | 7e-06 | 25/48 (LS 180, HEC-1-A, …) | top dose only | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +5.3 | 8e-06 | 25/49 (HS-578T, BT-474, …) | top dose only |  |
| [[Decitabine (drug)]] 5 µM |  | 1.14× | +3.4 | 0.030 | 10/48 (C-33 A, NCI-H460, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.037 | 17/48 (LOX-IMVI, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.09× | +3.3 | 0.037 | 11/48 (RKO, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.039 | 15/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.039 | 17/49 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.044 | 12/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -10.9 | 4e-25 | 33/49 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.798×** | -6.1 | 3e-07 | 25/49 (SK-MEL-2, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.804×** | -5.9 | 6e-07 | 27/48 (SW480, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -5.9 | 6e-07 | 28/48 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -5.5 | 4e-06 | 22/50 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **0.825×** | -5.2 | 2e-05 | 25/48 (HCT15, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.769×** | -5.1 | 3e-05 | 31/48 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.707×** | -4.9 | 7e-05 | 29/47 (NCI-H661, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.741×** | -4.2 | 0.001 | 20/38 (HT-29, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -4.2 | 0.002 | 21/45 (SW48, NCI-H460, …) | inconsistent across doses | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.004 | 18/48 (SNU-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.764×** | -3.8 | 0.007 | 22/45 (A498, A549, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -3.8 | 0.008 | 19/45 (Hs 766T, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.907× | -3.7 | 0.008 | 8/48 (A498, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.020 | 16/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Acetohexamide (drug)]] 5 µM |  | 0.924× | -3.0 | 0.090 | 0/48 | top dose only |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.896× | -3.0 | 0.095 | 8/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 139 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.0) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.76× (z +14.4) | — |
| [[NCI-H460 (line)]] | wt | 132 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +19.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -13.5) |
| [[SW 900 (line)]] | alt | 169 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 93.8 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 3.38× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -12.5) |
| [[C32 (line)]] | wt | 66.7 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.29× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 96.7 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 103 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +16.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 98.9 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.4) |
| [[RKO (line)]] | wt | 141 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 135 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.71× (z +17.5) | — |
| [[A-172 (line)]] | wt | 126 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +16.8) | — |
| [[A498 (line)]] | wt | 201 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 1.85× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -14.1) |
| [[A549 (line)]] | wt | 108 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.54× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -11.2) |
| [[BT-474 (line)]] | alt | 78.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.20× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 76.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.67× (z +15.4) | — |
| [[HCT15 (line)]] | alt | 132 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +10.4) | [[Thymol (drug)]] 0.5 µM 0.437× (z -8.7) |
| [[HOP62 (line)]] | alt | 116 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.11× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -9.1) |
| [[Hs 766T (line)]] | wt | 153 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.68× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -11.4) |
| [[HT-29 (line)]] | alt | 141 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 117 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +14.5) | — |
| [[J82 (line)]] | alt | 118 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.60× (z +12.5) | — |
| [[KATO III (line)]] | alt | 147 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.33× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -11.1) |
| [[LoVo (line)]] | wt | 122 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 111 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 84.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.44× (z +18.1) | — |
| [[NCI-H2030 (line)]] | alt | 74.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +14.1) | — |
| [[Panc 03.27 (line)]] | alt | 116 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 118 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +19.3) | — |
| [[RPMI-7951 (line)]] | alt | 123 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -8.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SHP-77 (line)]] | alt | 164 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +10.5) | — |
| [[SW480 (line)]] | alt | 106 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 100 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +9.5) | — |
| [[H4 (line)]] | wt | 100 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 80.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 111 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.22× (z +10.7) | — |
| [[SW48 (line)]] | wt | 120 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.2) ⚠ cell-cycle shift, explains ~16% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -11.7) |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0564× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN7]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GPATCH11]] | +0.61 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CCDC112]] | +0.57 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PJA2]] | +0.57 | +0.45 / +0.36 | both halves | 9e-05 |  |
| [[STAM2]] | +0.54 | +0.40 / +0.44 | both halves | 4e-05 | same gene group |
| [[MRPS34]] | +0.53 | +0.36 / +0.30 | both halves | 2e-04 |  |
| [[TTBK2]] | +0.52 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[TTC3P1]] | +0.52 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[IK]] | +0.51 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[AKAP9]] | +0.51 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[PDHB]] | +0.51 | +0.28 / +0.48 | both halves | 3e-04 |  |
| [[RPAP3]] | +0.51 | +0.34 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED28-DT]] | -0.57 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[SIAH2-AS1]] | -0.56 | -0.29 / -0.29 | both halves | 2e-04 |  |
| [[CCDC26]] | -0.55 | -0.41 / -0.32 | both halves | 1e-04 |  |
| [[RCC1]] | -0.55 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[PPP1R15B-AS1]] | -0.54 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[GSK3B-DT]] | -0.54 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[ACTR3-AS1]] | -0.54 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[CDK6-AS1]] | -0.53 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[CCNT2-AS1]] | -0.53 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[BHLHE40-AS1]] | -0.53 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[PBLD]] | -0.53 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[NINJ2]] | -0.52 | -0.30 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (14.5, 19.3); signed map (-19.9, -10.6). **Vector** length 117, 32.5% of its response variance represented; |z| ≥ 3 in 1,279 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +24.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +20.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +25.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +11.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +8.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.0 | +0.7 |
|  | [[Riluzole hydrochloride (drug)]] 0.5 µM |  | +2.0 | +2.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.3 | -10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.5 | -3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -4.2 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -5.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.8 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | MIA SH3 domain ER export factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:222,618,097-222,668,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ6077, FLJ39207, KIAA0268, TANGO, TANGO1 |
| Gene groups (HGNC) | CTAGE family; MIA family; SH3 domain containing |
| Reactome | 8 pathways, smallest: Cargo concentration in the ER; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JRA6](https://www.uniprot.org/uniprotkb/Q5JRA6) (Transport and Golgi organization protein 1 homolog):

> Plays a role in the transport of cargos that are too large to fit into COPII-coated vesicles and require specific mechanisms to be incorporated into membrane-bound carriers and exported from the endoplasmic reticulum. This protein is required for collagen VII (COL7A1) secretion by loading COL7A1 into transport carriers. It may participate in cargo loading of COL7A1 at endoplasmic reticulum exit sites by binding to COPII coat subunits Sec23/24 and guiding SH3-bound COL7A1 into a growing carrier. …

**Summary**, from NCBI Gene [375056](https://www.ncbi.nlm.nih.gov/gene/375056):

> Enables cargo receptor activity. Involved in several processes, including COPII-coated vesicle cargo loading; cell migration involved in sprouting angiogenesis; and regulation of leukocyte migration. Located in endoplasmic reticulum exit site and endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24008) · Entrez [375056](https://www.ncbi.nlm.nih.gov/gene/375056) · UniProt [Q5JRA6](https://www.uniprot.org/uniprotkb/Q5JRA6) · Ensembl [ENSG00000154305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154305)

## Data

Gene col 7796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7796); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7796]; `tensor/DDL_lfc|DDL_z.npy` [7796]; `embed/gene_vectors.npy` [7796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7796 or target_col == 7796). Every well: [[MIA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
