---
symbol: "ASAP1"
type: "gene"
col: 7715
ensembl_id: "ENSG00000153317"
name: "ArfGAP with SH3 domain, ankyrin repeat and PH domain 1"
location: "8q24.21-q24.22"
module: 116
arm: "+"
pooled_cpm: 433.28
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# ASAP1

*ArfGAP with SH3 domain, ankyrin repeat and PH domain 1* — 8q24.21-q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +12.1, q 5e-31, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.698× (z -7.3, q 2e-10, down in 36 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.786× (z -7.1, q 3e-10, down in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (J82 0.384×, SNU-423 0.459×, A549 0.491×, NCI-H1792 0.578×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (SNU-1 0.191×, A-427 0.306×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-427 0.274×, SNU-1 0.316×; ⚠ cell-cycle shift, explains ~63% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.495×, C-33 A 0.627×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.606×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASAP2]] (+0.65, fdr 7e-06), [[DOCK1]] (+0.65, fdr 7e-06), [[EGFR]] (+0.64, fdr 1e-05); moves opposite to [[MAPKAPK5-AS1]] (-0.59, fdr 1e-05), [[DUSP11]] (-0.58, fdr 1e-05), [[GOLPH3L]] (-0.57, fdr 9e-06).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MAPKAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +12.1 | 5e-31 | 33/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +7.7 | 4e-12 | 30/48 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.3 | 4e-11 | 32/48 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +7.3 | 4e-11 | 35/49 (C32, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.4 | 2e-08 | 32/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 2e-07 | 30/48 (HepG2/C3A, BT-474, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.9 | 3e-07 | 29/48 (HepG2/C3A, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 31/48 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.8 | 1e-04 | 27/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 2e-04 | 29/48 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.24×** | +4.5 | 3e-04 | 26/48 (HS-578T, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.5 | 3e-04 | 28/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.003 | 29/47 (C32, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.005 | 29/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.016 | 22/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.018 | 26/48 (SW480, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7715.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (J82 0.384×, SNU-423 0.459×, A549 0.491×, NCI-H1792 0.578×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (SNU-1 0.191×, A-427 0.306×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-427 0.274×, SNU-1 0.316×; ⚠ cell-cycle shift, explains ~63% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.495×, C-33 A 0.627×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.606×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -7.3 | 2e-10 | 36/47 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -7.1 | 3e-10 | 27/49 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.723×** | -6.8 | 2e-09 | 34/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -5.5 | 4e-06 | 26/44 (SW48, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.815×** | -4.3 | 0.002 | 27/49 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.829×** | -3.9 | 0.008 | 24/48 (SW 900, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -3.8 | 0.012 | 21/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.778×** | -3.8 | 0.012 | 30/48 (Hs 766T, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.849× | -3.4 | 0.038 | 20/48 (HOP62, SW 1088, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.872× | -3.3 | 0.060 | 18/48 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.814× | -3.1 | 0.11 | 21/48 (A549, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 396 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +26.4) | — |
| [[NCI-H460 (line)]] | wt | 222 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +22.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 698 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.0) | [[Adagrasib (drug)]] 0.05 µM 0.665× (z -16.2) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 315 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -15.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 323 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +20.8) | — |
| [[COLO 205 (line)]] | alt | 125 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +35.5) | — |
| [[HS-578T (line)]] | alt | 636 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -9.4) |
| [[SNU-1 (line)]] | wt | 362 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -21.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.495× (z -13.1) |
| [[SW480 (line)]] | alt | 327 | 2 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.70× (z +8.6) | [[Binimetinib (drug)]] 0.5 µM 0.606× (z -9.9) |
| [[H4 (line)]] | wt | 297 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.8) | — |
| [[HepG2_C3A (line)]] | wt | 358 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.92× (z +14.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.484× (z -9.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 489 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.4) | — |
| [[J82 (line)]] | alt | 977 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -19.3) |
| [[SW1417 (line)]] | alt | 486 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.521× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 243 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -16.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[AsPC-1 (line)]] | alt | 655 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 183 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 198 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 190 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.9) | — |
| [[RKO (line)]] | wt | 1,153 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.137× (z -23.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 526 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.524× (z -9.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 520 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -16.5) |
| [[A498 (line)]] | wt | 576 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 422 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.627× (z -10.6) |
| [[C32 (line)]] | wt | 562 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.561× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 559 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +15.4) | — |
| [[hTERT-HPNE (line)]] | wt | 660 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 169 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 557 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.440× (z -10.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 277 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 557 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -10.3) |
| [[SW48 (line)]] | wt | 253 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -15.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 594 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 400 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -9.8) |
| [[LS 180 (line)]] | wt | 182 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 335 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 587 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 475 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 447 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 418 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.426× (z -10.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 432 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 325 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 371 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 351 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 477 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 418 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAP2]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 | same gene group; STRING 907 |
| [[DOCK1]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 | same gene group |
| [[EGFR]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MIR4435-2HG]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ETS1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[DIAPH2]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RASAL2]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[DOCK5]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 | same gene group |
| [[PALM2AKAP2]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[LDLRAD3]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[BICD1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5-AS1]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[DUSP11]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[GOLPH3L]] | -0.57 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[PRMT9]] | -0.56 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[MBIP]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[IST1]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[APTR]] | -0.54 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[ZFPL1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[COPS4]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[FAM151B-DT]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.54 | -0.41 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity weakens ASAP1's drug response | lines that do not express AGR2 (32) vs lines expressing it (17) | the lines without AGR2 respond 0.97× as strongly (z diff -0.15); strongest at Idarubicin (hydrochloride) 5 µM: 0.73x vs 1.15x (z diff -8.0) | 0.006 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1; target measured in part of the lines; both ways; artifact flags |
| [[AGR2]] | B | AGR2 activity lowers ASAP1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.57× higher at baseline in the lines without AGR2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[ETS1]] | B | ETS1 activity raises ASAP1's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without ETS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[EVC]] | B | EVC activity raises ASAP1's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.53× lower at baseline in the lines without EVC | 0.044 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[BCAR3]] | B | BCAR3 activity raises ASAP1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without BCAR3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[HEG1]] | B | HEG1 activity raises ASAP1's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without HEG1 | 0.071 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPKAP1]] | C | ASAP1's natural level weakens MAPKAP1's drug response | ASAP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.07; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 10.3); signed map (12.0, 40.7). **Vector** length 139, 49.1% of its response variance represented; |z| ≥ 3 in 1,589 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Peretinoin (drug)]] 5 µM |  | +5.2 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +4.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.1 | +2.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +4.0 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.5 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -5.7 | -6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.2 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with SH3 domain, ankyrin repeat and PH domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.21-q24.22 — chr8:130,052,104-130,443,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP, KIAA1249, ZG14P, CENTB4; previously DDEF1 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing; SH3 domain containing |
| Reactome | 5 pathways, smallest: VxPx cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULH1](https://www.uniprot.org/uniprotkb/Q9ULH1) (Arf-GAP with SH3 domain, ANK repeat and PH domain-containing protein 1):

> Possesses phosphatidylinositol 4,5-bisphosphate-dependent GTPase-activating protein activity for ARF1 (ADP ribosylation factor 1) and ARF5 and a lesser activity towards ARF6. May coordinate membrane trafficking with cell growth or actin cytoskeleton remodeling by binding to both SRC and PIP2. May function as a signal transduction protein involved in the differentiation of fibroblasts into adipocytes and possibly other cell types. Part of the ciliary targeting complex containing Rab11, ASAP1, …

**Summary**, from NCBI Gene [50807](https://www.ncbi.nlm.nih.gov/gene/50807):

> This gene encodes an ADP-ribosylation factor (ARF) GTPase-activating protein. The GTPase-activating activity is stimulated by phosphatidylinositol 4,5-biphosphate (PIP2), and is greater towards ARF1 and ARF5, and lesser for ARF6. This gene maybe involved in regulation of membrane trafficking and cytoskeleton remodeling. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:2720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2720) · Entrez [50807](https://www.ncbi.nlm.nih.gov/gene/50807) · UniProt [Q9ULH1](https://www.uniprot.org/uniprotkb/Q9ULH1) · Ensembl [ENSG00000153317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153317)

## Data

Gene col 7715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7715); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7715]; `tensor/DDL_lfc|DDL_z.npy` [7715]; `embed/gene_vectors.npy` [7715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7715 or target_col == 7715). Every well: [[ASAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
