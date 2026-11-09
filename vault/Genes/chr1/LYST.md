---
symbol: "LYST"
type: "gene"
col: 6788
ensembl_id: "ENSG00000143669"
name: "lysosomal trafficking regulator"
location: "1q42.3"
module: 14
arm: "+"
pooled_cpm: 133.33
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LYST

*lysosomal trafficking regulator* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.64× (z +39.2, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.807× (z -4.6, q 0.002, down in 26 of 47 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.667× (z -4.4, q 0.002, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.284×, SNU-423 0.405×, Hs 766T 0.386×, NCI-H1573 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.113×, HS-578T 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.331×, A498 0.501×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 0.407×); [[Budesonide (drug)]] 0.5 µM in 1 line (Hs 766T 0.438×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 0.441×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2B]] (+0.58, fdr 1e-05), [[GULP1]] (+0.57, fdr 9e-06), [[AGPAT4]] (+0.56, fdr 1e-05); moves opposite to [[IQCB1]] (-0.58, fdr 1e-05), [[SNRNP40]] (-0.57, fdr 1e-05), [[TTI1]] (-0.55, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFATC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.64×** | +39.2 | 0e+00 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.67×** | +21.1 | 0e+00 | 44/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.35×** | +17.6 | 0e+00 | 44/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +13.3 | 3e-38 | 39/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +12.3 | 9e-33 | 38/47 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +10.1 | 4e-22 | 32/47 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +10.0 | 8e-22 | 39/47 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +10.0 | 8e-22 | 29/47 (SW480, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +8.0 | 7e-14 | 32/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +7.6 | 2e-12 | 37/48 (A-172, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.5 | 4e-09 | 27/48 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +6.4 | 6e-09 | 28/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +6.1 | 5e-08 | 21/47 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.21×** | +5.9 | 2e-07 | 22/47 (C32, SK-MEL-2, …) | all doses, flat | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.7 | 3e-07 | 24/46 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 4e-06 | 30/47 (BT-474, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.7 | 9e-05 | 22/46 (NCI-H460, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6788.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.284×, SNU-423 0.405×, Hs 766T 0.386×, NCI-H1573 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.113×, HS-578T 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.331×, A498 0.501×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 0.407×); [[Budesonide (drug)]] 0.5 µM in 1 line (Hs 766T 0.438×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 0.441×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.807×** | -4.6 | 0.002 | 26/47 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | **0.806×** | -4.5 | 0.002 | 22/46 (CFPAC-1, RPMI-7951, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.667×** | -4.4 | 0.002 | 23/47 (HS-578T, A549, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.685×** | -4.1 | 0.005 | 23/44 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.718×** | -3.6 | 0.032 | 19/46 (Panc 03.27, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | 0.840× | -3.5 | 0.048 | 19/44 (C-33 A, HS-578T, …) | all doses, flat | composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 0.897× | -3.3 | 0.076 | 14/47 (NCI-H1573, A498, …) | rises with dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.859× | -3.1 | 0.13 | 15/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.904× | -3.1 | 0.13 | 8/48 (NCI-H1792, NCI-H2347, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 134 | 22 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +44.7) | — |
| [[Hs 766T (line)]] | wt | 231 | 4 | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +29.6) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.407× (z -10.2) |
| [[HT-29 (line)]] | alt | 57.8 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.2) | — |
| [[SW480 (line)]] | alt | 75.8 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +47.2) | — |
| [[A-172 (line)]] | wt | 168 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +37.6) | — |
| [[LoVo (line)]] | wt | 82.4 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +27.9) | — |
| [[A-427 (line)]] | wt | 53.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +24.4) | — |
| [[NCI-H23 (line)]] | alt | 70.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +26.4) | — |
| [[AsPC-1 (line)]] | alt | 166 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +27.4) | — |
| [[COLO 205 (line)]] | alt | 72.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +41.2) | — |
| [[A498 (line)]] | wt | 225 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +21.9) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 63.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +14.9) | — |
| [[HEC-1-A (line)]] | alt | 87.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +19.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 247 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 50.3 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.03× (z +13.5) | — |
| [[C32 (line)]] | wt | 201 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +23.4) | — |
| [[HOP62 (line)]] | alt | 84.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +18.0) | — |
| [[NCI-H1573 (line)]] | alt | 224 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 204 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +38.2) | — |
| [[RKO (line)]] | wt | 71.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +18.7) | — |
| [[SNU-423 (line)]] | alt | 224 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 78.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +35.2) | — |
| [[CFPAC-1 (line)]] | alt | 119 | 2 (1 ⚠) | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.73× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.446× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[HS-578T (line)]] | alt | 113 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.400× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 55.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +18.4) | — |
| [[LS 180 (line)]] | wt | 119 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +20.8) | — |
| [[NCI-H1792 (line)]] | alt | 182 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +23.3) | [[Dinaciclib (drug)]] 0.5 µM 0.503× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 248 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +28.3) | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SK-MEL-2 (line)]] | alt | 89.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 283 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +21.7) | [[Docetaxel (drug)]] 0.05 µM 0.463× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.2) | — |
| [[C-33 A (line)]] | alt | 99.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[H4 (line)]] | wt | 82.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +24.2) | — |
| [[J82 (line)]] | alt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +29.2) | — |
| [[NCI-H2030 (line)]] | alt | 72.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +27.7) | — |
| [[NCI-H2347 (line)]] | alt | 207 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +20.0) | — |
| [[Panc 03.27 (line)]] | alt | 148 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 46.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +12.4) | — |
| [[A549 (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.1) | — |
| [[CHP-212 (line)]] | wt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 84.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 280 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 82.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +20.7) | — |
| [[SW48 (line)]] | wt | 90.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2B]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GULP1]] | +0.57 | +0.57 / +0.59 | both halves | 9e-06 | same gene group |
| [[AGPAT4]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ACVR1C]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[GEM]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[OPTN]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SLC41A2]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SQSTM1]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[GPR137C]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[NR3C1]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[C6orf141]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CRYM]] | +0.53 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCB1]] | -0.58 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[SNRNP40]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 | same gene group |
| [[TTI1]] | -0.55 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[MTRR]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MND1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SLF1]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[EIF3B]] | -0.51 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[EBPL]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[GLMN]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NDC1]] | -0.50 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[NSUN2]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[IMMT]] | -0.49 | -0.57 / -0.39 | both halves | 5e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC2]] | B | NFATC2 activity raises LYST's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without NFATC2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[TP63]] | B | TP63 activity raises LYST's level | lines that do not express TP63 (39) vs lines expressing it (11) | 1.82× lower at baseline in the lines without TP63 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, ENSG00000241168, TYR |
| [[DSCC1]] | C | DSCC1 activity strengthens LYST's drug response | lines that do not express DSCC1 (3) vs lines expressing it (45) | the lines without DSCC1 respond 0.40× as strongly (z diff +3.50); strongest at Homoharringtonine 0.5 µM: 1.12x vs 2.85x (z diff +6.4) | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.343). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, -1.7); signed map (8.1, 21.2). **Vector** length 132, 44.0% of its response variance represented; |z| ≥ 3 in 1,776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +21.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +10.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +4.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | -7.0 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -4.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.9 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -1.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -3.8 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.7 | -2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.7 | -2.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | lysosomal trafficking regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,661,041-235,883,724 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHS, Mauve; previously CHS1 |
| Gene groups (HGNC) | WD repeat domain containing; BEACH domain containing ; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99698](https://www.uniprot.org/uniprotkb/Q99698) (Lysosomal-trafficking regulator):

> Adapter protein that regulates and/or fission of intracellular vesicles such as lysosomes. Might regulate trafficking of effectors involved in exocytosis. In cytotoxic T-cells and natural killer (NK) cells, has role in the regulation of size, number and exocytosis of lytic granules. In macrophages and dendritic cells, regulates phagosome maturation by controlling the conversion of early phagosomal compartments into late phagosomes (By similarity). In macrophages and dendritic cells, …

**Summary**, from NCBI Gene [1130](https://www.ncbi.nlm.nih.gov/gene/1130):

> This gene encodes a protein that regulates intracellular protein trafficking in endosomes, and may be involved in pigmentation. Mutations in this gene are associated with Chediak-Higashi syndrome, a lysosomal storage disorder. Alternative splicing results in multiple transcript variants, though the full-length nature of some of these variants has not been determined. [provided by RefSeq, Apr 2013]

**Accessions** — [HGNC:1968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1968) · Entrez [1130](https://www.ncbi.nlm.nih.gov/gene/1130) · UniProt [Q99698](https://www.uniprot.org/uniprotkb/Q99698) · Ensembl [ENSG00000143669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143669)

## Data

Gene col 6788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6788); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6788]; `tensor/DDL_lfc|DDL_z.npy` [6788]; `embed/gene_vectors.npy` [6788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6788 or target_col == 6788). Every well: [[LYST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
