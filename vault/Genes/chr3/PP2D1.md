---
symbol: "PP2D1"
type: "gene"
col: 11478
ensembl_id: "ENSG00000183977"
name: "protein phosphatase 2C like domain containing 1"
location: "3p24.3"
module: 21
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PP2D1

*protein phosphatase 2C like domain containing 1* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +9.0, q 9e-17, up in 17 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +5.5, q 5e-06, up in 16 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0671×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H460 0.103×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOGT-DT]] (+0.87, fdr 7e-06), [[ZRANB2-AS1]] (+0.87, fdr 7e-06), [[FLJ40194]] (+0.87, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +9.0 | 9e-17 | 17/23 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +7.8 | 2e-12 | 4/7 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.4 | 2e-11 | 4/6 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.5 | 5e-06 | 16/36 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +5.5 | 5e-06 | 8/22 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.8 | 0.012 | 10/35 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.012 | 6/33 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.014 | 7/44 (LS 180, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.014 | 10/44 (HEC-1-A, H4, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.5 | 0.025 | 3/27 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.30×** | +3.5 | 0.028 | 5/36 (LoVo, LOX-IMVI, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.038 | 5/44 (NCI-H460, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.2 | 0.059 | 1/15 (KATO III) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.061 | 3/37 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.55×** | +3.0 | 0.086 | 3/8 (A-172, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11478.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0671×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H460 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 0.728× | -3.2 | 0.91 | 10/29 (LS 180, HS-578T, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0671× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 3.16 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.103× (z -9.9) |
| [[A-172 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOGT-DT]] | +0.87 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.87 | +0.78 / +0.85 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.87 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.85 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.83 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.83 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.82 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.82 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[CCDC65]] | +0.82 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.81 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[SLC3A1]] | +0.81 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.80 | +0.72 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | PP2D1's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | PP2D1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.041 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, 28.1); signed map (33.7, 5.6). **Vector** length 36.5, 3.38% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2C like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:19,979,961-20,012,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25449; previously C3orf48 |
| Matched by | ensembl_id |

UniProt [A8MPX8](https://www.uniprot.org/uniprotkb/A8MPX8) carries no function annotation.

**Summary**, from NCBI Gene [151649](https://www.ncbi.nlm.nih.gov/gene/151649):

> Predicted to enable protein serine/threonine phosphatase activity. Predicted to be involved in negative regulation of MAPK cascade and signal transduction. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28406) · Entrez [151649](https://www.ncbi.nlm.nih.gov/gene/151649) · UniProt [A8MPX8](https://www.uniprot.org/uniprotkb/A8MPX8) · Ensembl [ENSG00000183977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183977)

## Data

Gene col 11478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11478); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11478]; `tensor/DDL_lfc|DDL_z.npy` [11478]; `embed/gene_vectors.npy` [11478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11478 or target_col == 11478). Every well: [[PP2D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PP2D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
