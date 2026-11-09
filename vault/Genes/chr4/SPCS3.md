---
symbol: "SPCS3"
type: "gene"
col: 4950
ensembl_id: "ENSG00000129128"
name: "signal peptidase complex subunit 3"
location: "4q34.2"
module: 20
arm: "+"
pooled_cpm: 63.67
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SPCS3

*signal peptidase complex subunit 3* — 4q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.92× (z +23.4, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.71× (z +9.2, q 4e-18, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -13.2, q 6e-37, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC5]] (+0.65, fdr 7e-06), [[UGGT2]] (+0.63, fdr 1e-05), [[UGGT1]] (+0.60, fdr 1e-05); moves opposite to [[HEIH]] (-0.63, fdr 1e-05), [[NFKBIL1]] (-0.63, fdr 1e-05), [[CCDC174]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.92×** | +23.4 | 0e+00 | 48/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +21.2 | 0e+00 | 41/42 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +12.7 | 1e-34 | 39/44 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +9.2 | 4e-18 | 43/48 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.49×** | +6.8 | 9e-10 | 34/48 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.33×** | +4.7 | 3e-04 | 24/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.31×** | +4.6 | 3e-04 | 28/48 (hTERT-HPNE, AsPC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.31×** | +4.6 | 3e-04 | 27/48 (NCI-H2347, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.002 | 26/48 (NCI-H2347, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 21/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.24×** | +3.7 | 0.013 | 23/48 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.24×** | +3.6 | 0.013 | 20/48 (HEC-1-A, H4, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +3.4 | 0.026 | 18/47 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.15× | +3.4 | 0.032 | 8/49 (HEC-1-A, KATO III, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.042 | 17/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.063 | 15/46 (HOP62, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.069 | 20/47 (HOP62, PANC-1, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.096 | 13/48 (PANC-1, SHP-77, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.096 | 13/48 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -13.2 | 6e-37 | 37/47 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.789×** | -5.7 | 3e-06 | 29/48 (LS 180, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.740×** | -5.1 | 5e-05 | 27/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.541×** | -5.0 | 7e-05 | 31/48 (A498, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.789×** | -3.8 | 0.016 | 22/48 (A498, SW 1271, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.638×** | -3.7 | 0.018 | 20/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.806×** | -3.7 | 0.018 | 19/48 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.800×** | -3.7 | 0.018 | 23/48 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.816×** | -3.5 | 0.032 | 22/48 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.793×** | -3.4 | 0.032 | 22/49 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.833×** | -3.1 | 0.097 | 12/48 (HCT15, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.832× | -3.0 | 0.12 | 17/48 (HepG2/C3A, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 151 | 2 (2 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -18.3) |
| [[HS-578T (line)]] | alt | 53.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 55.6 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.07× (z +19.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 61.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.0) |
| [[HOP62 (line)]] | alt | 84.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +16.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 73.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.94× (z +8.5) | — |
| [[LoVo (line)]] | wt | 107 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 76.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -17.2) |
| [[PANC-1 (line)]] | alt | 56.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.5) |
| [[A-172 (line)]] | wt | 48.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.55× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 61.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +18.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 69.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.1) |
| [[LS 180 (line)]] | wt | 92.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +15.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 69.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 52.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 48.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +15.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 47.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +15.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 141 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.1) |
| [[SNU-423 (line)]] | alt | 21.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.75× (z +13.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 62.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +16.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +13.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 60.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 60.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 42.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.25× (z +14.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 76.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 35.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.33× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 66.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +12.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 87.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -18.8) |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 38.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 41.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 40.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 75.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +15.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 80.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 58.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 74.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 84.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 89.6 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0738× (z -8.5) |
| [[SW 900 (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[UGGT2]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[UGGT1]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[EIF5A]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[MACROH2A1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ATP2A2]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[FKBP1A]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DNAJC10]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[VMA21]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ITGB1]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 | pathway: Cell junction organization |
| [[TMED7]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 | STRING 432 |

## Genes that move opposite

*69 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEIH]] | -0.63 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TTC21A]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CBR3]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[C1orf131]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SNHG11]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SAP18]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[COIL]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[AMZ2P1-1]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MRPS31]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.1, -35.3); signed map (-24.9, -40.8). **Vector** length 105, 30.9% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +21.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +23.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +5.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Larotrectinib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -3.4 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.2 | -3.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -3.1 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | signal peptidase complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.2 — chr4:176,319,966-176,332,245 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22649, SPC22/23, SPC3, YLR066W, PRO3567 |
| Hallmark sets | ANDROGEN_RESPONSE, UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 22 pathways, smallest: Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP); Synthesis, secretion, and deacylation of Ghrelin; Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1) |
| Matched by | ensembl_id |

**Function**, from UniProt [P61009](https://www.uniprot.org/uniprotkb/P61009) (Signal peptidase complex subunit 3):

> Essential component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum. Essential for the SPC catalytic activity, possibly by stabilizing and positioning the active center of the complex close to the lumenal surface (By similarity).; (Microbial infection) Plays an important role in virion production of flaviviruses such as West Nile virus, Japanese …

**Summary**, from NCBI Gene [60559](https://www.ncbi.nlm.nih.gov/gene/60559):

> Involved in obsolete signal peptide processing and viral protein processing. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26212) · Entrez [60559](https://www.ncbi.nlm.nih.gov/gene/60559) · UniProt [P61009](https://www.uniprot.org/uniprotkb/P61009) · Ensembl [ENSG00000129128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129128)

## Data

Gene col 4950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4950); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4950]; `tensor/DDL_lfc|DDL_z.npy` [4950]; `embed/gene_vectors.npy` [4950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4950 or target_col == 4950). Every well: [[SPCS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPCS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
