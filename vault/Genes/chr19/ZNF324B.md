---
symbol: "ZNF324B"
type: "gene"
col: 14615
ensembl_id: "ENSG00000249471"
name: "zinc finger protein 324B"
location: "19q13.43"
module: 36
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ZNF324B

*zinc finger protein 324B* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.94× (z +15.3, q 0e+00, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.518× (z -6.6, q 2e-08, down in 15 of 45 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYCR3]] (+0.58, fdr 2e-05), [[SLC35C1]] (+0.57, fdr 5e-05), [[TTI1]] (+0.55, fdr 1e-04); moves opposite to [[SESN3]] (-0.50, fdr 2e-04), [[GKAP1]] (-0.48, fdr 0.001, ⚠ not reproduced), [[KPNA5]] (-0.44, fdr 0.001, ⚠ not reproduced), [[KLHL13]] (-0.41, fdr 5e-04), [[ABLIM1]] (-0.41, fdr 4e-04).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +15.3 | 0e+00 | 26/31 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.10×** | +14.2 | 3e-43 | 41/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.43×** | +12.4 | 6e-33 | 33/43 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.19×** | +11.7 | 3e-29 | 33/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.07×** | +7.3 | 4e-11 | 15/30 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.1 | 9e-11 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +6.8 | 8e-10 | 12/23 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.91×** | +6.2 | 5e-08 | 3/10 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +5.7 | 9e-07 | 9/44 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +5.4 | 4e-06 | 1/2 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.35×** | +4.2 | 0.001 | 2/43 (C-33 A, RKO) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.46×** | +3.8 | 0.008 | 4/40 (SW480, HCT15, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.38×** | +3.2 | 0.053 | 2/44 (A-427, NCI-H1792) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.053 | 2/45 (SW 900, A498) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.053 | 3/18 (A-172, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +3.1 | 0.066 | 1/37 (PANC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.078 | 1/43 (SW480) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.078 | 0/23 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.0 | 0.091 | 3/36 (RKO, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -6.6 | 2e-08 | 15/45 (SW1417, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -4.1 | 0.012 | 10/18 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -4.0 | 0.013 | 8/40 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.711×** | -3.4 | 0.084 | 5/45 (NCI-H2347, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Roxadustat (drug)]] 0.5 µM |  | **0.717×** | -3.4 | 0.086 | 7/43 (HS-578T, HT-29, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM |  | 0.725× | -3.2 | 0.11 | 11/42 (CFPAC-1, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.82 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.0658× (z -9.2) |
| [[PANC-1 (line)]] | alt | 1.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0803× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.714 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.806 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.555 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 14 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYCR3]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SLC35C1]] | +0.57 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[TTI1]] | +0.55 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[MLYCD]] | +0.53 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[EMC8]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D10B]] | +0.51 | +0.21 / +0.48 | both halves | 7e-04 |  |
| [[MEN1]] | +0.49 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[TOMM40]] | +0.49 | +0.35 / +0.42 | both halves | 1e-04 |  |
| [[LRRC14]] | +0.49 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[IL9RP3]] | +0.49 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TBL3]] | +0.49 | +0.33 / +0.43 | both halves | 1e-04 |  |
| [[SIRT3]] | +0.49 | +0.38 / +0.40 | both halves | 6e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SESN3]] | -0.50 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[GKAP1]] | -0.48 | -0.17 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[KPNA5]] | -0.44 | -0.18 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[FAM171B]] | -0.42 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[KLHL13]] | -0.41 | -0.23 / -0.32 | both halves | 5e-04 |  |
| [[ABLIM1]] | -0.41 | -0.24 / -0.47 | both halves | 4e-04 |  |
| [[ATF7IP2]] | -0.41 | -0.05 / -0.35 | ⚠ not reproduced | 0.005 |  |
| [[OAZ1]] | -0.41 | -0.13 / -0.35 | ⚠ not reproduced | 0.002 |  |
| [[LGALS3]] | -0.40 | -0.11 / -0.34 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.399). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-24.3, -47.9); signed map (-51.7, -0.0). **Vector** length 31.3, 2.53% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.6 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.8 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.7 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.7 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 324B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,451,611-58,457,833 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45850 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6AW86](https://www.uniprot.org/uniprotkb/Q6AW86) (Zinc finger protein 324B):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [388569](https://www.ncbi.nlm.nih.gov/gene/388569):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33107) · Entrez [388569](https://www.ncbi.nlm.nih.gov/gene/388569) · UniProt [Q6AW86](https://www.uniprot.org/uniprotkb/Q6AW86) · Ensembl [ENSG00000249471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249471)

## Data

Gene col 14615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14615); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14615]; `tensor/DDL_lfc|DDL_z.npy` [14615]; `embed/gene_vectors.npy` [14615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14615 or target_col == 14615). Every well: [[ZNF324B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF324B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
