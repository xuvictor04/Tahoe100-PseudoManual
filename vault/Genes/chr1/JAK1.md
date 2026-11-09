---
symbol: "JAK1"
type: "gene"
col: 8519
ensembl_id: "ENSG00000162434"
name: "Janus kinase 1"
location: "1p31.3"
module: 139
arm: "+"
pooled_cpm: 287.72
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# JAK1

*Janus kinase 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.74× (z +15.9, q 0e+00, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.651× (z -12.3, q 4e-32, down in 38 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.661× (z -6.0, q 3e-07, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF9]] (+0.60, fdr 1e-05), [[OSER1]] (+0.58, fdr 8e-06), [[BCL6]] (+0.56, fdr 1e-05); moves opposite to [[XXYLT1]] (-0.55, fdr 1e-05), [[PRDM15]] (-0.50, fdr 2e-05), [[LIMD1]] (-0.49, fdr 8e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ANTXR2]] → it (grade B ⚠); 6 go from it, the strongest it → [[CTDSPL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +15.9 | 0e+00 | 34/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +15.1 | 0e+00 | 30/48 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +7.7 | 3e-12 | 30/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +7.5 | 8e-12 | 31/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +7.4 | 1e-11 | 27/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.58×** | +6.6 | 4e-09 | 40/50 (LoVo, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +6.4 | 1e-08 | 31/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +6.1 | 9e-08 | 28/50 (A549, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.21×** | +5.6 | 1e-06 | 25/49 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.4 | 4e-06 | 24/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +5.0 | 4e-05 | 26/49 (LoVo, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.12× | +4.9 | 4e-05 | 12/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.18× | +4.9 | 5e-05 | 22/48 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.17× | +4.7 | 1e-04 | 15/47 (BT-474, KATO III, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.17× | +4.6 | 1e-04 | 13/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +4.3 | 7e-04 | 6/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 21/49 (H4, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 23/49 (Panc 03.27, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +4.1 | 0.001 | 15/48 (A549, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -12.3 | 4e-32 | 38/47 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -8.2 | 8e-14 | 36/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.807×** | -6.1 | 2e-07 | 24/44 (CFPAC-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.661×** | -6.0 | 3e-07 | 36/48 (NCI-H23, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.809×** | -5.8 | 6e-07 | 24/45 (NCI-H23, SW1417, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.825×** | -5.7 | 9e-07 | 27/48 (SW 900, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.677×** | -5.6 | 1e-06 | 31/48 (C32, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -5.2 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.892× | -4.8 | 8e-05 | 3/48 (CFPAC-1, SNU-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.716×** | -4.8 | 8e-05 | 33/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | 0.856× | -4.6 | 2e-04 | 22/48 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.733×** | -4.5 | 3e-04 | 27/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.813×** | -4.4 | 5e-04 | 21/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.902× | -4.4 | 5e-04 | 11/49 (A549, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.817×** | -4.3 | 6e-04 | 18/49 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.771×** | -3.8 | 0.005 | 20/48 (NCI-H23, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.057 | 12/48 (A498, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.069 | 14/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.906× | -2.9 | 0.089 | 17/48 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.818×** | -2.9 | 0.090 | 14/47 (NCI-H23, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.873× | -2.9 | 0.093 | 18/48 (NCI-H1573, AsPC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 217 | 18 (10 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.10× (z +19.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.29× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 382 | 12 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.532× (z -9.7) ⚠ toxic |
| [[BT-474 (line)]] | alt | 275 | 10 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 371 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +24.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -16.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 253 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +18.1) | — |
| [[LoVo (line)]] | wt | 256 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.574× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[NCI-H1573 (line)]] | alt | 408 | 6 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.45× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.443× (z -11.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 270 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +19.4) | — |
| [[A498 (line)]] | wt | 613 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -15.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 489 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +23.8) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 403 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 226 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.9) | — |
| [[A-427 (line)]] | wt | 178 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.70× (z +9.4) | — |
| [[H4 (line)]] | wt | 342 | 2 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.56× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.548× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HEC-1-A (line)]] | alt | 137 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.4) | — |
| [[NCI-H1792 (line)]] | alt | 345 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.525× (z -11.5) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 357 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.514× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2347 (line)]] | alt | 294 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.560× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 349 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.481× (z -12.3) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 297 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +22.7) | — |
| [[HT-29 (line)]] | alt | 263 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.506× (z -9.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 439 | 2 | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.19× (z +9.8) | — |
| [[J82 (line)]] | alt | 255 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +17.5) | — |
| [[KATO III (line)]] | alt | 262 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.452× (z -11.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 312 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.545× (z -9.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 212 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 302 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.6) | — |
| [[SW 900 (line)]] | alt | 275 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.96× (z +9.0) | [[Docetaxel (drug)]] 0.05 µM 0.393× (z -13.0) ⚠ transcription drop; cell-cycle shift, explains ~23% of this change |
| [[SW480 (line)]] | alt | 235 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.546× (z -11.9) ⚠ toxic |
| [[C32 (line)]] | wt | 252 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.462× (z -10.6) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 460 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 229 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 186 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.70× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 366 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.26× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 289 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.525× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 158 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 201 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 230 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF9]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[OSER1]] | +0.58 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[BCL6]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 | pathway: Interleukin-4 and Interleukin-13 signaling; STRING 419 |
| [[EPS8]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SOD2]] | +0.53 | +0.59 / +0.55 | both halves | 1e-05 | pathway: Interleukin-12 family signaling |
| [[YPEL2]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[DENND3]] | +0.52 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.52 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[DSTN]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ABI1]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[GSN]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 | STRING 440 |
| [[FLVCR2]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XXYLT1]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PRDM15]] | -0.50 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[LIMD1]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[MAD1L1]] | -0.47 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[STARD8]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SUV39H2]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ZNF544]] | -0.46 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[KHDC1]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[MYO19]] | -0.45 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ARPC5L]] | -0.44 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[ANXA10]] | -0.43 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ANTXR2]] | -0.43 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANTXR2]] | B | ANTXR2 activity raises JAK1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without ANTXR2 | 0.013 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[ZC3H12A]] | B | ZC3H12A activity raises JAK1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[MTOR]] | B | MTOR activity lowers JAK1's level | compounds that target MTOR: 4 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Sapanisertib) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds |
| [[PIK3CA]] | B | PIK3CA activity lowers JAK1's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ANXA10]] | B | ANXA10 activity raises JAK1's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.34× lower at baseline in the lines without ANXA10 | 0.096 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[B4GALT1]] | C | B4GALT1 activity raises JAK1's level | lines that do not express B4GALT1 (3) vs lines expressing it (47) | 1.49× lower at baseline in the lines without B4GALT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TIMP1, UGDH, ATXN1; maybe low, not absent; its own permutation p |
| [[SSBP2]] | C | SSBP2 activity lowers JAK1's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 1.36× higher at baseline in the lines without SSBP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTDSPL]] | B | JAK1, [[JAK3]] activity lowers CTDSPL's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[NALCN]] | B | JAK1, [[JAK3]] activity lowers NALCN's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PTPRB]] | B | JAK1, [[JAK3]] activity lowers PTPRB's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LYPD6B]] | B | JAK1, [[JAK3]] activity lowers LYPD6B's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ZNF704]] | B | JAK1, [[JAK3]] activity lowers ZNF704's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | JAK1's natural level lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | JAK1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.287 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 17.1); signed map (18.6, 26.8). **Vector** length 138, 45.5% of its response variance represented; |z| ≥ 3 in 1,825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +15.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.6 | +7.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +5.3 | +6.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.0 | +5.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +2.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.9 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.8 | +4.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.4 | -12.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.4 | -8.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -6.0 |
|  | [[EX229 (drug)]] 5 µM |  | -5.5 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.8 | -4.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | Janus kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:64,833,223-65,067,754 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JAK1A, JTK3; previously JAK1B |
| Gene groups (HGNC) | FERM domain containing; Jak family tyrosine kinases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 57 pathways, smallest: IFNG signaling activates MAPKs; Interleukin-9 signaling; Interleukin-21 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P23458](https://www.uniprot.org/uniprotkb/P23458) (Tyrosine-protein kinase JAK1):

> Non-membrane spanning protein tyrosine kinase that phosphorylates signal-transducing subunits of cytokine receptor complexes like IL2RB, IL10RA, IFNAR2, IL6ST, LIFR, OSMR and IL31RA. Functionally, is involved in the IFN-alpha/beta/gamma signal pathway. Mechanistically, in response to interferon-binding to IFNAR1-IFNAR2 heterodimer, phosphorylates and activates its binding partner IFNAR2, creating docking sites for STAT proteins. Directly phosphorylates STAT proteins but also activates STAT …

**Summary**, from NCBI Gene [3716](https://www.ncbi.nlm.nih.gov/gene/3716):

> This gene encodes a membrane protein that is a member of a class of protein-tyrosine kinases (PTK) characterized by the presence of a second phosphotransferase-related domain immediately N-terminal to the PTK domain. The encoded kinase phosphorylates STAT proteins (signal transducers and activators of transcription) and plays a key role in interferon-alpha/beta, interferon-gamma, and cytokine signal transduction. This gene plays a crucial role in effecting the expression of genes that mediate …

**Accessions** — [HGNC:6190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6190) · Entrez [3716](https://www.ncbi.nlm.nih.gov/gene/3716) · UniProt [P23458](https://www.uniprot.org/uniprotkb/P23458) · Ensembl [ENSG00000162434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162434)

## Data

Gene col 8519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8519); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8519]; `tensor/DDL_lfc|DDL_z.npy` [8519]; `embed/gene_vectors.npy` [8519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8519 or target_col == 8519). Every well: [[JAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
