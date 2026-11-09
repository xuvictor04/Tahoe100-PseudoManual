---
symbol: "ACAP1"
type: "gene"
col: 1032
ensembl_id: "ENSG00000072818"
name: "ArfGAP with coiled-coil, ankyrin repeat and PH domains 1"
location: "17p13.1"
module: 4
arm: "-"
pooled_cpm: 3.4
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ACAP1

*ArfGAP with coiled-coil, ankyrin repeat and PH domains 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.20× (z +7.4, q 9e-11, up in 6 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +4.5, q 0.001, up in 19 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.550× (z -4.0, q 0.043, down in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0622×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF9]] (+0.76, fdr 7e-06), [[FKBP2]] (+0.73, fdr 7e-06, ⚠ FKBP2 in the vector space only through flagged drug-doses), [[DCTN6-DT]] (+0.71, fdr 1e-05), [[KDM5B]] (+0.68, fdr 7e-06); moves opposite to [[PRKDC]] (-0.70, fdr 7e-06), [[ELAC2]] (-0.69, fdr 7e-06), [[NUP155]] (-0.69, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOTAIRM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +7.4 | 9e-11 | 6/6 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +4.9 | 3e-04 | 7/17 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.5 | 0.001 | 19/33 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +4.1 | 0.005 | 3/6 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +4.0 | 0.009 | 13/37 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.38×** | +3.6 | 0.028 | 9/28 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.72×** | +3.6 | 0.031 | 5/20 (A498, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.070 | 7/18 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.09× | +3.1 | 0.13 | 6/21 (A-427, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.58× | +3.0 | 0.15 | 8/32 (C32, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1032.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0622×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.550×** | -4.0 | 0.043 | 21/45 (Hs 766T, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.612× | -3.3 | 0.31 | 11/46 (HOP62, SW 1271, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.622× | -3.1 | 0.31 | 13/40 (COLO 205, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.632× | -3.0 | 0.31 | 10/39 (C32, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.77 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0622× (z -8.6) |
| [[A-172 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF9]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[FKBP2]] ⚠ | +0.73 | +0.61 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DCTN6-DT]] | +0.71 | +0.53 / +0.79 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.66 | +0.53 / +0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRIM7-AS2]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[IFI27L2]] | +0.66 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[MED19]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.65 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[SNHG9]] | +0.65 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[BTG1]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[POLR1H]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[METTL23]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.70 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[ELAC2]] | -0.69 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[NUP155]] | -0.69 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[PRPS1]] | -0.68 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[DROSHA]] | -0.68 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[RPE]] | -0.68 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[IPO5]] | -0.68 | -0.49 / -0.77 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.67 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.65 | -0.46 / -0.74 | both halves | 2e-05 |  |
| [[MTHFD1]] | -0.65 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[TMX1]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[UGGT1]] | -0.65 | -0.53 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOTAIRM1]] | B | HOTAIRM1 activity raises ACAP1's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without HOTAIRM1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.6, -30.4); signed map (-6.0, 11.3). **Vector** length 51.2, 7.76% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with coiled-coil, ankyrin repeat and PH domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,336,529-7,351,477 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0050; previously CENTB1 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15027](https://www.uniprot.org/uniprotkb/Q15027) (Arf-GAP with coiled-coil, ANK repeat and PH domain-containing protein 1):

> GTPase-activating protein (GAP) for ADP ribosylation factor 6 (ARF6) required for clathrin-dependent export of proteins from recycling endosomes to trans-Golgi network and cell surface. Required for regulated export of ITGB1 from recycling endosomes to the cell surface and ITGB1-dependent cell migration.

**Summary**, from NCBI Gene [9744](https://www.ncbi.nlm.nih.gov/gene/9744):

> Predicted to enable GTPase activator activity and zinc ion binding activity. Predicted to be involved in protein transport. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16467) · Entrez [9744](https://www.ncbi.nlm.nih.gov/gene/9744) · UniProt [Q15027](https://www.uniprot.org/uniprotkb/Q15027) · Ensembl [ENSG00000072818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072818)

## Data

Gene col 1032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1032); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1032]; `tensor/DDL_lfc|DDL_z.npy` [1032]; `embed/gene_vectors.npy` [1032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1032 or target_col == 1032). Every well: [[ACAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
