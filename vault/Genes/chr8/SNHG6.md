---
symbol: "SNHG6"
type: "gene"
col: 14449
ensembl_id: "ENSG00000245910"
name: "small nucleolar RNA host gene 6"
location: "8q13.1"
module: 43
arm: "+"
pooled_cpm: 100.35
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# SNHG6

*small nucleolar RNA host gene 6* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.23× (z +5.2, q 1e-04, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.91× (z +3.6, q 0.045, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS27]] (+0.90, fdr 7e-06), [[RPL36]] (+0.90, fdr 7e-06), [[RPL31]] (+0.90, fdr 7e-06); moves opposite to [[PSME3]] (-0.71, fdr 8e-06), [[PNPO]] (-0.70, fdr 1e-05), [[DR1]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.23×** | +5.2 | 1e-04 | 47/49 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.48×** | +4.9 | 3e-04 | 42/44 (NCI-H460, H4, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +4.2 | 0.006 | 45/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +3.6 | 0.045 | 39/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.85×** | +3.4 | 0.064 | 40/48 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.92×** | +3.4 | 0.074 | 36/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +3.2 | 0.096 | 39/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.81× | +3.1 | 0.13 | 40/48 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.46× | +3.0 | 0.16 | 28/49 (NCI-H2347, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 240 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 192 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS27]] | +0.90 | +0.81 / +0.92 | both halves | 7e-06 |  |
| [[RPL36]] | +0.90 | +0.76 / +0.94 | both halves | 7e-06 |  |
| [[RPL31]] | +0.90 | +0.75 / +0.94 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.90 | +0.74 / +0.93 | both halves | 7e-06 |  |
| [[RPL34]] | +0.89 | +0.73 / +0.93 | both halves | 7e-06 |  |
| [[RPS8]] | +0.89 | +0.75 / +0.92 | both halves | 7e-06 |  |
| [[RPS3]] ⚠ | +0.88 | +0.77 / +0.91 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS6]] ⚠ | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | +0.88 | +0.75 / +0.92 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.88 | +0.76 / +0.92 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | +0.88 | +0.80 / +0.90 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | +0.88 | +0.75 / +0.92 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | +0.87 | +0.84 / +0.89 | both halves | 7e-06 | same gene group |
| [[RPL26]] | +0.87 | +0.73 / +0.92 | both halves | 7e-06 |  |
| [[RPL23]] | +0.87 | +0.74 / +0.90 | both halves | 7e-06 |  |
| [[RPS19]] | +0.86 | +0.74 / +0.90 | both halves | 7e-06 |  |
| [[RPL36A]] | +0.86 | +0.72 / +0.90 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.71 | -0.57 / -0.71 | both halves | 8e-06 |  |
| [[PNPO]] | -0.70 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[DR1]] | -0.70 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[VMA21]] | -0.70 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.69 | -0.48 / -0.74 | both halves | 2e-05 |  |
| [[GPAA1]] | -0.69 | -0.65 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.875). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.8, -27.4); signed map (-59.0, -3.8). **Vector** length 93.3, 51.6% of its response variance represented; |z| ≥ 3 in 449 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.74 to 55); *Peptide chain elongation* (reactome, mean cos +0.75 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.74 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | +0.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.3 | +0.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.3 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.8 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.4 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.3 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -0.5 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.5 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 6 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q13.1 — chr8:66,920,561-66,926,398 (-) |
| Ensembl biotype | lncRNA |
| Also known as | U87HG, HBII-276HG, NCRNA00058 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [641638](https://www.ncbi.nlm.nih.gov/gene/641638):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32965) · Entrez [641638](https://www.ncbi.nlm.nih.gov/gene/641638) · Ensembl [ENSG00000245910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245910)

## Data

Gene col 14449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14449); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14449]; `tensor/DDL_lfc|DDL_z.npy` [14449]; `embed/gene_vectors.npy` [14449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14449 or target_col == 14449). Every well: [[SNHG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
