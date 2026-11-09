---
symbol: "SCN1A-AS1"
type: "gene"
col: 14062
ensembl_id: "ENSG00000236107"
name: "SCN1A and SCN9A antisense RNA 1"
location: "2q24.3"
module: 140
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# SCN1A-AS1

*SCN1A and SCN9A antisense RNA 1* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.78× (z +18.8, q 0e+00, up in 21 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0499×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCHLAP1]] (+0.74, fdr 1e-05), [[A2ML1-AS1]] (+0.71, fdr 1e-05), [[ST7-AS2]] (+0.71, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.78×** | +18.8 | 0e+00 | 21/25 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.56×** | +12.9 | 1e-35 | 6/8 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +10.2 | 3e-22 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +7.7 | 2e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.21×** | +6.8 | 2e-09 | 17/39 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +6.2 | 5e-08 | 19/43 (BT-474, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.1 | 3e-05 | 9/31 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.7 | 2e-04 | 2/8 (LoVo, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.6 | 3e-04 | 7/28 (NCI-H460, CHP-212, …) | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.60×** | +4.0 | 0.003 | 4/17 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 3/43 (A498, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.009 | 10/46 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.010 | 3/23 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.015 | 6/36 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.1 | 0.066 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.1 | 0.066 | 2/19 (J82, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.093 | 4/27 (CFPAC-1, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14062.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0499×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.658× | -3.6 | 0.21 | 4/46 (RKO, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.67× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 7.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0499× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCHLAP1]] | +0.74 | +0.50 / +0.86 | both halves | 1e-05 |  |
| [[A2ML1-AS1]] | +0.71 | +0.50 / +0.70 | both halves | 1e-05 | same gene group |
| [[ST7-AS2]] | +0.71 | +0.62 / +0.78 | both halves | 7e-06 | same gene group |
| [[SLC26A5]] | +0.71 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[SORCS3]] | +0.69 | +0.44 / +0.81 | both halves | 3e-05 |  |
| [[FAM217A]] | +0.69 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[DPYD-AS1]] | +0.69 | +0.53 / +0.75 | both halves | 1e-05 | same gene group |
| [[PTPRT]] | +0.68 | +0.46 / +0.79 | both halves | 3e-05 |  |
| [[IL1RAPL2]] | +0.68 | +0.52 / +0.79 | both halves | 1e-05 |  |
| [[USH2A]] | +0.68 | +0.47 / +0.83 | both halves | 2e-05 |  |
| [[CNBD1]] | +0.67 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.66 | +0.41 / +0.80 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SCN1A-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.6, 29.4); signed map (33.8, 8.5). **Vector** length 40.4, 4.25% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | SCN1A and SCN9A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q24.3 — chr2:165,957,188-166,390,771 (+) |
| Ensembl biotype | lncRNA |
| Also known as | SCN1ANAT, SCN1A-NAT |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54069) · Entrez [101929680](https://www.ncbi.nlm.nih.gov/gene/101929680) · Ensembl [ENSG00000236107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236107)

## Data

Gene col 14062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14062); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14062]; `tensor/DDL_lfc|DDL_z.npy` [14062]; `embed/gene_vectors.npy` [14062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14062 or target_col == 14062). Every well: [[SCN1A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCN1A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
