---
symbol: "CDC20-DT"
type: "gene"
col: 13976
ensembl_id: "ENSG00000234694"
name: "CDC20 divergent transcript"
location: "1p34.2"
module: 37
arm: "+"
pooled_cpm: 3.78
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CDC20-DT

*CDC20 divergent transcript* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +11.3, q 8e-27, up in 28 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.621× (z -6.7, q 6e-09, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TERB1]] (+0.75, fdr 7e-06), [[TMED7-TICAM2]] (+0.69, fdr 1e-05), [[C17orf100]] (+0.68, fdr 1e-05); moves opposite to [[C2CD5]] (-0.60, fdr 2e-05).
> It is in [[Module 037]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +11.3 | 8e-27 | 28/35 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +7.9 | 5e-13 | 26/42 (HT-29, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.6 | 1e-08 | 13/24 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.6 | 2e-06 | 2/5 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.3 | 0.002 | 11/33 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.008 | 7/46 (A498, LoVo, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.39× | +3.1 | 0.14 | 5/38 (A549, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.39× | +3.0 | 0.19 | 2/9 (AsPC-1, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.621×** | -6.7 | 6e-09 | 20/36 (A549, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -6.7 | 6e-09 | 27/45 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -6.2 | 1e-07 | 19/43 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -4.9 | 1e-04 | 20/44 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -4.7 | 2e-04 | 19/32 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -4.7 | 2e-04 | 17/43 (SW48, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.648×** | -4.3 | 0.001 | 17/44 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -3.6 | 0.019 | 8/44 (RKO, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -3.5 | 0.027 | 9/43 (SNU-1, AsPC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -3.4 | 0.036 | 14/42 (HS-578T, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -3.4 | 0.036 | 11/38 (NCI-H1573, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.533×** | -3.3 | 0.051 | 5/28 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 5.58 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0558× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0800× (z -9.5) |
| [[A-172 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERB1]] | +0.75 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | +0.69 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[C17orf100]] | +0.68 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.67 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[TICAM2]] | +0.67 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[ISY1-RAB43]] | +0.66 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[LINC02680]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF547]] | +0.65 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[RRH]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[NOXRED1]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[PHYHD1]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[HAVCR2]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5]] | -0.60 | -0.47 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.3, -18.8); signed map (12.0, 8.4). **Vector** length 58.4, 8.47% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -6.7 |
|  | [[NG25 (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | CDC20 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.2 — chr1:43,354,684-43,358,676 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55681) · Entrez [105378687](https://www.ncbi.nlm.nih.gov/gene/105378687) · Ensembl [ENSG00000234694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234694)

## Data

Gene col 13976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13976); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13976]; `tensor/DDL_lfc|DDL_z.npy` [13976]; `embed/gene_vectors.npy` [13976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13976 or target_col == 13976). Every well: [[CDC20-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC20-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
