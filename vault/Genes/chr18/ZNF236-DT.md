---
symbol: "ZNF236-DT"
type: "gene"
col: 15436
ensembl_id: "ENSG00000264278"
name: "ZNF236 divergent transcript"
location: "18q23"
module: 35
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ZNF236-DT

*ZNF236 divergent transcript* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.89× (z +15.6, q 0e+00, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +11.2, q 5e-27, up in 26 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.603× (z -3.8, q 0.065, down in 18 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJVK]] (+0.77, fdr 7e-06), [[PPP1R42]] (+0.74, fdr 7e-06), [[APPBP2-DT]] (+0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.89×** | +15.6 | 0e+00 | 3/3 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.65×** | +15.1 | 0e+00 | 13/14 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.26×** | +12.6 | 6e-34 | 5/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +11.2 | 5e-27 | 26/30 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.49×** | +8.9 | 7e-17 | 6/12 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +6.0 | 2e-07 | 11/43 (PANC-1, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.91×** | +4.8 | 1e-04 | 11/45 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.73×** | +4.0 | 0.004 | 5/40 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.050 | 9/23 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.2 | 0.066 | 6/30 (NCI-H460, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.2 | 0.078 | 3/15 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.603×** | -3.8 | 0.065 | 18/43 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.610×** | -3.7 | 0.065 | 12/46 (NCI-H23, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.02 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.8× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 4.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.91× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 2.96 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 24.5× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.725 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJVK]] | +0.77 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[PPP1R42]] | +0.74 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[APPBP2-DT]] | +0.71 | +0.57 / +0.62 | both halves | 1e-05 | same gene group |
| [[CARNMT1-AS1]] | +0.71 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ANKHD1-DT]] | +0.71 | +0.61 / +0.64 | both halves | 7e-06 | same gene group |
| [[CNPY2-AS1]] | +0.71 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[C2CD5-AS1]] | +0.70 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[GEMIN7-AS1]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | +0.68 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[ZKSCAN7-AS1]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.2, 24.3); signed map (31.6, -1.9). **Vector** length 50.8, 6.90% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +15.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Malotilate (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ZNF236 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q23 — chr18:76,794,732-76,822,295 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53779](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53779) · Entrez [100131655](https://www.ncbi.nlm.nih.gov/gene/100131655) · Ensembl [ENSG00000264278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264278)

## Data

Gene col 15436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15436); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15436]; `tensor/DDL_lfc|DDL_z.npy` [15436]; `embed/gene_vectors.npy` [15436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15436 or target_col == 15436). Every well: [[ZNF236-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF236-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
