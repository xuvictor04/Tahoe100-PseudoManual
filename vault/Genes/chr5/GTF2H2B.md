---
symbol: "GTF2H2B"
type: "gene"
col: 13522
ensembl_id: "ENSG00000226259"
name: "general transcription factor IIH subunit 2B (pseudogene)"
location: "5q13.2"
module: 30
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GTF2H2B

*general transcription factor IIH subunit 2B (pseudogene)* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.24× (z +8.1, q 3e-13, up in 18 of 22 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.85× (z +6.4, q 4e-08, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.723× (z -4.7, q 0.001, down in 19 of 40 measured lines) ⚠ cell-cycle shift, explains ~23% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.0659×, MIA PaCa-2 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0655×); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0552×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2H2]] (+0.74, fdr 7e-06), [[MALSU1]] (+0.70, fdr 7e-06), [[CRYZL1]] (+0.69, fdr 7e-06); moves opposite to [[TRIP12]] (-0.69, fdr 2e-05), [[ZNF655]] (-0.63, fdr 3e-05), [[TUG1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +8.1 | 3e-13 | 18/22 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +6.4 | 4e-08 | 24/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +6.3 | 6e-08 | 23/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +6.2 | 6e-08 | 18/47 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.2 | 8e-08 | 0/6 | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.075 | 4/33 (LoVo, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.0659×, MIA PaCa-2 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0655×); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.723×** | -4.7 | 0.001 | 19/40 (hTERT-HPNE, NCI-H1573, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.3 | 0.31 | 6/48 (NCI-H661, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0659× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[Hs 766T (line)]] | wt | 3.23 | 0 | 1 | — | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM 0.0552× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 7.17 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[Panc 03.27 (line)]] | alt | 3.98 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0655× (z -8.8) |
| [[A-172 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H2]] | +0.74 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CCZ1B]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FAM193B]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[LSM2]] | +0.65 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[MRPS5]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[GTF2H2C]] | +0.64 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[MYPOP]] | +0.64 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.63 | +0.64 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | -0.69 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[ZNF655]] | -0.63 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TUG1]] | -0.63 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | -0.62 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.62 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.62 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | -0.60 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[EIF4G2]] | -0.59 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CHD4]] | -0.59 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[LINC00667]] | -0.59 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[USP11]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GTF2H2B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.0, -13.1); signed map (-33.2, -3.7). **Vector** length 48.2, 5.50% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.4 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.3 | +6.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.1 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.1 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | -1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | -2.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIH subunit 2B (pseudogene) |
| Locus type | pseudogene |
| Location | 5q13.2 — chr5:70,415,352-70,447,526 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | DKFZP686M0199 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31393) · Entrez [653238](https://www.ncbi.nlm.nih.gov/gene/653238) · Ensembl [ENSG00000226259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226259)

## Data

Gene col 13522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13522); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13522]; `tensor/DDL_lfc|DDL_z.npy` [13522]; `embed/gene_vectors.npy` [13522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13522 or target_col == 13522). Every well: [[GTF2H2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2H2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
