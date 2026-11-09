---
symbol: "FRZB"
type: "gene"
col: 8613
ensembl_id: "ENSG00000162998"
name: "frizzled related protein"
location: "2q32.1"
module: 37
arm: "+"
pooled_cpm: 4.53
n_lines_expressing: 46
n_dd_up: 27
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# FRZB

*frizzled related protein* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.20× (z +9.6, q 5e-19, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.594× (z -4.3, q 0.005, down in 17 of 43 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.383× (z -4.2, q 0.006, down in 11 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.0667×, hTERT-HPNE 0.0959×, NCI-H460 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.0568×; ⚠ toxic); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0711×); [[Pimozide (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0936×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.0712×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCF2]] (+0.85, fdr 7e-06), [[SLC26A7]] (+0.79, fdr 7e-06), [[DCAF4L1]] (+0.78, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DDR2]] → it (grade B ⚠); 7 go from it, the strongest it → [[CMYA5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.20×** | +9.6 | 5e-19 | 33/42 (LoVo, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +7.8 | 2e-12 | 21/36 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.59×** | +7.4 | 3e-11 | 28/39 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.07×** | +6.0 | 3e-07 | 18/42 (HEC-1-A, NCI-H460, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.67×** | +5.9 | 3e-07 | 13/43 (HOP62, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.05×** | +5.6 | 2e-06 | 23/40 (A-427, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +5.3 | 1e-05 | 13/31 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.1 | 2e-05 | 2/8 (HOP62, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.54×** | +5.0 | 3e-05 | 13/42 (HCT15, HT-29, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.0 | 3e-05 | 11/25 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +5.0 | 3e-05 | 19/43 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.18×** | +5.0 | 3e-05 | 3/13 (NCI-H1573, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +4.9 | 4e-05 | 17/42 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.9 | 4e-05 | 14/33 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **3.02×** | +4.8 | 7e-05 | 10/39 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +4.4 | 4e-04 | 19/43 (HEC-1-A, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.70×** | +4.4 | 4e-04 | 10/43 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +4.4 | 4e-04 | 14/39 (LoVo, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.003 | 14/36 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8613.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.0667×, hTERT-HPNE 0.0959×, NCI-H460 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.0568×; ⚠ toxic); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0711×); [[Pimozide (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0936×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.0712×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.594×** | -4.3 | 0.005 | 17/43 (SK-MEL-2, HEC-1-A, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.585×** | -4.3 | 0.005 | 10/22 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[NG25 (drug)]] 5 µM |  | **0.383×** | -4.2 | 0.006 | 11/30 (HS-578T, A-427, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.652×** | -3.6 | 0.053 | 13/43 (LOX-IMVI, HCT15, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.656×** | -3.5 | 0.053 | 14/43 (LOX-IMVI, AN3 CA, …) | rises with dose |  |
| [[Flutamide (drug)]] 5 µM |  | 0.693× | -3.0 | 0.20 | 8/43 (BT-474, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.0936× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 8.12 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0711× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 8.53 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0568× (z -12.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0667× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 7.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCF2]] | +0.85 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.79 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.78 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[CORIN]] | +0.78 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[YIPF7]] | +0.75 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.73 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PXDNL]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SNX31]] | +0.72 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[CMYA5]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDR2]] | B | DDR2 activity raises FRZB's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without DDR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[ANKRD7]] | B | ANKRD7 activity raises FRZB's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 2.29× lower at baseline in the lines without ANKRD7 | 0.035 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises FRZB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC26A4]] | B | SLC26A4 activity raises FRZB's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.69× lower at baseline in the lines without SLC26A4 | 0.061 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMYA5]] | C | FRZB activity raises CMYA5's level | lines that do not express FRZB (4) vs lines expressing it (46) | 2.90× lower at baseline in the lines without FRZB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ANKDD1B]] | C | FRZB activity raises ANKDD1B's level | lines that do not express FRZB (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without FRZB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent; its own permutation p |
| [[LINC02646]] | C | FRZB activity raises LINC02646's level | lines that do not express FRZB (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without FRZB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent; its own permutation p |
| [[GLIPR1-AS1]] | C | FRZB activity raises GLIPR1-AS1's level | lines that do not express FRZB (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without FRZB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent; its own permutation p |
| [[SNHG14]] | C | FRZB activity raises SNHG14's level | lines that do not express FRZB (4) vs lines expressing it (46) | 3.25× lower at baseline in the lines without FRZB | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent |
| [[MGAM]] | C | FRZB activity raises MGAM's level | lines that do not express FRZB (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without FRZB | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent |
| [[KAZN]] | C | FRZB activity raises KAZN's level | lines that do not express FRZB (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without FRZB | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, -16.0); signed map (13.7, 5.1). **Vector** length 83.1, 16.1% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +6.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.4 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.2 | -4.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | frizzled related protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:182,833,275-182,866,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FRZB-PEN, FRZB1, SRFP3, FRP-3, SFRP3, FRE, FRITZ, FRZB-1 |
| Gene groups (HGNC) | Secreted frizzled-related proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92765](https://www.uniprot.org/uniprotkb/Q92765) (Secreted frizzled-related protein 3):

> Soluble frizzled-related proteins (sFRPS) function as modulators of Wnt signaling through direct interaction with Wnts. They have a role in regulating cell growth and differentiation in specific cell types. SFRP3/FRZB appears to be involved in limb skeletogenesis. Antagonist of Wnt8 signaling. Regulates chondrocyte maturation and long bone development.

**Summary**, from NCBI Gene [2487](https://www.ncbi.nlm.nih.gov/gene/2487):

> The protein encoded by this gene is a secreted protein that is involved in the regulation of bone development. Defects in this gene are a cause of female-specific osteoarthritis (OA) susceptibility. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:3959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3959) · Entrez [2487](https://www.ncbi.nlm.nih.gov/gene/2487) · UniProt [Q92765](https://www.uniprot.org/uniprotkb/Q92765) · Ensembl [ENSG00000162998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162998)

## Data

Gene col 8613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8613); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8613]; `tensor/DDL_lfc|DDL_z.npy` [8613]; `embed/gene_vectors.npy` [8613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8613 or target_col == 8613). Every well: [[FRZB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRZB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
