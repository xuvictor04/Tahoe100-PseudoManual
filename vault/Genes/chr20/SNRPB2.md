---
symbol: "SNRPB2"
type: "gene"
col: 4684
ensembl_id: "ENSG00000125870"
name: "small nuclear ribonucleoprotein polypeptide B2"
location: "20p12.1"
module: 12
arm: "+"
pooled_cpm: 67.26
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SNRPB2

*small nuclear ribonucleoprotein polypeptide B2* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.82× (z +5.4, q 3e-05, up in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 3.44×, NCI-H1573 2.46×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 3.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 4.17×; ⚠ cell-cycle shift, explains ~34% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRBF2]] (+0.75, fdr 7e-06), [[VIRMA]] (+0.73, fdr 7e-06), [[CIR1]] (+0.71, fdr 7e-06); moves opposite to [[AKT1]] (-0.68, fdr 7e-06), [[SMG1P3]] (-0.68, fdr 7e-06), [[NUP188]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 3.44×, NCI-H1573 2.46×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 3.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 4.17×; ⚠ cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +5.4 | 3e-05 | 41/48 (C32, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.83×** | +5.3 | 3e-05 | 40/49 (HCT15, A549, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.66×** | +4.6 | 8e-04 | 41/48 (C32, NCI-H1573, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.63×** | +4.5 | 8e-04 | 42/49 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.69×** | +4.3 | 0.002 | 33/44 (NCI-H23, A549, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.9 | 0.007 | 39/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.51×** | +3.7 | 0.016 | 36/48 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.52×** | +3.6 | 0.021 | 28/42 (A549, PANC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.46×** | +3.3 | 0.056 | 32/48 (C32, A549, …) | two highest doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 55.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 74.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[HCT15 (line)]] | alt | 58.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[NCI-H1573 (line)]] | alt | 35.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 140 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 94.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRBF2]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.73 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CIR1]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[SNW1]] | +0.70 | +0.76 / +0.61 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 997 |
| [[TCEAL8]] | +0.70 | +0.52 / +0.79 | both halves | 1e-05 |  |
| [[MMADHC]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.69 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[BCAS2]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 991 |
| [[SPOP]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 | STRING 634 |
| [[PHAX]] | +0.67 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[ZNF622]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | -0.68 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.68 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[NUP188]] | -0.64 | -0.35 / -0.78 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[DAZAP1]] | -0.63 | -0.56 / -0.65 | both halves | 1e-05 | same gene group |
| [[SUGP2]] | -0.61 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[SELENON]] | -0.61 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[UBQLN4]] | -0.60 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.60 | -0.38 / -0.70 | both halves | 6e-05 |  |
| [[RBBP7]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[UBE2G2]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[CDK2]] | -0.59 | -0.59 / -0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ADAM15]] | -0.59 | -0.58 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises SNRPB2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CDCA7 | 0.055 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.8, -7.4); signed map (-10.2, -9.0). **Vector** length 62.7, 20.4% of its response variance represented; |z| ≥ 3 in 501 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.8 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.6 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | -2.4 | +3.6 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:16,729,961-16,742,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Msl1, U2B'' |
| Gene groups (HGNC) | RNA binding motif containing; U2 small nuclear ribonucleoprotein |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P08579](https://www.uniprot.org/uniprotkb/P08579) (U2 small nuclear ribonucleoprotein B''):

> Involved in pre-mRNA splicing as component of the spliceosome. Associated with sn-RNP U2, where it contributes to the binding of stem loop IV of U2 snRNA.

**Summary**, from NCBI Gene [6629](https://www.ncbi.nlm.nih.gov/gene/6629):

> The protein encoded by this gene associates with stem loop IV of U2 small nuclear ribonucleoprotein (U2 snRNP) in the presence of snRNP-A'. The encoded protein may play a role in pre-mRNA splicing. Autoantibodies from patients with systemic lupus erythematosus frequently recognize epitopes on the encoded protein. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11155) · Entrez [6629](https://www.ncbi.nlm.nih.gov/gene/6629) · UniProt [P08579](https://www.uniprot.org/uniprotkb/P08579) · Ensembl [ENSG00000125870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125870)

## Data

Gene col 4684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4684); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4684]; `tensor/DDL_lfc|DDL_z.npy` [4684]; `embed/gene_vectors.npy` [4684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4684 or target_col == 4684). Every well: [[SNRPB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
