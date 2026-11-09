---
symbol: "ABCF1"
type: "gene"
col: 12892
ensembl_id: "ENSG00000204574"
name: "ATP binding cassette subfamily F member 1"
location: "6p21.33"
module: 11
arm: "+"
pooled_cpm: 120.76
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ABCF1

*ATP binding cassette subfamily F member 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +26.2, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 8.34× (z +16.9, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.714× (z -5.0, q 4e-04, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.370×, HOP62 0.459×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.541×, NCI-H23 0.599×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.416×; ⚠ cell-cycle shift, explains ~0% of this change); [[Proglumide (drug)]] 0.05 µM in 1 line (SW 1088 0.0860×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF6]] (+0.72, fdr 7e-06), [[MRFAP1L1]] (+0.69, fdr 7e-06), [[PRPF38B]] (+0.69, fdr 7e-06); moves opposite to [[KIAA1191]] (-0.58, fdr 5e-05), [[GLUD1]] (-0.57, fdr 1e-05), [[NAP1L4]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.36×** | +26.2 | 0e+00 | 48/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.34×** | +16.9 | 0e+00 | 49/49 (LoVo, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.09×** | +16.6 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.75×** | +15.5 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.00×** | +11.1 | 2e-26 | 44/48 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +11.0 | 2e-26 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.95×** | +10.2 | 1e-22 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.89×** | +9.7 | 1e-20 | 45/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.49×** | +6.1 | 8e-08 | 40/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.9 | 2e-07 | 41/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.43×** | +5.4 | 3e-06 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | **1.36×** | +4.7 | 1e-04 | 35/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 3e-04 | 35/47 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.34×** | +4.3 | 8e-04 | 35/47 (NCI-H460, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.002 | 30/48 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 29/48 (AN3 CA, SNU-423, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.057 | 22/49 (SNU-423, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.082 | 23/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.370×, HOP62 0.459×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.541×, NCI-H23 0.599×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.416×; ⚠ cell-cycle shift, explains ~0% of this change); [[Proglumide (drug)]] 0.05 µM in 1 line (SW 1088 0.0860×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -5.0 | 4e-04 | 32/48 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.801× | -3.3 | 0.30 | 24/47 (AN3 CA, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 82.5 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +22.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +17.1) | — |
| [[HOP62 (line)]] | alt | 110 | 9 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +23.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.0× (z +14.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.6) |
| [[PANC-1 (line)]] | alt | 194 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +24.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +16.5) | — |
| [[LoVo (line)]] | wt | 85.6 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +22.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.0× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 117 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +18.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.2× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 70.9 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.05× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 78.0 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +23.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +15.2) | — |
| [[NCI-H23 (line)]] | alt | 208 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.19× (z +11.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 111 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +23.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +16.4) | — |
| [[SNU-423 (line)]] | alt | 134 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +29.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +13.0) | — |
| [[A-172 (line)]] | wt | 83.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +22.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.25× (z +15.6) | — |
| [[A-427 (line)]] | wt | 154 | 5 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.09× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[A549 (line)]] | wt | 93.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +22.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.38× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 97.1 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +19.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.51× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 144 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.99× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 85.0 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +20.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.4× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 141 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +21.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +15.2) | — |
| [[KATO III (line)]] | alt | 126 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +15.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.01× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.3× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 198 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.37× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 103 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +20.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.84× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 99.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +24.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +13.8) | — |
| [[H4 (line)]] | wt | 116 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +19.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.20× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 120 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.39× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 90.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +20.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +13.6) | — |
| [[RKO (line)]] | wt | 122 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.5× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 128 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +18.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.34× (z +12.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.5) |
| [[SW480 (line)]] | alt | 101 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.45× (z +13.0) | — |
| [[A498 (line)]] | wt | 110 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +19.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 55.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +18.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.39× (z +12.5) | — |
| [[J82 (line)]] | alt | 256 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +21.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.89× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 133 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +16.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.18× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 144 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +18.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 137 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.7× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 82.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +17.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.64× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 83.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +17.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 17.7× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 108 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.40× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 127 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 156 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.77× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 117 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW 1088 (line)]] | alt | 98.3 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0860× (z -9.4) |
| [[SW 1271 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 201 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF6]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PRPF38B]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[CWC22]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MAGEF1]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[REXO4]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LLPH]] | +0.63 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ZC3H18]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MSL3P1]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1191]] | -0.58 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[GLUD1]] | -0.57 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[CLDND1]] | -0.56 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SELENOF]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[METTL9]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TMED4]] | -0.52 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SMG1P5]] | -0.52 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[HINT1]] | -0.52 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[TPGS2]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[GHITM]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.0, 0.3); signed map (-0.8, -20.6). **Vector** length 94.8, 34.3% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +15.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.1 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +11.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +2.5 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily F member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,571,393-30,597,179 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EST123147; previously ABC50 |
| Gene groups (HGNC) | ATP binding cassette subfamily F; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NE71](https://www.uniprot.org/uniprotkb/Q8NE71) (ATP-binding cassette sub-family F member 1):

> Isoform 2 is required for efficient Cap- and IRES-mediated mRNA translation initiation. Isoform 2 is not involved in the ribosome biogenesis.

**Summary**, from NCBI Gene [23](https://www.ncbi.nlm.nih.gov/gene/23):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the GCN20 subfamily. Unlike other members of the superfamily, this protein lacks the transmembrane domains which are characteristic of most ABC transporters. This protein may be …

**Accessions** — [HGNC:70](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:70) · Entrez [23](https://www.ncbi.nlm.nih.gov/gene/23) · UniProt [Q8NE71](https://www.uniprot.org/uniprotkb/Q8NE71) · Ensembl [ENSG00000204574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204574)

## Data

Gene col 12892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12892); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12892]; `tensor/DDL_lfc|DDL_z.npy` [12892]; `embed/gene_vectors.npy` [12892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12892 or target_col == 12892). Every well: [[ABCF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
