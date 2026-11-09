---
symbol: "WDR43"
type: "gene"
col: 8784
ensembl_id: "ENSG00000163811"
name: "WD repeat domain 43"
location: "2p23.2"
module: 33
arm: "+"
pooled_cpm: 249.32
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 13
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# WDR43

*WD repeat domain 43* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.23× (z +17.7, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.512× (z -10.3, q 3e-22, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.680× (z -6.0, q 4e-07, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP16]] (+0.76, fdr 7e-06), [[POLR1B]] (+0.75, fdr 7e-06), [[WDR3]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GNL3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.23×** | +17.7 | 0e+00 | 49/49 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **7.96×** | +17.4 | 0e+00 | 48/48 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +11.7 | 2e-29 | 41/48 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +11.2 | 6e-27 | 45/47 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +10.7 | 1e-24 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.39×** | +10.2 | 2e-22 | 37/38 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.80×** | +9.4 | 3e-19 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +8.8 | 1e-16 | 43/48 (Hs 766T, HT-29, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.73×** | +8.7 | 2e-16 | 39/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +7.5 | 5e-12 | 44/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +7.5 | 5e-12 | 38/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.10×** | +6.2 | 3e-08 | 45/48 (Hs 766T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.30×** | +5.9 | 2e-07 | 28/48 (A-172, SNU-423, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +5.8 | 2e-07 | 33/49 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.4 | 2e-06 | 32/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.87×** | +5.2 | 6e-06 | 41/48 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.80×** | +4.9 | 3e-05 | 37/48 (PANC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 3e-05 | 31/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +4.8 | 6e-05 | 40/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 29/48 (PANC-1, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -10.3 | 3e-22 | 37/44 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.574×** | -8.9 | 1e-16 | 41/49 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.680×** | -6.0 | 4e-07 | 39/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.778×** | -4.1 | 0.007 | 29/47 (LoVo, LS 180, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.784×** | -3.9 | 0.010 | 28/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.789×** | -3.8 | 0.010 | 30/48 (KATO III, C-33 A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.8 | 0.010 | 3/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.822×** | -3.8 | 0.010 | 28/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.806×** | -3.5 | 0.029 | 26/48 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.035 | 23/48 (LoVo, SW480, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.072 | 20/48 (CFPAC-1, LS 180, …) | top dose only | plate-row cell shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.072 | 22/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | **0.827×** | -3.1 | 0.090 | 23/48 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.828×** | -3.1 | 0.091 | 20/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 305 | 12 (5 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -17.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 236 | 5 (2 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.543× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 133 | 11 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.13× (z +16.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.38× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 376 | 8 (2 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 289 | 8 (4 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.78× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 345 | 7 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +14.1) | [[Adagrasib (drug)]] 0.05 µM 0.646× (z -16.0) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 299 | 7 (4 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.03× (z +11.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 11.3× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 353 | 4 (1 ⚠) | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 10.3× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -8.5) |
| [[COLO 205 (line)]] | alt | 123 | 7 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 21.8× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 105 | 7 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.11× (z +12.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 130 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.14× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 130 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +11.2) | — |
| [[A-172 (line)]] | wt | 147 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.1× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 164 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +16.2) | — |
| [[SK-MEL-2 (line)]] | alt | 206 | 5 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 12.5× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 403 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.62× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -19.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 206 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.03× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 245 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.40× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 144 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 376 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.14× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 494 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 12.7× (z +18.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -9.6) |
| [[SNU-1 (line)]] | wt | 365 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 7.21× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -15.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 235 | 4 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 12.5× (z +14.5) | — |
| [[RPMI-7951 (line)]] | alt | 193 | 3 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.63× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -12.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 386 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.8× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -8.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 376 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 183 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 8.92× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 141 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.62× (z +17.0) | — |
| [[H4 (line)]] | wt | 202 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 216 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.09× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 262 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.46× (z +13.7) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 7.99× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 136 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 15.0× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 469 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -10.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 311 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.43× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 273 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.07× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 263 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.54× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 142 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.60× (z +8.9) | — |
| [[J82 (line)]] | alt | 187 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.63× (z +10.7) | — |
| [[KATO III (line)]] | alt | 194 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.98× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 184 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.66× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 213 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.70× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 219 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 10.4× (z +10.0) | — |
| [[C32 (line)]] | wt | 197 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 19.4× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 292 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP16]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[POLR1B]] | +0.75 | +0.79 / +0.77 | both halves | 7e-06 | STRING 831 |
| [[WDR3]] | +0.75 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[DHX33]] | +0.72 | +0.71 / +0.74 | both halves | 7e-06 | STRING 708 |
| [[DDX31]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 | STRING 720 |
| [[SNHG17]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PVT1]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[USP10]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[UCK2]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[NME1]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PA2G4]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 733 |
| [[WDR36]] | +0.68 | +0.75 / +0.66 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises WDR43's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNL3]] | C | WDR43's natural level weakens GNL3's drug response | WDR43's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.06; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.0, -39.1); signed map (-6.5, -50.8). **Vector** length 120, 55.4% of its response variance represented; |z| ≥ 3 in 1,827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +8.8 |
|  | [[EX229 (drug)]] 5 µM |  | +6.3 | +5.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +6.2 | +10.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +11.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.9 | +6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.3 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +4.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.6 | +10.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -6.6 | +4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.0 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.5 | +5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.8 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -6.0 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:28,894,667-28,948,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0007, NET12, UTP5 |
| Gene groups (HGNC) | WD repeat domain containing; UTPa subcomplex; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15061](https://www.uniprot.org/uniprotkb/Q15061) (WD repeat-containing protein 43):

> Ribosome biogenesis factor that coordinates hyperactive transcription and ribogenesis. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal …

**Summary**, from NCBI Gene [23160](https://www.ncbi.nlm.nih.gov/gene/23160):

> Enables RNA binding activity. Involved in positive regulation of rRNA processing; positive regulation of transcription by RNA polymerase I; and ribosomal small subunit biogenesis. Located in fibrillar center. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28945) · Entrez [23160](https://www.ncbi.nlm.nih.gov/gene/23160) · UniProt [Q15061](https://www.uniprot.org/uniprotkb/Q15061) · Ensembl [ENSG00000163811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163811)

## Data

Gene col 8784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8784); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8784]; `tensor/DDL_lfc|DDL_z.npy` [8784]; `embed/gene_vectors.npy` [8784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8784 or target_col == 8784). Every well: [[WDR43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
