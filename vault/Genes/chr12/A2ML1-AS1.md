---
symbol: "A2ML1-AS1"
type: "gene"
col: 15001
ensembl_id: "ENSG00000256661"
name: "A2ML1 antisense RNA 1"
location: "12p13.31"
module: 21
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# A2ML1-AS1

*A2ML1 antisense RNA 1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.48× (z +11.0, q 3e-25, up in 22 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.5 µM in 1 line (A498 0.0709×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HRG-AS1]] (+0.83, fdr 7e-06), [[C2CD5-AS1]] (+0.82, fdr 7e-06), [[TICAM2-AS1]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +11.0 | 3e-25 | 22/31 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +9.8 | 3e-20 | 9/10 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +9.1 | 1e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +7.1 | 1e-10 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.6 | 6e-04 | 8/23 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.002 | 7/25 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.013 | 7/31 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.6 | 0.025 | 5/26 (A498, SW480, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.49×** | +3.4 | 0.048 | 6/33 (KATO III, SW480, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.2 | 0.074 | 4/20 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.074 | 3/42 (NCI-H1792, SK-MEL-2, …) | top dose only | position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.081 | 4/34 (A549, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.083 | 4/43 (LoVo, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.1 | 0.092 | 2/9 (A498, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15001.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.5 µM in 1 line (A498 0.0709×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -3.8 | 0.095 | 16/47 (SK-MEL-2, H4, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.675× | -3.1 | 0.53 | 3/46 (AN3 CA, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.81 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +9.6) | [[Allantoin (drug)]] 0.5 µM 0.0709× (z -8.7) |
| [[A-172 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HRG-AS1]] | +0.83 | +0.72 / +0.80 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.82 | +0.67 / +0.80 | both halves | 7e-06 | same gene group |
| [[TICAM2-AS1]] | +0.82 | +0.75 / +0.75 | both halves | 7e-06 | same gene group |
| [[UBOX5-AS1]] | +0.82 | +0.60 / +0.84 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.82 | +0.68 / +0.81 | both halves | 7e-06 | same gene group |
| [[BIRC6-AS2-1]] | +0.81 | +0.63 / +0.82 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.81 | +0.64 / +0.79 | both halves | 7e-06 | same gene group |
| [[VPS39-DT]] | +0.81 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.80 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.80 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.80 | +0.72 / +0.77 | both halves | 7e-06 | same gene group |
| [[SLC13A4]] | +0.79 | +0.60 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers A2ML1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.891). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 28.1); signed map (33.7, 6.0). **Vector** length 36.7, 3.58% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | A2ML1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.31 — chr12:8,776,219-8,830,947 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41022) · Entrez [100874108](https://www.ncbi.nlm.nih.gov/gene/100874108) · Ensembl [ENSG00000256661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256661)

## Data

Gene col 15001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15001); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15001]; `tensor/DDL_lfc|DDL_z.npy` [15001]; `embed/gene_vectors.npy` [15001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15001 or target_col == 15001). Every well: [[A2ML1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A2ML1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
