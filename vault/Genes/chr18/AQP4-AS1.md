---
symbol: "AQP4-AS1"
type: "gene"
col: 15281
ensembl_id: "ENSG00000260372"
name: "AQP4 antisense RNA 1"
location: "18q11.2"
module: 140
arm: "+"
pooled_cpm: 4.38
n_lines_expressing: 44
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# AQP4-AS1

*AQP4 antisense RNA 1* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.05× (z +19.6, q 0e+00, up in 21 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.0843×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.131×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PART1]] (+0.79, fdr 7e-06), [[LINC02755]] (+0.76, fdr 7e-06), [[LANCL1-AS1]] (+0.72, fdr 2e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.05×** | +19.6 | 0e+00 | 21/22 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.30×** | +11.5 | 3e-28 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +11.2 | 7e-27 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +10.9 | 2e-25 | 4/8 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.70×** | +8.5 | 3e-15 | 16/30 (SW 900, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.43×** | +7.6 | 3e-12 | 18/33 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.2 | 4e-08 | 6/24 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +5.7 | 1e-06 | 7/25 (C32, J82, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.6 | 2e-06 | 8/20 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.4 | 7e-04 | 10/37 (SHP-77, Hs 766T, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.1 | 0.002 | 1/7 (LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.005 | 2/28 (SK-MEL-2, SW1417) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.015 | 5/37 (A549, HEC-1-A, …) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.3 | 0.038 | 0/27 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.049 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.049 | 1/15 (SW 900) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15281.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.0843×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.131×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.685× | -3.2 | 0.45 | 7/29 (KATO III, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.684× | -3.0 | 0.45 | 4/28 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.0 | 0.45 | 9/40 (SW1417, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 159 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.60× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -14.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 1.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +10.1) | — |
| [[A549 (line)]] | wt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 3.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 4.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +8.7) | — |
| [[A-172 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PART1]] | +0.79 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LINC02755]] | +0.76 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.72 | +0.48 / +0.72 | both halves | 2e-05 | same gene group |
| [[LINC00922]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SORCS3]] | +0.72 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[C12orf40]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.68 | +0.39 / +0.65 | both halves | 5e-05 | same gene group |
| [[PCDH15]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ANO3]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC02006]] | +0.68 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[HPSE2]] | +0.67 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[GALNT17]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AQP4-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FENDRR]] | B | FENDRR activity raises AQP4-AS1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.13× lower at baseline in the lines without FENDRR | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.2, 26.2); signed map (32.9, 10.9). **Vector** length 38.8, 4.88% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +19.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | +0.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | AQP4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q11.2 — chr18:26,655,737-27,190,698 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ30507; previously C18orf16, CHST9-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [147429](https://www.ncbi.nlm.nih.gov/gene/147429):

> Predicted to be involved in RNA processing and SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be located in nucleolus. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26399) · Entrez [147429](https://www.ncbi.nlm.nih.gov/gene/147429) · Ensembl [ENSG00000260372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260372)

## Data

Gene col 15281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15281); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15281]; `tensor/DDL_lfc|DDL_z.npy` [15281]; `embed/gene_vectors.npy` [15281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15281 or target_col == 15281). Every well: [[AQP4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AQP4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
