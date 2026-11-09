---
symbol: "AKAP13-AS1"
type: "gene"
col: 15195
ensembl_id: "ENSG00000259367"
name: "AKAP13 antisense RNA 1"
location: "15q25.3"
module: 21
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# AKAP13-AS1

*AKAP13 antisense RNA 1* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +9.0, q 2e-16, up in 14 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.13× (z +7.9, q 7e-13, up in 23 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (A-172 18.3×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.827× (z -7.2, q 3e-10, down in 34 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Doxycycline (monohydrate) (drug)]] 5 µM: 0.686× (z -3.8, q 0.042, down in 9 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (SW1417 0.0677×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AsPC-1 0.0877×); [[Naproxen (drug)]] 0.05 µM in 1 line (HOP62 0.0897×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS39-DT]] (+0.76, fdr 7e-06), [[CRLF1]] (+0.75, fdr 1e-05), [[RN7SL2]] (+0.75, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[S100P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15195.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (A-172 18.3×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +9.0 | 2e-16 | 14/25 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +7.9 | 7e-13 | 23/44 (A-172, BT-474, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +7.6 | 6e-12 | 21/36 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +7.1 | 2e-10 | 3/6 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.1 | 5e-05 | 3/10 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.41×** | +3.6 | 0.031 | 7/23 (NCI-H1573, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.37×** | +3.3 | 0.085 | 8/35 (LoVo, NCI-H1792, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.53× | +3.2 | 0.11 | 6/30 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.12 | 4/41 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.35× | +3.0 | 0.13 | 8/35 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15195.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (SW1417 0.0677×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AsPC-1 0.0877×); [[Naproxen (drug)]] 0.05 µM in 1 line (HOP62 0.0897×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.827×** | -7.2 | 3e-10 | 34/48 (NCI-H1792, HEC-1-A, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.686×** | -3.8 | 0.042 | 9/44 (H4, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.14 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.3× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 4.67 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0877× (z -9.1) |
| [[HOP62 (line)]] | alt | 3.73 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0897× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 3.34 | 0 | 1 | — | [[Pimozide (drug)]] 5 µM 0.0603× (z -8.6) |
| [[SW1417 (line)]] | alt | 3.31 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0677× (z -9.4) |
| [[A-427 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS39-DT]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[CRLF1]] | +0.75 | +0.49 / +0.81 | both halves | 1e-05 |  |
| [[RN7SL2]] | +0.75 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 | same gene group |
| [[MAL2-AS1]] | +0.72 | +0.61 / +0.72 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 | same gene group |
| [[A2ML1-AS1]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 | same gene group |
| [[CNGB3]] | +0.71 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[BIRC6-AS2-1]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[CCDC39]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.69 | +0.59 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100P]] | B | S100P activity raises AKAP13-AS1's level | lines that do not express S100P (34) vs lines expressing it (16) | 1.16× lower at baseline in the lines without S100P | 0.054 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |
| [[SRRM3]] | B | SRRM3 activity lowers AKAP13-AS1's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.10× higher at baseline in the lines without SRRM3 | 0.085 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 29.4); signed map (34.7, 6.5). **Vector** length 40.5, 4.23% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | AKAP13 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q25.3 — chr15:85,619,623-85,670,948 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55975) · Entrez [123466214](https://www.ncbi.nlm.nih.gov/gene/123466214) · Ensembl [ENSG00000259367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259367)

## Data

Gene col 15195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15195); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15195]; `tensor/DDL_lfc|DDL_z.npy` [15195]; `embed/gene_vectors.npy` [15195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15195 or target_col == 15195). Every well: [[AKAP13-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP13-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
