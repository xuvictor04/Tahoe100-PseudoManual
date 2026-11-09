---
symbol: "CAPZA2"
type: "gene"
col: 12725
ensembl_id: "ENSG00000198898"
name: "capping actin protein of muscle Z-line subunit alpha 2"
location: "7q31.2"
module: 45
arm: "+"
pooled_cpm: 162.78
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# CAPZA2

*capping actin protein of muscle Z-line subunit alpha 2* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.24× (z +13.0, q 8e-36, up in 47 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.300×, NCI-H1573 0.397×, BT-474 0.369×, NCI-H2347 0.391×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.401×, RKO 0.460×, NCI-H1573 0.508×, NCI-H2347 0.490×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.287×, A-427 0.257×, CFPAC-1 0.441×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Docetaxel (Trihydrate) (drug)]] 0.05 µM in 1 line (SW 1088 0.145×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.509×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1CB]] (+0.62, fdr 1e-05), [[H3-3A]] (+0.61, fdr 7e-06), [[LTA4H]] (+0.60, fdr 1e-05); moves opposite to [[METTL2B]] (-0.55, fdr 2e-05), [[SDHAF2]] (-0.54, fdr 4e-05), [[AFG3L1P]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +13.0 | 8e-36 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +12.7 | 1e-34 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +12.6 | 5e-34 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +9.7 | 6e-20 | 44/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +9.5 | 2e-19 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +8.1 | 8e-14 | 32/47 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.1 | 7e-11 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +5.8 | 4e-07 | 27/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 8e-04 | 25/48 (PANC-1, SK-MEL-2, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +4.3 | 8e-04 | 29/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.004 | 21/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.19× | +3.7 | 0.011 | 22/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.035 | 17/48 (SNU-1, RKO, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.300×, NCI-H1573 0.397×, BT-474 0.369×, NCI-H2347 0.391×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.401×, RKO 0.460×, NCI-H1573 0.508×, NCI-H2347 0.490×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.287×, A-427 0.257×, CFPAC-1 0.441×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Docetaxel (Trihydrate) (drug)]] 0.05 µM in 1 line (SW 1088 0.145×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.509×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -4.2 | 0.016 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.838× | -3.8 | 0.046 | 24/48 (C32, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 0.841× | -3.6 | 0.058 | 22/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.847× | -3.5 | 0.058 | 18/48 (SW 900, Panc 03.27, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.851× | -3.4 | 0.068 | 16/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.075 | 15/48 (CHP-212, A-427, …) | two highest doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.851× | -3.3 | 0.075 | 19/49 (AsPC-1, SW1417, …) | top dose only | plate-row cell shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.898× | -3.3 | 0.080 | 18/49 (SNU-423, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.861× | -3.2 | 0.088 | 17/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.862× | -3.2 | 0.088 | 10/47 (RKO, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.861× | -3.0 | 0.13 | 12/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 98.1 | 13 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.03× (z +26.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.84× (z +25.9) | — |
| [[PANC-1 (line)]] | alt | 115 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +21.7) | — |
| [[NCI-H1573 (line)]] | alt | 605 | 6 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.83× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 115 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.61× (z +18.4) | — |
| [[C32 (line)]] | wt | 308 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.67× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.509× (z -9.0) |
| [[H4 (line)]] | wt | 104 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.03× (z +10.8) | — |
| [[LoVo (line)]] | wt | 139 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +23.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 156 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.44× (z +12.8) | — |
| [[A-427 (line)]] | wt | 94.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.39× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 125 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[RKO (line)]] | wt | 190 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.77× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW48 (line)]] | wt | 142 | 4 | 0 | [[PH-797804 (drug)]] 5 µM 7.67× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 227 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H1792 (line)]] | alt | 138 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.85× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 239 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SNU-1 (line)]] | wt | 115 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.99× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 188 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 203 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 102 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.97× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 152 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.71× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 149 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.84× (z +9.1) | — |
| [[KATO III (line)]] | alt | 185 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 109 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 130 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.17× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.20× (z +9.2) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1088 (line)]] | alt | 223 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.145× (z -9.0) |
| [[SW1417 (line)]] | alt | 230 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.30× (z +8.6) | — |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 183 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 176 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 183 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 126 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 131 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CB]] | +0.62 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[H3-3A]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[LTA4H]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[VAPA]] | +0.59 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SPOPL]] | +0.56 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[HBS1L]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CHASERR]] | +0.55 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ORC4]] | +0.55 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ATF2]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CDC73]] | +0.55 | +0.56 / +0.60 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[CAT]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL2B]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SDHAF2]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[AFG3L1P]] | -0.54 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[CRK]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SLC35C2]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[REXO1]] | -0.52 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[UBE2J2]] | -0.52 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[L3MBTL2]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SETX]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CDK11A]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SRP19]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[GLYR1]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-5.1, -8.0); signed map (-32.9, -15.8). **Vector** length 91.6, 25.5% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +5.8 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | +5.0 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | -1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | +1.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | capping actin protein of muscle Z-line subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.2 — chr7:116,811,070-116,922,049 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAPZ, CAPPA2 |
| Gene groups (HGNC) | Dynactin subunits |
| Reactome | 24 pathways, smallest: Advanced glycosylation endproduct receptor signaling; COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [P47755](https://www.uniprot.org/uniprotkb/P47755) (F-actin-capping protein subunit alpha-2):

> F-actin-capping proteins bind in a Ca(2+)-independent manner to the fast growing ends of actin filaments (barbed end) thereby blocking the exchange of subunits at these ends. Unlike other capping proteins (such as gelsolin and severin), these proteins do not sever actin filaments.

**Summary**, from NCBI Gene [830](https://www.ncbi.nlm.nih.gov/gene/830):

> The protein encoded by this gene is a member of the F-actin capping protein alpha subunit family. It is the alpha subunit of the barbed-end actin binding protein Cap Z. By capping the barbed end of actin filaments, Cap Z regulates the growth of the actin filaments at the barbed end. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1490) · Entrez [830](https://www.ncbi.nlm.nih.gov/gene/830) · UniProt [P47755](https://www.uniprot.org/uniprotkb/P47755) · Ensembl [ENSG00000198898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198898)

## Data

Gene col 12725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12725); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12725]; `tensor/DDL_lfc|DDL_z.npy` [12725]; `embed/gene_vectors.npy` [12725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12725 or target_col == 12725). Every well: [[CAPZA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPZA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
