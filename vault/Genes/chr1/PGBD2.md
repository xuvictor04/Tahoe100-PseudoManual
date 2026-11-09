---
symbol: "PGBD2"
type: "gene"
col: 11641
ensembl_id: "ENSG00000185220"
name: "piggyBac transposable element derived 2"
location: "1q44"
module: 7
arm: "+"
pooled_cpm: 3.86
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PGBD2

*piggyBac transposable element derived 2* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.57× (z +5.0, q 3e-04, up in 7 of 21 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.43× (z +4.1, q 0.007, up in 12 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.375× (z -11.3, q 9e-27, down in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.419× (z -10.0, q 5e-21, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF561]] (+0.62, fdr 1e-05), [[EXO5]] (+0.60, fdr 1e-05), [[ZNF777]] (+0.59, fdr 9e-05); moves opposite to [[RFX2]] (-0.57, fdr 1e-04), [[NR6A1]] (-0.55, fdr 5e-05), [[CSPP1]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.0 | 3e-04 | 7/21 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.007 | 12/45 (SNU-423, SW48, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.007 | 8/45 (PANC-1, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.029 | 0/45 | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.092 | 5/43 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.099 | 3/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.34× | +3.1 | 0.16 | 1/8 (A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.375×** | -11.3 | 9e-27 | 25/35 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -10.0 | 5e-21 | 33/47 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.544×** | -7.0 | 5e-10 | 22/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -6.1 | 1e-07 | 22/45 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.640×** | -4.9 | 1e-04 | 17/45 (SNU-423, PANC-1, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -4.2 | 0.002 | 16/44 (LS 180, SW1417, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -3.7 | 0.015 | 9/37 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.736×** | -3.5 | 0.031 | 10/47 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.088 | 12/46 (SK-MEL-2, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.752×** | -3.1 | 0.094 | 10/28 (A-172, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.77 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0393× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0902× (z -11.3) |
| [[SHP-77 (line)]] | alt | 3.71 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0335× (z -10.5) |
| [[A-172 (line)]] | wt | 4.94 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 4.28 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0679× (z -9.8) |
| [[HT-29 (line)]] | alt | 5.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0861× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 5.63 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0682× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0781× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 3.44 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0985× (z -9.3) |
| [[SW1417 (line)]] | alt | 3.95 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0980× (z -8.6) |
| [[A498 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF561]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[EXO5]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.59 | +0.67 / +0.36 | both halves | 9e-05 |  |
| [[RAE1]] | +0.57 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ZNF691]] | +0.57 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[ZNF746]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[RRN3P1]] | +0.55 | +0.54 / +0.43 | both halves | 4e-05 |  |
| [[RRN3]] | +0.55 | +0.67 / +0.30 | both halves | 2e-04 |  |
| [[ZBTB45]] | +0.55 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[MTHFS]] | +0.54 | +0.56 / +0.31 | both halves | 2e-04 |  |
| [[ZNF2]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[SPRYD4]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX2]] | -0.57 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[NR6A1]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CSPP1]] | -0.52 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[PEAK1]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[NBEAL1]] | -0.47 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[ELP4]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.8, 22.5); signed map (-7.6, -24.1). **Vector** length 48.1, 5.31% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -10.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -6.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -0.9 | +0.0 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | piggyBac transposable element derived 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:248,906,196-248,919,946 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PiggyBac transposable element derived family |
| Matched by | ensembl_id |

UniProt [Q6P3X8](https://www.uniprot.org/uniprotkb/Q6P3X8) carries no function annotation.

**Summary**, from NCBI Gene [267002](https://www.ncbi.nlm.nih.gov/gene/267002):

> The piggyBac family of proteins, found in diverse animals, are transposases related to the transposase of the canonical piggyBac transposon from the moth, Trichoplusia ni. This family also includes genes in several genomes, including human, that appear to have been derived from the piggyBac transposons. This gene belongs to the subfamily of piggyBac transposable element derived (PGBD) genes. The PGBD proteins appear to be novel, with no obvious relationship to other transposases, or other known …

**Accessions** — [HGNC:19399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19399) · Entrez [267002](https://www.ncbi.nlm.nih.gov/gene/267002) · UniProt [Q6P3X8](https://www.uniprot.org/uniprotkb/Q6P3X8) · Ensembl [ENSG00000185220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185220)

## Data

Gene col 11641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11641); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11641]; `tensor/DDL_lfc|DDL_z.npy` [11641]; `embed/gene_vectors.npy` [11641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11641 or target_col == 11641). Every well: [[PGBD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGBD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
