---
symbol: "FBXO28"
type: "gene"
col: 6797
ensembl_id: "ENSG00000143756"
name: "F-box protein 28"
location: "1q42.11"
module: 114
arm: "+"
pooled_cpm: 97.39
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# FBXO28

*F-box protein 28* — 1q42.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.07× (z +7.8, q 3e-12, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.407× (z -18.4, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 0.630× (z -4.9, q 5e-05, down in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (AsPC-1 0.0701×, C32 0.140×, SW 900 0.228×, PANC-1 0.274×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (CFPAC-1 0.214×, NCI-H1792 0.239×, PANC-1 0.285×, SW 900 0.257×, …; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.0657×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH1]] (+0.81, fdr 7e-06), [[ZNF791]] (+0.74, fdr 7e-06), [[PCF11-AS1]] (+0.71, fdr 1e-05); moves opposite to [[LBR]] (-0.63, fdr 1e-05), [[RBBP7]] (-0.61, fdr 1e-05), [[CNN3]] (-0.61, fdr 7e-06).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +7.8 | 3e-12 | 36/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.5 | 2e-08 | 31/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +6.4 | 4e-08 | 31/48 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +6.3 | 4e-08 | 27/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.002 | 27/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.3 | 0.002 | 19/48 (AsPC-1, HT-29, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.2 | 0.002 | 24/48 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.15× | +4.1 | 0.003 | 20/48 (HT-29, LS 180, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.054 | 10/48 (SNU-1, SW1417, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.11 | 10/48 (SW1417, HS-578T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.11 | 15/48 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.11× | +3.1 | 0.11 | 7/48 (CFPAC-1, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6797.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (AsPC-1 0.0701×, C32 0.140×, SW 900 0.228×, PANC-1 0.274×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (CFPAC-1 0.214×, NCI-H1792 0.239×, PANC-1 0.285×, SW 900 0.257×, …; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.0657×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.407×** | -18.4 | 0e+00 | 47/49 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -18.2 | 0e+00 | 43/44 (AsPC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.438×** | -15.6 | 0e+00 | 39/45 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.644×** | -9.0 | 3e-17 | 41/48 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -8.5 | 3e-15 | 34/47 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.747×** | -6.0 | 2e-07 | 30/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.696×** | -5.2 | 1e-05 | 29/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.630×** | -4.9 | 5e-05 | 27/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.786×** | -4.9 | 5e-05 | 26/48 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.8 | 8e-05 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -4.8 | 8e-05 | 21/48 (SW480, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.820×** | -4.1 | 0.002 | 25/48 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.832×** | -3.5 | 0.022 | 17/48 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.862× | -3.0 | 0.094 | 18/49 (SW 1088, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 125 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -16.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 127 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -17.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 90.1 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.71× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -13.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 125 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0701× (z -29.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -13.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 103 | 0 | 4 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -17.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -14.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 80.2 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0657× (z -18.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 114 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 59.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -13.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 87.7 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.57× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 125 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.77× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 131 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -14.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -15.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -16.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -17.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 84.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -15.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 86.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -20.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.56× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -10.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 76.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.17× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 94.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 82.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 69.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 99.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -12.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -10.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[CHP-212 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -17.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 86.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH1]] | +0.81 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.74 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PCF11-AS1]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ZSWIM3]] | +0.70 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[HSCB]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[C19orf25]] | +0.68 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[TEFM]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZNF200]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[BRAP]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ZNF721]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ZNF506]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LBR]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[CNN3]] | -0.61 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[SSX2IP]] | -0.61 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[NONO]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.60 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.58 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PSIP1]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.56 | -0.46 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FBXO28's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF234]] | C | ZNF234 activity raises FBXO28's level | lines that do not express ZNF234 (4) vs lines expressing it (46) | 1.40× lower at baseline in the lines without ZNF234 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF222, ZNF551, ZNF264 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.3, 4.3); signed map (-4.3, -11.5). **Vector** length 124, 37.3% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.8 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.5 | +4.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +3.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.8 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -15.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -18.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -18.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.1 | -4.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.9 | -2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.11 — chr1:224,114,111-224,162,047 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10766, KIAA0483, Fbx28, CENP-30 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVF7](https://www.uniprot.org/uniprotkb/Q9NVF7) (F-box only protein 28):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex, promoting ubiquitination and proteasomal degradation of specific target proteins including TOP2A, RAB27A or itself. Regulates topoisomerase IIalpha/TOP2A decatenation activity and plays an important role in maintaining genomic stability. Plays a role in lipid metabolism and inflammation through the ubiquitinated degradation of RAB27A (By similarity). Strongly regulates beta-cell survival …

**Summary**, from NCBI Gene [23219](https://www.ncbi.nlm.nih.gov/gene/23219):

> Members of the F-box protein family, such as FBXO28, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29046) · Entrez [23219](https://www.ncbi.nlm.nih.gov/gene/23219) · UniProt [Q9NVF7](https://www.uniprot.org/uniprotkb/Q9NVF7) · Ensembl [ENSG00000143756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143756)

## Data

Gene col 6797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6797); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6797]; `tensor/DDL_lfc|DDL_z.npy` [6797]; `embed/gene_vectors.npy` [6797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6797 or target_col == 6797). Every well: [[FBXO28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
