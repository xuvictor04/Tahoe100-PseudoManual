---
symbol: "RPUSD2"
type: "gene"
col: 9241
ensembl_id: "ENSG00000166133"
name: "RNA pseudouridine synthase domain containing 2"
location: "15q15.1"
module: 119
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# RPUSD2

*RNA pseudouridine synthase domain containing 2* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.73× (z +8.9, q 3e-16, up in 9 of 10 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +8.3, q 3e-14, up in 17 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KTI12]] (+0.77, fdr 7e-06), [[NCBP2AS2]] (+0.71, fdr 7e-06), [[C16orf91]] (+0.69, fdr 7e-06); moves opposite to [[CTNNA1]] (-0.55, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.73×** | +8.9 | 3e-16 | 9/10 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +8.3 | 3e-14 | 17/29 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +8.0 | 2e-13 | 24/42 (LoVo, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.27×** | +7.3 | 5e-11 | 0/1 | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.09×** | +6.8 | 1e-09 | 20/45 (PANC-1, A-172, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.03×** | +6.5 | 6e-09 | 7/10 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.88×** | +5.8 | 4e-07 | 15/43 (SW480, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +5.6 | 1e-06 | 15/44 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +5.5 | 3e-06 | 8/35 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.3 | 5e-06 | 9/31 (CFPAC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +5.3 | 6e-06 | 4/44 (SW1417, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +4.5 | 3e-04 | 11/40 (LoVo, LOX-IMVI, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +4.5 | 3e-04 | 6/24 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.91×** | +4.3 | 8e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.65×** | +4.2 | 8e-04 | 0/2 | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +4.1 | 0.002 | 3/17 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.58×** | +3.9 | 0.004 | 6/26 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[LJI308 (drug)]] 0.5 µM |  | **1.71×** | +3.5 | 0.014 | 2/28 (J82, Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.5 | 0.014 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +3.4 | 0.020 | 6/26 (LoVo, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.030 | 1/17 (Hs 766T) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.040 | 4/20 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.58 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.860 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTI12]] | +0.77 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NCBP2AS2]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[C16orf91]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TMEM11]] | +0.68 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[BRIX1]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[YRDC]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[FASTKD3]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZNF7]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MIEF1]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[TARS2]] | +0.67 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[GEMIN6]] | +0.67 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[BLOC1S4]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNA1]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.3, -9.1); signed map (-11.1, -10.9). **Vector** length 34.6, 3.27% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.6 | +5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +3.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.0 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -0.9 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | +0.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -0.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA pseudouridine synthase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,569,299-40,574,949 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C18B11, FLJ31409, PUS9; previously C15orf19 |
| Gene groups (HGNC) | RNA pseudouridylate synthase domain containing; Pseudouridine synthases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ73](https://www.uniprot.org/uniprotkb/Q8IZ73) (Pseudouridylate synthase RPUSD2):

> Pseudouridine synthase that catalyzes pseudouridylation of mRNAs. In addition, it catalyzes the formation of pseudouridine mainly at positions 31 and 32 in the anticodon loop of cytosolic and mitochondrial tRNAs, and at position 34 of certain cytosolic tRNAs such as tRNA(Ile).

**Summary**, from NCBI Gene [27079](https://www.ncbi.nlm.nih.gov/gene/27079):

> Enables pseudouridine synthase activity. Involved in mRNA pseudouridine synthesis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24180) · Entrez [27079](https://www.ncbi.nlm.nih.gov/gene/27079) · UniProt [Q8IZ73](https://www.uniprot.org/uniprotkb/Q8IZ73) · Ensembl [ENSG00000166133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166133)

## Data

Gene col 9241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9241); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9241]; `tensor/DDL_lfc|DDL_z.npy` [9241]; `embed/gene_vectors.npy` [9241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9241 or target_col == 9241). Every well: [[RPUSD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPUSD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
