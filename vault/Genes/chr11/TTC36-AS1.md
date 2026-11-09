---
symbol: "TTC36-AS1"
type: "gene"
col: 14938
ensembl_id: "ENSG00000255435"
name: "TTC36 and KMT2A antisense RNA 1"
location: "11q23.3"
module: 21
arm: "+"
pooled_cpm: 3.44
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TTC36-AS1

*TTC36 and KMT2A antisense RNA 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +7.9, q 2e-12, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.7, q 4e-09, up in 13 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Resveratrol (drug)]] 0.05 µM in 1 line (KATO III 0.0552×); [[Arbutin (drug)]] 5 µM in 1 line (NCI-H2030 0.0716×); [[Triamcinolone (drug)]] 5 µM in 1 line (MIA PaCa-2 0.149×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA2-AS1]] (+0.84, fdr 7e-06), [[ASB14]] (+0.81, fdr 7e-06), [[CHMP3-AS1]] (+0.79, fdr 7e-06); moves opposite to [[ICMT]] (-0.66, fdr 1e-05), [[PRKDC]] (-0.63, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.9 | 2e-12 | 5/6 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.5 | 1e-11 | 15/22 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.7 | 4e-09 | 4/6 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.7 | 4e-09 | 13/37 (HEC-1-A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +6.5 | 9e-09 | 19/35 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +5.0 | 7e-05 | 6/17 (LoVo, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +4.0 | 0.005 | 4/22 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.055 | 5/30 (AsPC-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.094 | 7/40 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.10 | 3/34 (J82, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.50× | +3.0 | 0.11 | 1/9 (A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bicalutamide (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.11 | 3/43 (A549, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.33× | +3.0 | 0.11 | 3/41 (BT-474, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Resveratrol (drug)]] 0.05 µM in 1 line (KATO III 0.0552×); [[Arbutin (drug)]] 5 µM in 1 line (NCI-H2030 0.0716×); [[Triamcinolone (drug)]] 5 µM in 1 line (MIA PaCa-2 0.149×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.711× | -3.3 | 0.41 | 9/44 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -3.2 | 0.41 | 8/48 (AN3 CA, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.17 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0775× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 3.21 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0617× (z -8.7) |
| [[KATO III (line)]] | alt | 4.37 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0552× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 3.78 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0980× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.48 | 0 | 1 | — | [[Triamcinolone (drug)]] 5 µM 0.149× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 3.17 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0716× (z -9.8) |
| [[A-427 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA2-AS1]] | +0.84 | +0.82 / +0.79 | both halves | 7e-06 | same gene group |
| [[ASB14]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.79 | +0.77 / +0.79 | both halves | 7e-06 | same gene group |
| [[PKD2L2]] | +0.79 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[CNGB3]] | +0.78 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.77 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.77 | +0.66 / +0.78 | both halves | 7e-06 | same gene group |
| [[SPATA21]] | +0.77 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[EAF1-AS1]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 | same gene group |
| [[RN7SL2]] | +0.76 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.76 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.76 | +0.64 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICMT]] | -0.66 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.0, 27.2); signed map (32.6, 5.5). **Vector** length 34.4, 2.89% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TTC36 and KMT2A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q23.3 — chr11:118,510,273-118,531,094 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55495) · Entrez [101929089](https://www.ncbi.nlm.nih.gov/gene/101929089) · Ensembl [ENSG00000255435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255435)

## Data

Gene col 14938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14938); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14938]; `tensor/DDL_lfc|DDL_z.npy` [14938]; `embed/gene_vectors.npy` [14938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14938 or target_col == 14938). Every well: [[TTC36-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC36-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
