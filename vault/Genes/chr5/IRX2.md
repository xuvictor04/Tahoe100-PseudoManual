---
symbol: "IRX2"
type: "gene"
col: 9975
ensembl_id: "ENSG00000170561"
name: "iroquois homeobox 2"
location: "5p15.33"
module: 20
arm: "-"
pooled_cpm: 5.9
n_lines_expressing: 20
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IRX2

*iroquois homeobox 2* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.77× (z +8.4, q 2e-14, up in 14 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.0766×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.147×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.164×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TWIST1]] (+0.56, fdr 2e-05), [[POLR1H]] (+0.56, fdr 3e-05), [[ZIC2]] (+0.56, fdr 1e-05); moves opposite to [[UGGT1]] (-0.50, fdr 1e-04), [[PSMD2]] (-0.49, fdr 5e-05), [[API5]] (-0.49, fdr 3e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Pralsetinib (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +8.4 | 2e-14 | 14/16 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.69×** | +7.4 | 5e-11 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.58×** | +7.2 | 1e-10 | 11/13 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.99×** | +5.7 | 2e-06 | 11/16 (COLO 205, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +5.5 | 6e-06 | 10/16 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +4.7 | 2e-04 | 1/8 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.16×** | +4.5 | 6e-04 | 3/11 (SW1417, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.0 | 0.004 | 8/14 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +3.7 | 0.013 | 14/16 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.25×** | +3.4 | 0.041 | 4/13 (SNU-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.23×** | +3.4 | 0.041 | 6/15 (SW48, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +3.3 | 0.044 | 8/16 (NCI-H460, BT-474, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.71×** | +3.1 | 0.079 | 7/13 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.079 | 0/16 | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.1 | 0.079 | 2/15 (SW 900, SW480) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9975.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.0766×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.147×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.164×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.553× | -3.2 | 0.45 | 6/18 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.359× | -3.2 | 0.45 | 1/17 (SNU-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.870× | -3.0 | 0.46 | 7/18 (NCI-H2347, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 122 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0766× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 2.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 10.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +8.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.2) | — |
| [[A-172 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWIST1]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[POLR1H]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZIC2]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[IRX5]] | +0.54 | +0.39 / +0.59 | both halves | 5e-05 | same gene group; STRING 408 |
| [[TNFRSF10C]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[SLC35E3]] | +0.52 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[ZNF330]] | +0.51 | +0.37 / +0.58 | both halves | 7e-05 |  |
| [[SNHG9]] | +0.51 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[RANGRF]] | +0.50 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[APOC1]] | +0.50 | +0.20 / +0.61 | both halves | 7e-04 |  |
| [[CD247]] | +0.49 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[LRRC37B]] | +0.48 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGGT1]] | -0.50 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[PSMD2]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[API5]] | -0.49 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[TGOLN2]] | -0.48 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[SRP9]] | -0.48 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[DLD]] | -0.47 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[CDC42]] | -0.47 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[CLTC]] | -0.46 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[GTF3C1]] | -0.46 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ACTR3]] | -0.46 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[AGO1]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[SUDS3]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Pralsetinib (drug)]] 5 µM | B | IRX2 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express IRX2 (30) vs lines expressing it (18) | the lines without IRX2: 0.86× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000251652, NRK, HEPHL1 |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.440). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (21.5, -3.9); signed map (-4.4, 5.5). **Vector** length 41.8, 12.7% of its response variance represented; |z| ≥ 3 in 252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.8 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +7.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +0.8 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.7 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.7 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | iroquois homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:2,745,845-2,751,677 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Reactome | 2 pathways, smallest: Nephron development; Kidney development |
| Matched by | ensembl_id |

UniProt [Q9BZI1](https://www.uniprot.org/uniprotkb/Q9BZI1) carries no function annotation.

**Summary**, from NCBI Gene [153572](https://www.ncbi.nlm.nih.gov/gene/153572):

> IRX2 is a member of the Iroquois homeobox gene family. Members of this family appear to play multiple roles during pattern formation of vertebrate embryos.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:14359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14359) · Entrez [153572](https://www.ncbi.nlm.nih.gov/gene/153572) · UniProt [Q9BZI1](https://www.uniprot.org/uniprotkb/Q9BZI1) · Ensembl [ENSG00000170561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170561)

## Data

Gene col 9975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9975); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9975]; `tensor/DDL_lfc|DDL_z.npy` [9975]; `embed/gene_vectors.npy` [9975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9975 or target_col == 9975). Every well: [[IRX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
