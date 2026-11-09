---
symbol: "KPNA3"
type: "gene"
col: 2266
ensembl_id: "ENSG00000102753"
name: "karyopherin subunit alpha 3"
location: "13q14.2"
module: 18
arm: "+"
pooled_cpm: 74.72
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# KPNA3

*karyopherin subunit alpha 3* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.06× (z +20.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.848× (z -6.5, q 3e-08, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.767× (z -3.9, q 0.014, down in 11 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.136×, SNU-1 0.373×, HEC-1-A 0.520×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.515×, HepG2/C3A 0.536×; ⚠ cell-cycle shift, explains ~70% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Alpelisib (drug)]] 5 µM in 1 line (HCT15 0.0817×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAP1GDS1]] (+0.71, fdr 7e-06), [[LARP1]] (+0.70, fdr 7e-06), [[VWA8]] (+0.67, fdr 7e-06); moves opposite to [[FAM117A]] (-0.54, fdr 3e-05), [[METTL25B]] (-0.54, fdr 6e-05), [[MXD1]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADAM8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +20.3 | 0e+00 | 45/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +16.7 | 0e+00 | 40/48 (SW480, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +15.9 | 0e+00 | 43/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.61×** | +13.3 | 2e-38 | 41/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +12.8 | 3e-35 | 40/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +11.9 | 7e-31 | 37/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +11.8 | 4e-30 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +11.5 | 1e-28 | 37/47 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +11.2 | 3e-27 | 41/49 (SW480, LS 180, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.47×** | +10.9 | 1e-25 | 35/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +10.0 | 5e-22 | 35/44 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +9.0 | 1e-17 | 29/48 (HEC-1-A, LS 180, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +8.1 | 3e-14 | 30/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +7.6 | 8e-13 | 36/49 (Hs 766T, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +7.6 | 9e-13 | 29/48 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +7.3 | 1e-11 | 21/48 (SW480, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +6.3 | 7e-09 | 27/49 (SW480, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.5 | 2e-04 | 13/49 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +4.4 | 2e-04 | 17/48 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.9 | 0.002 | 13/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2266.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.136×, SNU-1 0.373×, HEC-1-A 0.520×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.515×, HepG2/C3A 0.536×; ⚠ cell-cycle shift, explains ~70% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Alpelisib (drug)]] 5 µM in 1 line (HCT15 0.0817×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.848× | -6.5 | 3e-08 | 24/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.799×** | -6.3 | 9e-08 | 27/48 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.858× | -4.3 | 0.003 | 19/49 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.767×** | -3.9 | 0.014 | 11/49 (CHP-212, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.872× | -3.7 | 0.026 | 8/48 (SNU-1, RKO, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.781×** | -3.6 | 0.028 | 17/44 (AN3 CA, J82, …) | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.885× | -3.4 | 0.047 | 14/47 (SNU-423, HCT15, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.843× | -3.4 | 0.047 | 11/48 (SW 1088, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.886× | -3.3 | 0.065 | 6/49 (SW48, A-172, …) | top dose only | plate-row cell shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.065 | 11/48 (Panc 03.27, HS-578T, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimitespib (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.065 | 11/48 (SHP-77, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rifaximin (drug)]] 0.05 µM |  | 0.884× | -3.2 | 0.067 | 6/48 (NCI-H2030, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 108 | 12 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 83.2 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 59.0 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.58× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 94.4 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.520× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HOP62 (line)]] | alt | 47.2 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.13× (z +11.5) | — |
| [[KATO III (line)]] | alt | 59.8 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 68.3 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 95.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 73.2 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +12.6) | — |
| [[LoVo (line)]] | wt | 78.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 49.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +10.2) | — |
| [[A-427 (line)]] | wt | 126 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.15× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HepG2_C3A (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.353× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~4% of this change |
| [[MIA PaCa-2 (line)]] | alt | 78.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 77.4 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.81× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.636× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[A498 (line)]] | wt | 80.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0906× (z -9.4) ⚠ toxic |
| [[BT-474 (line)]] | alt | 64.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.70× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 87.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[C32 (line)]] | wt | 76.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 57.9 | 0 | 1 | — | [[Alpelisib (drug)]] 5 µM 0.0817× (z -9.3) |
| [[HS-578T (line)]] | alt | 58.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 51.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +9.2) | — |
| [[J82 (line)]] | alt | 120 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 49.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 94.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[RKO (line)]] | wt | 99.8 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.39× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 134 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.92× (z +10.4) | — |
| [[A-172 (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP1GDS1]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 | same gene group |
| [[LARP1]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[VWA8]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[UBE2K]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[NIN]] | +0.63 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[HACD3]] | +0.62 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[HEATR3]] | +0.62 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[BLMH]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[USP46]] | +0.60 | +0.69 / +0.57 | both halves | 8e-06 |  |
| [[RNF130]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PDS5A]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[METTL25B]] | -0.54 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[MXD1]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[APBA3]] | -0.51 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[CHCHD7]] | -0.51 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[ADAM8]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[KLHL28]] | -0.50 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ZNF490]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[PPP1R11]] | -0.50 | -0.46 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM8]] | B | ADAM8 activity lowers KPNA3's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.58× higher at baseline in the lines without ADAM8 | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.7, -34.7); signed map (-18.6, -50.3). **Vector** length 113, 33.5% of its response variance represented; |z| ≥ 3 in 1,315 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.3 | +20.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +16.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.4 | +10.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +7.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -6.8 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +2.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.6 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -3.6 | -6.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.1 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,699,320-49,792,682 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRP1gamma, SRP4, hSRP1, IPOA4 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Reactome | 10 pathways, smallest: NS1 Mediated Effects on Host Pathways; Maturation of DENV proteins; ISG15 antiviral mechanism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00505](https://www.uniprot.org/uniprotkb/O00505) (Importin subunit alpha-4):

> Functions in nuclear protein import as an adapter protein for nuclear receptor KPNB1. Binds specifically and directly to substrates containing either a simple or bipartite NLS motif. Docking of the importin/substrate complex to the nuclear pore complex (NPC) is mediated by KPNB1 through binding to nucleoporin FxFG repeats and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin-beta …

**Summary**, from NCBI Gene [3839](https://www.ncbi.nlm.nih.gov/gene/3839):

> The transport of molecules between the nucleus and the cytoplasm in eukaryotic cells is mediated by the nuclear pore complex (NPC), which consists of 60-100 proteins. Small molecules (up to 70 kD) can pass through the nuclear pore by nonselective diffusion while larger molecules are transported by an active process. The protein encoded by this gene belongs to the importin alpha family, and is involved in nuclear protein import. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:6396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6396) · Entrez [3839](https://www.ncbi.nlm.nih.gov/gene/3839) · UniProt [O00505](https://www.uniprot.org/uniprotkb/O00505) · Ensembl [ENSG00000102753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102753)

## Data

Gene col 2266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2266); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2266]; `tensor/DDL_lfc|DDL_z.npy` [2266]; `embed/gene_vectors.npy` [2266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2266 or target_col == 2266). Every well: [[KPNA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
