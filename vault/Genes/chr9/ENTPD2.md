---
symbol: "ENTPD2"
type: "gene"
col: 603
ensembl_id: "ENSG00000054179"
name: "ectonucleoside triphosphate diphosphohydrolase 2"
location: "9q34.3"
module: 44
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 28
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 21
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# ENTPD2

*ectonucleoside triphosphate diphosphohydrolase 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.67× (z +10.7, q 5e-24, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.509× (z -5.6, q 1e-05, down in 11 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (RKO 0.0421×, LS 180 0.0696×, SW480 0.123×, KATO III 0.133×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HT-29 0.0372×, LS 180 0.101×, KATO III 0.117×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 0.175×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMTK3]] (+0.62, fdr 5e-05), [[AZGP1]] (+0.61, fdr 1e-05), [[PNKD]] (+0.60, fdr 2e-05); moves opposite to [[MMADHC-DT]] (-0.55, fdr 4e-04), [[TTC6]] (-0.54, fdr 3e-04), [[SMIM10L1]] (-0.53, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MUC3A]] → it (grade C ⚠); 21 go from it, the strongest it → [[ELMO3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.67×** | +10.7 | 5e-24 | 18/24 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.45×** | +10.2 | 6e-22 | 18/23 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +9.4 | 2e-18 | 3/6 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +7.8 | 8e-13 | 7/13 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +6.9 | 6e-10 | 14/23 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +6.8 | 8e-10 | 4/7 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +4.7 | 3e-04 | 17/24 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +4.6 | 3e-04 | 10/20 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.17×** | +4.5 | 4e-04 | 1/20 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 11/24 (SW480, HCT15, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.02×** | +4.1 | 0.002 | 4/13 (LS 180, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.011 | 3/21 (SW480, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.5 | 0.017 | 5/12 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.031 | 2/21 (HT-29, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.2 | 0.046 | 3/20 (RKO, A-427, …) | rises with dose | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.057 | 1/18 (HT-29) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 603.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (RKO 0.0421×, LS 180 0.0696×, SW480 0.123×, KATO III 0.133×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HT-29 0.0372×, LS 180 0.101×, KATO III 0.117×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 0.175×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -5.6 | 1e-05 | 11/23 (A549, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -5.0 | 1e-04 | 14/21 (RKO, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.660× | -3.4 | 0.11 | 9/23 (LS 180, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.676× | -3.1 | 0.26 | 11/24 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.677× | -3.0 | 0.26 | 10/24 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 14.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -9.5) |
| [[HT-29 (line)]] | alt | 7.74 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0372× (z -20.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -8.9) |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0696× (z -14.4) |
| [[LoVo (line)]] | wt | 7.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 11.2 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 5.06× (z +9.3) | — |
| [[NCI-H661 (line)]] | alt | 1.73 | 1 | 0 | [[Clonidine (hydrochloride) (drug)]] 5 µM 2.24× (z +36.1) | — |
| [[RKO (line)]] | wt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0421× (z -17.4) |
| [[SW480 (line)]] | alt | 3.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -9.5) |
| [[A-172 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK3]] | +0.62 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[AZGP1]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PNKD]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TMEM63C]] | +0.58 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[CKMT1B]] | +0.58 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[FBXL16]] | +0.57 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[EFNA4]] | +0.57 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[NRTN]] | +0.57 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[MUC3A]] | +0.56 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[HDAC11]] | +0.56 | +0.49 / +0.31 | both halves | 2e-04 |  |
| [[TNNI3]] | +0.56 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[CORO2A]] | +0.56 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.55 | -0.45 / -0.24 | both halves | 4e-04 |  |
| [[TTC6]] | -0.54 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[SMIM10L1]] | -0.53 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[AP5M1]] | -0.53 | -0.41 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[PBLD]] | -0.51 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[ST7]] | -0.51 | -0.33 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[GULP1]] | -0.50 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[FOXA1]] | -0.50 | -0.54 / -0.22 | both halves | 6e-04 |  |
| [[RAB30-DT]] | -0.49 | -0.34 / -0.26 | both halves | 4e-04 |  |
| [[C11orf58]] | -0.48 | -0.39 / -0.23 | both halves | 5e-04 |  |
| [[SLC25A21]] | -0.48 | -0.32 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[WDR33]] | -0.48 | -0.42 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[RBM12B]] | -0.48 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[RHBDD3]] | -0.48 | -0.35 / -0.22 | both halves | 6e-04 |  |
| [[RCC1L]] | -0.48 | -0.31 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC3A]] | C | MUC3A activity raises ENTPD2's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.51× lower at baseline in the lines without MUC3A | 0.022 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B; co-absent with the target |
| [[MCF2L]] | C | MCF2L activity raises ENTPD2's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.54× lower at baseline in the lines without MCF2L | 0.028 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2; co-absent with the target |
| [[EPHA1]] | C | EPHA1 activity raises ENTPD2's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without EPHA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[FGFR4]] | C | FGFR4 activity raises ENTPD2's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.68× lower at baseline in the lines without FGFR4 | 0.061 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises ENTPD2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.11× lower at baseline in the lines without PRSS8 | 0.066 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |
| [[PKP2]] | C | PKP2 activity raises ENTPD2's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.77× lower at baseline in the lines without PKP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN; co-absent with the target |
| [[CKMT1B]] | C | CKMT1B activity raises ENTPD2's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without CKMT1B | 0.090 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 6, C 15. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELMO3]] | B | ENTPD2 activity raises ELMO3's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without ENTPD2 | 0.017 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[MMP15]] | B | ENTPD2 activity raises MMP15's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without ENTPD2 | 0.031 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[FCHO1]] | B | ENTPD2 activity raises FCHO1's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 1.45× lower at baseline in the lines without ENTPD2 | 0.040 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[RHPN1]] | B | ENTPD2 activity raises RHPN1's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without ENTPD2 | 0.063 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[CLMN]] | B | ENTPD2 activity raises CLMN's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without ENTPD2 | 0.067 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[FKBP1B]] | B | ENTPD2 activity raises FKBP1B's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without ENTPD2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[LMTK3]] | C | ENTPD2 activity raises LMTK3's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 3.72× lower at baseline in the lines without ENTPD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |
| [[TJP3]] | C | ENTPD2 activity raises TJP3's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 4.84× lower at baseline in the lines without ENTPD2 | 0.002 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |
| [[LLGL2]] | C | ENTPD2 activity raises LLGL2's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 4.83× lower at baseline in the lines without ENTPD2 | 0.005 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |
| [[PDE9A]] | C | ENTPD2 activity raises PDE9A's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 4.07× lower at baseline in the lines without ENTPD2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |
| [[PKP2]] | C | ENTPD2 activity raises PKP2's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 4.41× lower at baseline in the lines without ENTPD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |
| [[PRSS8]] | C | ENTPD2 activity raises PRSS8's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 4.95× lower at baseline in the lines without ENTPD2 | 0.013 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.374). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.7, -4.5); signed map (-24.3, 31.2). **Vector** length 51.2, 11.3% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleoside triphosphate diphosphohydrolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,048,107-137,054,061 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NTPDase-2; previously CD39L1 |
| Gene groups (HGNC) | Ectonucleoside triphosphate diphosphohydrolase family |
| Reactome | 3 pathways, smallest: Phosphate bond hydrolysis by NTPDase proteins; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5L3](https://www.uniprot.org/uniprotkb/Q9Y5L3) (Ectonucleoside triphosphate diphosphohydrolase 2):

> Catalyzes the hydrolysis of nucleoside triphosphates (NTPs) and diphosphates (NDPs), with a marked preference for triphosphonucleosides over diphosphonucleosides. The enzyme sequentially removes phosphate groups in two successive steps, converting NTPs to nucleoside monophosphates (NMPs) via NDP intermediates. This activity contributes to the regulation of extracellular nucleotides levels. ATP hydrolysis is characterized by fast ADP accumulation and delayed AMP formation, reflecting limited ADP …

**Summary**, from NCBI Gene [954](https://www.ncbi.nlm.nih.gov/gene/954):

> The protein encoded by this gene is the type 2 enzyme of the ecto-nucleoside triphosphate diphosphohydrolase family (E-NTPDase). E-NTPDases are a family of ecto-nucleosidases that hydrolyze 5'-triphosphates. This ecto-ATPase is an integral membrane protein. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3364) · Entrez [954](https://www.ncbi.nlm.nih.gov/gene/954) · UniProt [Q9Y5L3](https://www.uniprot.org/uniprotkb/Q9Y5L3) · Ensembl [ENSG00000054179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054179)

## Data

Gene col 603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 603); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 603]; `tensor/DDL_lfc|DDL_z.npy` [603]; `embed/gene_vectors.npy` [603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 603 or target_col == 603). Every well: [[ENTPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
