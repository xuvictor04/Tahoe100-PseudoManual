---
symbol: "ST7-AS2"
type: "gene"
col: 13530
ensembl_id: "ENSG00000226367"
name: "ST7 antisense RNA 2"
location: "7q31.2"
module: 21
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ST7-AS2

*ST7 antisense RNA 2* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +12.0, q 2e-30, up in 31 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (SW480 0.0741×; ⚠ transcription drop); [[Monocrotaline (drug)]] 0.05 µM in 1 line (SW480 0.0707×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (LoVo 0.0704×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USH2A]] (+0.86, fdr 7e-06), [[C2CD5-AS1]] (+0.84, fdr 7e-06), [[PPP1R9A-AS1]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PAMR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +12.0 | 2e-30 | 31/33 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +11.0 | 2e-25 | 1/1 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +9.9 | 8e-21 | 10/11 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +8.1 | 9e-14 | 3/4 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.28×** | +7.5 | 7e-12 | 28/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +5.6 | 2e-06 | 5/11 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.53×** | +5.5 | 3e-06 | 10/34 (SW48, LS 180, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.0 | 5e-05 | 10/34 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.6 | 3e-04 | 10/27 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13530.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (SW480 0.0741×; ⚠ transcription drop); [[Monocrotaline (drug)]] 0.05 µM in 1 line (SW480 0.0707×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (LoVo 0.0704×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.787× | -3.1 | 0.53 | 4/46 (SNU-423, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.716× | -3.0 | 0.53 | 5/45 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.31 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0741× (z -12.5) ⚠ transcription drop · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.0707× (z -11.8) |
| [[LoVo (line)]] | wt | 2.66 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0704× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USH2A]] | +0.86 | +0.69 / +0.89 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.84 | +0.72 / +0.83 | both halves | 7e-06 | same gene group |
| [[PPP1R9A-AS1]] | +0.82 | +0.76 / +0.76 | both halves | 7e-06 | same gene group |
| [[LINC00861]] | +0.82 | +0.60 / +0.83 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.82 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.82 | +0.70 / +0.76 | both halves | 7e-06 | same gene group |
| [[A2ML1-AS1]] | +0.81 | +0.64 / +0.79 | both halves | 7e-06 | same gene group |
| [[HRG-AS1]] | +0.80 | +0.71 / +0.75 | both halves | 7e-06 | same gene group |
| [[CNTNAP5]] | +0.80 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.79 | +0.75 / +0.66 | both halves | 7e-06 | same gene group |
| [[GALNTL6]] | +0.78 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.78 | +0.70 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAMR1]] | B | PAMR1 activity raises ST7-AS2's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.13× lower at baseline in the lines without PAMR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[LINC01579]] | B | LINC01579 activity raises ST7-AS2's level | lines that do not express LINC01579 (13) vs lines expressing it (37) | 1.15× lower at baseline in the lines without LINC01579 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, CNTNAP2, CACNA1C; maybe low, not absent |
| [[LINC01807]] | B | LINC01807 activity raises ST7-AS2's level | lines that do not express LINC01807 (11) vs lines expressing it (39) | 1.11× lower at baseline in the lines without LINC01807 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000253496, SLC2A14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.8, 27.9); signed map (32.9, 7.5). **Vector** length 37.7, 3.49% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.8 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ST7 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q31.2 — chr7:117,072,072-117,146,480 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ST7AS2; previously ST7OT2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:16044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16044) · Entrez [93654](https://www.ncbi.nlm.nih.gov/gene/93654) · Ensembl [ENSG00000226367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226367)

## Data

Gene col 13530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13530); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13530]; `tensor/DDL_lfc|DDL_z.npy` [13530]; `embed/gene_vectors.npy` [13530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13530 or target_col == 13530). Every well: [[ST7-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST7-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
