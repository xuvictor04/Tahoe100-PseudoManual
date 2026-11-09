---
symbol: "NUDT22"
type: "gene"
col: 7406
ensembl_id: "ENSG00000149761"
name: "nudix hydrolase 22"
location: "11q13.1"
module: 3
arm: "+"
pooled_cpm: 12.21
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# NUDT22

*nudix hydrolase 22* — 11q13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.338× (z -8.3, q 5e-14, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPT1]] (+0.81, fdr 7e-06, ⚠ same locus), [[SEC61G]] (+0.76, fdr 1e-05), [[MPG]] (+0.76, fdr 1e-05), [[MRPL55]] (+0.74, fdr 3e-05); moves opposite to [[EWSR1]] (-0.74, fdr 5e-05), [[SFPQ]] (-0.69, fdr 2e-04), [[SRSF1]] (-0.66, fdr 6e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.33× | +3.1 | 0.56 | 19/45 (RKO, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | 1.49× | +3.1 | 0.56 | 16/42 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.338×** | -8.3 | 5e-14 | 43/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.479×** | -8.0 | 4e-13 | 37/46 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.402×** | -7.0 | 5e-10 | 43/47 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.462×** | -5.7 | 2e-06 | 33/46 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.487×** | -5.5 | 4e-06 | 32/44 (C-33 A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -5.4 | 7e-06 | 32/44 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -5.0 | 4e-05 | 33/46 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.333×** | -4.4 | 7e-04 | 31/42 (Panc 03.27, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -4.3 | 0.001 | 27/46 (LOX-IMVI, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.555×** | -4.2 | 0.002 | 18/32 (KATO III, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.602×** | -3.9 | 0.005 | 23/47 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.660×** | -3.2 | 0.070 | 22/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.642×** | -3.1 | 0.075 | 16/47 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -3.0 | 0.094 | 17/39 (HCT15, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 15.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.0) |
| [[J82 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -9.6) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -8.9) |
| [[HOP62 (line)]] | alt | 7.12 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -8.8) |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.4) |
| [[KATO III (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 8.27 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0937× (z -11.8) |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.0) |
| [[RKO (line)]] | wt | 8.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0778× (z -9.6) |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 11 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPT1]] | +0.81 | +0.67 / +0.85 | both halves | 7e-06 | STRING 862; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SEC61G]] | +0.76 | +0.55 / +0.85 | both halves | 1e-05 |  |
| [[MPG]] | +0.76 | +0.49 / +0.83 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.74 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[ING2]] | +0.74 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[C16orf91]] | +0.73 | +0.39 / +0.78 | both halves | 5e-05 |  |
| [[IMP3]] | +0.72 | +0.43 / +0.78 | both halves | 3e-05 |  |
| [[CCDC107]] | +0.71 | +0.42 / +0.78 | both halves | 4e-05 |  |
| [[POLR2H]] | +0.70 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.70 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[OCEL1]] | +0.70 | +0.35 / +0.72 | both halves | 1e-04 |  |
| [[SDHAF1]] | +0.69 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[EMC6]] | +0.68 | +0.23 / +0.77 | both halves | 5e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.74 | -0.40 / -0.80 | both halves | 5e-05 |  |
| [[SFPQ]] | -0.69 | -0.30 / -0.75 | both halves | 2e-04 |  |
| [[SRSF1]] | -0.66 | -0.38 / -0.66 | both halves | 6e-05 |  |
| [[DHFR]] | -0.66 | -0.22 / -0.75 | both halves | 6e-04 |  |
| [[LIN7C]] | -0.66 | -0.33 / -0.75 | both halves | 1e-04 |  |
| [[ARPP19]] | -0.64 | -0.25 / -0.70 | both halves | 4e-04 |  |
| [[RCN1]] | -0.64 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[SGPL1]] | -0.64 | -0.34 / -0.74 | both halves | 1e-04 |  |
| [[DPY19L4]] | -0.63 | -0.21 / -0.70 | both halves | 6e-04 |  |
| [[GALC]] | -0.63 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[NONO]] | -0.62 | -0.34 / -0.76 | both halves | 1e-04 |  |
| [[YWHAE]] | -0.62 | -0.31 / -0.64 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.6, -18.9); signed map (-30.8, 11.2). **Vector** length 82.1, 21.0% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.4 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.3 | +1.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -8.6 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.5 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.4 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -3.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,225,941-64,230,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13045 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRQ3](https://www.uniprot.org/uniprotkb/Q9BRQ3) (Uridine diphosphate glucose pyrophosphatase NUDT22):

> Pyrophosphatase hydrolyzing the diphosphate bond in the nucleotide-sugars UDP-glucose and UDP-galactose with a preference for the former, yielding glucose 1-phosphate or galactose 1-phosphate and UMP.

**Summary**, from NCBI Gene [84304](https://www.ncbi.nlm.nih.gov/gene/84304):

> Enables UDP-sugar diphosphatase activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28189) · Entrez [84304](https://www.ncbi.nlm.nih.gov/gene/84304) · UniProt [Q9BRQ3](https://www.uniprot.org/uniprotkb/Q9BRQ3) · Ensembl [ENSG00000149761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149761)

## Data

Gene col 7406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7406); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7406]; `tensor/DDL_lfc|DDL_z.npy` [7406]; `embed/gene_vectors.npy` [7406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7406 or target_col == 7406). Every well: [[NUDT22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
