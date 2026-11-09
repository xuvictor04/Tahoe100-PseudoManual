---
symbol: "MECP2"
type: "gene"
col: 9745
ensembl_id: "ENSG00000169057"
name: "methyl-CpG binding protein 2"
location: "Xq28"
module: 51
arm: "+"
pooled_cpm: 114.77
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# MECP2

*methyl-CpG binding protein 2* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.47× (z +17.2, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.540× (z -23.0, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTMR3]] (+0.57, fdr 1e-05), [[ZNF329]] (+0.56, fdr 3e-05), [[SCAF8]] (+0.55, fdr 3e-05); moves opposite to [[GLS]] (-0.47, fdr 8e-05), [[ITGA6]] (-0.46, fdr 3e-05), [[ITPRID2]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.47×** | +17.2 | 0e+00 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +11.4 | 1e-27 | 40/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +8.3 | 2e-14 | 28/48 (HT-29, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +6.2 | 7e-08 | 26/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 0.003 | 13/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.005 | 17/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.030 | 18/48 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.14× | +3.2 | 0.093 | 13/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.14 | 8/48 (C32, NCI-H2030, …) | top dose only |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.14 | 2/48 (HCT15, NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.540×** | -23.0 | 0e+00 | 46/49 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.548×** | -15.9 | 0e+00 | 45/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.576×** | -14.5 | 1e-45 | 45/48 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.591×** | -13.8 | 2e-41 | 45/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.711×** | -9.0 | 2e-17 | 37/49 (A549, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.707×** | -8.8 | 2e-16 | 32/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.723×** | -8.2 | 2e-14 | 27/48 (SNU-423, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.735×** | -8.1 | 3e-14 | 35/48 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.739×** | -7.7 | 1e-12 | 32/50 (SW480, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.735×** | -7.5 | 3e-12 | 33/45 (A-427, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -7.5 | 3e-12 | 0/50 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -7.3 | 1e-11 | 26/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.785×** | -6.4 | 7e-09 | 31/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.810×** | -5.3 | 4e-06 | 24/47 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.848× | -4.3 | 6e-04 | 21/48 (C32, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.905× | -3.7 | 0.007 | 10/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.767×** | -3.7 | 0.008 | 16/49 (A549, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.008 | 21/47 (SW48, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 145 | 2 | 8 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.46× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 156 | 2 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 97.6 | 2 | 6 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 4.45× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 125 | 4 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.83× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -18.9) |
| [[A-172 (line)]] | wt | 150 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -22.1) |
| [[NCI-H23 (line)]] | alt | 166 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -11.1) |
| [[SNU-423 (line)]] | alt | 173 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -17.1) |
| [[C32 (line)]] | wt | 117 | 2 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 10.0× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 91.9 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 126 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.19× (z +9.8) | [[Lonafarnib (drug)]] 5 µM 0.0819× (z -17.2) ⚠ toxic |
| [[SW 900 (line)]] | alt | 186 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -15.9) |
| [[A-427 (line)]] | wt | 111 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.31× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A549 (line)]] | wt | 108 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -19.6) |
| [[SW480 (line)]] | alt | 122 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.75× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -18.5) |
| [[A498 (line)]] | wt | 99.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -11.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -10.2) |
| [[J82 (line)]] | alt | 137 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 132 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.78× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -21.5) |
| [[Hs 766T (line)]] | wt | 130 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.99× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -10.4) |
| [[HT-29 (line)]] | alt | 143 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.542× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 76.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 94.0 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -12.4) |
| [[RKO (line)]] | wt | 99.2 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -13.7) |
| [[SW1417 (line)]] | alt | 141 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 3.55× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 142 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.07× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 77.8 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.65× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 81.1 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.97× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -8.5) |
| [[HS-578T (line)]] | alt | 75.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 77.0 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0795× (z -13.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.8) |
| [[KATO III (line)]] | alt | 121 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.30× (z +10.8) | — |
| [[LoVo (line)]] | wt | 64.2 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.54× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.9) |
| [[LS 180 (line)]] | wt | 54.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.99× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 125 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.37× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 151 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.48× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 77.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.1) |
| [[C-33 A (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.433× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 115 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +14.5) | — |
| [[H4 (line)]] | wt | 98.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.170× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 97.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 94.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 119 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.26× (z +8.9) | — |
| [[SW48 (line)]] | wt | 64.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.1) |
| [[CHP-212 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 164 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR3]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ZNF329]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SCAF8]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[EBLN2]] | +0.55 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[SUGT1P3-1]] | +0.54 | +0.41 / +0.31 | both halves | 2e-04 |  |
| [[TAB2]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[POGZ]] | +0.53 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[TEN1]] | +0.53 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[CARF]] | +0.53 | +0.35 / +0.54 | both halves | 1e-04 | STRING 509 |
| [[ZNF428]] | +0.52 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[IP6K1]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ZNF592]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ITGA6]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ITPRID2]] | -0.45 | -0.43 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MECP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.0, 14.5); signed map (8.8, -18.0). **Vector** length 77.7, 18.7% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +17.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +2.4 | -3.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.8 | -0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.8 | +0.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.5 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -23.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.0 | -8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | methyl-CpG binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,021,573-154,137,103 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RTT, MRX16, MRX79 |
| Gene groups (HGNC) | Methyl-CpG binding domain containing |
| Reactome | 16 pathways, smallest: Loss of MECP2 binding ability to 5mC-DNA; Loss of phosphorylation of MECP2 at T308; MECP2 regulates transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P51608](https://www.uniprot.org/uniprotkb/P51608) (Methyl-CpG-binding protein 2):

> Chromosomal protein that binds to methylated DNA. It can bind specifically to a single methyl-CpG pair. It is not influenced by sequences flanking the methyl-CpGs. Mediates transcriptional repression through interaction with histone deacetylase and the corepressor SIN3A. Binds both 5-methylcytosine (5mC) and 5-hydroxymethylcytosine (5hmC)-containing DNA, with a preference for 5-methylcytosine (5mC).

**Summary**, from NCBI Gene [4204](https://www.ncbi.nlm.nih.gov/gene/4204):

> DNA methylation is the major modification of eukaryotic genomes and plays an essential role in mammalian development. Human proteins MECP2, MBD1, MBD2, MBD3, and MBD4 comprise a family of nuclear proteins related by the presence in each of a methyl-CpG binding domain (MBD). Each of these proteins, with the exception of MBD3, is capable of binding specifically to methylated DNA. MECP2, MBD1 and MBD2 can also repress transcription from methylated gene promoters. In contrast to other MBD family …

**Accessions** — [HGNC:6990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6990) · Entrez [4204](https://www.ncbi.nlm.nih.gov/gene/4204) · UniProt [P51608](https://www.uniprot.org/uniprotkb/P51608) · Ensembl [ENSG00000169057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169057)

## Data

Gene col 9745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9745); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9745]; `tensor/DDL_lfc|DDL_z.npy` [9745]; `embed/gene_vectors.npy` [9745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9745 or target_col == 9745). Every well: [[MECP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MECP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
