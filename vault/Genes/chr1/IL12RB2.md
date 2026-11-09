---
symbol: "IL12RB2"
type: "gene"
col: 1331
ensembl_id: "ENSG00000081985"
name: "interleukin 12 receptor subunit beta 2"
location: "1p31.3"
module: 53
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# IL12RB2

*interleukin 12 receptor subunit beta 2* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +12.1, q 4e-31, up in 34 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0823×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW480 0.113×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKD2L2]] (+0.81, fdr 7e-06), [[SPATC1]] (+0.81, fdr 7e-06), [[LINC01618]] (+0.79, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +12.1 | 4e-31 | 34/37 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.70×** | +9.3 | 6e-18 | 29/44 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +9.0 | 3e-17 | 25/38 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +8.1 | 8e-14 | 13/20 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +8.0 | 2e-13 | 1/7 (A498) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +7.3 | 2e-11 | 20/37 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +7.3 | 2e-11 | 1/5 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +6.9 | 3e-10 | 18/38 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.3 | 7e-06 | 20/44 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.3 | 7e-06 | 17/35 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.0 | 3e-05 | 5/21 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.9 | 4e-05 | 13/46 (HOP62, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.5 | 3e-04 | 7/23 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 0.001 | 13/44 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.003 | 9/43 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.026 | 9/40 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.074 | 12/44 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.081 | 3/47 (SW480, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1331.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0823×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW480 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -3.6 | 0.21 | 16/48 (KATO III, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 5.12 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0823× (z -8.8) |
| [[SW480 (line)]] | alt | 3.69 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.113× (z -8.8) |
| [[A-172 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD2L2]] | +0.81 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.81 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[LINC01618]] | +0.79 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.79 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.79 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[MASP2]] | +0.78 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.77 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[TG]] | +0.77 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.76 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[CCNP]] | +0.75 | +0.71 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IL12RB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F2]] | B | F2 activity raises IL12RB2's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.26× lower at baseline in the lines without F2 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, -10.0); signed map (22.1, 10.3). **Vector** length 49.1, 5.39% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 12 receptor subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:67,307,364-67,398,724 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibronectin type III domain containing; Interleukin receptors |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 7 pathways, smallest: Differentiation of naive CD4+ T cells to T helper 1 cells (Th1 cells); Interleukin-35 Signalling; Interleukin-12 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99665](https://www.uniprot.org/uniprotkb/Q99665) (Interleukin-12 receptor subunit beta-2):

> Receptor for interleukin-12. This subunit is the signaling component coupling to the JAK2/STAT4 pathway. Promotes the proliferation of T-cells as well as NK cells. Induces the promotion of T-cells towards the Th1 phenotype by strongly enhancing IFN-gamma production.

**Summary**, from NCBI Gene [3595](https://www.ncbi.nlm.nih.gov/gene/3595):

> The protein encoded by this gene is a type I transmembrane protein identified as a subunit of the interleukin 12 receptor complex. The coexpression of this and IL12RB1 proteins was shown to lead to the formation of high-affinity IL12 binding sites and reconstitution of IL12 dependent signaling. The expression of this gene is up-regulated by interferon gamma in Th1 cells, and plays a role in Th1 cell differentiation. The up-regulation of this gene is found to be associated with a number of …

**Accessions** — [HGNC:5972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5972) · Entrez [3595](https://www.ncbi.nlm.nih.gov/gene/3595) · UniProt [Q99665](https://www.uniprot.org/uniprotkb/Q99665) · Ensembl [ENSG00000081985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081985)

## Data

Gene col 1331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1331); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1331]; `tensor/DDL_lfc|DDL_z.npy` [1331]; `embed/gene_vectors.npy` [1331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1331 or target_col == 1331). Every well: [[IL12RB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL12RB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
