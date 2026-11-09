---
symbol: "CSKMT"
type: "gene"
col: 13219
ensembl_id: "ENSG00000214756"
name: "citrate synthase lysine methyltransferase"
location: "11q12.3"
module: 24
arm: "+"
pooled_cpm: 8.32
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CSKMT

*citrate synthase lysine methyltransferase* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.90× (z +10.5, q 7e-23, up in 29 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +5.6, q 3e-06, up in 33 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.185×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG19]] (+0.88, fdr 7e-06), [[SNHG25]] (+0.80, fdr 7e-06), [[DCTN6-DT]] (+0.77, fdr 7e-06); moves opposite to [[PDAP1]] (-0.73, fdr 7e-06), [[XRCC6]] (-0.66, fdr 1e-05), [[CCT7]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.90×** | +10.5 | 7e-23 | 29/30 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.03×** | +9.4 | 2e-18 | 14/14 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.47×** | +7.8 | 1e-12 | 36/37 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.54×** | +6.3 | 3e-08 | 18/22 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.90×** | +5.8 | 9e-07 | 39/44 (NCI-H460, KATO III, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +5.6 | 3e-06 | 33/41 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +5.0 | 6e-05 | 23/35 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +4.9 | 7e-05 | 28/45 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.26×** | +4.4 | 6e-04 | 30/46 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.12×** | +4.1 | 0.003 | 26/46 (KATO III, SW1417, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **2.07×** | +3.9 | 0.004 | 25/39 (A-172, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.05×** | +3.9 | 0.005 | 23/45 (SW480, A-172, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.54×** | +3.4 | 0.032 | 16/37 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.34×** | +3.1 | 0.086 | 16/42 (SW480, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.32×** | +3.1 | 0.086 | 14/33 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **2.29×** | +3.0 | 0.094 | 14/45 (SW1417, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.185×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 10.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 24.9× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 9.33 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.4× (z +10.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 8.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.9× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 6.93 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 1 | — | [[Pyridoxine (hydrochloride) (drug)]] 5 µM 0.185× (z -9.0) |
| [[SW480 (line)]] | alt | 7.70 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 16 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG19]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.77 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.75 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[KIZ-AS1]] ⚠ | +0.73 | +0.58 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EFCAB14-AS1]] | +0.73 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[RN7SL2]] | +0.72 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | +0.68 | +0.62 / +0.66 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[MIR4458HG]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[STK32C]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[RPL36]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.73 | -0.62 / -0.78 | both halves | 7e-06 |  |
| [[XRCC6]] | -0.66 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[CCT7]] | -0.63 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[AKAP11]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PSMC3]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.8, -23.1); signed map (-28.8, 7.0). **Vector** length 64.8, 15.0% of its response variance represented; |z| ≥ 3 in 585 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +2.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | citrate synthase lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,665,309-62,668,496 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U99HG, CS-KMT; previously METTL12 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Reactome | 3 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MUP2](https://www.uniprot.org/uniprotkb/A8MUP2) (Citrate synthase-lysine N-methyltransferase CSKMT, mitochondrial):

> Protein-lysine methyltransferase that selectively trimethylates citrate synthase (CS) in mitochondria. Seems to conduct trimethylation in a highly distributive manner rather than in a processive manner, and thus introduces a single methyl group per binding event.

**Summary**, from NCBI Gene [751071](https://www.ncbi.nlm.nih.gov/gene/751071):

> Enables protein-lysine N-methyltransferase activity. Involved in peptidyl-lysine dimethylation; peptidyl-lysine monomethylation; and peptidyl-lysine trimethylation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33113) · Entrez [751071](https://www.ncbi.nlm.nih.gov/gene/751071) · UniProt [A8MUP2](https://www.uniprot.org/uniprotkb/A8MUP2) · Ensembl [ENSG00000214756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214756)

## Data

Gene col 13219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13219); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13219]; `tensor/DDL_lfc|DDL_z.npy` [13219]; `embed/gene_vectors.npy` [13219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13219 or target_col == 13219). Every well: [[CSKMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSKMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
