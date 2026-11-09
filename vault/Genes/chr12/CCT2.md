---
symbol: "CCT2"
type: "gene"
col: 9265
ensembl_id: "ENSG00000166226"
name: "chaperonin containing TCP1 subunit 2"
location: "12q15"
module: 4
arm: "+"
pooled_cpm: 88.94
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 5
n_dd_up_clean: 24
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CCT2

*chaperonin containing TCP1 subunit 2* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.91× (z +16.3, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.39× (z +13.3, q 4e-38, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.901× (z -5.3, q 6e-05, down in 6 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.742× (z -4.2, q 0.007, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT5]] (+0.85, fdr 7e-06), [[CCT3]] (+0.79, fdr 7e-06), [[CCT4]] (+0.77, fdr 7e-06); moves opposite to [[PHPT1]] (-0.69, fdr 7e-06), [[TNRC6C]] (-0.68, fdr 8e-06), [[TERF2IP]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 24 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.91×** | +16.3 | 0e+00 | 48/49 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.69×** | +13.8 | 6e-41 | 42/44 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +13.3 | 4e-38 | 46/48 (C32, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.37×** | +12.2 | 5e-32 | 40/45 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.15×** | +11.7 | 2e-29 | 47/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +11.3 | 7e-28 | 44/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.97×** | +10.4 | 3e-23 | 45/48 (HOP62, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **2.07×** | +10.2 | 2e-22 | 42/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.93×** | +10.0 | 7e-22 | 46/48 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +9.4 | 3e-19 | 46/49 (PANC-1, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.82×** | +9.1 | 3e-18 | 46/48 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.81×** | +8.6 | 5e-16 | 39/48 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.82×** | +8.3 | 5e-15 | 43/44 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.44×** | +7.8 | 2e-13 | 32/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +7.7 | 4e-13 | 43/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.44×** | +7.1 | 3e-11 | 40/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.9 | 2e-05 | 27/48 (A-172, NCI-H1792, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.83×** | +4.8 | 3e-05 | 37/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.7 | 7e-05 | 27/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 4e-04 | 31/49 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 7e-04 | 25/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 7e-04 | 26/47 (HOP62, H4, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.001 | 30/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.001 | 28/48 (NCI-H1792, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -5.3 | 6e-05 | 6/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.742×** | -4.2 | 0.007 | 28/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.824×** | -4.1 | 0.007 | 22/48 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.789×** | -3.7 | 0.030 | 24/50 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.6 | 0.037 | 22/49 (RKO, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.795×** | -3.5 | 0.038 | 22/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.853× | -3.4 | 0.059 | 18/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.802×** | -3.3 | 0.059 | 20/49 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.834× | -3.3 | 0.062 | 17/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.808× | -3.1 | 0.11 | 17/49 (Hs 766T, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 81.3 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +16.5) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +13.5) | — |
| [[A498 (line)]] | wt | 74.1 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +9.5) | — |
| [[A-172 (line)]] | wt | 43.7 | 7 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.43× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 53.5 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.56× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 57.1 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.79× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 58.1 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 86.0 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.54× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 109 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.52× (z +9.6) | — |
| [[A549 (line)]] | wt | 89.6 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +12.0) | — |
| [[J82 (line)]] | alt | 85.6 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.9 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.12× (z +10.5) | [[Adagrasib (drug)]] 0.05 µM 0.649× (z -13.1) ⚠ position not correctable |
| [[SNU-423 (line)]] | alt | 67.6 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[C32 (line)]] | wt | 42.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +13.1) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.14× (z +12.7) | — |
| [[LoVo (line)]] | wt | 103 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[LOX-IMVI (line)]] | wt | 127 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.0) | — |
| [[SW480 (line)]] | alt | 118 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.85× (z +11.0) | — |
| [[A-427 (line)]] | wt | 179 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.78× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 58.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 80.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 48.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.19× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 57.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.38× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 68.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.47× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 35.3 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.41× (z +10.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 56.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[LS 180 (line)]] | wt | 81.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H23 (line)]] | alt | 199 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 50.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 151 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.36× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 47.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 90.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 121 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.65× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 90.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.13× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.176× (z -10.7) |
| [[HCT15 (line)]] | alt | 92.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.59× (z +8.5) | — |
| [[KATO III (line)]] | alt | 76.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2030 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.74× (z +8.6) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 77.6 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.67× (z +8.5) | — |
| [[NCI-H596 (line)]] | alt | 88.1 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.371× (z -8.9) |
| [[RKO (line)]] | wt | 226 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT3]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT4]] | +0.77 | +0.80 / +0.74 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[MAK16]] | +0.74 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[ATIC]] | +0.74 | +0.72 / +0.78 | both halves | 7e-06 | STRING 436 |
| [[AGPS]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[NUDC]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 | STRING 704 |
| [[NAA15]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[FKTN]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[DLAT]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.70 | +0.76 / +0.64 | both halves | 7e-06 | STRING 839 |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHPT1]] | -0.69 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.68 | -0.58 / -0.66 | both halves | 8e-06 | pathway: Cilium Assembly |
| [[TERF2IP]] | -0.68 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.67 | -0.47 / -0.74 | both halves | 2e-05 |  |
| [[SERF2]] | -0.67 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[HLA-A]] | -0.66 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.65 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[ZNF821]] | -0.64 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[STX5]] | -0.64 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.64 | -0.66 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CCT2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises CCT2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.852). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.0, -32.7); signed map (-12.1, -45.2). **Vector** length 102, 40.2% of its response variance represented; |z| ≥ 3 in 1,489 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.56 to 8); *tRNA processing* (reactome, mean cos +0.56 to 10); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.50 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +11.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +7.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.4 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.9 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.2 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.9 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:69,585,426-69,601,570 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cctb |
| Gene groups (HGNC) | Chaperonin containing TCP1 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 21 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; BBSome-mediated cargo-targeting to cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P78371](https://www.uniprot.org/uniprotkb/P78371) (T-complex protein 1 subunit beta):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance. As part of the TRiC complex may play a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia.

**Summary**, from NCBI Gene [10576](https://www.ncbi.nlm.nih.gov/gene/10576):

> The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including actin and tubulin. Two transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:1615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1615) · Entrez [10576](https://www.ncbi.nlm.nih.gov/gene/10576) · UniProt [P78371](https://www.uniprot.org/uniprotkb/P78371) · Ensembl [ENSG00000166226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166226)

## Data

Gene col 9265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9265); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9265]; `tensor/DDL_lfc|DDL_z.npy` [9265]; `embed/gene_vectors.npy` [9265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9265 or target_col == 9265). Every well: [[CCT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
