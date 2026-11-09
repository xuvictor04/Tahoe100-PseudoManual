---
symbol: "SPRYD4"
type: "gene"
col: 10717
ensembl_id: "ENSG00000176422"
name: "SPRY domain containing 4"
location: "12q13.3"
module: 1
arm: "+"
pooled_cpm: 5.39
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SPRYD4

*SPRY domain containing 4* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.67× (z +8.1, q 3e-13, up in 22 of 46 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.46× (z +6.0, q 5e-07, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.446× (z -9.1, q 7e-17, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK5]] (+0.72, fdr 7e-06), [[PTCD1]] (+0.71, fdr 1e-05), [[STARD7-AS1]] (+0.71, fdr 1e-05); moves opposite to [[NBEAL1]] (-0.62, fdr 8e-05), [[DNAJC1]] (-0.61, fdr 3e-05), [[SPAG9]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.67×** | +8.1 | 3e-13 | 22/46 (Panc 03.27, A-427, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.0 | 5e-07 | 19/48 (HEC-1-A, A498, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.7 | 2e-06 | 19/31 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.9 | 1e-04 | 9/48 (SW480, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.032 | 9/46 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.37× | +3.2 | 0.12 | 2/14 (SW1417, A549) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.446×** | -9.1 | 7e-17 | 29/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.494×** | -7.9 | 8e-13 | 30/47 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.523×** | -7.3 | 7e-11 | 27/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.534×** | -7.0 | 3e-10 | 25/46 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.571×** | -6.3 | 4e-08 | 22/41 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.592×** | -5.7 | 1e-06 | 22/44 (COLO 205, A-427, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.606×** | -5.4 | 5e-06 | 16/35 (A549, NCI-H23, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.745×** | -4.7 | 2e-04 | 19/47 (SW1417, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.799×** | -3.6 | 0.023 | 16/39 (SNU-423, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.753×** | -3.2 | 0.073 | 8/47 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Gefitinib (drug)]] 5 µM |  | **0.753×** | -3.2 | 0.073 | 3/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.587×** | -3.1 | 0.083 | 6/46 (HepG2/C3A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.87 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.142× (z -10.6) ⚠ cell-cycle shift, explains ~95% of this change |
| [[PANC-1 (line)]] | alt | 6.14 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.116× (z -9.0) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 4.32 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.0575× (z -9.8) |
| [[A549 (line)]] | wt | 6.82 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0772× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0996× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 4.76 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0974× (z -8.5) |
| [[SW480 (line)]] | alt | 10.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -8.5) |
| [[A-172 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | +0.72 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PTCD1]] | +0.71 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.71 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB26]] | +0.70 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[UQCC1]] | +0.69 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[GTF3C2-AS2]] | +0.68 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[WASH2P-1]] | +0.68 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[RRN3P1]] | +0.68 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TIGD1]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[TMEM147-AS1]] | +0.67 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[THBS4]] | +0.67 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[UNC50]] | +0.66 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL1]] | -0.62 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[DNAJC1]] | -0.61 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.61 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[DNAAF3]] | -0.58 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[ARL3]] | -0.58 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CAST]] | -0.58 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[CDKN2D]] | -0.57 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[LGALS1]] | -0.56 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[RNF24]] | -0.56 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.4, 18.9); signed map (28.8, -19.1). **Vector** length 63.3, 9.22% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.5 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SPRY domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,468,578-56,479,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686N0877 |
| Matched by | ensembl_id |

UniProt [Q8WW59](https://www.uniprot.org/uniprotkb/Q8WW59) carries no function annotation.

**Summary**, from NCBI Gene [283377](https://www.ncbi.nlm.nih.gov/gene/283377):

> Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27468) · Entrez [283377](https://www.ncbi.nlm.nih.gov/gene/283377) · UniProt [Q8WW59](https://www.uniprot.org/uniprotkb/Q8WW59) · Ensembl [ENSG00000176422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176422)

## Data

Gene col 10717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10717); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10717]; `tensor/DDL_lfc|DDL_z.npy` [10717]; `embed/gene_vectors.npy` [10717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10717 or target_col == 10717). Every well: [[SPRYD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRYD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
