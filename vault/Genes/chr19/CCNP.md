---
symbol: "CCNP"
type: "gene"
col: 2562
ensembl_id: "ENSG00000105219"
name: "cyclin P"
location: "19q13.2"
module: 53
arm: "+"
pooled_cpm: 3.81
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CCNP

*cyclin P* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.13× (z +14.0, q 1e-41, up in 23 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.191×); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Neratinib (maleate) (drug)]] 0.05 µM in 1 line (HT-29 0.0670×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.76, fdr 7e-06), [[TINCR]] (+0.76, fdr 7e-06), [[ARL9]] (+0.76, fdr 7e-06); moves opposite to [[RPE]] (-0.66, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +14.0 | 1e-41 | 23/29 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +12.0 | 8e-31 | 19/29 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +6.9 | 7e-10 | 17/35 (PANC-1, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +6.1 | 2e-07 | 17/29 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +5.8 | 6e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.9 | 7e-05 | 5/13 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.9 | 7e-05 | 6/42 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.008 | 7/31 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.010 | 3/23 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.012 | 6/24 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.014 | 7/41 (PANC-1, A498, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.022 | 3/23 (LoVo, NCI-H1573, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.4 | 0.030 | 1/5 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.033 | 6/37 (MIA PaCa-2, PANC-1, …) | top dose only | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.44×** | +3.2 | 0.058 | 6/28 (RPMI-7951, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.191×); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Neratinib (maleate) (drug)]] 0.05 µM in 1 line (HT-29 0.0670×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | 0.675× | -3.3 | 0.54 | 10/30 (LoVo, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +11.5) | — |
| [[C32 (line)]] | wt | 2.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 2.55 | 0 | 1 | — | [[Neratinib (maleate) (drug)]] 0.05 µM 0.0670× (z -8.5) |
| [[KATO III (line)]] | alt | 21.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.191× (z -8.7) |
| [[LoVo (line)]] | wt | 3.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 1.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 1.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +10.4) | — |
| [[A-172 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.76 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[TINCR]] | +0.76 | +0.70 / +0.84 | both halves | 7e-06 |  |
| [[ARL9]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.76 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.75 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[PILRA]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.74 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[TEX29]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[USP50]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCNP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIA]] | B | MIA activity raises CCNP's level | lines that do not express MIA (10) vs lines expressing it (40) | 1.71× lower at baseline in the lines without MIA | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NPHS1]] | C | NPHS1 activity lowers CCNP's level | lines that do not express NPHS1 (4) vs lines expressing it (46) | 2.43× higher at baseline in the lines without NPHS1 | 0.043 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.1, -17.2); signed map (14.9, 10.0). **Vector** length 60.8, 9.60% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +14.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.7 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cyclin P |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,222,208-40,226,697 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13265; previously CNTD2 |
| Gene groups (HGNC) | Cyclins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8S5](https://www.uniprot.org/uniprotkb/Q9H8S5) (Cyclin-P):

> Seems to be involved in the regulation of proliferation and migration.

**Summary**, from NCBI Gene [79935](https://www.ncbi.nlm.nih.gov/gene/79935):

> Predicted to enable cyclin-dependent protein serine/threonine kinase regulator activity. Predicted to be involved in G1/S transition of mitotic cell cycle. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25805) · Entrez [79935](https://www.ncbi.nlm.nih.gov/gene/79935) · UniProt [Q9H8S5](https://www.uniprot.org/uniprotkb/Q9H8S5) · Ensembl [ENSG00000105219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105219)

## Data

Gene col 2562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2562); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2562]; `tensor/DDL_lfc|DDL_z.npy` [2562]; `embed/gene_vectors.npy` [2562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2562 or target_col == 2562). Every well: [[CCNP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
