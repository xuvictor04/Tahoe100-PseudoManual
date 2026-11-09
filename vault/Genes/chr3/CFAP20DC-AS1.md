---
symbol: "CFAP20DC-AS1"
type: "gene"
col: 14316
ensembl_id: "ENSG00000242428"
name: "CFAP20DC antisense RNA 1"
location: "3p14.2"
module: 21
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CFAP20DC-AS1

*CFAP20DC antisense RNA 1* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +11.4, q 2e-27, up in 24 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.669× (z -4.1, q 0.021, down in 12 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW480 0.0501×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H1573 0.124×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HRG-AS1]] (+0.77, fdr 9e-06), [[HPSE2]] (+0.76, fdr 1e-05), [[SLC13A4]] (+0.75, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFAP20DC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +11.4 | 2e-27 | 24/33 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +9.9 | 8e-21 | 2/4 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +9.3 | 2e-18 | 9/14 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +6.4 | 2e-08 | 19/40 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.86×** | +6.3 | 4e-08 | 7/15 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +6.2 | 5e-08 | 3/6 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.79×** | +4.2 | 0.002 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.035 | 3/36 (CFPAC-1, RKO, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.4 | 0.036 | 7/34 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.038 | 1/35 (A498) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.038 | 4/41 (NCI-H460, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW480 0.0501×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H1573 0.124×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.669×** | -4.1 | 0.021 | 12/44 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.722× | -3.3 | 0.23 | 9/41 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.732× | -3.2 | 0.25 | 8/45 (SNU-1, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.67 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.124× (z -8.5) |
| [[SW480 (line)]] | alt | 2.60 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0501× (z -12.5) |
| [[A-172 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HRG-AS1]] | +0.77 | +0.57 / +0.79 | both halves | 9e-06 | same gene group |
| [[HPSE2]] | +0.76 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.75 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.74 | +0.56 / +0.73 | both halves | 1e-05 | same gene group |
| [[CHMP3-AS1]] | +0.74 | +0.51 / +0.73 | both halves | 1e-05 | same gene group |
| [[PTPRT]] | +0.73 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.72 | +0.53 / +0.73 | both halves | 1e-05 | same gene group |
| [[LANCL1-AS1]] | +0.71 | +0.48 / +0.70 | both halves | 2e-05 | same gene group |
| [[UBOX5-AS1]] | +0.71 | +0.52 / +0.72 | both halves | 1e-05 | same gene group |
| [[C12orf40]] | +0.71 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ST7-AS2]] | +0.71 | +0.48 / +0.74 | both halves | 2e-05 | same gene group |
| [[OPCML]] | +0.70 | +0.45 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP20DC]] | B | CFAP20DC activity raises CFAP20DC-AS1's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without CFAP20DC | 0.063 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.4, 27.6); signed map (32.3, 7.1). **Vector** length 38.7, 3.77% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CFAP20DC antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.2 — chr3:58,824,437-59,019,093 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C3orf67-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41063) · Entrez [101929238](https://www.ncbi.nlm.nih.gov/gene/101929238) · Ensembl [ENSG00000242428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242428)

## Data

Gene col 14316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14316); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14316]; `tensor/DDL_lfc|DDL_z.npy` [14316]; `embed/gene_vectors.npy` [14316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14316 or target_col == 14316). Every well: [[CFAP20DC-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP20DC-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
