---
symbol: "ZRANB2-AS1"
type: "gene"
col: 13996
ensembl_id: "ENSG00000235079"
name: "ZRANB2 antisense RNA 1"
location: "1p31.1"
module: 21
arm: "+"
pooled_cpm: 3.93
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ZRANB2-AS1

*ZRANB2 antisense RNA 1* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +10.3, q 3e-22, up in 21 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.3, q 1e-05, up in 15 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.873× (z -5.0, q 4e-04, down in 15 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Larotrectinib (drug)]] 5 µM: 0.776× (z -3.7, q 0.058, down in 15 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 2 lines (J82 0.0807×, CFPAC-1 0.101×); [[Trifluridine (drug)]] 5 µM in 1 line (SHP-77 0.101×; ⚠ cell-cycle shift, explains ~3% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW480 0.152×); [[Megestrol (drug)]] 0.5 µM in 1 line (Hs 766T 0.0775×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TICAM2-AS1]] (+0.90, fdr 7e-06), [[FAM217A]] (+0.89, fdr 7e-06), [[EOGT-DT]] (+0.89, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC144NL-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +10.3 | 3e-22 | 21/24 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +10.3 | 3e-22 | 3/7 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +9.3 | 2e-18 | 8/10 (NCI-H460, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.32×** | +8.6 | 9e-16 | 20/26 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.3 | 1e-05 | 14/37 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.3 | 1e-05 | 15/39 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.3 | 0.001 | 9/27 (NCI-H2347, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.26×** | +3.3 | 0.066 | 10/37 (LoVo, NCI-H460, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.068 | 2/36 (LOX-IMVI, SW480) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.068 | 3/44 (A-427, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.075 | 4/45 (LS 180, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.082 | 10/44 (HOP62, NCI-H1573, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.089 | 12/44 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.0 | 0.096 | 4/43 (NCI-H1573, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13996.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 2 lines (J82 0.0807×, CFPAC-1 0.101×); [[Trifluridine (drug)]] 5 µM in 1 line (SHP-77 0.101×; ⚠ cell-cycle shift, explains ~3% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW480 0.152×); [[Megestrol (drug)]] 0.5 µM in 1 line (Hs 766T 0.0775×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.873× | -5.0 | 4e-04 | 15/48 (SHP-77, SW1417, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.776×** | -3.7 | 0.058 | 15/44 (SW480, NCI-H1573, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.98 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.101× (z -8.9) |
| [[Hs 766T (line)]] | wt | 5.22 | 0 | 1 | — | [[Megestrol (drug)]] 0.5 µM 0.0775× (z -9.3) |
| [[J82 (line)]] | alt | 3.85 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0807× (z -9.2) |
| [[SHP-77 (line)]] | alt | 3.73 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 5 µM 0.101× (z -9.8) ⚠ cell-cycle shift, explains ~3% of this change |
| [[SW480 (line)]] | alt | 4.19 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.152× (z -9.7) |
| [[A-172 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2-AS1]] | +0.90 | +0.80 / +0.87 | both halves | 7e-06 | same gene group |
| [[FAM217A]] | +0.89 | +0.82 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[EOGT-DT]] | +0.89 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.87 | +0.78 / +0.85 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.87 | +0.82 / +0.88 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.86 | +0.77 / +0.84 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.86 | +0.74 / +0.88 | both halves | 7e-06 | same gene group |
| [[RN7SL1]] | +0.85 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.85 | +0.77 / +0.85 | both halves | 7e-06 | same gene group |
| [[LRRC37A16P]] | +0.84 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.84 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.84 | +0.76 / +0.80 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144NL-1]] | B | CCDC144NL-1 activity raises ZRANB2-AS1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.14× lower at baseline in the lines without CCDC144NL-1 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.925). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 28.1); signed map (34.0, 5.4). **Vector** length 34.9, 3.06% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ZRANB2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p31.1 — chr1:71,048,855-71,067,184 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43594) · Entrez [100132618](https://www.ncbi.nlm.nih.gov/gene/100132618) · Ensembl [ENSG00000235079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235079)

## Data

Gene col 13996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13996); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13996]; `tensor/DDL_lfc|DDL_z.npy` [13996]; `embed/gene_vectors.npy` [13996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13996 or target_col == 13996). Every well: [[ZRANB2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZRANB2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
