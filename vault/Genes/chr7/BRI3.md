---
symbol: "BRI3"
type: "gene"
col: 8994
ensembl_id: "ENSG00000164713"
name: "brain protein I3"
location: "7q21.3"
module: 24
arm: "+"
pooled_cpm: 67.64
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# BRI3

*brain protein I3* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.56× (z +6.5, q 6e-08, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.734× (z -4.3, q 0.010, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.67, fdr 1e-05), [[COMMD6]] (+0.67, fdr 7e-06), [[SNHG25]] (+0.67, fdr 7e-06); moves opposite to [[PDAP1]] (-0.67, fdr 7e-06), [[DCLRE1A]] (-0.65, fdr 7e-06), [[XRCC5]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NEMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.5 | 6e-08 | 39/48 (SW48, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.9 | 1e-06 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +5.4 | 1e-05 | 35/48 (SW480, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.006 | 32/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +4.0 | 0.006 | 27/48 (SW1417, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.013 | 31/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.015 | 29/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.016 | 25/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.018 | 28/47 (C32, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.018 | 24/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.5 | 0.024 | 27/48 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.030 | 26/48 (HS-578T, A-427, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.067 | 20/48 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.094 | 17/49 (NCI-H2347, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.734×** | -4.3 | 0.010 | 29/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.610×** | -3.7 | 0.048 | 27/48 (SK-MEL-2, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.048 | 24/48 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.3 | 0.12 | 24/48 (RKO, HT-29, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 57.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.98× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.104× (z -9.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 99.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.67 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SAT2]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[LAMTOR4]] | +0.66 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[RENO1]] | +0.66 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[RPLP2]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[RPS21]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.67 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.65 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[CCT7]] | -0.65 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[DARS2]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[PUS7L]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ANP32E]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[HNRNPA2B1]] | -0.61 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[IPO8]] | -0.61 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[EIF4G1]] | -0.60 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[PSMC3]] | -0.60 | -0.61 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEMP2]] | B | NEMP2 activity lowers BRI3's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 1.17× higher at baseline in the lines without NEMP2 | 0.066 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |
| [[SLC28A2-AS1]] | B | SLC28A2-AS1 activity lowers BRI3's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.35× higher at baseline in the lines without SLC28A2-AS1 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.0, -23.6); signed map (-27.8, 7.3). **Vector** length 124, 37.9% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.7 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.1 | +3.7 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +4.6 | +3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | brain protein I3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:98,252,379-98,310,441 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O95415](https://www.uniprot.org/uniprotkb/O95415) (Membrane protein BRI3):

> Participates in tumor necrosis factor-alpha (TNF)-induced cell death. May be a target of Wnt/beta-catenin signaling in the liver.

**Summary**, from NCBI Gene [25798](https://www.ncbi.nlm.nih.gov/gene/25798):

> Enables identical protein binding activity. Predicted to be located in azurophil granule membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1109) · Entrez [25798](https://www.ncbi.nlm.nih.gov/gene/25798) · UniProt [O95415](https://www.uniprot.org/uniprotkb/O95415) · Ensembl [ENSG00000164713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164713)

## Data

Gene col 8994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8994); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8994]; `tensor/DDL_lfc|DDL_z.npy` [8994]; `embed/gene_vectors.npy` [8994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8994 or target_col == 8994). Every well: [[BRI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
