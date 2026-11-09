---
symbol: "CTDSPL2-DT"
type: "gene"
col: 15218
ensembl_id: "ENSG00000259595"
name: "CTDSPL2 divergent transcript"
location: "15q15.3"
module: 21
arm: "+"
pooled_cpm: 3.03
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CTDSPL2-DT

*CTDSPL2 divergent transcript* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.98× (z +14.8, q 0e+00, up in 36 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (HOP62 0.0576×); [[vincristine (drug)]] 0.05 µM in 1 line (J82 0.0547×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.89, fdr 7e-06), [[EHBP1-AS1]] (+0.86, fdr 7e-06), [[C2CD5-AS1]] (+0.84, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.98×** | +14.8 | 0e+00 | 36/37 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.4 | 1e-18 | 16/19 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.6 | 1e-15 | 4/5 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +7.7 | 2e-12 | 17/35 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +7.7 | 2e-12 | 4/6 (AsPC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.0 | 2e-07 | 12/31 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.5 | 2e-06 | 6/17 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.7 | 2e-04 | 12/36 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.5 | 0.030 | 7/35 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.038 | 12/43 (HEC-1-A, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.086 | 6/46 (HOP62, SW1417, …) | top dose only | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.086 | 3/41 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.089 | 1/29 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (HOP62 0.0576×); [[vincristine (drug)]] 0.05 µM in 1 line (J82 0.0547×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -3.9 | 0.062 | 18/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.92 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 2.91 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0576× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 3.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +9.3) | — |
| [[J82 (line)]] | alt | 2.68 | 0 | 1 | — | [[vincristine (drug)]] 0.05 µM 0.0547× (z -8.6) |
| [[A-172 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.89 | +0.77 / +0.86 | both halves | 7e-06 |  |
| [[EHBP1-AS1]] | +0.86 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[C2CD5-AS1]] | +0.84 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.83 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.82 | +0.77 / +0.80 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.82 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.81 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[ASB14]] | +0.81 | +0.79 / +0.85 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.81 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.81 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.80 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[PRKCA-AS1]] | +0.80 | +0.74 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CTDSPL2-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYT1L]] | B | MYT1L activity raises CTDSPL2-DT's level | lines that do not express MYT1L (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without MYT1L | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01811, XIRP2, ENSG00000232855; maybe low, not absent |
| [[LINC01579]] | B | LINC01579 activity raises CTDSPL2-DT's level | lines that do not express LINC01579 (13) vs lines expressing it (37) | 1.11× lower at baseline in the lines without LINC01579 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, CNTNAP2, CACNA1C; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.894). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.7, 27.0); signed map (32.9, 5.1). **Vector** length 41.2, 4.13% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CTDSPL2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q15.3 — chr15:44,402,685-44,427,144 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55415) · Entrez [120017340](https://www.ncbi.nlm.nih.gov/gene/120017340) · Ensembl [ENSG00000259595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259595)

## Data

Gene col 15218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15218); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15218]; `tensor/DDL_lfc|DDL_z.npy` [15218]; `embed/gene_vectors.npy` [15218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15218 or target_col == 15218). Every well: [[CTDSPL2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTDSPL2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
