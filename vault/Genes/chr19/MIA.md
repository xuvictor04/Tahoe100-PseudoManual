---
symbol: "MIA"
type: "gene"
col: 15373
ensembl_id: "ENSG00000261857"
name: "MIA SH3 domain containing"
location: "19q13.2"
module: 37
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 40
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# MIA

*MIA SH3 domain containing* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.08× (z +16.5, q 0e+00, up in 20 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB12]] (+0.74, fdr 7e-06), [[SNX31]] (+0.73, fdr 7e-06), [[DCAF4L1]] (+0.72, fdr 7e-06); moves opposite to [[OCRL]] (-0.66, fdr 3e-05), [[ECHS1]] (-0.65, fdr 3e-05), [[API5]] (-0.65, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[EMC1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.08×** | +16.5 | 0e+00 | 20/20 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.29×** | +11.2 | 2e-26 | 1/1 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.13×** | +9.7 | 4e-20 | 7/10 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.98×** | +9.6 | 1e-19 | 14/22 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.95×** | +9.0 | 3e-17 | 12/16 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.51×** | +8.0 | 8e-14 | 3/4 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.68×** | +7.3 | 2e-11 | 7/7 (KATO III, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.66×** | +7.3 | 2e-11 | 16/21 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +6.7 | 1e-09 | 7/9 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.97×** | +5.7 | 8e-07 | 5/34 (PANC-1, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.88×** | +5.3 | 6e-06 | 5/24 (SW48, LoVo, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +4.2 | 0.001 | 4/10 (SK-MEL-2, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.7 | 0.010 | 3/18 (HOP62, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.74×** | +3.3 | 0.040 | 12/34 (SW 900, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.047 | 6/24 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.71×** | +3.2 | 0.049 | 1/11 (SW480) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.04×** | +3.0 | 0.079 | 5/10 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **1.66×** | +3.0 | 0.081 | 2/35 (HEC-1-A, A-427) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Asciminib (drug)]] 0.5 µM |  | 0.590× | -3.2 | 0.36 | 8/34 (COLO 205, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.576× | -3.1 | 0.36 | 8/34 (SHP-77, AN3 CA, …) | top dose only | plate-row cell shift |
| [[Allantoin (drug)]] 5 µM |  | 0.696× | -3.1 | 0.36 | 7/33 (NCI-H1573, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.67 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.754 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.973 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.957 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.649 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.731 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB12]] | +0.74 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SNX31]] | +0.73 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CASS4]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 | same gene group |
| [[PP2D1]] | +0.70 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PIWIL2]] | +0.70 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.69 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SPATC1]] | +0.69 | +0.46 / +0.72 | both halves | 2e-05 |  |
| [[SPX]] | +0.68 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LINC01482]] | +0.67 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.67 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCRL]] | -0.66 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[ECHS1]] | -0.65 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[API5]] | -0.65 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[DLAT]] | -0.64 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ZDHHC21]] | -0.62 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[DLD]] | -0.62 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[FARSB]] | -0.61 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[PHF6]] | -0.61 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[BCKDK]] | -0.60 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TTLL12]] | -0.59 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[USP14]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PDHA1]] | -0.59 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MIA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMC1-AS1]] | B | MIA activity raises EMC1-AS1's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without MIA | 0.046 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CCNP]] | B | MIA activity raises CCNP's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.71× lower at baseline in the lines without MIA | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LDHC]] | B | MIA activity raises LDHC's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without MIA | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[APOE]] | B | MIA activity raises APOE's level | lines that do not express MIA (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without MIA | 0.088 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HLA-DMA]] | B | MIA activity raises HLA-DMA's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.37× lower at baseline in the lines without MIA | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, -17.8); signed map (11.4, 5.2). **Vector** length 35.7, 4.85% of its response variance represented; |z| ≥ 3 in 647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +0.9 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MIA SH3 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,771,648-40,777,490 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD-RAP, MIA1 |
| Gene groups (HGNC) | MIA family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16674](https://www.uniprot.org/uniprotkb/Q16674) (Melanoma-derived growth regulatory protein):

> Elicits growth inhibition on melanoma cells in vitro as well as some other neuroectodermal tumors, including gliomas.

**Summary**, from NCBI Gene [8190](https://www.ncbi.nlm.nih.gov/gene/8190):

> Predicted to enable growth factor activity. Predicted to be involved in extracellular matrix organization. Predicted to act upstream of or within cell-matrix adhesion. Predicted to be located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7076) · Entrez [8190](https://www.ncbi.nlm.nih.gov/gene/8190) · UniProt [Q16674](https://www.uniprot.org/uniprotkb/Q16674) · Ensembl [ENSG00000261857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261857)

## Data

Gene col 15373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15373); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15373]; `tensor/DDL_lfc|DDL_z.npy` [15373]; `embed/gene_vectors.npy` [15373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15373 or target_col == 15373). Every well: [[MIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
