---
symbol: "MYL6B-AS1"
type: "gene"
col: 15066
ensembl_id: "ENSG00000257809"
name: "MYL6B antisense RNA 1"
location: "12q13.2"
module: 35
arm: "+"
pooled_cpm: 2.19
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MYL6B-AS1

*MYL6B antisense RNA 1* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +9.8, q 5e-20, up in 19 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.611× (z -4.8, q 0.001, down in 17 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (PANC-1 0.0981×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (HEC-1-A 0.0994×; ⚠ toxic).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF546]] (+0.67, fdr 1e-05), [[SEC1P]] (+0.66, fdr 1e-05), [[KCTD21-AS1]] (+0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02608]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +9.8 | 5e-20 | 19/28 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.2 | 1e-10 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +7.1 | 3e-10 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.7 | 3e-09 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +5.0 | 6e-05 | 11/38 (SW480, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.054 | 7/40 (KATO III, NCI-H23, …) | inconsistent across doses |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.054 | 3/36 (Panc 03.27, SHP-77, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15066.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (PANC-1 0.0981×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (HEC-1-A 0.0994×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -4.8 | 0.001 | 17/41 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -4.5 | 0.002 | 14/43 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.648×** | -4.0 | 0.010 | 12/39 (PANC-1, SNU-423, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.90 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0981× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 2.80 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0994× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF546]] | +0.67 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SEC1P]] | +0.66 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[KCTD21-AS1]] | +0.66 | +0.54 / +0.58 | both halves | 1e-05 | same gene group |
| [[ISY1-RAB43]] | +0.65 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[SPOCK2]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[LINC02608]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[AGBL2]] | +0.64 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[PJVK]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FLRT1]] | +0.63 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[LINC02951]] | +0.63 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.62 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[PSMG3-AS1]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02608]] | C | LINC02608 activity lowers MYL6B-AS1's level | lines that do not express LINC02608 (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without LINC02608 | 0.017 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GNA14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.1, 24.3); signed map (32.3, -3.3). **Vector** length 37.6, 3.67% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.5 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MYL6B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.2 — chr12:56,150,796-56,158,220 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55472) · Entrez [120766150](https://www.ncbi.nlm.nih.gov/gene/120766150) · Ensembl [ENSG00000257809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257809)

## Data

Gene col 15066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15066); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15066]; `tensor/DDL_lfc|DDL_z.npy` [15066]; `embed/gene_vectors.npy` [15066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15066 or target_col == 15066). Every well: [[MYL6B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYL6B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
