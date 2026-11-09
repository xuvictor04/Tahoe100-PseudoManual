---
symbol: "IRX5"
type: "gene"
col: 10755
ensembl_id: "ENSG00000176842"
name: "iroquois homeobox 5"
location: "16q12.2"
module: 20
arm: "-"
pooled_cpm: 3.41
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IRX5

*iroquois homeobox 5* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.88× (z +16.2, q 0e+00, up in 27 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW 900 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change); [[Dihydroartemisinin (drug)]] 5 µM in 1 line (SW1417 0.0523×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF503]] (+0.71, fdr 7e-06), [[FOXA2]] (+0.70, fdr 7e-06), [[PDCD7]] (+0.70, fdr 7e-06); moves opposite to [[MRPL42]] (-0.64, fdr 3e-05), [[AGO1]] (-0.63, fdr 5e-05), [[PABIR2]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FAM199X]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.88×** | +16.2 | 0e+00 | 27/29 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.44×** | +9.1 | 2e-17 | 21/29 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.25×** | +8.2 | 4e-14 | 15/18 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +6.8 | 2e-09 | 22/27 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.7 | 3e-04 | 13/29 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.70×** | +3.7 | 0.021 | 12/34 (HS-578T, SHP-77, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.66×** | +3.7 | 0.021 | 4/15 (PANC-1, HOP62, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.64×** | +3.6 | 0.023 | 14/37 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.64×** | +3.6 | 0.023 | 4/22 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.030 | 7/40 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | 1.56× | +3.1 | 0.10 | 9/24 (HOP62, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW 900 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change); [[Dihydroartemisinin (drug)]] 5 µM in 1 line (SW1417 0.0523×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.30 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.68× (z +10.5) | — |
| [[A-172 (line)]] | wt | 4.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +9.1) | — |
| [[A498 (line)]] | wt | 3.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +8.8) | — |
| [[A549 (line)]] | wt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 2.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.03× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[SW1417 (line)]] | alt | 3.44 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 5 µM 0.0523× (z -9.2) |
| [[SW480 (line)]] | alt | 4.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +10.1) | — |
| [[A-427 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF503]] | +0.71 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[FOXA2]] | +0.70 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[PDCD7]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ZBTB7A]] | +0.68 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[EFNA2]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ING2]] | +0.67 | +0.46 / +0.77 | both halves | 3e-05 |  |
| [[MSX1]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.63 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[POLR1H]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TPRN]] | +0.63 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[F12]] | +0.62 | +0.31 / +0.72 | both halves | 2e-04 |  |
| [[ZMYM5]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL42]] | -0.64 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[AGO1]] | -0.63 | -0.39 / -0.66 | both halves | 5e-05 |  |
| [[PABIR2]] | -0.63 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[FAM91A1]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[NONO]] | -0.61 | -0.38 / -0.67 | both halves | 6e-05 |  |
| [[HNRNPA3]] | -0.60 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[OPA1]] | -0.60 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[DLD]] | -0.60 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[RPE]] | -0.60 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[AP3M1]] | -0.59 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[RAD23B]] | -0.59 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[API5]] | -0.59 | -0.20 / -0.66 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IRX5's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FKBP9]] | C | FKBP9's natural level strengthens IRX5's drug response | FKBP9's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.28; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM199X]] | B | IRX5 activity raises FAM199X's level | lines that do not express IRX5 (6) vs lines expressing it (44) | 1.29× lower at baseline in the lines without IRX5 | 0.095 | ⚠ within organs, on part of the lines; also absent: ADGRB2, HOXC8, HOXC4 |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.7, -23.8); signed map (-3.7, 8.4). **Vector** length 52.3, 8.61% of its response variance represented; |z| ≥ 3 in 661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.5 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +1.9 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.8 | +1.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +0.8 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | -2.2 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.7 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Ivermectin (drug)]] 5 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | iroquois homeobox 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:54,930,865-54,934,485 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IRX-2a |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [P78411](https://www.uniprot.org/uniprotkb/P78411) (Iroquois-class homeodomain protein IRX-5):

> Establishes the cardiac repolarization gradient by its repressive actions on the KCND2 potassium-channel gene. Required for retinal cone bipolar cell differentiation. May regulate contrast adaptation in the retina and control specific aspects of visual function in circuits of the mammalian retina (By similarity). Could be involved in the regulation of both the cell cycle and apoptosis in prostate cancer cells. Involved in craniofacial and gonadal development. Modulates the migration of …

**Summary**, from NCBI Gene [10265](https://www.ncbi.nlm.nih.gov/gene/10265):

> This gene encodes a member of the iroquois homeobox gene family, which are involved in several embryonic developmental processes. Knockout mice lacking this gene show that it is required for retinal cone bipolar cell differentiation, and that it negatively regulates potassium channel gene expression in the heart to ensure coordinated cardiac repolarization. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:14361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14361) · Entrez [10265](https://www.ncbi.nlm.nih.gov/gene/10265) · UniProt [P78411](https://www.uniprot.org/uniprotkb/P78411) · Ensembl [ENSG00000176842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176842)

## Data

Gene col 10755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10755); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10755]; `tensor/DDL_lfc|DDL_z.npy` [10755]; `embed/gene_vectors.npy` [10755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10755 or target_col == 10755). Every well: [[IRX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
