---
symbol: "NCOA2"
type: "gene"
col: 6402
ensembl_id: "ENSG00000140396"
name: "nuclear receptor coactivator 2"
location: "8q13.3"
module: 46
arm: "+"
pooled_cpm: 177.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 42
n_dd_up_clean: 8
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# NCOA2

*nuclear receptor coactivator 2* — 8q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +12.0, q 2e-30, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.212× (z -26.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDFY3]] (+0.76, fdr 7e-06), [[ARID1B]] (+0.73, fdr 7e-06), [[TLK2]] (+0.68, fdr 1e-05); moves opposite to [[CMIP]] (-0.58, fdr 3e-05), [[FCHO1]] (-0.58, fdr 1e-04), [[TMEM241]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +12.0 | 2e-30 | 42/49 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.3 | 8e-11 | 39/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.5 | 0.001 | 35/48 (C32, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.002 | 31/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.002 | 31/50 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.30×** | +4.0 | 0.007 | 30/50 (AsPC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.012 | 30/47 (C32, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.012 | 22/48 (AsPC-1, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.025 | 19/48 (C32, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.066 | 20/48 (AsPC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.066 | 25/50 (AsPC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.094 | 22/48 (C32, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.212×** | -26.4 | 0e+00 | 48/48 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.217×** | -25.9 | 0e+00 | 48/48 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.225×** | -25.3 | 0e+00 | 48/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.408×** | -15.2 | 0e+00 | 48/48 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.419×** | -13.4 | 8e-39 | 41/45 (C32, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.479×** | -12.0 | 3e-31 | 40/44 (SNU-1, SHP-77, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.496×** | -11.9 | 9e-31 | 46/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.501×** | -11.0 | 3e-26 | 43/49 (A-172, C32, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.633×** | -11.0 | 4e-26 | 46/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.613×** | -8.3 | 6e-15 | 39/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.711×** | -8.2 | 1e-14 | 33/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.625×** | -8.0 | 6e-14 | 36/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.637×** | -7.7 | 8e-13 | 42/49 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.651×** | -7.3 | 1e-11 | 34/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -7.0 | 1e-10 | 38/48 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.777×** | -6.0 | 5e-08 | 35/49 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.512×** | -5.3 | 3e-06 | 41/49 (LOX-IMVI, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -5.2 | 5e-06 | 33/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.742×** | -5.1 | 9e-06 | 36/48 (SW 1271, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.759×** | -4.4 | 2e-04 | 32/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.580×** | -4.3 | 3e-04 | 41/48 (NCI-H2347, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 314 | 1 | 21 (12 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -25.6) |
| [[NCI-H460 (line)]] | wt | 106 | 1 | 16 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +12.2) | [[Belinostat (drug)]] 5 µM 0.181× (z -23.0) |
| [[LOX-IMVI (line)]] | wt | 204 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -24.2) |
| [[HS-578T (line)]] | alt | 195 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -26.3) |
| [[CFPAC-1 (line)]] | alt | 153 | 1 | 12 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.175× (z -20.4) |
| [[Panc 03.27 (line)]] | alt | 167 | 2 | 11 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -27.9) |
| [[NCI-H2030 (line)]] | alt | 255 | 0 | 12 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.227× (z -16.9) |
| [[NCI-H2347 (line)]] | alt | 240 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -27.6) |
| [[SNU-423 (line)]] | alt | 131 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -24.3) |
| [[A-172 (line)]] | wt | 108 | 1 | 10 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -16.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.265× (z -16.2) |
| [[C32 (line)]] | wt | 236 | 3 | 8 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -15.0) |
| [[HT-29 (line)]] | alt | 242 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -21.0) |
| [[LoVo (line)]] | wt | 153 | 1 | 10 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +16.5) | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -25.7) |
| [[NCI-H1792 (line)]] | alt | 164 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -22.8) |
| [[A498 (line)]] | wt | 253 | 1 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -19.3) |
| [[AsPC-1 (line)]] | alt | 252 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -25.1) |
| [[COLO 205 (line)]] | alt | 319 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -19.7) |
| [[HEC-1-A (line)]] | alt | 169 | 3 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -23.4) |
| [[SK-MEL-2 (line)]] | alt | 133 | 1 | 8 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.273× (z -14.8) |
| [[KATO III (line)]] | alt | 187 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -24.9) |
| [[RKO (line)]] | wt | 215 | 3 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +17.9) | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -18.5) |
| [[SW1417 (line)]] | alt | 209 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -23.4) |
| [[SW480 (line)]] | alt | 129 | 1 | 7 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.171× (z -24.8) |
| [[HepG2_C3A (line)]] | wt | 186 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.216× (z -15.8) |
| [[HOP62 (line)]] | alt | 129 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -16.1) |
| [[LS 180 (line)]] | wt | 247 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -26.2) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -17.3) |
| [[SW 900 (line)]] | alt | 177 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -13.6) |
| [[SW48 (line)]] | wt | 162 | 2 | 5 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.209× (z -14.5) |
| [[A-427 (line)]] | wt | 165 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.313× (z -13.0) |
| [[Hs 766T (line)]] | wt | 108 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -15.3) |
| [[J82 (line)]] | alt | 156 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -22.9) |
| [[NCI-H23 (line)]] | alt | 86.6 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.260× (z -12.4) |
| [[NCI-H661 (line)]] | alt | 353 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -14.7) |
| [[SHP-77 (line)]] | alt | 211 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.230× (z -17.6) |
| [[A549 (line)]] | wt | 185 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -18.4) |
| [[BT-474 (line)]] | alt | 248 | 1 | 4 | [[Neratinib (maleate) (drug)]] 5 µM 1.67× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -18.6) |
| [[HCT15 (line)]] | alt | 164 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -14.5) |
| [[C-33 A (line)]] | alt | 173 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -14.2) |
| [[H4 (line)]] | wt | 104 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.160× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 90.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.213× (z -13.4) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 125 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -12.1) |
| [[SNU-1 (line)]] | wt | 244 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0622× (z -29.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.131× (z -22.4) |
| [[AN3 CA (line)]] | alt | 220 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -13.1) |
| [[CHP-212 (line)]] | wt | 137 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -9.8) |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 171 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDFY3]] | +0.76 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ARID1B]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[TLK2]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[HOXB7]] | +0.67 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ZNF362]] | +0.66 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[EFCAB2]] | +0.65 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[CREBBP]] | +0.64 | +0.45 / +0.56 | both halves | 3e-05 | same gene group; pathway: Activation of gene expression by SREBF (SREBP); STRING 997 |
| [[DYRK1A]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[RAF1]] | +0.63 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[BBX]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[PRDM2]] | +0.62 | +0.52 / +0.37 | both halves | 7e-05 |  |
| [[ATAD2B]] | +0.62 | +0.35 / +0.58 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMIP]] | -0.58 | -0.47 / -0.46 | both halves | 3e-05 | STRING 441 |
| [[FCHO1]] | -0.58 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[TMEM241]] | -0.57 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TXNL4A]] | -0.56 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[SYP]] | -0.56 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[CADM4]] | -0.55 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[DGKD]] | -0.55 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[SGSM1]] | -0.55 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[KCTD20]] | -0.55 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ANKS6]] | -0.55 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[NME7]] | -0.54 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[HEMK1]] | -0.54 | -0.34 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NCOA2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF470]] | B | ZNF470 activity lowers NCOA2's level | lines that do not express ZNF470 (18) vs lines expressing it (32) | 1.30× higher at baseline in the lines without ZNF470 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZFP28, ZNF71, ZIM2-AS1 |
| [[GALNT18]] | B | GALNT18 activity lowers NCOA2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.33× higher at baseline in the lines without GALNT18 | 0.048 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[LAMA1]] | B | LAMA1 activity lowers NCOA2's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.27× higher at baseline in the lines without LAMA1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[ARAP3]] | B | ARAP3 activity lowers NCOA2's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without ARAP3 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[ADRA1B]] | C | ADRA1B activity weakens NCOA2's drug response | lines that do not express ADRA1B (24) vs lines expressing it (25) | the lines without ADRA1B respond 0.97× as strongly (z diff -0.46); strongest at Panobinostat 0.5 µM: 0.20x vs 0.20x (z diff -1.1) | 0.090 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.4, 14.2); signed map (27.8, -23.5). **Vector** length 125, 53.3% of its response variance represented; |z| ≥ 3 in 1,704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +15.9 | +12.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.9 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.9 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -14.5 | -11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -12.1 | -7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -9.6 | -15.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.3 | -25.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.1 | -11.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.1 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.6 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.6 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor coactivator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.3 — chr8:70,109,782-70,403,808 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRC-2, TIF2, GRIP1, NCoA-2, KAT13C, bHLHe75 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Lysine acetyltransferases; PAS domain containing |
| Reactome | 48 pathways, smallest: Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Recycling of bile acids and salts; Endogenous sterols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15596](https://www.uniprot.org/uniprotkb/Q15596) (Nuclear receptor coactivator 2):

> Transcriptional coactivator for steroid receptors and nuclear receptors. Coactivator of the steroid binding domain (AF-2) but not of the modulating N-terminal domain (AF-1). Required with NCOA1 to control energy balance between white and brown adipose tissues. Critical regulator of glucose metabolism regulation, acts as a RORA coactivator to specifically modulate G6PC1 expression. Involved in the positive regulation of the transcriptional activity of the glucocorticoid receptor NR3C1 by …

**Summary**, from NCBI Gene [10499](https://www.ncbi.nlm.nih.gov/gene/10499):

> The protein encoded by this gene functions as a transcriptional coactivator for nuclear hormone receptors, including steroid, thyroid, retinoid, and vitamin D receptors. The encoded protein acts as an intermediary factor for the ligand-dependent activity of these nuclear receptors, which regulate their target genes upon binding of cognate response elements. This gene has been found to be involved in translocations that result in fusions with other genes in various cancers, including the lysine …

**Accessions** — [HGNC:7669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7669) · Entrez [10499](https://www.ncbi.nlm.nih.gov/gene/10499) · UniProt [Q15596](https://www.uniprot.org/uniprotkb/Q15596) · Ensembl [ENSG00000140396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140396)

## Data

Gene col 6402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6402); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6402]; `tensor/DDL_lfc|DDL_z.npy` [6402]; `embed/gene_vectors.npy` [6402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6402 or target_col == 6402). Every well: [[NCOA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
