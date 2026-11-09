---
symbol: "RAB35"
type: "gene"
col: 3275
ensembl_id: "ENSG00000111737"
name: "RAB35, member RAS oncogene family"
location: "12q24.23"
module: 36
arm: "+"
pooled_cpm: 36.43
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# RAB35

*RAB35, member RAS oncogene family* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.70× (z +12.8, q 5e-35, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.630× (z -10.8, q 2e-24, down in 24 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.681× (z -4.9, q 1e-04, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (AsPC-1 0.0730×, SW480 0.222×, LS 180 0.149×, NCI-H2030 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 0.308×, AsPC-1 0.396×, LOX-IMVI 0.420×, LoVo 0.461×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Panc 03.27 0.157×, RKO 0.298×, LOX-IMVI 0.385×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.340×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRK]] (+0.62, fdr 2e-05), [[ADRM1]] (+0.59, fdr 1e-05), [[GATAD2A]] (+0.59, fdr 1e-05); moves opposite to [[PREPL]] (-0.57, fdr 1e-05), [[CISD2]] (-0.53, fdr 4e-05), [[HMGN1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPHB4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +12.8 | 5e-35 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +11.9 | 5e-30 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +10.5 | 1e-23 | 38/48 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +5.2 | 3e-05 | 21/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +5.1 | 4e-05 | 20/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +4.8 | 1e-04 | 23/48 (C-33 A, SW480, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **1.23×** | +4.8 | 1e-04 | 20/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +4.7 | 2e-04 | 16/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +4.6 | 2e-04 | 18/48 (SW480, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 3e-04 | 17/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.001 | 0/48 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.13× | +4.2 | 0.001 | 16/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 18/47 (A549, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | 1.20× | +4.1 | 0.002 | 16/47 (SW480, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.003 | 11/46 (SHP-77, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.014 | 10/47 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.014 | 14/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.5 | 0.015 | 5/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.026 | 17/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.042 | 6/48 (MIA PaCa-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.14× | +3.0 | 0.061 | 11/47 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.088 | 8/48 (COLO 205, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (AsPC-1 0.0730×, SW480 0.222×, LS 180 0.149×, NCI-H2030 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 0.308×, AsPC-1 0.396×, LOX-IMVI 0.420×, LoVo 0.461×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Panc 03.27 0.157×, RKO 0.298×, LOX-IMVI 0.385×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.340×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -10.8 | 2e-24 | 24/38 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.741×** | -7.3 | 9e-11 | 28/46 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -5.1 | 5e-05 | 17/48 (NCI-H23, SK-MEL-2, …) | rises with dose | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.818×** | -4.9 | 1e-04 | 19/48 (hTERT-HPNE, SK-MEL-2, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -4.9 | 1e-04 | 20/47 (HCT15, A498, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -4.3 | 0.002 | 17/48 (A498, SHP-77, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.828×** | -4.3 | 0.002 | 18/43 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.869× | -3.3 | 0.067 | 14/47 (A-172, AsPC-1, …) | top dose only |  |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | **0.830×** | -3.2 | 0.076 | 9/48 (NCI-H661, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.895× | -3.2 | 0.083 | 8/48 (NCI-H23, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.901× | -3.1 | 0.088 | 5/48 (AsPC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.881× | -3.1 | 0.088 | 10/47 (SW 1271, C32, …) | two highest doses | low cells (technical?) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.882× | -3.1 | 0.088 | 12/48 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 31.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.04× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -18.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 39.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 47.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0730× (z -25.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 49.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.10× (z +9.7) | — |
| [[A-172 (line)]] | wt | 43.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.340× (z -10.3) |
| [[A-427 (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -12.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRK]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[ADRM1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[GATAD2A]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RRP7A]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ARL16]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[RIC8A]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TUBB6]] | +0.53 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CCM2]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[TRAPPC10]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[MEF2B]] | +0.53 | +0.37 / +0.53 | both halves | 8e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PREPL]] | -0.57 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[CISD2]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[HMGN1]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[EPHX2]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CDC73]] | -0.50 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[MATR3]] | -0.50 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[NDUFV2]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ARHGAP12]] | -0.50 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ATG3]] | -0.49 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PEX2]] | -0.49 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[NDUFA5]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TMEM106B]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB4]] | B | EPHB4 activity raises RAB35's level | compounds that target EPHB4: 2 of 3 lower it (NG25, NVP-BHG712) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-15.6, -6.9); signed map (-22.1, -25.7). **Vector** length 90.5, 18.5% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +11.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +12.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -5.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB35, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:120,095,099-120,117,502 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H-ray |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 6 pathways, smallest: TBC/RABGAPs; RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15286](https://www.uniprot.org/uniprotkb/Q15286) (Ras-related protein Rab-35):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB35 is involved in the process of endocytosis and is an essential rate-limiting regulator of the fast recycling …

**Summary**, from NCBI Gene [11021](https://www.ncbi.nlm.nih.gov/gene/11021):

> Enables G protein activity and anion binding activity. Involved in several processes, including endosomal transport; plasma membrane to endosome transport; and protein localization to endosome. Located in several cellular components, including clathrin-coated endocytic vesicle; clathrin-coated pit; and intercellular bridge. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9774) · Entrez [11021](https://www.ncbi.nlm.nih.gov/gene/11021) · UniProt [Q15286](https://www.uniprot.org/uniprotkb/Q15286) · Ensembl [ENSG00000111737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111737)

## Data

Gene col 3275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3275); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3275]; `tensor/DDL_lfc|DDL_z.npy` [3275]; `embed/gene_vectors.npy` [3275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3275 or target_col == 3275). Every well: [[RAB35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
