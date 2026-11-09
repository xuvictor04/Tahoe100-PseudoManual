---
symbol: "MDP1"
type: "gene"
col: 13148
ensembl_id: "ENSG00000213920"
name: "magnesium dependent phosphatase 1"
location: "14q12"
module: 35
arm: "+"
pooled_cpm: 4.44
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MDP1

*magnesium dependent phosphatase 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.87× (z +11.8, q 3e-29, up in 8 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +6.8, q 2e-09, up in 23 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 6.58×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.490× (z -6.5, q 5e-08, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGP]] (+0.79, fdr 7e-06), [[ZNF425]] (+0.72, fdr 1e-05), [[NDUFAF1]] (+0.70, fdr 7e-06); moves opposite to [[PARP1]] (-0.57, fdr 1e-04), [[DCAF16]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXA10-AS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13148.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 6.58×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.87×** | +11.8 | 3e-29 | 8/8 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +9.9 | 2e-20 | 22/24 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +8.2 | 5e-14 | 9/12 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.8 | 2e-09 | 23/38 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.4 | 1e-05 | 14/28 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.6 | 0.028 | 12/29 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 1.43× | +3.1 | 0.15 | 6/44 (J82, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.490×** | -6.5 | 5e-08 | 29/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -6.3 | 6e-08 | 23/44 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.546×** | -5.5 | 8e-06 | 24/44 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -3.5 | 0.077 | 13/39 (SHP-77, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.701× | -3.2 | 0.15 | 7/47 (A-172, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.86 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0750× (z -8.9) |
| [[A-427 (line)]] | wt | 6.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0690× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 5.01 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +8.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 4.48 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0576× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 5.34 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -8.9) ⚠ transcription drop |
| [[A498 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGP]] | +0.79 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[ZNF425]] | +0.72 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[NDUFAF1]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[PPCS]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PHYH]] | +0.64 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[ANKHD1-DT]] | +0.64 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[C11orf71]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[COPZ2]] | +0.63 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[NEK8]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[HHLA3]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.62 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP1]] | -0.57 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DCAF16]] | -0.54 | -0.63 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA10-AS]] | B | HOXA10-AS activity lowers MDP1's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 1.21× higher at baseline in the lines without HOXA10-AS | 0.031 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (6.8, 20.9); signed map (21.5, -12.4). **Vector** length 37.8, 3.84% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -2.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.9 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | magnesium dependent phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,213,943-24,216,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5987, FN6Pase |
| Gene groups (HGNC) | HAD Asp-based protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V88](https://www.uniprot.org/uniprotkb/Q86V88) (Magnesium-dependent phosphatase 1):

> Magnesium-dependent phosphatase which may act as a tyrosine phosphatase.

**Summary**, from NCBI Gene [145553](https://www.ncbi.nlm.nih.gov/gene/145553):

> Predicted to enable acid phosphatase activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28781) · Entrez [145553](https://www.ncbi.nlm.nih.gov/gene/145553) · UniProt [Q86V88](https://www.uniprot.org/uniprotkb/Q86V88) · Ensembl [ENSG00000213920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213920)

## Data

Gene col 13148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13148); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13148]; `tensor/DDL_lfc|DDL_z.npy` [13148]; `embed/gene_vectors.npy` [13148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13148 or target_col == 13148). Every well: [[MDP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
