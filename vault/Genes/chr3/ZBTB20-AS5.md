---
symbol: "ZBTB20-AS5"
type: "gene"
col: 14311
ensembl_id: "ENSG00000242290"
name: "ZBTB20 antisense RNA 5"
location: "3q13.31"
module: 21
arm: "+"
pooled_cpm: 2.98
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ZBTB20-AS5

*ZBTB20 antisense RNA 5* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.53× (z +9.2, q 3e-17, up in 11 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +8.1, q 1e-13, up in 23 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dihydroartemisinin (drug)]] 5 µM in 1 line (HEC-1-A 0.0547×); [[Auranofin (drug)]] 5 µM in 1 line (HS-578T 0.0618×); [[Pentoxifylline (drug)]] 0.05 µM in 1 line (A-172 0.0906×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OMG]] (+0.79, fdr 7e-06), [[C2CD5-AS1]] (+0.78, fdr 7e-06), [[CHMP3-AS1]] (+0.77, fdr 7e-06); moves opposite to [[PHF6]] (-0.63, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AMBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +9.2 | 3e-17 | 11/17 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.3 | 3e-14 | 3/5 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.1 | 1e-13 | 23/35 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.3 | 3e-08 | 14/32 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.7 | 1e-06 | 11/21 (LoVo, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +5.6 | 2e-06 | 1/7 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +4.6 | 3e-04 | 10/44 (NCI-H460, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.002 | 12/43 (AN3 CA, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.002 | 9/35 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.1 | 0.003 | 3/20 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.4 | 0.036 | 8/26 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.048 | 13/43 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.059 | 6/42 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.075 | 5/32 (LOX-IMVI, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14311.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dihydroartemisinin (drug)]] 5 µM in 1 line (HEC-1-A 0.0547×); [[Auranofin (drug)]] 5 µM in 1 line (HS-578T 0.0618×); [[Pentoxifylline (drug)]] 0.05 µM in 1 line (A-172 0.0906×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.860× | -5.4 | 5e-05 | 22/48 (COLO 205, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.733× | -3.1 | 0.58 | 3/45 (CHP-212, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.68 | 0 | 2 (1 ⚠) | — | [[Dihydroartemisinin (drug)]] 5 µM 0.0547× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 2.46 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 14.8× (z +10.1) | — |
| [[A-172 (line)]] | wt | 3.81 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0906× (z -8.9) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 4.18 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0618× (z -9.5) |
| [[A-427 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OMG]] | +0.79 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.78 | +0.62 / +0.80 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.77 | +0.64 / +0.79 | both halves | 7e-06 | same gene group |
| [[SLC23A1]] | +0.77 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[RN7SL1]] | +0.76 | +0.69 / +0.82 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.75 | +0.63 / +0.80 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[EHBP1-AS1]] | +0.73 | +0.63 / +0.72 | both halves | 7e-06 | same gene group |
| [[FLJ40194]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.73 | +0.57 / +0.75 | both halves | 1e-05 | same gene group |
| [[OXR1-AS1]] | +0.73 | +0.63 / +0.71 | both halves | 7e-06 | same gene group |
| [[GEMIN7-AS1]] | +0.73 | +0.62 / +0.72 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF6]] | -0.63 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMBP]] | B | AMBP activity raises ZBTB20-AS5's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.22× lower at baseline in the lines without AMBP | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[TOP2A]] | B | TOP2A activity lowers ZBTB20-AS5's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 27.1); signed map (33.2, 4.7). **Vector** length 41.7, 4.20% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.3 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -5.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ZBTB20 antisense RNA 5 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q13.31 — chr3:114,445,521-114,529,452 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52841) · Entrez [101929754](https://www.ncbi.nlm.nih.gov/gene/101929754) · Ensembl [ENSG00000242290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242290)

## Data

Gene col 14311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14311); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14311]; `tensor/DDL_lfc|DDL_z.npy` [14311]; `embed/gene_vectors.npy` [14311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14311 or target_col == 14311). Every well: [[ZBTB20-AS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB20-AS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
