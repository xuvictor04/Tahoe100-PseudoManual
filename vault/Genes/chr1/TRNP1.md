---
symbol: "TRNP1"
type: "gene"
col: 14800
ensembl_id: "ENSG00000253368"
name: "TMF1 regulated nuclear protein 1"
location: "1p36.11"
module: 141
arm: "+"
pooled_cpm: 12.81
n_lines_expressing: 40
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# TRNP1

*TMF1 regulated nuclear protein 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.84× (z +13.8, q 1e-40, up in 22 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.82× (z +9.1, q 2e-17, up in 26 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.502× (z -6.1, q 8e-07, down in 25 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.577× (z -4.8, q 4e-04, down in 23 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.388×, HT-29 0.311×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (HEC-1-A 0.405×, PANC-1 0.298×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.113×; ⚠ cell-cycle shift, explains ~60% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HEC-1-A 0.303×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.137×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGF2BP2]] (+0.65, fdr 7e-06), [[PTPRN2]] (+0.64, fdr 1e-05), [[SH2D3A]] (+0.60, fdr 2e-05); moves opposite to [[METTL4]] (-0.55, fdr 3e-05), [[PMS2]] (-0.53, fdr 1e-04), [[EEF1AKMT3]] (-0.53, fdr 4e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PRKG2-AS1]] → it (grade B ⚠); 5 go from it, the strongest it → [[IGF2BP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.84×** | +13.8 | 1e-40 | 22/23 (AsPC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.62×** | +10.8 | 7e-25 | 15/16 (AsPC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.46×** | +10.1 | 1e-21 | 19/20 (NCI-H2347, A549, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +9.1 | 2e-17 | 26/35 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +8.6 | 1e-15 | 29/37 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +8.0 | 8e-14 | 24/37 (HCT15, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +7.9 | 3e-13 | 27/36 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.82×** | +7.4 | 7e-12 | 20/32 (A498, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.08×** | +6.4 | 1e-08 | 22/33 (C-33 A, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +5.7 | 8e-07 | 22/37 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +5.4 | 4e-06 | 19/34 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.76×** | +4.7 | 1e-04 | 16/34 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.5 | 4e-04 | 22/35 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +4.4 | 4e-04 | 11/31 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 15/36 (A549, NCI-H2347, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.72×** | +3.4 | 0.023 | 11/32 (HT-29, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.050 | 11/34 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.050 | 9/35 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.076 | 8/35 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.076 | 9/34 (NCI-H2347, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14800.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.388×, HT-29 0.311×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (HEC-1-A 0.405×, PANC-1 0.298×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.113×; ⚠ cell-cycle shift, explains ~60% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HEC-1-A 0.303×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.137×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.502×** | -6.1 | 8e-07 | 25/37 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -4.8 | 4e-04 | 23/35 (HOP62, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.437×** | -3.8 | 0.027 | 13/32 (KATO III, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.693× | -3.2 | 0.18 | 5/38 (HS-578T, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 60.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.303× (z -9.0) |
| [[A498 (line)]] | wt | 6.52 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +10.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.88× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -9.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.137× (z -8.8) |
| [[HT-29 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.298× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.000 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGF2BP2]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PTPRN2]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SH2D3A]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ADRA1B]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[BCAN-AS1]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[GALE]] | +0.57 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[EPPK1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[RAPH1]] | +0.55 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[AKAP13]] | +0.55 | +0.32 / +0.57 | both halves | 2e-04 |  |
| [[STMN3]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[RHOBTB2]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[EZR]] | +0.54 | +0.46 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL4]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[PMS2]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[EEF1AKMT3]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[MSL1]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[MFSD8]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[LINC01232]] | -0.50 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[SLC39A7]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PDHX]] | -0.49 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[PRDM10]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[USF1]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TSNAX-DISC1]] | -0.48 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[PPP1R8]] | -0.48 | -0.15 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[TIAL1]] | -0.48 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG2-AS1]] | B | PRKG2-AS1 activity raises TRNP1's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without PRKG2-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[SH2D3A]] | B | SH2D3A activity raises TRNP1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without SH2D3A | 0.006 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[EPPK1]] | B | EPPK1 activity raises TRNP1's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.90× lower at baseline in the lines without EPPK1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[CD22]] | B | CD22 activity raises TRNP1's level | lines that do not express CD22 (21) vs lines expressing it (29) | 1.89× lower at baseline in the lines without CD22 | 0.074 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent |
| [[AREG]] | B | AREG activity raises TRNP1's level | lines that do not express AREG (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without AREG | 0.090 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGF2BP2]] | B | TRNP1 activity raises IGF2BP2's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without TRNP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[SNED1]] | B | TRNP1 activity lowers SNED1's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 1.72× higher at baseline in the lines without TRNP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[PRKG2-AS1]] | B | TRNP1 activity raises PRKG2-AS1's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 1.99× lower at baseline in the lines without TRNP1 | 0.086 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[ADRA1B]] | B | TRNP1 activity raises ADRA1B's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without TRNP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[RHOBTB2]] | B | TRNP1 activity lowers RHOBTB2's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without TRNP1 | 0.095 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.3, 2.2); signed map (7.3, 35.7). **Vector** length 78.7, 18.1% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.6 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.5 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TMF1 regulated nuclear protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,993,692-27,000,886 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRNP; previously C1orf225 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NT89](https://www.uniprot.org/uniprotkb/Q6NT89) (TMF-regulated nuclear protein 1):

> DNA-binding factor that regulates the expression of a subset of genes and plays a key role in tangential, radial, and lateral expansion of the brain neocortex. Regulates neural stem cells proliferation and the production of intermediate neural progenitors and basal radial glial cells affecting the process of cerebral cortex gyrification. May control the proliferation rate of cells by regulating their progression through key cell-cycle transition points (By similarity).

**Summary**, from NCBI Gene [388610](https://www.ncbi.nlm.nih.gov/gene/388610):

> Predicted to enable DNA binding activity. Predicted to be involved in several processes, including cerebellar cortex morphogenesis; neural precursor cell proliferation; and regulation of cell cycle. Predicted to be located in euchromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34348) · Entrez [388610](https://www.ncbi.nlm.nih.gov/gene/388610) · UniProt [Q6NT89](https://www.uniprot.org/uniprotkb/Q6NT89) · Ensembl [ENSG00000253368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253368)

## Data

Gene col 14800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14800); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14800]; `tensor/DDL_lfc|DDL_z.npy` [14800]; `embed/gene_vectors.npy` [14800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14800 or target_col == 14800). Every well: [[TRNP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRNP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
