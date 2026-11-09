---
symbol: "MYO7A"
type: "gene"
col: 6017
ensembl_id: "ENSG00000137474"
name: "myosin VIIA"
location: "11q13.5"
module: 53
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# MYO7A

*myosin VIIA* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.79× (z +11.7, q 7e-29, up in 34 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.501× (z -6.1, q 7e-07, down in 20 of 42 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.553× (z -5.2, q 6e-05, down in 13 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGMN]] (+0.62, fdr 1e-05), [[SYT5]] (+0.61, fdr 1e-05), [[MAPK8IP1]] (+0.60, fdr 1e-05); moves opposite to [[TADA2A]] (-0.52, fdr 3e-05), [[TRMT61B]] (-0.52, fdr 3e-05), [[ARMC8]] (-0.51, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LPAR5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.79×** | +11.7 | 7e-29 | 34/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.40×** | +10.9 | 4e-25 | 21/41 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +9.2 | 6e-18 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **2.83×** | +9.1 | 8e-18 | 30/42 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +7.0 | 2e-10 | 14/29 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +6.8 | 1e-09 | 18/38 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.14×** | +6.7 | 2e-09 | 17/34 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +6.6 | 3e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +6.5 | 4e-09 | 5/14 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +5.9 | 2e-07 | 8/32 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +5.9 | 2e-07 | 17/40 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.006 | 11/41 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.8 | 0.006 | 4/43 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.009 | 10/35 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.57×** | +3.7 | 0.010 | 5/25 (SW1417, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.028 | 7/39 (HEC-1-A, Hs 766T, …) | top dose only |  |
| [[SBI-0640756 (drug)]] 5 µM |  | **2.01×** | +3.2 | 0.044 | 0/20 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.501×** | -6.1 | 7e-07 | 20/42 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -5.2 | 6e-05 | 13/38 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -4.9 | 1e-04 | 16/37 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.376×** | -4.5 | 0.001 | 11/34 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.636×** | -4.0 | 0.008 | 15/24 (HT-29, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.642×** | -3.9 | 0.009 | 12/37 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.650×** | -3.8 | 0.013 | 9/41 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.742×** | -3.7 | 0.015 | 7/40 (RPMI-7951, C-33 A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -3.5 | 0.031 | 10/40 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.076 | 10/39 (hTERT-HPNE, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 21.3 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0234× (z -14.8) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0946× (z -9.7) |
| [[LoVo (line)]] | wt | 4.20 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0350× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Carbamazepine (drug)]] 0.5 µM 0.0465× (z -9.0) |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0832× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 3.24 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 5 µM 0.0481× (z -8.5) |
| [[SW480 (line)]] | alt | 2.09 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0536× (z -9.5) |
| [[A-172 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.830 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.906 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.567 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGMN]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SYT5]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MAPK8IP1]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[RAP1GAP]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZDHHC11B]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[C19orf38]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[HAP1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MROH3P]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MIR9-1HG]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[IRAG1-AS1]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TMEM25]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RINL]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA2A]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TRMT61B]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[LSM6]] | -0.50 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[PKD2]] | -0.49 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[PTGR3]] | -0.47 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[FBXL5]] | -0.47 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[MTCH2]] | -0.46 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[AP4E1]] | -0.46 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[TMEM209]] | -0.45 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[ORC5]] | -0.45 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MECR]] | -0.45 | -0.46 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR5]] | B | LPAR5 activity raises MYO7A's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without LPAR5 | 0.012 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[SLC44A4]] | B | SLC44A4 activity raises MYO7A's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.12× lower at baseline in the lines without SLC44A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[MUC20]] | B | MUC20 activity raises MYO7A's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without MUC20 | 0.017 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[ADCY4]] | B | ADCY4 activity raises MYO7A's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 1.75× lower at baseline in the lines without ADCY4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[MROH3P]] | B | MROH3P activity raises MYO7A's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without MROH3P | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[CDH1]] | B | CDH1 activity raises MYO7A's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 1.62× lower at baseline in the lines without CDH1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.1, -17.1); signed map (-2.5, 23.9). **Vector** length 56.3, 8.02% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +6.5 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +2.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.8 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | +0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -3.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | myosin VIIA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:77,128,246-77,215,241 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NSRD2; previously USH1B, DFNB2, DFNA11 |
| Gene groups (HGNC) | A-kinase anchoring proteins; Myosin heavy chains, class VII; FERM domain containing; SH3 domain containing |
| Reactome | 6 pathways, smallest: The canonical retinoid cycle in rods (twilight vision); Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13402](https://www.uniprot.org/uniprotkb/Q13402) (Unconventional myosin-VIIa):

> Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. Their highly divergent tails bind to membranous compartments, which are then moved relative to actin filaments. In the retina, plays an important role in the renewal of the outer photoreceptor disks. Plays an important role in the distribution and migration of retinal pigment epithelial (RPE) melanosomes and phagosomes, and in the regulation of opsin transport in retinal …

**Summary**, from NCBI Gene [4647](https://www.ncbi.nlm.nih.gov/gene/4647):

> This gene is a member of the myosin gene family. Myosins are mechanochemical proteins characterized by the presence of a motor domain, an actin-binding domain, a neck domain that interacts with other proteins, and a tail domain that serves as an anchor. This gene encodes an unconventional myosin with a very short tail. Defects in this gene are associated with the mouse shaker-1 phenotype and the human Usher syndrome 1B which are characterized by deafness, reduced vestibular function, and (in …

**Accessions** — [HGNC:7606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7606) · Entrez [4647](https://www.ncbi.nlm.nih.gov/gene/4647) · UniProt [Q13402](https://www.uniprot.org/uniprotkb/Q13402) · Ensembl [ENSG00000137474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137474)

## Data

Gene col 6017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6017); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6017]; `tensor/DDL_lfc|DDL_z.npy` [6017]; `embed/gene_vectors.npy` [6017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6017 or target_col == 6017). Every well: [[MYO7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
