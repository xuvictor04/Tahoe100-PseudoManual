---
symbol: "LRRC57"
type: "gene"
col: 11152
ensembl_id: "ENSG00000180979"
name: "leucine rich repeat containing 57"
location: "15q15.2"
module: 40
arm: "-"
pooled_cpm: 16.89
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# LRRC57

*leucine rich repeat containing 57* — 15q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +12.0, q 3e-30, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.920× (z -5.4, q 2e-05, down in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.593× (z -5.4, q 2e-05, down in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBXN2A]] (+0.70, fdr 1e-05), [[TAX1BP3]] (+0.61, fdr 3e-05), [[RO60]] (+0.58, fdr 3e-05); moves opposite to [[CSNK2A1]] (-0.57, fdr 3e-05), [[DUXAP10]] (-0.57, fdr 3e-05), [[TOMM20]] (-0.57, fdr 1e-04).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +12.0 | 3e-30 | 33/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.76×** | +11.1 | 5e-26 | 27/39 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.48×** | +10.9 | 2e-25 | 32/47 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +10.1 | 5e-22 | 31/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.68×** | +9.8 | 2e-20 | 19/29 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +8.9 | 5e-17 | 31/43 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.53×** | +8.3 | 6e-15 | 30/46 (SW480, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.7 | 7e-13 | 26/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.53×** | +7.7 | 1e-12 | 23/34 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +7.2 | 4e-11 | 28/47 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.41×** | +6.7 | 8e-10 | 23/43 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +6.7 | 8e-10 | 22/47 (SW480, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.6 | 2e-09 | 23/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +6.4 | 6e-09 | 24/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +6.1 | 3e-08 | 21/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.1 | 4e-08 | 17/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 1e-07 | 18/47 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.002 | 10/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.003 | 13/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +3.0 | 0.055 | 7/48 (A498, SW 900, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.061 | 4/47 (H4, PANC-1, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.086 | 7/44 (HS-578T, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +2.8 | 0.098 | 7/47 (C32, LOX-IMVI, …) | two highest doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.098 | 9/45 (LOX-IMVI, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -5.4 | 2e-05 | 2/48 (SK-MEL-2, H4) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.593×** | -5.4 | 2e-05 | 20/45 (RKO, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.875× | -3.7 | 0.044 | 7/48 (CHP-212, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.833×** | -3.5 | 0.064 | 14/46 (SNU-1, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.848× | -3.2 | 0.14 | 4/48 (SW 1271, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 21.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.16× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.21× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN2A]] | +0.70 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TAX1BP3]] | +0.61 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[RO60]] | +0.58 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[UBE2A]] | +0.57 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[LEPROT]] | +0.56 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ATXN7]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TAPBP]] | +0.55 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[ZHX1]] | +0.55 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[NFYB]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CHRAC1]] | +0.55 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[RAP2C]] | +0.54 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[BMPR2]] | +0.54 | +0.48 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK2A1]] | -0.57 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[DUXAP10]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TOMM20]] | -0.57 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[SPATC1L]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NOP58]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SND1]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[CUZD1]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[GP6-AS1]] | -0.54 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[CCNB1IP1]] | -0.54 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[CLINT1]] | -0.53 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[MRPS28]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[HERPUD1]] | -0.53 | -0.51 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity lowers LRRC57's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without RAB20 | 0.020 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LRRC57's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-9.2, 0.8); signed map (21.5, -20.6). **Vector** length 71.8, 12.2% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.5 | +6.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.3 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +4.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:42,537,820-42,548,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36812 |
| Matched by | ensembl_id |

UniProt [Q8N9N7](https://www.uniprot.org/uniprotkb/Q8N9N7) carries no function annotation.

**Summary**, from NCBI Gene [255252](https://www.ncbi.nlm.nih.gov/gene/255252):

> Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26719) · Entrez [255252](https://www.ncbi.nlm.nih.gov/gene/255252) · UniProt [Q8N9N7](https://www.uniprot.org/uniprotkb/Q8N9N7) · Ensembl [ENSG00000180979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180979)

## Data

Gene col 11152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11152); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11152]; `tensor/DDL_lfc|DDL_z.npy` [11152]; `embed/gene_vectors.npy` [11152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11152 or target_col == 11152). Every well: [[LRRC57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
