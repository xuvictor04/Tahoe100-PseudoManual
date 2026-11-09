---
symbol: "NXN"
type: "gene"
col: 9519
ensembl_id: "ENSG00000167693"
name: "nucleoredoxin"
location: "17p13.3"
module: 160
arm: "+"
pooled_cpm: 95.81
n_lines_expressing: 40
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# NXN

*nucleoredoxin* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.34× (z +20.0, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.608× (z -11.3, q 1e-26, down in 22 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.737× (z -7.2, q 8e-11, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACS1]] (+0.53, fdr 7e-05), [[ATP11A]] (+0.50, fdr 5e-05), [[SLC66A2]] (+0.48, fdr 3e-05); moves opposite to [[RNF14]] (-0.49, fdr 5e-05), [[ANGEL2]] (-0.48, fdr 2e-05), [[NEK3]] (-0.48, fdr 2e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC34]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +20.0 | 0e+00 | 37/38 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +14.3 | 3e-44 | 34/38 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +13.6 | 1e-39 | 34/38 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +10.9 | 1e-25 | 23/38 (A549, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +7.6 | 4e-12 | 23/38 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +7.1 | 1e-10 | 18/39 (A549, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +6.1 | 8e-08 | 19/38 (HOP62, HEC-1-A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.62×** | +6.0 | 2e-07 | 19/38 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +5.6 | 1e-06 | 21/39 (A549, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +4.7 | 2e-04 | 17/38 (A549, SHP-77, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.20×** | +4.3 | 8e-04 | 19/38 (NCI-H23, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.42×** | +4.3 | 9e-04 | 17/39 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +4.3 | 9e-04 | 17/38 (NCI-H460, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.003 | 13/38 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.012 | 11/38 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.070 | 7/39 (J82, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -11.3 | 1e-26 | 22/34 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.657×** | -9.9 | 1e-20 | 25/39 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.659×** | -9.8 | 2e-20 | 32/38 (J82, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -7.2 | 8e-11 | 23/38 (SNU-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -6.7 | 2e-09 | 20/35 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.822×** | -4.6 | 4e-04 | 19/38 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.827×** | -4.3 | 0.001 | 20/37 (SW1417, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.829×** | -4.3 | 0.001 | 15/37 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.709×** | -4.2 | 0.001 | 12/29 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.891× | -3.9 | 0.006 | 12/39 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.855× | -3.7 | 0.011 | 14/38 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.867× | -3.4 | 0.034 | 13/38 (SW480, KATO III, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | 0.877× | -3.1 | 0.082 | 6/38 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.083 | 6/38 (J82, C32, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.086 | 12/37 (SW480, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.880× | -3.0 | 0.086 | 11/38 (C32, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.7 | 9 (5 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +21.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.40× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 161 | 4 (1 ⚠) | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.617× (z -8.9) |
| [[A549 (line)]] | wt | 45.0 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +23.8) | — |
| [[A-172 (line)]] | wt | 63.7 | 8 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 97.2 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +23.5) | [[Docetaxel (drug)]] 0.05 µM 0.439× (z -9.9) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 87.0 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -19.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 111 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -19.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 193 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.340× (z -11.4) |
| [[PANC-1 (line)]] | alt | 233 | 3 (1 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 4.46× (z +21.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.44× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -15.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 84.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +21.5) | — |
| [[HS-578T (line)]] | alt | 66.6 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.9) | — |
| [[LoVo (line)]] | wt | 78.3 | 5 (4 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +13.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.36× (z +11.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.545× (z -8.5) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A498 (line)]] | wt | 169 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +19.0) | — |
| [[C-33 A (line)]] | alt | 173 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0807× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.9) |
| [[HOP62 (line)]] | alt | 76.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +17.0) | — |
| [[SHP-77 (line)]] | alt | 42.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 173 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -11.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[C32 (line)]] | wt | 69.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.311× (z -10.5) |
| [[Hs 766T (line)]] | wt | 31.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +12.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.63× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -21.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 52.5 | 1 (1 ⚠) | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +9.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Harringtonine (drug)]] 0.5 µM 0.177× (z -11.9) |
| [[SW1417 (line)]] | alt | 42.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -11.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 198 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 95.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -8.5) ⚠ cell-cycle shift, explains ~86% of this change |
| [[COLO 205 (line)]] | alt | 65.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -8.5) ⚠ cell-cycle shift, explains ~86% of this change |
| [[RPMI-7951 (line)]] | alt | 56.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +14.9) | — |
| [[SW 900 (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.74 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACS1]] | +0.53 | +0.56 / +0.37 | both halves | 7e-05 |  |
| [[ATP11A]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[SLC66A2]] | +0.48 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[KCNQ1]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RCOR1]] | +0.47 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[IFFO2]] | +0.47 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[ARHGEF18]] | +0.47 | +0.50 / +0.32 | both halves | 1e-04 |  |
| [[MAGI1]] | +0.47 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[TMC6]] | +0.46 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[ZFPM1]] | +0.46 | +0.31 / +0.47 | both halves | 2e-04 |  |
| [[TTYH3]] | +0.45 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[CAMK1D]] | +0.45 | +0.43 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF14]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ANGEL2]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NEK3]] | -0.48 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RBM45]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SMPDL3A]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[PGGT1B]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[PIGC]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[UNC50]] | -0.46 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[ZNF419]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZNF287]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ACCS]] | -0.44 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[KCTD18]] | -0.43 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC34]] | B | LRRC34 activity raises NXN's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without LRRC34 | 0.098 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-10.0, 31.1); signed map (-18.1, 42.0). **Vector** length 104, 25.5% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +20.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.4 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +13.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +0.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.1 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -9.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -4.9 | -9.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.9 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleoredoxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:799,310-979,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12614, NRX |
| Gene groups (HGNC) | Nucleoredoxin family; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DKJ4](https://www.uniprot.org/uniprotkb/Q6DKJ4) (Nucleoredoxin):

> Functions as a redox-dependent negative regulator of the Wnt signaling pathway, possibly by preventing ubiquitination of DVL3 by the BCR(KLHL12) complex. May also function as a transcriptional regulator act as a regulator of protein phosphatase 2A (PP2A) (By similarity).

**Summary**, from NCBI Gene [64359](https://www.ncbi.nlm.nih.gov/gene/64359):

> This gene encodes a member of the thioredoxin superfamily, a group of small, multifunctional redox-active proteins. Members of this family are characterized by a conserved active motif called the thioredoxin fold that catalyzes disulfide bond formation and isomerization. The encoded protein acts a redox-dependent regulator of the Wnt signaling pathway and is involved in cell growth and differentiation. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:18008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18008) · Entrez [64359](https://www.ncbi.nlm.nih.gov/gene/64359) · UniProt [Q6DKJ4](https://www.uniprot.org/uniprotkb/Q6DKJ4) · Ensembl [ENSG00000167693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167693)

## Data

Gene col 9519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9519); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9519]; `tensor/DDL_lfc|DDL_z.npy` [9519]; `embed/gene_vectors.npy` [9519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9519 or target_col == 9519). Every well: [[NXN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NXN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
