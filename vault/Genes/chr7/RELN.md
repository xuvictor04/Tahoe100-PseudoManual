---
symbol: "RELN"
type: "gene"
col: 12082
ensembl_id: "ENSG00000189056"
name: "reelin"
location: "7q22.1"
module: 165
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# RELN

*reelin* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.62× (z +26.9, q 0e+00, up in 25 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.512×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC26]] (+0.75, fdr 7e-06), [[USH2A]] (+0.75, fdr 7e-06), [[SYT16]] (+0.74, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12082.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.62×** | +26.9 | 0e+00 | 25/27 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.75×** | +14.0 | 4e-42 | 3/5 (hTERT-HPNE, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.27×** | +13.6 | 1e-39 | 31/39 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.21×** | +13.4 | 5e-39 | 7/11 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.41×** | +11.6 | 4e-29 | 30/43 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +11.4 | 3e-28 | 18/27 (hTERT-HPNE, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.70×** | +11.3 | 9e-28 | 3/6 (hTERT-HPNE, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.14×** | +10.0 | 1e-21 | 16/43 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +8.2 | 1e-14 | 13/25 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +7.8 | 4e-13 | 17/32 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +7.3 | 2e-11 | 13/24 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +7.0 | 1e-10 | 15/33 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +6.1 | 4e-08 | 10/33 (C32, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +5.0 | 3e-05 | 1/8 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.1 | 0.002 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.7 | 0.007 | 1/19 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.512×; ⚠ position not correctable).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 2.45 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 50.8× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 3.77 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 1.82 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.77× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 1.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.17× (z +8.8) | — |
| [[A549 (line)]] | wt | 1.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 1.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.512× (z -9.6) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 1.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +10.8) | — |
| [[J82 (line)]] | alt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +8.8) | — |
| [[LoVo (line)]] | wt | 1.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +8.5) | — |
| [[SW480 (line)]] | alt | 1.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.9) | — |
| [[A-172 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC26]] | +0.75 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[USH2A]] | +0.75 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[SYT16]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.74 | +0.56 / +0.81 | both halves | 1e-05 |  |
| [[MIR4300HG]] | +0.74 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.74 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.73 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.73 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.72 | +0.58 / +0.81 | both halves | 7e-06 |  |
| [[RYR3]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.72 | +0.58 / +0.79 | both halves | 8e-06 |  |
| [[GALNTL6]] | +0.71 | +0.56 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RELN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRATD1]] | B | LRATD1 activity raises RELN's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 1.44× lower at baseline in the lines without LRATD1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.0, 30.5); signed map (31.2, 16.5). **Vector** length 52.8, 7.39% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +26.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +14.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +0.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | reelin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:103,471,381-103,989,658 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RL, PRO1598 |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: Reelin signalling pathway; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [P78509](https://www.uniprot.org/uniprotkb/P78509) (Reelin):

> Extracellular matrix serine protease secreted by pioneer neurons that plays a role in layering of neurons in the cerebral cortex and cerebellum by coordinating cell positioning during neurodevelopment. Regulates microtubule function in neurons and neuronal migration. Binding to the extracellular domains of lipoprotein receptors VLDLR and LRP8/APOER2 induces tyrosine phosphorylation of DAB1 and modulation of TAU phosphorylation. Affects migration of sympathetic preganglionic neurons in the …

**Summary**, from NCBI Gene [5649](https://www.ncbi.nlm.nih.gov/gene/5649):

> This gene encodes a large secreted extracellular matrix protein thought to control cell-cell interactions critical for cell positioning and neuronal migration during brain development. This protein may be involved in schizophrenia, autism, bipolar disorder, major depression and in migration defects associated with temporal lobe epilepsy. Mutations of this gene are associated with autosomal recessive lissencephaly with cerebellar hypoplasia. Two transcript variants encoding distinct isoforms …

**Accessions** — [HGNC:9957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9957) · Entrez [5649](https://www.ncbi.nlm.nih.gov/gene/5649) · UniProt [P78509](https://www.uniprot.org/uniprotkb/P78509) · Ensembl [ENSG00000189056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189056)

## Data

Gene col 12082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12082); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12082]; `tensor/DDL_lfc|DDL_z.npy` [12082]; `embed/gene_vectors.npy` [12082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12082 or target_col == 12082). Every well: [[RELN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
