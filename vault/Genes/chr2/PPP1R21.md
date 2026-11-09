---
symbol: "PPP1R21"
type: "gene"
col: 8591
ensembl_id: "ENSG00000162869"
name: "protein phosphatase 1 regulatory subunit 21"
location: "2p16.3"
module: 3
arm: "+"
pooled_cpm: 92.93
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PPP1R21

*protein phosphatase 1 regulatory subunit 21* — 2p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.37× (z +7.9, q 8e-13, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.499× (z -17.4, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MORC3]] (+0.59, fdr 1e-05), [[CCDC82]] (+0.59, fdr 2e-05), [[DUSP18]] (+0.59, fdr 1e-05); moves opposite to [[DHRS4L2]] (-0.59, fdr 4e-05), [[PPP2CA]] (-0.59, fdr 1e-05), [[PATZ1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02666]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +7.9 | 8e-13 | 33/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.9 | 8e-13 | 29/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +7.8 | 1e-12 | 30/48 (C32, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +7.8 | 1e-12 | 36/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +5.8 | 9e-07 | 26/49 (C32, BT-474, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +5.5 | 4e-06 | 25/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +5.3 | 9e-06 | 27/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +5.2 | 2e-05 | 23/48 (A498, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.0 | 4e-05 | 22/50 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +4.5 | 4e-04 | 19/47 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.18× | +4.4 | 6e-04 | 17/50 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +4.4 | 6e-04 | 20/48 (A-427, RKO, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.8 | 0.007 | 5/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.012 | 12/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.5 | 0.018 | 9/49 (SW480, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.050 | 9/49 (HT-29, A-172, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.050 | 10/50 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.050 | 9/48 (C32, A-172, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.13× | +3.0 | 0.069 | 12/49 (HOP62, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.499×** | -17.4 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -15.4 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -14.4 | 4e-45 | 46/49 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.665×** | -14.4 | 6e-45 | 34/48 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.353×** | -13.7 | 1e-40 | 44/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -12.6 | 3e-34 | 43/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.612×** | -11.4 | 5e-28 | 33/45 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -11.3 | 1e-27 | 40/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -10.7 | 5e-25 | 37/47 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.644×** | -10.6 | 2e-24 | 33/48 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.712×** | -8.5 | 9e-16 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.523×** | -8.5 | 1e-15 | 28/38 (AsPC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.729×** | -7.9 | 1e-13 | 28/48 (A549, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -7.5 | 4e-12 | 29/48 (SNU-423, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.750×** | -7.2 | 2e-11 | 27/49 (A-427, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -5.7 | 3e-07 | 26/48 (PANC-1, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.821×** | -4.6 | 1e-04 | 23/48 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.866× | -3.4 | 0.019 | 17/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.848× | -2.9 | 0.077 | 7/49 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 93.2 | 0 | 11 (6 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.147× (z -12.3) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.411× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -16.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.185× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -24.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.496× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 94.9 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -15.7) |
| [[PANC-1 (line)]] | alt | 111 | 2 | 7 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.445× (z -14.3) |
| [[SNU-423 (line)]] | alt | 95.0 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -18.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -10.3) |
| [[A549 (line)]] | wt | 152 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -23.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.181× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.225× (z -11.2) |
| [[HOP62 (line)]] | alt | 89.8 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.360× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.530× (z -11.3) |
| [[SW480 (line)]] | alt | 98.8 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 143 | 0 | 5 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0947× (z -14.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.199× (z -10.1) |
| [[C32 (line)]] | wt | 80.3 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.90× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.399× (z -8.8) |
| [[LS 180 (line)]] | wt | 106 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -13.4) |
| [[HCT15 (line)]] | alt | 125 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.372× (z -10.3) |
| [[KATO III (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 113 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[NCI-H23 (line)]] | alt | 221 | 1 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -24.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[A-172 (line)]] | wt | 87.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.239× (z -8.7) |
| [[A-427 (line)]] | wt | 138 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -29.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.219× (z -10.6) |
| [[A498 (line)]] | wt | 52.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +12.9) | — |
| [[H4 (line)]] | wt | 111 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.300× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 79.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -9.8) |
| [[HS-578T (line)]] | alt | 74.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.158× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 72.0 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0853× (z -11.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.0) |
| [[Hs 766T (line)]] | wt | 80.3 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -10.5) |
| [[HT-29 (line)]] | alt | 48.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 82.6 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.157× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 83.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.360× (z -10.0) |
| [[AN3 CA (line)]] | alt | 56.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.148× (z -9.3) |
| [[C-33 A (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[COLO 205 (line)]] | alt | 51.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[HEC-1-A (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[J82 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -10.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 84.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.476× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.9) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW 1271 (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -8.7) |
| [[SW1417 (line)]] | alt | 79.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -9.7) |
| [[BT-474 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORC3]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CCDC82]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[DUSP18]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[WDR44]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[KATNBL1]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[WIPF2]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CSTB]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ABHD18]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.56 | +0.42 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS4L2]] | -0.59 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PPP2CA]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PATZ1]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ILF3]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ERH]] | -0.57 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[EWSR1]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[FUBP1]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[CAPRIN1]] | -0.50 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[RMDN2]] | -0.50 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[MTMR2]] | -0.50 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[COPS3]] | -0.49 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02666]] | C | LINC02666's natural level weakens PPP1R21's drug response | LINC02666's natural level across 35 lines (lineage-adjusted; a glimpse) | r -0.77, reverse -0.34; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.0, -0.9); signed map (-15.6, 17.8). **Vector** length 110, 34.6% of its response variance represented; |z| ≥ 3 in 1,340 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.7 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.2 | +5.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.1 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.8 | -11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | -7.5 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -7.1 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -6.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.7 | -14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -13.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.9 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.3 — chr2:48,440,598-48,515,391 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16566, Fy-2, FERRY2; previously CCDC128, KLRAQ1 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; FERRY complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMI0](https://www.uniprot.org/uniprotkb/Q6ZMI0) (Protein phosphatase 1 regulatory subunit 21):

> Component of the FERRY complex (Five-subunit Endosomal Rab5 and RNA/ribosome intermediary). The FERRY complex directly interacts with mRNAs and RAB5A, and functions as a RAB5A effector involved in the localization and the distribution of specific mRNAs most likely by mediating their endosomal transport. The complex recruits mRNAs and ribosomes to early endosomes through direct mRNA-interaction. In the complex, PPP1R21 serves as a binding hub connecting all five complex subunits and mediating …

**Summary**, from NCBI Gene [129285](https://www.ncbi.nlm.nih.gov/gene/129285):

> Enables mRNA binding activity and protein-macromolecule adaptor activity. Involved in regulation of intracellular mRNA localization. Located in early endosome. Is active in early endosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30595) · Entrez [129285](https://www.ncbi.nlm.nih.gov/gene/129285) · UniProt [Q6ZMI0](https://www.uniprot.org/uniprotkb/Q6ZMI0) · Ensembl [ENSG00000162869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162869)

## Data

Gene col 8591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8591); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8591]; `tensor/DDL_lfc|DDL_z.npy` [8591]; `embed/gene_vectors.npy` [8591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8591 or target_col == 8591). Every well: [[PPP1R21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
