---
symbol: "ABHD15-AS1"
type: "gene"
col: 15434
ensembl_id: "ENSG00000264031"
name: "ABHD15 antisense RNA 1"
location: "17q11.2"
module: 21
arm: "+"
pooled_cpm: 7.23
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ABHD15-AS1

*ABHD15 antisense RNA 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +17.5, q 0e+00, up in 38 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Delamanid (drug)]] 0.5 µM in 1 line (C-33 A 0.0716×); [[Trimetrexate (drug)]] 0.05 µM in 1 line (SHP-77 0.0849×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0917×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA21]] (+0.81, fdr 7e-06), [[ZNF451-AS1]] (+0.81, fdr 7e-06), [[FLJ40194]] (+0.79, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +17.5 | 0e+00 | 38/43 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +11.2 | 8e-27 | 13/15 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +11.2 | 9e-27 | 27/30 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.8 | 1e-09 | 10/20 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.7 | 3e-04 | 16/42 (LOX-IMVI, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.002 | 14/44 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.9 | 0.008 | 10/39 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.008 | 11/42 (HOP62, SW48, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.28×** | +3.5 | 0.028 | 6/47 (HCT15, NCI-H23, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.4 | 0.042 | 2/16 (NCI-H2347, C-33 A) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.28×** | +3.3 | 0.052 | 9/37 (LoVo, RKO, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.069 | 8/48 (A-172, HOP62, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.2 | 0.069 | 5/48 (HCT15, HOP62, …) | top dose only | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.087 | 2/45 (LOX-IMVI, A-427) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.087 | 10/45 (HOP62, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Delamanid (drug)]] 0.5 µM in 1 line (C-33 A 0.0716×); [[Trimetrexate (drug)]] 0.05 µM in 1 line (SHP-77 0.0849×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0917×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -6.5 | 4e-08 | 13/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.850× | -3.3 | 0.28 | 8/47 (HS-578T, KATO III, …) | inconsistent across doses | position effect removed |
| [[Clotrimazole (drug)]] 5 µM |  | 0.855× | -3.2 | 0.28 | 7/48 (SNU-1, SW 1271, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 7.43 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0849× (z -9.8) |
| [[A498 (line)]] | wt | 7.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +11.2) | — |
| [[A549 (line)]] | wt | 9.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +10.9) | — |
| [[C-33 A (line)]] | alt | 8.60 | 0 | 1 | — | [[Delamanid (drug)]] 0.5 µM 0.0716× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 6.08 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0896× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 7.67 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0917× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 9.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 9.25 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.149× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 7.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0911× (z -8.7) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 6.98 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA21]] | +0.81 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[ZNF451-AS1]] | +0.81 | +0.71 / +0.80 | both halves | 7e-06 | same gene group |
| [[FLJ40194]] | +0.79 | +0.55 / +0.84 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.78 | +0.63 / +0.79 | both halves | 7e-06 | same gene group |
| [[FAM184B]] | +0.78 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.78 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.77 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.76 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[EHBP1-AS1]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 | same gene group |
| [[C12orf40]] | +0.75 | +0.58 / +0.76 | both halves | 8e-06 |  |
| [[COLEC11]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MYH11]] | +0.74 | +0.63 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABHD15-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 26.8); signed map (33.4, 4.3). **Vector** length 44.8, 4.92% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.4 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ABHD15 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q11.2 — chr17:29,560,547-29,707,090 (+) |
| Ensembl biotype | lncRNA |
| Also known as | linc-TP53I13, lnc-TP53I13 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49685) · Entrez [104355133](https://www.ncbi.nlm.nih.gov/gene/104355133) · Ensembl [ENSG00000264031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264031)

## Data

Gene col 15434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15434); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15434]; `tensor/DDL_lfc|DDL_z.npy` [15434]; `embed/gene_vectors.npy` [15434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15434 or target_col == 15434). Every well: [[ABHD15-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD15-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
