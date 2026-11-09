---
symbol: "PSMB6"
type: "gene"
col: 6626
ensembl_id: "ENSG00000142507"
name: "proteasome 20S subunit beta 6"
location: "17p13.2"
module: 64
arm: "+"
pooled_cpm: 33.93
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMB6

*proteasome 20S subunit beta 6* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.13× (z +8.1, q 4e-13, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.84× (z +7.4, q 5e-11, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.242×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA4]] (+0.74, fdr 7e-06), [[PSMB4]] (+0.72, fdr 7e-06), [[PSMA5]] (+0.68, fdr 8e-06); moves opposite to [[TFRC]] (-0.49, fdr 4e-05), [[SIAE]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RNASEL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.13×** | +8.1 | 4e-13 | 41/43 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.84×** | +7.4 | 5e-11 | 46/48 (COLO 205, PANC-1, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.54×** | +6.3 | 5e-08 | 34/38 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.38×** | +6.1 | 1e-07 | 46/47 (COLO 205, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.22×** | +5.3 | 1e-05 | 42/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.7 | 3e-04 | 40/47 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.03×** | +4.6 | 4e-04 | 32/41 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +4.5 | 5e-04 | 43/48 (COLO 205, C32, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.76×** | +4.0 | 0.004 | 34/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.41×** | +3.5 | 0.031 | 32/48 (C32, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6626.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.242×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.402× | -3.4 | 0.26 | 36/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.408× | -3.3 | 0.26 | 35/47 (SNU-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.735× | -3.1 | 0.26 | 25/48 (A498, SW1417, …) | rises with dose |  |
| [[Baicalin (drug)]] 5 µM |  | 0.737× | -3.0 | 0.26 | 29/48 (SNU-1, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 39.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA4]] | +0.74 | +0.82 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB4]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA5]] | +0.68 | +0.72 / +0.58 | both halves | 8e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD7]] | +0.67 | +0.71 / +0.65 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 993 |
| [[ADRM1]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 945 |
| [[PSMB5]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA7]] | +0.64 | +0.66 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[TM2D2]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[BRF2]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PSMA1]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD3]] | +0.61 | +0.74 / +0.48 | both halves | 2e-05 | same gene group; pathway: ABC transporter disorders; STRING 995 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFRC]] | -0.49 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SIAE]] | -0.49 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNASEL]] | B | RNASEL activity lowers PSMB6's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 1.46× higher at baseline in the lines without RNASEL | 0.068 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers PSMB6's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-43.2, -4.3); signed map (-24.2, -24.9). **Vector** length 65.4, 21.1% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.2 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +7.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | -0.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -4.6 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -4.2 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -3.8 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -3.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,796,144-4,798,502 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Y, DELTA |
| Gene groups (HGNC) | Proteasome |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P28072](https://www.uniprot.org/uniprotkb/P28072) (Proteasome subunit beta type-6):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5694](https://www.ncbi.nlm.nih.gov/gene/5694):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. The encoded protein is a member of the proteasome B-type family, …

**Accessions** — [HGNC:9543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9543) · Entrez [5694](https://www.ncbi.nlm.nih.gov/gene/5694) · UniProt [P28072](https://www.uniprot.org/uniprotkb/P28072) · Ensembl [ENSG00000142507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142507)

## Data

Gene col 6626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6626); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6626]; `tensor/DDL_lfc|DDL_z.npy` [6626]; `embed/gene_vectors.npy` [6626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6626 or target_col == 6626). Every well: [[PSMB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
