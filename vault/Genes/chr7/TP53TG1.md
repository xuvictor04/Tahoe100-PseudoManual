---
symbol: "TP53TG1"
type: "gene"
col: 11250
ensembl_id: "ENSG00000182165"
name: "TP53 target 1"
location: "7q21.12"
module: 45
arm: "+"
pooled_cpm: 2.87
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TP53TG1

*TP53 target 1* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.14× (z +8.2, q 2e-13, up in 18 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.500× (z -5.2, q 1e-04, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EID2B]] (+0.73, fdr 1e-05), [[SNX2]] (+0.68, fdr 1e-05), [[NTPCR]] (+0.67, fdr 1e-05); moves opposite to [[NOLC1]] (-0.55, fdr 4e-05), [[NUP188]] (-0.55, fdr 5e-05), [[CCDC18]] (-0.55, fdr 7e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.14×** | +8.2 | 2e-13 | 18/43 (C32, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +7.7 | 3e-12 | 9/12 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +7.2 | 8e-11 | 4/5 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.39×** | +6.3 | 3e-08 | 10/15 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.22×** | +6.0 | 2e-07 | 23/45 (A-172, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +5.3 | 1e-05 | 2/4 (A498, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +5.1 | 3e-05 | 21/42 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.2 | 0.002 | 6/16 (HT-29, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +3.9 | 0.006 | 18/44 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.010 | 10/42 (C32, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.026 | 8/43 (HOP62, Hs 766T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.029 | 9/42 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.039 | 7/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +3.3 | 0.045 | 11/42 (A498, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.500×** | -5.2 | 1e-04 | 20/45 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -4.1 | 0.011 | 20/42 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -4.0 | 0.011 | 15/41 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -4.0 | 0.011 | 17/43 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.728×** | -3.4 | 0.083 | 17/31 (NCI-H2347, PANC-1, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.442× | -3.2 | 0.12 | 7/29 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.69 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 2.52 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0539× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 2.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 3.08 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 2.54 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0375× (z -11.4) |
| [[A-172 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID2B]] | +0.73 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[SNX2]] | +0.68 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[NTPCR]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[C12orf76]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[CLN8-AS1]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SPACA9]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RPS27L]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MRPL39]] | +0.63 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[LAMTOR2]] | +0.62 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[AKAP1-DT]] | +0.61 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NUDT7]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TP53INP1]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOLC1]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[NUP188]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[CCDC18]] | -0.55 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[SLC4A7]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.54 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[MYLK2]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[EHBP1]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[MYH15]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[CDC37]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-4.0, -8.4); signed map (-25.6, -8.9). **Vector** length 50.3, 7.14% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | TP53 target 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q21.12 — chr7:87,322,943-87,345,560 (-) |
| Ensembl biotype | lncRNA |
| Also known as | H_RG012D21.9, LINC00096, TP53LC12; previously TP53AP1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:17026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17026) · Entrez [11257](https://www.ncbi.nlm.nih.gov/gene/11257) · Ensembl [ENSG00000182165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182165)

## Data

Gene col 11250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11250); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11250]; `tensor/DDL_lfc|DDL_z.npy` [11250]; `embed/gene_vectors.npy` [11250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11250 or target_col == 11250). Every well: [[TP53TG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TP53TG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
