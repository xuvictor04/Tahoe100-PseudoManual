---
symbol: "AZI2"
type: "gene"
col: 8704
ensembl_id: "ENSG00000163512"
name: "5-azacytidine induced 2"
location: "3p24.1"
module: 28
arm: "+"
pooled_cpm: 58.54
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AZI2

*5-azacytidine induced 2* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +12.7, q 6e-34, up in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.65× (z +11.1, q 2e-26, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.452× (z -17.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMPCB]] (+0.59, fdr 2e-05), [[ZFP37]] (+0.59, fdr 2e-05), [[COPS5]] (+0.58, fdr 1e-05); moves opposite to [[GNB1L]] (-0.58, fdr 1e-05), [[TBC1D4]] (-0.57, fdr 1e-05), [[LINC02595]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +12.7 | 6e-34 | 33/48 (NCI-H2347, AsPC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +11.1 | 2e-26 | 41/48 (PANC-1, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.9 | 5e-21 | 34/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +9.1 | 9e-18 | 38/48 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +9.1 | 2e-17 | 38/49 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +8.7 | 4e-16 | 34/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +7.1 | 1e-10 | 30/48 (NCI-H2347, COLO 205, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +4.6 | 2e-04 | 19/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +4.4 | 6e-04 | 24/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.15× | +4.3 | 8e-04 | 15/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.2 | 0.001 | 20/48 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 15/49 (LOX-IMVI, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.17× | +3.5 | 0.019 | 18/48 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.5 | 0.019 | 16/44 (A-427, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.025 | 14/48 (NCI-H460, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.097 | 15/48 (HOP62, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -17.7 | 0e+00 | 47/48 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.471×** | -16.8 | 0e+00 | 47/48 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.597×** | -11.5 | 2e-28 | 44/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.790×** | -7.4 | 1e-11 | 25/49 (A549, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -6.5 | 1e-08 | 27/48 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.754×** | -6.3 | 3e-08 | 34/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.792×** | -5.0 | 5e-05 | 22/48 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -4.9 | 8e-05 | 23/48 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -4.9 | 8e-05 | 23/49 (A549, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.803×** | -4.7 | 1e-04 | 20/50 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.866× | -4.5 | 3e-04 | 20/49 (A549, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | 0.842× | -3.7 | 0.010 | 17/43 (BT-474, A549, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.848× | -3.7 | 0.010 | 18/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.864× | -3.3 | 0.044 | 14/49 (A549, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.906× | -3.1 | 0.074 | 16/48 (A-172, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 97.2 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.442× (z -11.9) |
| [[A-172 (line)]] | wt | 70.8 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -12.3) |
| [[A549 (line)]] | wt | 95.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 83.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 72.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -12.6) |
| [[SNU-423 (line)]] | alt | 86.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -14.9) |
| [[SW480 (line)]] | alt | 56.1 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.82× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.471× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 46.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -13.2) |
| [[HOP62 (line)]] | alt | 92.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 53.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -10.1) |
| [[SW 900 (line)]] | alt | 58.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -11.6) |
| [[AN3 CA (line)]] | alt | 55.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.146× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 60.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.10× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 60.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -10.8) |
| [[LoVo (line)]] | wt | 39.1 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -8.6) |
| [[PANC-1 (line)]] | alt | 53.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 93.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.360× (z -10.4) |
| [[SHP-77 (line)]] | alt | 65.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.356× (z -9.8) |
| [[A-427 (line)]] | wt | 56.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[A498 (line)]] | wt | 33.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[C32 (line)]] | wt | 66.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[H4 (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 35.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 51.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 49.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.34× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW1417 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C-33 A (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMPCB]] | +0.59 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ZFP37]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[COPS5]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[AMZ2P1-1]] | +0.58 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[IFT74]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TRMT10B]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.57 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[USP47]] | +0.57 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ZNF226]] | +0.57 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CEBPD]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD49]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZNF227]] | +0.56 | +0.55 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.57 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[LINC02595]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[LSM4]] | -0.54 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[PKP4]] | -0.54 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[CD9]] | -0.54 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ACTN4]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[EIF5A]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[VKORC1L1]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NSD2]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[FANCA]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ARHGAP8]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AZI2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises AZI2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.0, 4.9); signed map (5.8, -22.2). **Vector** length 113, 31.8% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.0 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.6 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +9.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.1 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.9 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.5 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -1.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.0 | +0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | 5-azacytidine induced 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.1 — chr3:28,315,003-28,349,050 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAP1, FLJ21939, AZ2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6S1](https://www.uniprot.org/uniprotkb/Q9H6S1) (5-azacytidine-induced protein 2):

> Adapter protein which binds TBK1 and IKBKE playing a role in antiviral innate immunity. Activates serine/threonine-protein kinase TBK1 and facilitates its oligomerization. Enhances the phosphorylation of NF-kappa-B p65 subunit RELA by TBK1. Promotes TBK1-induced as well as TNF or PMA-induced activation of NF-kappa-B. Participates in IFNB promoter activation via TICAM1.

**Summary**, from NCBI Gene [64343](https://www.ncbi.nlm.nih.gov/gene/64343):

> AZI2, or NAP1, contributes to the activation of NFKB (see MIM 164011)-dependent gene expression by activating IKK-related kinases, such as NAK (TBK1; MIM 604834) (Fujita et al., 2003 [PubMed 14560022]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24002) · Entrez [64343](https://www.ncbi.nlm.nih.gov/gene/64343) · UniProt [Q9H6S1](https://www.uniprot.org/uniprotkb/Q9H6S1) · Ensembl [ENSG00000163512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163512)

## Data

Gene col 8704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8704); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8704]; `tensor/DDL_lfc|DDL_z.npy` [8704]; `embed/gene_vectors.npy` [8704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8704 or target_col == 8704). Every well: [[AZI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AZI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
