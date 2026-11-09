---
symbol: "SP2-DT"
type: "gene"
col: 15449
ensembl_id: "ENSG00000264920"
name: ""
location: ""
module: 24
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SP2-DT

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.82× (z +8.6, q 3e-15, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +7.8, q 1e-12, up in 20 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Acetazolamide (drug)]] 0.5 µM in 1 line (SW1417 0.0534×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM27]] (+0.69, fdr 2e-05), [[DNAJC30]] (+0.66, fdr 1e-05), [[ZNF358]] (+0.65, fdr 3e-05); moves opposite to [[NOLC1]] (-0.53, fdr 6e-04), [[LRRC59]] (-0.51, fdr 3e-05), [[NONO]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +8.6 | 3e-15 | 2/3 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +8.6 | 3e-15 | 10/12 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +7.8 | 1e-12 | 20/31 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +6.8 | 1e-09 | 2/3 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +4.9 | 1e-04 | 12/26 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.0 | 0.006 | 3/14 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.057 | 4/41 (SW480, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.63× | +3.1 | 0.12 | 7/31 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.59× | +3.1 | 0.12 | 5/30 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.96× | +3.0 | 0.14 | 3/28 (NCI-H23, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15449.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Acetazolamide (drug)]] 0.5 µM in 1 line (SW1417 0.0534×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.594× | -3.5 | 0.13 | 17/45 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.578× | -3.5 | 0.13 | 10/44 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.604× | -3.4 | 0.13 | 12/38 (COLO 205, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.613× | -3.2 | 0.22 | 12/40 (Panc 03.27, A-427, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 3.38 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0534× (z -8.9) |
| [[A-172 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | +0.69 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[DNAJC30]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ZNF358]] | +0.65 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[ZNF236-DT]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[C1orf56]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[EXOC3-AS1]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ZNF232-AS1]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PIAS1]] | +0.61 | +0.27 / +0.61 | both halves | 3e-04 |  |
| [[AKAP1-DT]] | +0.60 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MIR762HG]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[NDUFB1]] | +0.60 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[OXLD1]] | +0.60 | +0.43 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOLC1]] | -0.53 | -0.22 / -0.62 | both halves | 6e-04 |  |
| [[LRRC59]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[NONO]] | -0.50 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[MTHFD1]] | -0.50 | -0.28 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-48.0, 9.3); signed map (-5.0, -2.0). **Vector** length 41.3, 5.12% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

> [!warning] No registry record
> SP2-DT has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15449); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15449]; `tensor/DDL_lfc|DDL_z.npy` [15449]; `embed/gene_vectors.npy` [15449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15449 or target_col == 15449). Every well: [[SP2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SP2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
