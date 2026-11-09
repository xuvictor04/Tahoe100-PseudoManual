---
symbol: "PPP3R1"
type: "gene"
col: 13306
ensembl_id: "ENSG00000221823"
name: "protein phosphatase 3 regulatory subunit B, alpha"
location: "2p14"
module: 3
arm: "+"
pooled_cpm: 185.04
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PPP3R1

*protein phosphatase 3 regulatory subunit B, alpha* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.43× (z +13.2, q 5e-37, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.484× (z -14.4, q 5e-44, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.760× (z -5.6, q 2e-06, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGAP3]] (+0.61, fdr 1e-05), [[RANBP9]] (+0.61, fdr 1e-05), [[L3MBTL3]] (+0.58, fdr 1e-05); moves opposite to [[HUS1]] (-0.56, fdr 4e-05), [[TAF9]] (-0.51, fdr 1e-05), [[CCDC113]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.43×** | +13.2 | 5e-37 | 47/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +11.9 | 3e-30 | 45/49 (PANC-1, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.0 | 2e-13 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +7.8 | 8e-13 | 32/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +7.7 | 1e-12 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 2e-06 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 9e-05 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.18× | +4.6 | 2e-04 | 20/48 (NCI-H460, MIA PaCa-2, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.5 | 4e-04 | 28/48 (RKO, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.4 | 6e-04 | 23/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.4 | 6e-04 | 17/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.4 | 6e-04 | 29/48 (LS 180, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.005 | 23/48 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.2 | 0.061 | 19/38 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.061 | 17/48 (LoVo, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -14.4 | 5e-44 | 44/44 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.546×** | -12.4 | 5e-33 | 45/49 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -10.2 | 3e-22 | 40/45 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.760×** | -5.6 | 2e-06 | 32/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -5.4 | 1e-05 | 26/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.774×** | -5.3 | 1e-05 | 30/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -4.8 | 1e-04 | 30/48 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.810×** | -4.2 | 0.002 | 25/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.876× | -3.9 | 0.007 | 14/48 (MIA PaCa-2, A-427, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.6 | 0.015 | 21/48 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.883× | -3.6 | 0.015 | 7/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.6 | 0.015 | 24/48 (A-172, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.844× | -3.5 | 0.020 | 18/47 (NCI-H23, HOP62, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -3.5 | 0.022 | 21/48 (Hs 766T, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.849× | -3.4 | 0.028 | 19/48 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.860× | -3.3 | 0.038 | 18/49 (NCI-H23, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.895× | -3.2 | 0.039 | 8/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.039 | 17/48 (NCI-H23, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.865× | -3.2 | 0.047 | 14/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.747×** | -3.1 | 0.047 | 20/47 (SW 900, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.862× | -3.1 | 0.054 | 12/48 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.866× | -3.0 | 0.071 | 11/49 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.760×** | -3.0 | 0.072 | 21/48 (COLO 205, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 171 | 14 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +21.2) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +16.5) | — |
| [[SW480 (line)]] | alt | 235 | 8 (3 ⚠) | 5 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.55× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.529× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 221 | 3 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.74× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.468× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 3 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.8) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.04× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -18.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 154 | 7 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +14.0) | — |
| [[A549 (line)]] | wt | 219 | 4 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.5) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.40× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.484× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 136 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.91× (z +15.1) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 4.74× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 251 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.04× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -16.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 268 | 2 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.04× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.526× (z -9.1) |
| [[HT-29 (line)]] | alt | 223 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.79× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.497× (z -9.2) |
| [[LS 180 (line)]] | wt | 208 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 133 | 1 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.09× (z +9.2) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -12.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A-427 (line)]] | wt | 265 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.99× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 146 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.96× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 147 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.57× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.55× (z +9.7) | — |
| [[KATO III (line)]] | alt | 190 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.09× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 206 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.66× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 202 | 3 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.18× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 130 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -14.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 213 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.30× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -15.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 183 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.5) ⚠ cell-cycle shift, explains ~13% of this change | [[Dinaciclib (drug)]] 5 µM 0.490× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 176 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.38× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 191 | 2 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.92× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -12.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 186 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.60× (z +14.5) | — |
| [[COLO 205 (line)]] | alt | 179 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.24× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 204 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 144 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.15× (z +9.6) ⚠ toxic | [[Docetaxel (drug)]] 0.05 µM 0.500× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 180 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.63× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 253 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 150 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.41× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -21.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 170 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.2) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[BT-474 (line)]] | alt | 125 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.26× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 221 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.318× (z -8.5) |
| [[HCT15 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -13.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 183 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.69× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 199 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.35× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -17.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 144 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.83× (z +9.5) | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0780× (z -10.9) |
| [[AN3 CA (line)]] | alt | 150 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP3]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[RANBP9]] | +0.61 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[L3MBTL3]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.58 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PDE4A]] | +0.57 | +0.40 / +0.60 | both halves | 5e-05 | pathway: DARPP-32 events |
| [[MFSD14CP]] | +0.57 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[CNOT6L]] | +0.57 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[TMEM38A]] | +0.56 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ANKRD13D]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SIAH2]] | +0.55 | +0.64 / +0.39 | both halves | 6e-05 |  |
| [[TSHZ1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CSNK1G2]] | +0.54 | +0.58 / +0.43 | both halves | 3e-05 | pathway: Signaling by WNT |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUS1]] | -0.56 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[TAF9]] | -0.51 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CCDC113]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MANBAL]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ZNF624]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[FLII]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RPAP2]] | -0.49 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[DHRS12]] | -0.48 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[ZNF468]] | -0.47 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[SBDS]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SRRD]] | -0.47 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ZNF776]] | -0.46 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.324). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.0, -4.9); signed map (-19.3, 17.7). **Vector** length 103, 34.8% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | +6.4 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +13.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +1.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.9 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | +5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 3 regulatory subunit B, alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:68,178,857-68,256,237 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CALNB1, CNB, CNB1 |
| Gene groups (HGNC) | Protein phosphatase 3 regulatory subunits; EF-hand domain containing; Calcineurin subunits |
| Hallmark sets | APOPTOSIS |
| Reactome | 23 pathways, smallest: Calcineurin activates NFAT; CLEC7A (Dectin-1) induces NFAT activation; Activation of BAD and translocation to mitochondria |
| Matched by | ensembl_id |

**Function**, from UniProt [P63098](https://www.uniprot.org/uniprotkb/P63098) (Calcineurin subunit B type 1):

> Regulatory subunit of calcineurin, a calcium-dependent, calmodulin stimulated protein phosphatase. Confers calcium sensitivity.

**Summary**, from NCBI Gene [5534](https://www.ncbi.nlm.nih.gov/gene/5534):

> Enables phosphatase binding activity and protein domain specific binding activity. Involved in calcineurin-NFAT signaling cascade and positive regulation of transcription by RNA polymerase II. Located in plasma membrane. Part of calcineurin complex. Implicated in Alzheimer's disease and dilated cardiomyopathy. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9317) · Entrez [5534](https://www.ncbi.nlm.nih.gov/gene/5534) · UniProt [P63098](https://www.uniprot.org/uniprotkb/P63098) · Ensembl [ENSG00000221823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221823)

## Data

Gene col 13306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13306); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13306]; `tensor/DDL_lfc|DDL_z.npy` [13306]; `embed/gene_vectors.npy` [13306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13306 or target_col == 13306). Every well: [[PPP3R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP3R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
