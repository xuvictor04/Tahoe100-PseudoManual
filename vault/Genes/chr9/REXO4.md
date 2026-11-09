---
symbol: "REXO4"
type: "gene"
col: 7261
ensembl_id: "ENSG00000148300"
name: "RNA exonuclease 4"
location: "9q34.2"
module: 11
arm: "+"
pooled_cpm: 26.39
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# REXO4

*RNA exonuclease 4* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.10× (z +9.0, q 2e-16, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.542× (z -7.4, q 9e-11, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF6]] (+0.82, fdr 7e-06), [[NOL8]] (+0.80, fdr 7e-06), [[UTP14A]] (+0.78, fdr 7e-06); moves opposite to [[GNAS]] (-0.63, fdr 7e-06), [[PRCP]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +9.0 | 2e-16 | 38/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.02×** | +7.0 | 9e-10 | 38/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +6.5 | 2e-08 | 32/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.4 | 3e-08 | 32/47 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +6.0 | 3e-07 | 36/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.58×** | +5.3 | 1e-05 | 26/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.47×** | +4.7 | 2e-04 | 20/44 (NCI-H2347, NCI-H1792, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +4.4 | 7e-04 | 32/48 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +4.2 | 0.002 | 25/48 (CFPAC-1, HepG2/C3A, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.003 | 29/47 (LOX-IMVI, A-172, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +3.9 | 0.004 | 22/46 (RKO, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.007 | 17/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +3.6 | 0.012 | 22/48 (HepG2/C3A, A549, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.022 | 20/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.31×** | +3.3 | 0.042 | 19/47 (LoVo, COLO 205, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.542×** | -7.4 | 9e-11 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.563×** | -6.9 | 1e-09 | 35/47 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -6.8 | 1e-09 | 31/47 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -5.4 | 9e-06 | 29/48 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -4.4 | 0.001 | 24/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.747×** | -3.5 | 0.040 | 19/48 (A549, Panc 03.27, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.818×** | -3.4 | 0.047 | 20/48 (SHP-77, SW1417, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.1 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.34× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -10.9) |
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.374× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.414× (z -8.7) |
| [[RKO (line)]] | wt | 80.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -8.5) |
| [[A-172 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0514× (z -20.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 32.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.315× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[A-427 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF6]] | +0.82 | +0.84 / +0.80 | both halves | 7e-06 | STRING 673 |
| [[NOL8]] | +0.80 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.78 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[NIFK]] | +0.77 | +0.82 / +0.76 | both halves | 7e-06 | STRING 623 |
| [[AGGF1]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.76 | +0.78 / +0.80 | both halves | 7e-06 | STRING 703 |
| [[RBAK]] | +0.75 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.75 | +0.84 / +0.71 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.74 | +0.80 / +0.75 | both halves | 7e-06 | STRING 731 |
| [[CCDC137]] | +0.73 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[RRS1]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 | STRING 508 |
| [[CINP]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.63 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[PRCP]] | -0.60 | -0.34 / -0.68 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.5, 1.1); signed map (-1.4, -21.7). **Vector** length 105, 28.9% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | -7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[ERK5-IN-2 (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA exonuclease 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,406,059-133,418,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hPMC2; previously XPMC2H |
| Gene groups (HGNC) | Exonucleases |
| Matched by | ensembl_id |

UniProt [Q9GZR2](https://www.uniprot.org/uniprotkb/Q9GZR2) carries no function annotation.

**Summary**, from NCBI Gene [57109](https://www.ncbi.nlm.nih.gov/gene/57109):

> Enables DNA binding activity and nuclease activity. Involved in DNA catabolic process and DNA repair. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12820) · Entrez [57109](https://www.ncbi.nlm.nih.gov/gene/57109) · UniProt [Q9GZR2](https://www.uniprot.org/uniprotkb/Q9GZR2) · Ensembl [ENSG00000148300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148300)

## Data

Gene col 7261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7261); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7261]; `tensor/DDL_lfc|DDL_z.npy` [7261]; `embed/gene_vectors.npy` [7261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7261 or target_col == 7261). Every well: [[REXO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REXO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
