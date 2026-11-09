---
symbol: "EBF4"
type: "gene"
col: 1551
ensembl_id: "ENSG00000088881"
name: "EBF transcription factor 4"
location: "20p13"
module: 102
arm: "+"
pooled_cpm: 8.94
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 28
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# EBF4

*EBF transcription factor 4* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +9.1, q 3e-17, up in 20 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.542× (z -8.0, q 7e-13, down in 21 of 36 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.655× (z -5.5, q 4e-06, down in 18 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSI1]] (+0.59, fdr 7e-06), [[CDH23]] (+0.59, fdr 1e-05), [[RHBDL3]] (+0.58, fdr 2e-05); moves opposite to [[ARMC1]] (-0.47, fdr 6e-05), [[SLC25A14]] (-0.47, fdr 1e-04), [[ELP3]] (-0.44, fdr 4e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[RET]] → it (grade B ⚠); 28 go from it, the strongest it → [[FAM171A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +9.1 | 3e-17 | 20/36 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +8.3 | 4e-14 | 19/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.31×** | +5.1 | 7e-05 | 15/36 (HOP62, SHP-77, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.003 | 13/34 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Cytarabine (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.008 | 9/35 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +3.9 | 0.008 | 5/35 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.016 | 10/35 (NCI-H2030, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.017 | 6/36 (HepG2/C3A, NCI-H460, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.66×** | +3.4 | 0.035 | 6/34 (J82, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.035 | 6/33 (BT-474, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +3.4 | 0.037 | 5/20 (NCI-H460, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.047 | 3/35 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +3.2 | 0.057 | 5/36 (C-33 A, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.2 | 0.059 | 5/15 (SW 900, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +3.1 | 0.072 | 6/35 (A498, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.072 | 8/36 (PANC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.096 | 5/36 (BT-474, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.542×** | -8.0 | 7e-13 | 21/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.548×** | -7.8 | 1e-12 | 22/35 (hTERT-HPNE, SW48, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.585×** | -6.7 | 3e-09 | 21/35 (NCI-H1792, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.626×** | -6.1 | 2e-07 | 19/34 (NCI-H2030, J82, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -5.5 | 4e-06 | 18/35 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.684×** | -4.9 | 7e-05 | 16/36 (LoVo, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.513×** | -4.5 | 5e-04 | 15/35 (SW 900, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.701×** | -4.4 | 6e-04 | 13/29 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.717×** | -4.3 | 1e-03 | 19/33 (A-172, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.547×** | -4.1 | 0.003 | 14/33 (A549, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.736×** | -4.0 | 0.003 | 12/35 (HOP62, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.728×** | -4.0 | 0.003 | 14/35 (HOP62, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.751×** | -3.7 | 0.008 | 13/36 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.591×** | -3.5 | 0.016 | 9/29 (PANC-1, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.029 | 12/34 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.622×** | -3.2 | 0.043 | 10/30 (SK-MEL-2, A549, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.716×** | -3.1 | 0.056 | 5/36 (BT-474, NCI-H661, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.9 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 26.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -13.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0537× (z -9.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 16.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[BT-474 (line)]] | alt | 8.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0840× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[H4 (line)]] | wt | 15.1 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0807× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0316× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 6.57 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 8.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0812× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 7.07 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.897 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSI1]] | +0.59 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CDH23]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RHBDL3]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[GRID1]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[SHC2]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RASGEF1C]] | +0.57 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[MAP3K10]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[MELTF]] | +0.55 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[DOCK3]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CRMP1]] | +0.55 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[PALM]] | +0.54 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[DGCR5]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC1]] | -0.47 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[SLC25A14]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[ELP3]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[EIF2B1]] | -0.43 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[GALK2]] | -0.42 | -0.27 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RET]] | B | RET activity raises EBF4's level | lines that do not express RET (28) vs lines expressing it (22) | 2.75× lower at baseline in the lines without RET | 8e-04 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[ELFN1]] | B | ELFN1 activity raises EBF4's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without ELFN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[DPYSL5]] | B | DPYSL5 activity raises EBF4's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without DPYSL5 | 0.046 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[CHD5]] | B | CHD5 activity raises EBF4's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without CHD5 | 0.051 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[SLC4A3]] | B | SLC4A3 activity raises EBF4's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.33× lower at baseline in the lines without SLC4A3 | 0.053 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[HAGLR]] | B | HAGLR activity raises EBF4's level | lines that do not express HAGLR (14) vs lines expressing it (36) | 3.19× lower at baseline in the lines without HAGLR | 0.059 | ⚠ within organs, on part of the lines; also absent: ARNT2, BEND6, ITPR1 |
| [[BRSK2]] | B | BRSK2 activity raises EBF4's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without BRSK2 | 0.090 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[PLEKHO1]] | B | PLEKHO1 activity raises EBF4's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without PLEKHO1 | 0.095 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 28, C 0. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM171A1]] | B | EBF4 activity raises FAM171A1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.73× lower at baseline in the lines without EBF4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[PLEKHO1]] | B | EBF4 activity raises PLEKHO1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.87× lower at baseline in the lines without EBF4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[SIMC1]] | B | EBF4 activity raises SIMC1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.57× lower at baseline in the lines without EBF4 | 0.007 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[EMID1]] | B | EBF4 activity raises EMID1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.90× lower at baseline in the lines without EBF4 | 0.009 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[RHBDL3]] | B | EBF4 activity raises RHBDL3's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.71× lower at baseline in the lines without EBF4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[BRSK2]] | B | EBF4 activity raises BRSK2's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without EBF4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[ARMC1]] | B | EBF4 activity raises ARMC1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.24× lower at baseline in the lines without EBF4 | 0.015 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[ULK2]] | B | EBF4 activity raises ULK2's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 3.78× lower at baseline in the lines without EBF4 | 0.024 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[NKAIN1]] | B | EBF4 activity raises NKAIN1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without EBF4 | 0.029 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[FAXC]] | B | EBF4 activity raises FAXC's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.29× lower at baseline in the lines without EBF4 | 0.032 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[SLC4A3]] | B | EBF4 activity raises SLC4A3's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.99× lower at baseline in the lines without EBF4 | 0.036 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[GBX1]] | B | EBF4 activity raises GBX1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.96× lower at baseline in the lines without EBF4 | 0.036 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.1, 36.9); signed map (27.1, 24.5). **Vector** length 62.9, 10.9% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.0 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.6 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | EBF transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,692,780-2,760,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1442, COE4, RP5-860F19.3, O/E-4 |
| Gene groups (HGNC) | EBF transcription factors; IPT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQW3](https://www.uniprot.org/uniprotkb/Q9BQW3) (Transcription factor COE4):

> Transcription factor. Binds to specific sequence motif 5'-CCCNNG[GA]G-3' in regulatory elements of putative target immunoregulatory genes such as NKG7, GZMA, and TBX21. Positively modulates transcription of NKG7. May play a role in regulating FAS/CD95-mediated apoptosis in cytotoxic NK cells and T-cells, probably downstream of interleukin IL2 signaling.

**Summary**, from NCBI Gene [57593](https://www.ncbi.nlm.nih.gov/gene/57593):

> EBF4 belongs to the conserved Olf/EBF family of helix-loop-helix transcription factors, members of which play important roles in neural development and B-cell maturation (Wang et al., 2002 [PubMed 12139918]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29278) · Entrez [57593](https://www.ncbi.nlm.nih.gov/gene/57593) · UniProt [Q9BQW3](https://www.uniprot.org/uniprotkb/Q9BQW3) · Ensembl [ENSG00000088881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088881)

## Data

Gene col 1551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1551); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1551]; `tensor/DDL_lfc|DDL_z.npy` [1551]; `embed/gene_vectors.npy` [1551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1551 or target_col == 1551). Every well: [[EBF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
