---
symbol: "RWDD1"
type: "gene"
col: 3288
ensembl_id: "ENSG00000111832"
name: "RWD domain containing 1"
location: "6q22.1"
module: 30
arm: "+"
pooled_cpm: 29.49
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# RWDD1

*RWD domain containing 1* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +7.5, q 4e-11, up in 35 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.84× (z +4.8, q 2e-04, up in 31 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOT1]] (+0.65, fdr 1e-05), [[RBM27]] (+0.65, fdr 7e-06), [[MTDH]] (+0.64, fdr 3e-05); moves opposite to [[CCNT2-AS1]] (-0.59, fdr 1e-04), [[DDX5]] (-0.56, fdr 4e-05), [[NEMP1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.73×** | +7.5 | 4e-11 | 35/37 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.98×** | +6.7 | 5e-09 | 38/42 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.81×** | +4.9 | 2e-04 | 28/40 (A-427, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.84×** | +4.8 | 2e-04 | 31/48 (SW480, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.69×** | +4.6 | 4e-04 | 31/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.004 | 36/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.0 | 0.004 | 34/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.008 | 32/47 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +3.7 | 0.011 | 27/48 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.52×** | +3.7 | 0.011 | 27/48 (LS 180, SNU-423, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.58×** | +3.4 | 0.033 | 24/47 (A549, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.034 | 27/47 (HEC-1-A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.45×** | +3.3 | 0.044 | 21/48 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.42×** | +3.1 | 0.070 | 20/47 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.42×** | +3.1 | 0.070 | 21/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOT1]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RBM27]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[MTDH]] | +0.64 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[MPHOSPH10]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[CRYZL1]] | +0.63 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[NSA2]] | +0.63 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[SUCLG1]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[EXOSC1]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CCZ1]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[DHX57]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 | same gene group |
| [[CINP]] | +0.61 | +0.64 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2-AS1]] | -0.59 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[DDX5]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[NEMP1]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PNRC2]] | -0.55 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[CCDC200]] | -0.54 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[SRSF5]] | -0.54 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.54 | -0.32 / -0.59 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-37.4, -10.7); signed map (-20.4, -8.5). **Vector** length 64.2, 18.0% of its response variance represented; |z| ≥ 3 in 511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | -3.1 | +3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -2.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -0.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RWD domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:116,571,409-116,597,675 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DFRP2, PTD013 |
| Gene groups (HGNC) | RWD domain containing |
| Reactome | 2 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H446](https://www.uniprot.org/uniprotkb/Q9H446) (RWD domain-containing protein 1):

> Protects DRG2 from proteolytic degradation (By similarity). May function as a coactivator of the AR/androgen receptor transcription factor during development.

**Summary**, from NCBI Gene [51389](https://www.ncbi.nlm.nih.gov/gene/51389):

> Enables transcription coactivator activity. Involved in androgen receptor signaling pathway. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20993) · Entrez [51389](https://www.ncbi.nlm.nih.gov/gene/51389) · UniProt [Q9H446](https://www.uniprot.org/uniprotkb/Q9H446) · Ensembl [ENSG00000111832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111832)

## Data

Gene col 3288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3288); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3288]; `tensor/DDL_lfc|DDL_z.npy` [3288]; `embed/gene_vectors.npy` [3288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3288 or target_col == 3288). Every well: [[RWDD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RWDD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
