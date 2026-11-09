---
symbol: "TLK1"
type: "gene"
col: 12622
ensembl_id: "ENSG00000198586"
name: "tousled like kinase 1"
location: "2q31.1"
module: 51
arm: "+"
pooled_cpm: 242.29
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TLK1

*tousled like kinase 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.71× (z +17.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.237× (z -45.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD2]] (+0.76, fdr 1e-05), [[SCAF8]] (+0.67, fdr 1e-05), [[TLK2]] (+0.67, fdr 7e-06); moves opposite to [[AMPD2]] (-0.64, fdr 3e-05), [[FAM131A]] (-0.57, fdr 1e-04), [[PDCD6]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARID2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +17.2 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +14.8 | 0e+00 | 45/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +12.5 | 8e-34 | 32/48 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +11.6 | 7e-29 | 36/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +11.2 | 4e-27 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +10.7 | 1e-24 | 42/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +9.6 | 9e-20 | 36/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +8.2 | 2e-14 | 29/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +5.8 | 4e-07 | 0/50 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +5.4 | 4e-06 | 23/47 (J82, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.3 | 7e-06 | 23/48 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.16× | +4.6 | 2e-04 | 19/48 (H4, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.16× | +4.4 | 6e-04 | 16/48 (hTERT-HPNE, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.8 | 0.006 | 21/45 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.10× | +3.1 | 0.078 | 9/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.237×** | -45.9 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.274×** | -41.3 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.323×** | -36.1 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -20.0 | 0e+00 | 43/44 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.549×** | -19.2 | 0e+00 | 43/49 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.558×** | -18.7 | 0e+00 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -15.5 | 0e+00 | 40/49 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.655×** | -13.5 | 1e-39 | 48/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -11.5 | 9e-29 | 34/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.708×** | -10.6 | 2e-24 | 43/47 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.700×** | -10.5 | 4e-24 | 31/45 (NCI-H2030, A549, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -9.6 | 4e-20 | 31/48 (SW480, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.593×** | -8.0 | 4e-14 | 43/49 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.793×** | -7.1 | 5e-11 | 28/50 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~2% of this change | 0.843× | -5.4 | 2e-06 | 23/48 (SW 1271, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.906× | -4.5 | 2e-04 | 12/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.753×** | -4.4 | 4e-04 | 31/48 (NCI-H2347, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.888× | -3.8 | 0.004 | 11/49 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.898× | -3.5 | 0.013 | 3/48 (NCI-H661, C32, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.891× | -3.4 | 0.014 | 5/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.876× | -3.0 | 0.052 | 14/47 (AsPC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 260 | 7 (1 ⚠) | 9 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +23.1) | [[Panobinostat (drug)]] 5 µM 0.181× (z -45.7) |
| [[NCI-H1573 (line)]] | alt | 383 | 7 (2 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +19.8) | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -32.1) |
| [[NCI-H23 (line)]] | alt | 393 | 5 (1 ⚠) | 10 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -37.3) |
| [[NCI-H460 (line)]] | wt | 231 | 9 (3 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -28.4) |
| [[LOX-IMVI (line)]] | wt | 249 | 5 (1 ⚠) | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -25.7) |
| [[PANC-1 (line)]] | alt | 278 | 6 (1 ⚠) | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +26.1) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -31.8) |
| [[AsPC-1 (line)]] | alt | 321 | 3 (1 ⚠) | 9 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.131× (z -40.9) |
| [[HEC-1-A (line)]] | alt | 283 | 2 | 10 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 2.68× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -33.0) |
| [[A549 (line)]] | wt | 229 | 1 | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.185× (z -32.3) |
| [[HOP62 (line)]] | alt | 180 | 6 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -26.6) |
| [[HT-29 (line)]] | alt | 264 | 3 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -32.6) |
| [[NCI-H2030 (line)]] | alt | 416 | 1 | 10 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 3.13× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.236× (z -22.6) |
| [[NCI-H2347 (line)]] | alt | 202 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -30.5) |
| [[Panc 03.27 (line)]] | alt | 202 | 1 | 10 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.91× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.179× (z -32.2) |
| [[A498 (line)]] | wt | 263 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -33.4) |
| [[HepG2_C3A (line)]] | wt | 347 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -21.8) |
| [[LS 180 (line)]] | wt | 223 | 4 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -28.1) |
| [[RKO (line)]] | wt | 272 | 4 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +18.7) | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -25.4) |
| [[SW1417 (line)]] | alt | 299 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -31.6) |
| [[BT-474 (line)]] | alt | 162 | 2 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -31.4) |
| [[C32 (line)]] | wt | 175 | 3 | 6 | [[TAK-901 (drug)]] 5 µM 7.81× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.298× (z -19.4) |
| [[CFPAC-1 (line)]] | alt | 201 | 2 (1 ⚠) | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.02× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -18.0) |
| [[H4 (line)]] | wt | 188 | 6 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -14.4) |
| [[J82 (line)]] | alt | 235 | 1 | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -22.8) |
| [[KATO III (line)]] | alt | 170 | 4 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.160× (z -31.3) |
| [[SK-MEL-2 (line)]] | alt | 217 | 2 | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.50× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -20.2) |
| [[A-427 (line)]] | wt | 231 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.282× (z -22.7) |
| [[C-33 A (line)]] | alt | 282 | 2 | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.232× (z -22.7) |
| [[MIA PaCa-2 (line)]] | alt | 266 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -27.3) |
| [[NCI-H1792 (line)]] | alt | 215 | 2 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.69× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -23.9) |
| [[COLO 205 (line)]] | alt | 165 | 4 | 3 | [[TAK-901 (drug)]] 5 µM 7.60× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.185× (z -23.5) |
| [[SW 900 (line)]] | alt | 232 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -23.1) |
| [[SW48 (line)]] | wt | 217 | 3 | 4 | [[PH-797804 (drug)]] 5 µM 5.85× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -22.0) |
| [[A-172 (line)]] | wt | 204 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -20.1) |
| [[hTERT-HPNE (line)]] | wt | 138 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -14.0) |
| [[HCT15 (line)]] | alt | 290 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -19.6) |
| [[Hs 766T (line)]] | wt | 174 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -21.7) |
| [[HS-578T (line)]] | alt | 171 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -21.7) |
| [[RPMI-7951 (line)]] | alt | 235 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -17.3) |
| [[SNU-1 (line)]] | wt | 305 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.287× (z -18.6) |
| [[SNU-423 (line)]] | alt | 200 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -24.9) |
| [[AN3 CA (line)]] | alt | 242 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -10.1) |
| [[LoVo (line)]] | wt | 181 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -26.6) |
| [[NCI-H661 (line)]] | alt | 351 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -12.9) |
| [[SHP-77 (line)]] | alt | 136 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -13.7) |
| [[SW 1271 (line)]] | alt | 267 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.0) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -10.5) |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 1 | — | [[Everolimus (drug)]] 5 µM 0.0816× (z -9.0) |
| [[SW 1088 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD2]] | +0.76 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[SCAF8]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TLK2]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 | STRING 995 |
| [[USP24]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[SENP6]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.65 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[ZFX]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SRSF4]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.61 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[RNF115]] | +0.61 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[CUL5]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NCOR1]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMPD2]] | -0.64 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[FAM131A]] | -0.57 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[PDCD6]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SLCO4A1]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[FRMD8]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[QSOX1]] | -0.55 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[RER1]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.55 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[CSNK1E]] | -0.54 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[TPD52L2]] | -0.54 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[PPARD]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.54 | -0.29 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARID2]] | C | ARID2's natural level strengthens TLK1's drug response | ARID2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.00; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.3, 4.4); signed map (11.6, -34.2). **Vector** length 88.7, 29.1% of its response variance represented; |z| ≥ 3 in 1,579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +12.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.1 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.0 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -11.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -18.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -36.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | +0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | tousled like kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:170,990,823-171,231,314 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0137, PKU-BETA |
| Gene groups (HGNC) | Tousled like kinase family |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKI8](https://www.uniprot.org/uniprotkb/Q9UKI8) (Serine/threonine-protein kinase tousled-like 1):

> Rapidly and transiently inhibited by phosphorylation following the generation of DNA double-stranded breaks during S-phase. This is cell cycle checkpoint and ATM-pathway dependent and appears to regulate processes involved in chromatin assembly. Isoform 3 phosphorylates and enhances the stability of the t-SNARE SNAP23, augmenting its assembly with syntaxin. Isoform 3 protects the cells from the ionizing radiation by facilitating the repair of DSBs. In vitro, phosphorylates histone H3 at …

**Summary**, from NCBI Gene [9874](https://www.ncbi.nlm.nih.gov/gene/9874):

> The protein encoded by this gene is a serine/threonine kinase that may be involved in the regulation of chromatin assembly. The encoded protein is only active when it is phosphorylated, and this phosphorylation is cell cycle-dependent, with the maximal activity of this protein coming during S phase. The catalytic activity of this protein is diminished by DNA damage and by blockage of DNA replication. Three transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:11841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11841) · Entrez [9874](https://www.ncbi.nlm.nih.gov/gene/9874) · UniProt [Q9UKI8](https://www.uniprot.org/uniprotkb/Q9UKI8) · Ensembl [ENSG00000198586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198586)

## Data

Gene col 12622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12622); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12622]; `tensor/DDL_lfc|DDL_z.npy` [12622]; `embed/gene_vectors.npy` [12622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12622 or target_col == 12622). Every well: [[TLK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
