---
symbol: "BRMS1L"
type: "gene"
col: 2043
ensembl_id: "ENSG00000100916"
name: "BRMS1 like transcriptional repressor"
location: "14q13.2"
module: 62
arm: "+"
pooled_cpm: 25.45
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# BRMS1L

*BRMS1 like transcriptional repressor* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.96× (z +37.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.708× (z -8.3, q 5e-14, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.237×, C-33 A 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0902×, NCI-H1792 0.109×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (AN3 CA 0.0735×); [[Brimonidine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0858×); [[Allantoin (drug)]] 0.5 µM in 1 line (COLO 205 0.108×).
> Its strongest partners by |cos| (50 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 50 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAIM]] (+0.56, fdr 0.001, ⚠ one half only (not replicated)), [[REV3L]] (+0.55, fdr 5e-05), [[SLC25A21]] (+0.55, fdr 0.001, ⚠ not reproduced), [[FAS]] (+0.54, fdr 2e-04), [[TP53I3]] (+0.54, fdr 1e-04); moves opposite to [[LMCD1-AS1]] (-0.52, fdr 0.001, ⚠ not reproduced), [[KCTD20]] (-0.50, fdr 3e-04), [[HEMK1]] (-0.47, fdr 9e-04, ⚠ not reproduced), [[PGK1]] (-0.46, fdr 3e-04), [[FGGY]] (-0.46, fdr 6e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +37.1 | 0e+00 | 48/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +18.8 | 0e+00 | 34/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +18.4 | 0e+00 | 42/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +15.8 | 0e+00 | 37/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +13.8 | 3e-41 | 39/48 (A549, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.71×** | +12.4 | 3e-33 | 34/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +9.9 | 4e-21 | 32/48 (A-172, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +9.8 | 1e-20 | 31/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +9.5 | 1e-19 | 24/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.45×** | +8.9 | 3e-17 | 30/47 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +8.7 | 1e-16 | 28/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.33×** | +6.8 | 4e-10 | 26/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.32×** | +6.7 | 1e-09 | 21/43 (NCI-H23, J82, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +6.6 | 1e-09 | 21/47 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.29×** | +5.8 | 2e-07 | 19/37 (CFPAC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +5.4 | 2e-06 | 23/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +4.5 | 2e-04 | 11/47 (MIA PaCa-2, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.002 | 4/47 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.9 | 0.002 | 12/48 (A549, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.15× | +3.4 | 0.015 | 7/47 (SNU-423, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.016 | 6/47 (SNU-423, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2043.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.237×, C-33 A 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0902×, NCI-H1792 0.109×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (AN3 CA 0.0735×); [[Brimonidine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0858×); [[Allantoin (drug)]] 0.5 µM in 1 line (COLO 205 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -8.3 | 5e-14 | 26/47 (SW480, C-33 A, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.829×** | -4.3 | 0.004 | 14/47 (HS-578T, SW1417, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.851× | -3.9 | 0.016 | 15/48 (COLO 205, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.846× | -3.9 | 0.016 | 6/47 (C-33 A, KATO III, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.848× | -3.7 | 0.029 | 14/47 (HCT15, HOP62, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.753×** | -3.6 | 0.032 | 12/39 (SK-MEL-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.862× | -3.5 | 0.032 | 14/47 (LS 180, Hs 766T, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.906× | -3.3 | 0.060 | 3/48 (HCT15, C-33 A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.086 | 8/47 (SNU-423, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 0.871× | -3.2 | 0.086 | 10/47 (BT-474, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | 0.879× | -3.1 | 0.11 | 6/46 (LOX-IMVI, SW 900, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.7 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +22.1) | — |
| [[A549 (line)]] | wt | 24.7 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.2) | — |
| [[SW480 (line)]] | alt | 28.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +19.8) | — |
| [[C32 (line)]] | wt | 22.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 20.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 15.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +14.6) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.109× (z -8.8) ⚠ toxic |
| [[RKO (line)]] | wt | 28.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +14.6) | — |
| [[A-172 (line)]] | wt | 13.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +13.7) | — |
| [[A-427 (line)]] | wt | 36.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 14.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +19.3) | — |
| [[AN3 CA (line)]] | alt | 34.1 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0735× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 15.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 10.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +8.6) | [[Allantoin (drug)]] 0.5 µM 0.108× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 21.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +15.6) | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.1) | — |
| [[J82 (line)]] | alt | 28.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.1) | — |
| [[LoVo (line)]] | wt | 19.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +15.8) | — |
| [[NCI-H23 (line)]] | alt | 42.5 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H2347 (line)]] | alt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.8) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0902× (z -9.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 20.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 20.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +14.0) | — |
| [[SW48 (line)]] | wt | 39.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 8.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 48.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +11.2) | — |
| [[KATO III (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 44.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 46.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 44 of them with an alert (⚠; 44 not replicated); shown: the 12 strongest and the 7 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | +0.56 | +0.52 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[REV3L]] | +0.55 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[SLC25A21]] | +0.55 | +0.50 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[FAS]] | +0.54 | +0.39 / +0.29 | both halves | 2e-04 |  |
| [[TP53I3]] | +0.54 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[SESN1]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[HOXC9]] | +0.53 | +0.36 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[EFCAB5]] | +0.53 | +0.59 / +0.05 | ⚠ one half (not replicated) | 0.005 |  |
| [[BORCS7]] | +0.52 | +0.40 / +0.29 | both halves | 3e-04 |  |
| [[TRAF3IP2-AS1]] | +0.52 | +0.44 / +0.13 | ⚠ not reproduced | 0.002 |  |
| [[TIAL1]] | +0.52 | +0.17 / +0.40 | ⚠ not reproduced | 0.001 |  |
| [[HOXB7]] | +0.52 | +0.36 / +0.15 | ⚠ not reproduced | 0.001 |  |
| [[SNX5]] | +0.51 | +0.46 / +0.23 | both halves | 5e-04 |  |
| [[INKA2]] | +0.51 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[TP53]] | +0.51 | +0.49 / +0.22 | both halves | 6e-04 | pathway: HALLMARK_E2F_TARGETS |
| [[ACTA2]] | +0.51 | +0.42 / +0.26 | both halves | 4e-04 |  |
| [[HOXC6]] | +0.50 | +0.41 / +0.22 | both halves | 6e-04 |  |
| [[DOCK8]] | +0.50 | +0.35 / +0.34 | both halves | 1e-04 |  |
| [[MDM2]] | +0.50 | +0.32 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMCD1-AS1]] | -0.52 | -0.16 / -0.32 | ⚠ not reproduced | 0.001 |  |
| [[KCTD20]] | -0.50 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[HEMK1]] | -0.47 | -0.40 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[PGK1]] | -0.46 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[NCAM1]] | -0.46 | -0.36 / -0.07 | ⚠ not reproduced | 0.004 |  |
| [[FGGY]] | -0.46 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[INIP]] | -0.45 | -0.29 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[TECPR1]] | -0.45 | -0.31 / -0.04 | ⚠ not reproduced | 0.005 |  |
| [[CMIP]] | -0.45 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[SLC39A3]] | -0.45 | -0.19 / -0.18 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 1, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens BRMS1L's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.69× as strongly (z diff +1.53); strongest at Topotecan (hydrochloride) 5 µM: 1.34x vs 2.44x (z diff +3.8) | 0.012 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers BRMS1L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MDM2]] | C | MDM2's natural level strengthens BRMS1L's drug response | MDM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.27; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | BRMS1L's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | BRMS1L's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.024 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.2, 34.4); signed map (39.8, -22.3). **Vector** length 86.8, 18.1% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +37.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +18.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +13.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +15.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +4.5 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +9.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +9.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -4.5 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.4 | +8.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.2 | +6.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | BRMS1 like transcriptional repressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:35,826,338-35,932,325 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11296, FLJ39177, p40; previously BRMS1 |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5PSV4](https://www.uniprot.org/uniprotkb/Q5PSV4) (Breast cancer metastasis-suppressor 1-like protein):

> Involved in the histone deacetylase (HDAC1)-dependent transcriptional repression activity. When overexpressed in lung cancer cell line that lacks p53/TP53 expression, inhibits cell growth.

**Summary**, from NCBI Gene [84312](https://www.ncbi.nlm.nih.gov/gene/84312):

> The protein encoded by this gene shows sequence similarity to the human breast carcinoma metastasis suppressor (BRMS1) protein and the mammalian Sds3 (suppressor of defective silencing 3) proteins. This protein is a component of the mSin3a family of histone deacetylase complexes (HDAC). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20512) · Entrez [84312](https://www.ncbi.nlm.nih.gov/gene/84312) · UniProt [Q5PSV4](https://www.uniprot.org/uniprotkb/Q5PSV4) · Ensembl [ENSG00000100916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100916)

## Data

Gene col 2043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2043); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2043]; `tensor/DDL_lfc|DDL_z.npy` [2043]; `embed/gene_vectors.npy` [2043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2043 or target_col == 2043). Every well: [[BRMS1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRMS1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
