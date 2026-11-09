---
symbol: "THAP7"
type: "gene"
col: 11536
ensembl_id: "ENSG00000184436"
name: "THAP domain containing 7"
location: "22q11.21"
module: 7
arm: "+"
pooled_cpm: 3.41
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# THAP7

*THAP domain containing 7* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.38× (z +5.8, q 4e-06, up in 1 of 5 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.312× (z -8.1, q 3e-13, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KTI12]] (+0.74, fdr 7e-06), [[FADD]] (+0.70, fdr 7e-06), [[COA3]] (+0.69, fdr 7e-06); moves opposite to [[FAM81A]] (-0.58, fdr 6e-05), [[SLC35F5]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.38×** | +5.8 | 4e-06 | 1/5 (NCI-H2347) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.81×** | +4.1 | 0.009 | 18/45 (AsPC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +3.8 | 0.029 | 10/20 (Panc 03.27, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 1.39× | +3.3 | 0.14 | 2/44 (RKO, HT-29) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | 1.62× | +3.2 | 0.14 | 8/24 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.57× | +3.1 | 0.16 | 15/44 (Hs 766T, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11536.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.312×** | -8.1 | 3e-13 | 34/46 (HCT15, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -6.3 | 1e-07 | 31/43 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.419×** | -6.0 | 3e-07 | 30/44 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -5.8 | 8e-07 | 20/31 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.42 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0492× (z -11.1) |
| [[KATO III (line)]] | alt | 7.12 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0659× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 3.22 | 0 | 1 | — | [[Lumateperone (tosylate) (drug)]] 0.05 µM 0.0516× (z -9.2) |
| [[PANC-1 (line)]] | alt | 3.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0406× (z -12.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 6.46 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0453× (z -12.0) |
| [[SW480 (line)]] | alt | 3.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0534× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTI12]] | +0.74 | +0.66 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[FADD]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[COA3]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[DDX28]] | +0.69 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[C6orf47]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMEM11]] | +0.67 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[EXOSC4]] | +0.67 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[MRPL57]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[MRPS26]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[TRMT10C]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[BLOC1S4]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[HPS6]] | +0.62 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.58 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[SLC35F5]] | -0.53 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.4, -0.3); signed map (-4.6, -24.8). **Vector** length 50.0, 6.90% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +1.7 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -2.6 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -0.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,999,104-21,002,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10963 |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT49](https://www.uniprot.org/uniprotkb/Q9BT49) (THAP domain-containing protein 7):

> Chromatin-associated, histone tail-binding protein that represses transcription via recruitment of HDAC3 and nuclear hormone receptor corepressors.

**Summary**, from NCBI Gene [80764](https://www.ncbi.nlm.nih.gov/gene/80764):

> Enables several functions, including C2H2 zinc finger domain binding activity; histone deacetylase binding activity; and transcription corepressor binding activity. Involved in chromatin organization and negative regulation of transcription by RNA polymerase II. Located in chromatin and nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23190) · Entrez [80764](https://www.ncbi.nlm.nih.gov/gene/80764) · UniProt [Q9BT49](https://www.uniprot.org/uniprotkb/Q9BT49) · Ensembl [ENSG00000184436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184436)

## Data

Gene col 11536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11536); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11536]; `tensor/DDL_lfc|DDL_z.npy` [11536]; `embed/gene_vectors.npy` [11536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11536 or target_col == 11536). Every well: [[THAP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
