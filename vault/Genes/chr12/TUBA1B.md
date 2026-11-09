---
symbol: "TUBA1B"
type: "gene"
col: 4432
ensembl_id: "ENSG00000123416"
name: "tubulin alpha 1b"
location: "12q13.12"
module: 6
arm: "+"
pooled_cpm: 132.39
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TUBA1B

*tubulin alpha 1b* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.15× (z +12.8, q 8e-35, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.85× (z +6.8, q 1e-09, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.505× (z -7.5, q 4e-11, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRM2]] (+0.75, fdr 7e-06), [[SPC25]] (+0.75, fdr 7e-06), [[NCAPG2]] (+0.75, fdr 7e-06); moves opposite to [[EPB41L4A-AS1]] (-0.63, fdr 1e-05), [[SNHG32]] (-0.63, fdr 2e-05), [[MTIF3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **5.15×** | +12.8 | 8e-35 | 48/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.64×** | +11.5 | 2e-28 | 43/43 (A549, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.27×** | +8.6 | 2e-15 | 43/44 (Panc 03.27, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **2.64×** | +7.6 | 4e-12 | 47/47 (C32, NCI-H2030, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.52×** | +7.2 | 5e-11 | 46/47 (C32, PANC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.85×** | +6.8 | 1e-09 | 44/47 (C32, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.92×** | +5.1 | 2e-05 | 39/47 (C32, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.87×** | +4.9 | 6e-05 | 42/47 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.77×** | +4.5 | 5e-04 | 37/47 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.74×** | +4.4 | 8e-04 | 41/48 (C32, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.003 | 44/47 (A498, J82, …) | top dose only | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.56×** | +3.5 | 0.022 | 34/47 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.033 | 32/47 (C32, LoVo, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **1.58×** | +3.3 | 0.035 | 30/47 (C32, LOX-IMVI, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.51×** | +3.3 | 0.040 | 29/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.50×** | +3.2 | 0.043 | 34/48 (HOP62, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.505×** | -7.5 | 4e-11 | 40/47 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.488×** | -5.6 | 7e-06 | 45/47 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.505×** | -5.3 | 2e-05 | 43/47 (NCI-H661, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -4.9 | 1e-04 | 32/48 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.550×** | -4.6 | 4e-04 | 37/47 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.561×** | -4.5 | 7e-04 | 38/47 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.698×** | -3.9 | 0.006 | 27/47 (LS 180, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.604×** | -3.9 | 0.006 | 35/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -3.8 | 0.009 | 28/47 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.615×** | -3.8 | 0.009 | 35/47 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.636×** | -3.5 | 0.022 | 30/46 (KATO III, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.621×** | -3.5 | 0.022 | 36/48 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.601×** | -3.4 | 0.029 | 34/49 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.439×** | -3.3 | 0.033 | 37/48 (HOP62, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.450×** | -3.3 | 0.043 | 32/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.479×** | -3.0 | 0.089 | 32/48 (HOP62, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.680×** | -3.0 | 0.089 | 29/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 66.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 4.47× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 126 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.4) |
| [[H4 (line)]] | wt | 190 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.6) |
| [[HOP62 (line)]] | alt | 115 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.62× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.1) |
| [[PANC-1 (line)]] | alt | 111 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW480 (line)]] | alt | 229 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.9) |
| [[A-427 (line)]] | wt | 324 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.5) |
| [[A498 (line)]] | wt | 229 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A549 (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.85× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 182 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.6) |
| [[HT-29 (line)]] | alt | 77.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.04× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.78× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 110 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 232 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.15× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[RKO (line)]] | wt | 107 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.4) |
| [[SNU-1 (line)]] | wt | 106 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -12.7) |
| [[SNU-423 (line)]] | alt | 89.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.85× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW1417 (line)]] | alt | 75.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW48 (line)]] | wt | 130 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.1) |
| [[A-172 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[CFPAC-1 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HCT15 (line)]] | alt | 205 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -15.4) |
| [[Hs 766T (line)]] | wt | 76.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HS-578T (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.11× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[J82 (line)]] | alt | 187 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[KATO III (line)]] | alt | 140 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LOX-IMVI (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1573 (line)]] | alt | 64.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.89× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2347 (line)]] | alt | 140 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.53× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[RPMI-7951 (line)]] | alt | 87.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SHP-77 (line)]] | alt | 148 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Vinblastine (sulfate) (drug)]] 5 µM 0.415× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.91× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 900 (line)]] | alt | 96.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.20× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[AN3 CA (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[BT-474 (line)]] | alt | 161 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.8) |
| [[CHP-212 (line)]] | wt | 68.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.75× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 97.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2030 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.47× (z +9.6) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H661 (line)]] | alt | 231 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.130× (z -9.4) |
| [[SW 1088 (line)]] | alt | 170 | 0 | 1 | — | [[Sildenafil (drug)]] 0.05 µM 0.0570× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 146 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRM2]] | +0.75 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[SPC25]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 | pathway: EML4 and NUDC in mitotic spindle formation |
| [[NCAPG2]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[TUBB]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 999 |
| [[CENPO]] | +0.73 | +0.79 / +0.69 | both halves | 7e-06 | pathway: EML4 and NUDC in mitotic spindle formation |
| [[MELK]] | +0.73 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[WDR76]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CENPN]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 | pathway: EML4 and NUDC in mitotic spindle formation |
| [[DTL]] | +0.71 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[CENPK]] | +0.71 | +0.76 / +0.63 | both halves | 7e-06 | pathway: EML4 and NUDC in mitotic spindle formation |
| [[EXO1]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins |
| [[POLQ]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | -0.63 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.63 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[MTIF3]] | -0.61 | -0.64 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.1, -47.5); signed map (-40.4, -43.6). **Vector** length 106, 40.2% of its response variance represented; |z| ≥ 3 in 1,427 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.53 to 65); *DNA strand elongation* (reactome, mean cos +0.55 to 28); *DNA Replication* (reactome, mean cos +0.55 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +6.2 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +6.0 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.5 | +4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +4.2 | +7.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +0.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +2.6 | +3.2 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.4 | +1.7 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.2 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.8 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.9 | -1.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | tubulin alpha 1b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,127,782-49,131,397 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K-ALPHA-1 |
| Gene groups (HGNC) | Tubulin alpha family |
| Reactome | 84 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P68363](https://www.uniprot.org/uniprotkb/P68363) (Tubulin alpha-1B chain):

> Tubulin is the major constituent of microtubules, protein filaments consisting of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [10376](https://www.ncbi.nlm.nih.gov/gene/10376):

> Enables several functions, including GTP binding activity; double-stranded RNA binding activity; and ubiquitin protein ligase binding activity. A structural constituent of cytoskeleton. Involved in microtubule cytoskeleton organization. Located in cilium and microtubule. Is active in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18809) · Entrez [10376](https://www.ncbi.nlm.nih.gov/gene/10376) · UniProt [P68363](https://www.uniprot.org/uniprotkb/P68363) · Ensembl [ENSG00000123416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123416)

## Data

Gene col 4432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4432); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4432]; `tensor/DDL_lfc|DDL_z.npy` [4432]; `embed/gene_vectors.npy` [4432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4432 or target_col == 4432). Every well: [[TUBA1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBA1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
