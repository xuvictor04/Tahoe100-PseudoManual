---
symbol: "PAFAH1B3"
type: "gene"
col: 1259
ensembl_id: "ENSG00000079462"
name: "platelet activating factor acetylhydrolase 1b catalytic subunit 3"
location: "19q13.1"
module: 83
arm: "-"
pooled_cpm: 9.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# PAFAH1B3

*platelet activating factor acetylhydrolase 1b catalytic subunit 3* — 19q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.66× (z +10.4, q 2e-22, up in 32 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.86× (z +8.4, q 1e-14, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.519× (z -7.4, q 7e-11, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANTKMT]] (+0.78, fdr 2e-05), [[C20orf27]] (+0.74, fdr 8e-06), [[KCTD17]] (+0.72, fdr 3e-05); moves opposite to [[SMIM15-AS1]] (-0.72, fdr 6e-05), [[MFF-DT]] (-0.72, fdr 8e-05), [[PCBP1-AS1]] (-0.72, fdr 1e-04).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.66×** | +10.4 | 2e-22 | 32/35 (PANC-1, A498, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.86×** | +8.4 | 1e-14 | 39/46 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.50×** | +7.3 | 4e-11 | 38/47 (HT-29, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.49×** | +7.0 | 3e-10 | 14/16 (LOX-IMVI, A498, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.46×** | +6.7 | 3e-09 | 18/23 (KATO III, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.05×** | +5.7 | 9e-07 | 35/47 (A-172, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.5 | 7e-04 | 27/37 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.70×** | +4.2 | 0.002 | 23/37 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +3.7 | 0.012 | 19/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.57×** | +3.5 | 0.028 | 14/35 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.058 | 18/46 (HEC-1-A, A-427, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.063 | 16/47 (NCI-H460, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.519×** | -7.4 | 7e-11 | 33/43 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -6.8 | 3e-09 | 25/42 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -4.2 | 0.004 | 22/43 (SW48, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.579×** | -4.1 | 0.005 | 20/45 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -3.7 | 0.026 | 20/47 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.403×** | -3.4 | 0.055 | 17/42 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.666× | -3.1 | 0.16 | 15/45 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.447× | -3.1 | 0.16 | 6/45 (A498, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -9.5) |
| [[SW48 (line)]] | wt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0444× (z -11.1) |
| [[SW480 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.5) |
| [[A-172 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTKMT]] | +0.78 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[C20orf27]] | +0.74 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[KCTD17]] | +0.72 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[SNRNP25]] | +0.72 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.71 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TMEM256]] | +0.68 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[TSPAN33]] | +0.68 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[TMEM160]] | +0.68 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LAGE3]] | +0.66 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[SMYD3]] | +0.66 | +0.52 / +0.26 | both halves | 4e-04 |  |
| [[YIF1B]] | +0.66 | +0.38 / +0.40 | both halves | 6e-05 |  |
| [[TMEM14A]] | +0.66 | +0.51 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | -0.72 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[MFF-DT]] | -0.72 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[PCBP1-AS1]] | -0.72 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[PBLD]] | -0.71 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[ATXN1L]] | -0.71 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[GLIPR1-AS1]] | -0.70 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZFHX2-AS1]] | -0.69 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | -0.68 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[CCT6B]] | -0.68 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[MMADHC-DT]] | -0.68 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[DHX38]] | -0.67 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[LINC01134]] | -0.67 | -0.46 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAM]] | B | BCAM activity raises PAFAH1B3's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without BCAM | 0.015 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[RAC3]] | B | RAC3 activity raises PAFAH1B3's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without RAC3 | 0.049 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |
| [[FCHO1]] | B | FCHO1 activity raises PAFAH1B3's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without FCHO1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[SIGIRR]] | B | SIGIRR activity lowers PAFAH1B3's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without SIGIRR | 0.074 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.804). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.9, -5.0); signed map (-31.2, 2.5). **Vector** length 63.1, 13.1% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.6 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.6 | +7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +3.3 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.0 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | platelet activating factor acetylhydrolase 1b catalytic subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.1 — chr19:42,297,033-42,303,546 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 5 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15102](https://www.uniprot.org/uniprotkb/Q15102) (Platelet-activating factor acetylhydrolase IB subunit alpha1):

> Alpha1 catalytic subunit of the cytosolic type I platelet-activating factor (PAF) acetylhydrolase (PAF-AH (I)) heterotetrameric enzyme that catalyzes the hydrolyze of the acetyl group at the sn-2 position of PAF and its analogs and modulates the action of PAF. The activity and substrate specificity of PAF-AH (I) are affected by its subunit composition. Both alpha1/alpha1 homodimer (PAFAH1B3/PAFAH1B3 homodimer) and alpha1/alpha2 heterodimer(PAFAH1B3/PAFAH1B2 heterodimer) hydrolyze …

**Summary**, from NCBI Gene [5050](https://www.ncbi.nlm.nih.gov/gene/5050):

> This gene encodes an acetylhydrolase that catalyzes the removal of an acetyl group from the glycerol backbone of platelet-activating factor. The encoded enzyme is a subunit of the platelet-activating factor acetylhydrolase isoform 1B complex, which consists of the catalytic beta and gamma subunits and the regulatory alpha subunit. This complex functions in brain development. A translocation between this gene on chromosome 19 and the CDC-like kinase 2 gene on chromosome 1 has been observed, and …

**Accessions** — [HGNC:8576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8576) · Entrez [5050](https://www.ncbi.nlm.nih.gov/gene/5050) · UniProt [Q15102](https://www.uniprot.org/uniprotkb/Q15102) · Ensembl [ENSG00000079462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079462)

## Data

Gene col 1259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1259); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1259]; `tensor/DDL_lfc|DDL_z.npy` [1259]; `embed/gene_vectors.npy` [1259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1259 or target_col == 1259). Every well: [[PAFAH1B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAFAH1B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
