---
symbol: "MAGEB2"
type: "gene"
col: 1803
ensembl_id: "ENSG00000099399"
name: "MAGE family member B2"
location: "Xp21.2"
module: 158
arm: "+"
pooled_cpm: 3.62
n_lines_expressing: 8
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# MAGEB2

*MAGE family member B2* — Xp21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.62× (z +10.6, q 2e-23, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.69× (z +4.1, q 0.003, up in 5 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGEA1]] (+0.69, fdr 7e-06), [[MAGEA10]] (+0.61, fdr 1e-05), [[PHLDA1]] (+0.56, fdr 3e-05); moves opposite to [[MAZ]] (-0.46, fdr 2e-04), [[SEC61A2]] (-0.46, fdr 4e-05), [[LRRC27]] (-0.43, fdr 3e-04).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GTSF1]] → it (grade C ⚠); 3 go from it, the strongest it → [[MAGEA10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.62×** | +10.6 | 2e-23 | 3/5 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.80×** | +10.3 | 2e-22 | 3/4 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.12×** | +7.3 | 5e-11 | 1/5 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.61×** | +5.4 | 1e-05 | 1/5 (SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.4 | 0.001 | 1/6 (NCI-H1792) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.56×** | +4.2 | 0.003 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.2 | 0.003 | 1/6 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.003 | 5/6 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +4.0 | 0.005 | 5/6 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.015 | 2/6 (NCI-H460, NCI-H1792) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.55×** | +3.5 | 0.027 | 3/5 (LOX-IMVI, NCI-H1573, …) | top dose only | composition shift; position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.4 | 0.037 | 1/6 (SHP-77) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.69×** | +3.3 | 0.050 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.065 | 5/6 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.92×** | +3.1 | 0.065 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.75×** | +3.1 | 0.065 | 0/6 | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +3.0 | 0.086 | 5/6 (SHP-77, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.70×** | +2.9 | 0.096 | 0/6 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.499× | -3.6 | 0.11 | 0/6 | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.522× | -3.5 | 0.11 | 0/6 | rises with dose | plate-row cell shift |
| [[Trametinib (drug)]] 5 µM |  | 0.529× | -3.4 | 0.11 | 4/6 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 39.0 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.53× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.799 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGEA1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; STRING 435 |
| [[MAGEA10]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 | same gene group |
| [[PHLDA1]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ARC]] | +0.52 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[CCDC152]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[BCAN-AS2]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[IL31RA]] | +0.50 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[NRG3]] | +0.49 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[MAGEA4]] | +0.49 | +0.42 / +0.56 | both halves | 4e-05 | same gene group |
| [[LTBP2]] | +0.49 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[XKR6]] | +0.48 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[LINC01204]] | +0.48 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAZ]] | -0.46 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[SEC61A2]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[LRRC27]] | -0.43 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[DCUN1D4]] | -0.43 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[STK38]] | -0.42 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[HINT1]] | -0.41 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[KIF13A]] | -0.41 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[NCOA1]] | -0.41 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[ZDHHC24]] | -0.41 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[MAP3K2]] | -0.41 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[EGFL8]] | -0.41 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[RNF38]] | -0.40 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTSF1]] | C | GTSF1 activity raises MAGEB2's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.22× lower at baseline in the lines without GTSF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[MAGEA10]] | C | MAGEA10 activity raises MAGEB2's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 4.62× lower at baseline in the lines without MAGEA10 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[MAGEA1]] | C | MAGEA1 activity raises MAGEB2's level | lines that do not express MAGEA1 (37) vs lines expressing it (13) | 2.67× lower at baseline in the lines without MAGEA1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; co-absent with the target |
| [[RAB38]] | C | RAB38 activity raises MAGEB2's level | lines that do not express RAB38 (23) vs lines expressing it (27) | 1.96× lower at baseline in the lines without RAB38 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000255102, TMEM154, ENSG00000233539; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA10]] | C | MAGEB2 activity raises MAGEA10's level | lines that do not express MAGEB2 (42) vs lines expressing it (8) | 6.92× lower at baseline in the lines without MAGEB2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, MAGEA10, TBXT; co-absent with the target |
| [[GTSF1]] | C | MAGEB2 activity raises GTSF1's level | lines that do not express MAGEB2 (42) vs lines expressing it (8) | 4.11× lower at baseline in the lines without MAGEB2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, MAGEA10, TBXT; co-absent with the target |
| [[FRMPD4]] | C | MAGEB2 activity raises FRMPD4's level | lines that do not express MAGEB2 (42) vs lines expressing it (8) | 2.54× lower at baseline in the lines without MAGEB2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, MAGEA10, TBXT; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.6, 16.9); signed map (30.6, 35.0). **Vector** length 21.5, 8.26% of its response variance represented; |z| ≥ 3 in 119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +1.5 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.5 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.5 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -0.9 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.7 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.6 | -0.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.6 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MAGE family member B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.2 — chrX:30,215,563-30,220,089 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAM6, MAGE-XP-2, MGC26438, CT3.2 |
| Gene groups (HGNC) | MAGE family |
| Matched by | ensembl_id |

**Function**, from UniProt [O15479](https://www.uniprot.org/uniprotkb/O15479) (Melanoma-associated antigen B2):

> May enhance ubiquitin ligase activity of RING-type zinc finger-containing E3 ubiquitin-protein ligases. Proposed to act through recruitment and/or stabilization of the Ubl-conjugating enzyme (E2) at the E3:substrate complex.

**Summary**, from NCBI Gene [4113](https://www.ncbi.nlm.nih.gov/gene/4113):

> This gene is a member of the MAGEB gene family. The members of this family have their entire coding sequences located in the last exon, and the encoded proteins show 50 to 68% sequence identity to each other. The promoters and first exons of the MAGEB genes show considerable variability, suggesting that the existence of this gene family enables the same function to be expressed under different transcriptional controls. This gene is localized in the DSS (dosage-sensitive sex reversal) critical …

**Accessions** — [HGNC:6809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6809) · Entrez [4113](https://www.ncbi.nlm.nih.gov/gene/4113) · UniProt [O15479](https://www.uniprot.org/uniprotkb/O15479) · Ensembl [ENSG00000099399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099399)

## Data

Gene col 1803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1803); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1803]; `tensor/DDL_lfc|DDL_z.npy` [1803]; `embed/gene_vectors.npy` [1803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1803 or target_col == 1803). Every well: [[MAGEB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGEB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
