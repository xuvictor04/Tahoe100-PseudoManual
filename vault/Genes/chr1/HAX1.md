---
symbol: "HAX1"
type: "gene"
col: 6774
ensembl_id: "ENSG00000143575"
name: "HCLS1 associated protein X-1"
location: "1q21.3"
module: 12
arm: "+"
pooled_cpm: 29.76
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# HAX1

*HCLS1 associated protein X-1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.40× (z +8.2, q 1e-13, up in 33 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.70×, NCI-H460 3.84×, HEC-1-A 4.28×, NCI-H23 3.33×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 4.83×, PANC-1 4.00×, HEC-1-A 4.90×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 7.09×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.615× (z -4.7, q 8e-04, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCC1]] (+0.64, fdr 7e-06), [[NFKBIL1]] (+0.63, fdr 7e-06), [[BUD31]] (+0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ICA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6774.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.70×, NCI-H460 3.84×, HEC-1-A 4.28×, NCI-H23 3.33×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 4.83×, PANC-1 4.00×, HEC-1-A 4.90×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 7.09×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.2 | 1e-13 | 33/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +7.2 | 2e-10 | 39/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.71×** | +5.2 | 3e-05 | 35/46 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.5 | 9e-04 | 21/40 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.39× | +3.1 | 0.25 | 23/44 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -4.7 | 8e-04 | 32/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.616×** | -4.7 | 8e-04 | 36/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.635×** | -4.4 | 0.002 | 34/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tadalafil (drug)]] 5 µM |  | 0.713× | -3.2 | 0.23 | 22/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.722× | -3.0 | 0.28 | 21/46 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +20.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 24.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +9.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0595× (z -9.8) |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0828× (z -8.8) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 64.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCC1]] | +0.64 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[BUD31]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[STK16]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BCAS2]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PLRG1]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MMADHC]] | +0.60 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[UFL1]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RBSN]] | +0.59 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[ZNF205]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[XBP1]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DDIT3]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICA1]] | B | ICA1 activity raises HAX1's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without ICA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.5, 0.5); signed map (-8.2, -8.6). **Vector** length 66.7, 15.9% of its response variance represented; |z| ≥ 3 in 550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.4 | +0.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.4 | +0.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.1 | -0.1 |
|  | [[Acetohexamide (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Drospirenone (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -0.9 | -1.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | HCLS1 associated protein X-1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,272,355-154,275,875 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HS1BP1, HCLSBP1, HAX-1 |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, GLYCOLYSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [O00165](https://www.uniprot.org/uniprotkb/O00165) (HCLS1-associated protein X-1):

> Recruits the Arp2/3 complex to the cell cortex and regulates reorganization of the cortical actin cytoskeleton via its interaction with KCNC3 and the Arp2/3 complex. Slows down the rate of inactivation of KCNC3 channels. Promotes GNA13-mediated cell migration. Involved in the clathrin-mediated endocytosis pathway. May be involved in internalization of ABC transporters such as ABCB11. May inhibit CASP9 and CASP3. Promotes cell survival. May regulate intracellular calcium pools.

**Summary**, from NCBI Gene [10456](https://www.ncbi.nlm.nih.gov/gene/10456):

> The protein encoded by this gene is known to associate with hematopoietic cell-specific Lyn substrate 1, a substrate of Src family tyrosine kinases. It also interacts with the product of the polycystic kidney disease 2 gene, mutations in which are associated with autosomal-dominant polycystic kidney disease, and with the F-actin-binding protein, cortactin. It was earlier thought that this gene product is mainly localized in the mitochondria, however, recent studies indicate it to be localized …

**Accessions** — [HGNC:16915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16915) · Entrez [10456](https://www.ncbi.nlm.nih.gov/gene/10456) · UniProt [O00165](https://www.uniprot.org/uniprotkb/O00165) · Ensembl [ENSG00000143575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143575)

## Data

Gene col 6774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6774); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6774]; `tensor/DDL_lfc|DDL_z.npy` [6774]; `embed/gene_vectors.npy` [6774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6774 or target_col == 6774). Every well: [[HAX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
