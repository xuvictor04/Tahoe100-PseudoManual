---
symbol: "ARID1A"
type: "gene"
col: 3945
ensembl_id: "ENSG00000117713"
name: "AT-rich interaction domain 1A"
location: "1p36.11"
module: 46
arm: "+"
pooled_cpm: 138.37
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ARID1A

*AT-rich interaction domain 1A* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.10× (z +15.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.312× (z -24.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD1B]] (+0.68, fdr 1e-05), [[ARHGEF17]] (+0.66, fdr 3e-05), [[CREBBP]] (+0.66, fdr 7e-05); moves opposite to [[CDA]] (-0.59, fdr 4e-05), [[CSGALNACT2]] (-0.58, fdr 3e-05), [[PIGH]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BACE2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Digitoxin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +15.9 | 0e+00 | 44/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +11.3 | 5e-27 | 44/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +10.7 | 2e-24 | 41/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +9.9 | 6e-21 | 39/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +9.8 | 1e-20 | 37/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +9.0 | 2e-17 | 39/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +8.4 | 4e-15 | 36/48 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.1 | 7e-11 | 28/49 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.15× | +4.3 | 1e-03 | 21/48 (RKO, A549, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.006 | 23/48 (C32, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.027 | 15/47 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.069 | 20/47 (LoVo, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.312×** | -24.9 | 0e+00 | 48/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.318×** | -24.5 | 0e+00 | 47/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.429×** | -18.1 | 0e+00 | 47/49 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.439×** | -16.9 | 0e+00 | 41/44 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.465×** | -16.4 | 0e+00 | 46/48 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.736×** | -9.3 | 2e-18 | 40/48 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -8.8 | 1e-16 | 34/45 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.686×** | -8.0 | 6e-14 | 35/48 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.701×** | -7.6 | 2e-12 | 38/49 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.775×** | -5.5 | 3e-06 | 37/48 (H4, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.838× | -5.4 | 4e-06 | 25/48 (A-172, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.819×** | -4.3 | 9e-04 | 25/48 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.827×** | -4.1 | 0.002 | 24/48 (RPMI-7951, C-33 A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.822×** | -4.0 | 0.003 | 21/48 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.834× | -3.7 | 0.007 | 23/47 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.870× | -3.0 | 0.090 | 21/48 (BT-474, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 151 | 6 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.231× (z -23.7) |
| [[HS-578T (line)]] | alt | 110 | 7 (2 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.42× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 177 | 4 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.89× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -24.0) |
| [[NCI-H2347 (line)]] | alt | 120 | 3 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -16.5) |
| [[A-427 (line)]] | wt | 212 | 2 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.48× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.202× (z -22.6) |
| [[AsPC-1 (line)]] | alt | 71.0 | 5 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +19.8) | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -15.8) |
| [[HOP62 (line)]] | alt | 138 | 4 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.317× (z -14.4) |
| [[HT-29 (line)]] | alt | 139 | 3 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.27× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 116 | 5 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.74× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.289× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 124 | 4 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.29× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.259× (z -18.6) |
| [[RKO (line)]] | wt | 141 | 5 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +17.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.397× (z -10.9) |
| [[BT-474 (line)]] | alt | 157 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -22.7) |
| [[NCI-H23 (line)]] | alt | 238 | 2 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.158× (z -26.2) |
| [[PANC-1 (line)]] | alt | 218 | 3 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.82× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.264× (z -20.6) |
| [[A498 (line)]] | wt | 111 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.26× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 184 | 2 | 5 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.63× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.288× (z -19.8) |
| [[LOX-IMVI (line)]] | wt | 233 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.18× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -17.4) |
| [[LS 180 (line)]] | wt | 122 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.273× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 145 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.220× (z -20.2) |
| [[A549 (line)]] | wt | 77.6 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.22× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.453× (z -9.2) |
| [[AN3 CA (line)]] | alt | 328 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.250× (z -11.7) |
| [[KATO III (line)]] | alt | 81.2 | 3 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.315× (z -14.4) |
| [[LoVo (line)]] | wt | 102 | 4 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 158 | 2 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.79× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.191× (z -22.8) |
| [[COLO 205 (line)]] | alt | 113 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.256× (z -13.7) |
| [[H4 (line)]] | wt | 131 | 3 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.376× (z -8.9) |
| [[J82 (line)]] | alt | 184 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -17.9) |
| [[Panc 03.27 (line)]] | alt | 114 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.380× (z -12.9) |
| [[SHP-77 (line)]] | alt | 157 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -16.7) |
| [[SNU-1 (line)]] | wt | 235 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.17× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -12.9) |
| [[SW1417 (line)]] | alt | 120 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.303× (z -15.5) |
| [[SW48 (line)]] | wt | 124 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.229× (z -12.3) |
| [[A-172 (line)]] | wt | 95.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.444× (z -10.1) |
| [[C-33 A (line)]] | alt | 118 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -13.6) |
| [[C32 (line)]] | wt | 103 | 2 | 2 | [[PH-797804 (drug)]] 5 µM 4.74× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -9.3) |
| [[Hs 766T (line)]] | wt | 115 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 1 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.50× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.304× (z -12.6) |
| [[SNU-423 (line)]] | alt | 89.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -10.4) |
| [[SW 900 (line)]] | alt | 135 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.259× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 74.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 105 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.320× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 104 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.73× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 270 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0744× (z -18.7) |
| [[CHP-212 (line)]] | wt | 97.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Larotrectinib (drug)]] 0.5 µM 0.235× (z -9.0) |
| [[HCT15 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 108 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.87× (z +10.4) | — |
| [[SW 1088 (line)]] | alt | 91.6 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0819× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD1B]] | +0.68 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[ARHGEF17]] | +0.66 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CREBBP]] | +0.66 | +0.38 / +0.61 | both halves | 7e-05 | pathway: ATP-dependent chromatin remodelers; STRING 849 |
| [[ZFX]] | +0.65 | +0.33 / +0.68 | both halves | 1e-04 |  |
| [[ARID1B]] | +0.65 | +0.49 / +0.56 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[ARID2]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 998 |
| [[ATXN7]] | +0.64 | +0.34 / +0.64 | both halves | 1e-04 | pathway: Chromatin modifying enzymes |
| [[RAF1]] | +0.63 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[ZNF827]] | +0.62 | +0.45 / +0.50 | both halves | 3e-05 | pathway: ATP-dependent chromatin remodelers |
| [[ATAD2B]] | +0.62 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TCF12]] | +0.60 | +0.49 / +0.47 | both halves | 2e-05 | pathway: ATP-dependent chromatin remodelers |
| [[TNPO2]] | +0.60 | +0.57 / +0.39 | both halves | 6e-05 | same gene group |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDA]] | -0.59 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CSGALNACT2]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[PIGH]] | -0.56 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[GNAI3]] | -0.56 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[NBPF3]] | -0.55 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[BTBD9]] | -0.54 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[STX7]] | -0.54 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[SGSM1]] | -0.54 | -0.21 / -0.51 | both halves | 6e-04 |  |
| [[STAM2]] | -0.54 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[FCHO1]] | -0.53 | -0.17 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[HDAC11]] | -0.53 | -0.30 / -0.37 | both halves | 2e-04 | STRING 431 |
| [[GIPR]] | -0.53 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[MOCS2]] | -0.52 | -0.32 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BACE2]] | B | BACE2 activity lowers ARID1A's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.42× higher at baseline in the lines without BACE2 | 0.077 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Digitoxin (drug)]] 5 µM | C | the direction of ARID1A's effect on the cells' numbers under Digitoxin 5 µM is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of ARID1A in 15 lines vs 33 not recorded | the ARID1A-altered lines: 0.76× the cells of the other lines | 1.000 over the table, 0.055 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.3, 13.2); signed map (26.6, -23.7). **Vector** length 125, 41.4% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.7 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.7 | +15.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +9.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.1 | +1.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +4.0 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -24.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.4 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -24.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.3 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,693,236-26,782,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B120, P270, C10rf4, BAF250, BAF250a; previously C1orf4, SMARCF1 |
| Gene groups (HGNC) | AT-rich interaction domain containing; Armadillo like helical domain containing; BAF complex subunits |
| Reactome | 29 pathways, smallest: Positive Regulation of CDH1 Gene Transcription; Formation of the canonical BAF (cBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O14497](https://www.uniprot.org/uniprotkb/O14497) (AT-rich interactive domain-containing protein 1A):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Binds DNA non-specifically. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF complex) and the neuron-specific chromatin remodeling …

**Summary**, from NCBI Gene [8289](https://www.ncbi.nlm.nih.gov/gene/8289):

> This gene encodes a member of the SWI/SNF family, whose members have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, which is required for transcriptional activation of genes normally repressed by chromatin. It possesses at least two conserved domains that could be important for its function. First, it has …

**Accessions** — [HGNC:11110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11110) · Entrez [8289](https://www.ncbi.nlm.nih.gov/gene/8289) · UniProt [O14497](https://www.uniprot.org/uniprotkb/O14497) · Ensembl [ENSG00000117713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117713)

## Data

Gene col 3945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3945); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3945]; `tensor/DDL_lfc|DDL_z.npy` [3945]; `embed/gene_vectors.npy` [3945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3945 or target_col == 3945). Every well: [[ARID1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
