---
symbol: "SND1"
type: "gene"
col: 12357
ensembl_id: "ENSG00000197157"
name: "staphylococcal nuclease and tudor domain containing 1"
location: "7q32.1"
module: 42
arm: "+"
pooled_cpm: 471.1
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SND1

*staphylococcal nuclease and tudor domain containing 1* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.97× (z +12.0, q 3e-30, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.416× (z -14.9, q 0e+00, down in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.583× (z -9.5, q 4e-19, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED3]] (+0.70, fdr 7e-06), [[COG5]] (+0.69, fdr 1e-05), [[PDIA5]] (+0.67, fdr 1e-05); moves opposite to [[UBXN2A]] (-0.67, fdr 2e-05), [[ZNF253]] (-0.63, fdr 2e-05), [[C3orf38]] (-0.59, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +12.0 | 3e-30 | 48/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +10.7 | 3e-24 | 48/48 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +9.4 | 8e-19 | 47/48 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +9.2 | 6e-18 | 48/48 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +6.7 | 2e-09 | 45/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.2 | 2e-05 | 35/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +4.9 | 7e-05 | 37/49 (NCI-H2347, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.4 | 6e-04 | 22/48 (HS-578T, SW1417, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.001 | 38/48 (LOX-IMVI, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.1 | 0.002 | 24/47 (COLO 205, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.002 | 40/48 (NCI-H2347, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.009 | 33/48 (SW 900, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.013 | 37/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.15× | +3.2 | 0.046 | 5/49 (RKO, BT-474, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.046 | 24/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.046 | 20/49 (HOP62, C32, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.20× | +3.2 | 0.046 | 22/48 (SNU-423, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.416×** | -14.9 | 0e+00 | 47/47 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.583×** | -9.5 | 4e-19 | 47/48 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -9.3 | 3e-18 | 41/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.601×** | -9.0 | 3e-17 | 48/49 (NCI-H23, C32, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -8.6 | 9e-16 | 40/44 (NCI-H23, SW48, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -8.4 | 6e-15 | 40/45 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.727×** | -5.4 | 5e-06 | 29/48 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.820×** | -4.7 | 2e-04 | 32/48 (AsPC-1, CHP-212, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.772×** | -4.6 | 3e-04 | 35/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.814×** | -3.6 | 0.016 | 28/48 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -3.4 | 0.029 | 14/48 (HOP62, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.030 | 27/47 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.3 | 0.045 | 15/48 (C32, RKO, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.1 | 0.069 | 23/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.877× | -3.1 | 0.069 | 13/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.844× | -3.0 | 0.089 | 20/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 441 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -15.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -10.9) |
| [[HOP62 (line)]] | alt | 389 | 4 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -14.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.488× (z -10.9) |
| [[HS-578T (line)]] | alt | 456 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 685 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -19.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 463 | 3 (1 ⚠) | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -13.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.487× (z -10.6) |
| [[A-427 (line)]] | wt | 300 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -13.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 779 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -14.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -13.5) |
| [[A549 (line)]] | wt | 380 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -16.6) |
| [[AsPC-1 (line)]] | alt | 503 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.06× (z +10.1) | [[Radotinib (drug)]] 5 µM 0.553× (z -11.1) |
| [[BT-474 (line)]] | alt | 377 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[C-33 A (line)]] | alt | 442 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.344× (z -13.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 385 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -10.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 499 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.416× (z -10.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.514× (z -8.6) |
| [[LoVo (line)]] | wt | 878 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -14.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 532 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.88× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -9.6) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.450× (z -8.9) |
| [[A-172 (line)]] | wt | 215 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +13.1) | [[Harringtonine (drug)]] 5 µM 0.377× (z -12.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 539 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -12.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.436× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 288 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.517× (z -9.2) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 332 | 2 (1 ⚠) | 3 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.19× (z +11.1) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 3.30× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -12.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.519× (z -9.3) |
| [[PANC-1 (line)]] | alt | 393 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.429× (z -10.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.9) |
| [[SHP-77 (line)]] | alt | 350 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -10.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.562× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 611 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.469× (z -9.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -8.9) |
| [[SW1417 (line)]] | alt | 704 | 1 (1 ⚠) | 4 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.99× (z +9.1) ⚠ unreliable plate only | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.238× (z -18.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.492× (z -9.4) |
| [[C32 (line)]] | wt | 954 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.411× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 303 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -8.7) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 385 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.311× (z -15.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.437× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 414 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.453× (z -9.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 700 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -8.9) |
| [[H4 (line)]] | wt | 546 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 365 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.7) | — |
| [[RKO (line)]] | wt | 806 | 2 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.21× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.311× (z -14.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 364 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +14.2) | — |
| [[SW 900 (line)]] | alt | 504 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.386× (z -13.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 286 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.86× (z +9.1) ⚠ unreliable plate only | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.401× (z -12.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 501 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 387 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.80× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.412× (z -12.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 415 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -13.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 543 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 349 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.488× (z -9.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 552 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 288 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.341× (z -12.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 576 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.307× (z -12.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 414 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -8.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 487 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.483× (z -9.0) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 332 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 459 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 691 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 339 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED3]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[COG5]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PDIA5]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 | same gene group |
| [[HM13]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[MANF]] | +0.67 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[P4HB]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 | STRING 528 |
| [[ST6GALNAC4]] | +0.66 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SSR3]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CALU]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[HSPA5]] | +0.65 | +0.63 / +0.57 | both halves | 9e-06 | STRING 486 |
| [[TMED9]] | +0.64 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[SEC61A1]] | +0.64 | +0.75 / +0.54 | both halves | 1e-05 | STRING 778 |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN2A]] | -0.67 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[ZNF253]] | -0.63 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[C3orf38]] | -0.59 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PLEKHF2]] | -0.59 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[CASD1]] | -0.58 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MIR181A2HG]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[WAC-AS1]] | -0.58 | -0.52 / -0.26 | both halves | 3e-04 |  |
| [[RBM48]] | -0.58 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[TSTD3]] | -0.58 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[WBP4]] | -0.57 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ZNF85]] | -0.56 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[RNF146]] | -0.55 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, -32.3); signed map (-53.0, 8.6). **Vector** length 143, 59.6% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.52 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.51 to 9); *IRE1alpha activates chaperones* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.7 | +9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.6 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.7 | +9.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.7 | +10.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +6.2 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.2 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -13.3 | -14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.5 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.8 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -7.1 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.3 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | staphylococcal nuclease and tudor domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:127,652,194-128,092,609 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TDRD11, p100, TSN |
| Gene groups (HGNC) | Tudor domain containing; MicroRNA protein coding host genes; RISC loading complex subunits |
| Reactome | 3 pathways, smallest: Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling; Diseases of signal transduction by growth factor receptors and second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7KZF4](https://www.uniprot.org/uniprotkb/Q7KZF4) (Staphylococcal nuclease domain-containing protein 1):

> Endonuclease that mediates miRNA decay of both protein-free and AGO2-loaded miRNAs. As part of its function in miRNA decay, regulates mRNAs involved in G1-to-S phase transition. Functions as a bridging factor between STAT6 and the basal transcription factor. Plays a role in PIM1 regulation of MYB activity. Functions as a transcriptional coactivator for STAT5 (By similarity).; (Microbial infection) Functions as a transcriptional coactivator for the Epstein-Barr virus nuclear antigen 2 (EBNA2).; …

**Summary**, from NCBI Gene [27044](https://www.ncbi.nlm.nih.gov/gene/27044):

> This gene encodes a transcriptional co-activator that interacts with the acidic domain of Epstein-Barr virus nuclear antigen 2 (EBNA 2), a transcriptional activator that is required for B-lymphocyte transformation. Other transcription factors that interact with this protein are signal transducers and activators of transcription, STATs. This protein is also thought to be essential for normal cell growth. A similar protein in mammals and other organisms is a component of the RNA-induced silencing …

**Accessions** — [HGNC:30646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30646) · Entrez [27044](https://www.ncbi.nlm.nih.gov/gene/27044) · UniProt [Q7KZF4](https://www.uniprot.org/uniprotkb/Q7KZF4) · Ensembl [ENSG00000197157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197157)

## Data

Gene col 12357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12357); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12357]; `tensor/DDL_lfc|DDL_z.npy` [12357]; `embed/gene_vectors.npy` [12357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12357 or target_col == 12357). Every well: [[SND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
