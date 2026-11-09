---
symbol: "LLPH"
type: "gene"
col: 6283
ensembl_id: "ENSG00000139233"
name: "LLP homolog, long-term synaptic facilitation factor"
location: "12q14.3"
module: 11
arm: "+"
pooled_cpm: 26.23
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# LLPH

*LLP homolog, long-term synaptic facilitation factor* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.42× (z +9.1, q 7e-17, up in 43 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.75× (z +8.7, q 8e-16, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 0.181×, HepG2/C3A 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRFAP1L1]] (+0.79, fdr 7e-06), [[TRMT10C]] (+0.78, fdr 7e-06), [[ZNF75A]] (+0.74, fdr 7e-06); moves opposite to [[STT3B]] (-0.66, fdr 9e-06), [[SETD3]] (-0.65, fdr 7e-06), [[CRTAP]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRP11]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +9.1 | 7e-17 | 43/45 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.75×** | +8.7 | 8e-16 | 44/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.05×** | +7.7 | 4e-12 | 44/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.06×** | +7.4 | 2e-11 | 41/47 (C32, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +7.3 | 4e-11 | 38/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.61×** | +7.2 | 7e-11 | 36/47 (HS-578T, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.60×** | +5.0 | 4e-05 | 36/48 (LoVo, SNU-423, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.8 | 1e-04 | 32/47 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.7 | 1e-04 | 35/48 (PANC-1, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.55×** | +4.7 | 2e-04 | 25/44 (A498, NCI-H23, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.51×** | +4.4 | 6e-04 | 34/45 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.50×** | +4.3 | 7e-04 | 30/47 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.50×** | +4.3 | 8e-04 | 26/48 (LoVo, HOP62, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 27/48 (PANC-1, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.005 | 21/48 (C32, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.029 | 24/47 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.062 | 20/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.067 | 17/48 (HT-29, KATO III, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 0.181×, HepG2/C3A 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.6) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HS-578T (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.0) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.66× (z +9.8) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1L1]] | +0.79 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.78 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.74 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[SURF6]] | +0.74 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[PHAX]] | +0.74 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[RPP14]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.73 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[UTP3]] | +0.71 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[EID2]] | +0.71 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[MRM2]] | +0.71 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[KTI12]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.66 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[SETD3]] | -0.65 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[CRTAP]] | -0.62 | -0.56 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP11]] | C | LRP11's natural level strengthens LLPH's drug response | LRP11's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.13; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.8, 2.3); signed map (-1.1, -20.8). **Vector** length 76.5, 19.0% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.7 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | -3.3 | +4.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LLP homolog, long-term synaptic facilitation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:66,116,555-66,130,750 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14817, hLLP; previously C12orf31 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRT6](https://www.uniprot.org/uniprotkb/Q9BRT6) (Protein LLP homolog):

> In hippocampal neurons, regulates dendritic and spine growth and synaptic transmission.

**Summary**, from NCBI Gene [84298](https://www.ncbi.nlm.nih.gov/gene/84298):

> Enables RNA binding activity. Predicted to be involved in dendrite extension and positive regulation of dendritic spine development. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28229) · Entrez [84298](https://www.ncbi.nlm.nih.gov/gene/84298) · UniProt [Q9BRT6](https://www.uniprot.org/uniprotkb/Q9BRT6) · Ensembl [ENSG00000139233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139233)

## Data

Gene col 6283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6283); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6283]; `tensor/DDL_lfc|DDL_z.npy` [6283]; `embed/gene_vectors.npy` [6283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6283 or target_col == 6283). Every well: [[LLPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LLPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
