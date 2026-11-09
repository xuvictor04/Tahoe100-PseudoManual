---
symbol: "COA3"
type: "gene"
col: 11479
ensembl_id: "ENSG00000183978"
name: "cytochrome c oxidase assembly factor 3"
location: "17q21.2"
module: 7
arm: "+"
pooled_cpm: 6.22
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# COA3

*cytochrome c oxidase assembly factor 3* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +5.3, q 4e-05, up in 6 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.70× (z +3.5, q 0.068, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.432× (z -5.5, q 2e-05, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL57]] (+0.78, fdr 7e-06), [[NDUFA8]] (+0.75, fdr 7e-06), [[MRPL46]] (+0.73, fdr 7e-06); moves opposite to [[TXNDC5]] (-0.60, fdr 4e-05), [[RPN1]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +5.3 | 4e-05 | 6/12 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.23×** | +5.3 | 4e-05 | 21/30 (A549, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.76×** | +3.7 | 0.039 | 18/32 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +3.5 | 0.068 | 18/46 (NCI-H1792, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.068 | 14/46 (A-427, KATO III, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.085 | 13/47 (AsPC-1, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.42× | +3.2 | 0.10 | 11/48 (Hs 766T, C-33 A, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.60× | +3.1 | 0.15 | 11/46 (KATO III, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -5.5 | 2e-05 | 33/46 (H4, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.597×** | -4.8 | 5e-04 | 22/41 (SW 900, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.524×** | -4.2 | 0.004 | 24/47 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.576×** | -3.6 | 0.044 | 19/46 (SW480, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.607× | -3.3 | 0.12 | 22/42 (HOP62, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.615× | -3.2 | 0.12 | 18/44 (Panc 03.27, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.710× | -3.2 | 0.12 | 22/39 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.632× | -3.0 | 0.19 | 19/46 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.43 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0642× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 9.48 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0846× (z -9.8) |
| [[A-172 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 11 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL57]] | +0.78 | +0.61 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[NDUFA8]] | +0.75 | +0.61 / +0.79 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 738 |
| [[MRPL46]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[MED11]] | +0.71 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[C18orf21]] | +0.70 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[THAP7]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ISCA2]] | +0.68 | +0.54 / +0.75 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[HDDC3]] | +0.66 | +0.40 / +0.74 | both halves | 5e-05 |  |
| [[CINP]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[GEMIN6]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[MRPL36]] | +0.65 | +0.32 / +0.72 | both halves | 2e-04 |  |
| [[TRAPPC5]] | +0.65 | +0.33 / +0.70 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | -0.60 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[RPN1]] | -0.55 | -0.31 / -0.61 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-42.9, -6.7); signed map (-17.7, -8.2). **Vector** length 54.7, 10.1% of its response variance represented; |z| ≥ 3 in 572 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,795,147-42,798,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC009, MITRAC12, COX25, hCOA3; previously CCDC56 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2R0](https://www.uniprot.org/uniprotkb/Q9Y2R0) (Cytochrome c oxidase assembly factor 3 homolog, mitochondrial):

> Core component of the MITRAC (mitochondrial translation regulation assembly intermediate of cytochrome c oxidase complex) complex, that regulates cytochrome c oxidase assembly. MITRAC complexes regulate both translation of mitochondrial encoded components and assembly of nuclear-encoded components imported in mitochondrion. Required for efficient translation of MT-CO1 and mitochondrial respiratory chain complex IV assembly.

**Summary**, from NCBI Gene [28958](https://www.ncbi.nlm.nih.gov/gene/28958):

> This gene encodes a member of the cytochrome c oxidase assembly factor family. Studies of a related gene in fly suggest that the encoded protein is localized to mitochondria and is essential for cytochrome c oxidase function. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:24990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24990) · Entrez [28958](https://www.ncbi.nlm.nih.gov/gene/28958) · UniProt [Q9Y2R0](https://www.uniprot.org/uniprotkb/Q9Y2R0) · Ensembl [ENSG00000183978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183978)

## Data

Gene col 11479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11479); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11479]; `tensor/DDL_lfc|DDL_z.npy` [11479]; `embed/gene_vectors.npy` [11479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11479 or target_col == 11479). Every well: [[COA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
