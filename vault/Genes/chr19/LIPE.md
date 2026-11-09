---
symbol: "LIPE"
type: "gene"
col: 1257
ensembl_id: "ENSG00000079435"
name: "lipase E, hormone sensitive type"
location: "19q13.2"
module: 161
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# LIPE

*lipase E, hormone sensitive type* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.60× (z +9.1, q 8e-17, up in 26 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (HEC-1-A 0.0870×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0486×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (J82 0.0676×).
> Its strongest partners by |cos| (52 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 48 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGFR4]] (+0.52, fdr 6e-05), [[FBXO46]] (+0.52, fdr 6e-05), [[LMTK3]] (+0.52, fdr 2e-04); moves opposite to [[DPH6-DT]] (-0.53, fdr 8e-04, ⚠ not reproduced), [[SPRY3]] (-0.51, fdr 4e-04), [[CHD1-DT]] (-0.50, fdr 0.002, ⚠ not reproduced), [[UHMK1]] (-0.48, fdr 4e-05), [[CBR4]] (-0.47, fdr 4e-04).
> It is in [[Module 161]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.60×** | +9.1 | 8e-17 | 26/42 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.58×** | +9.0 | 8e-17 | 28/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.43×** | +8.4 | 8e-15 | 24/41 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.2 | 1e-10 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.4 | 2e-08 | 10/28 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.96×** | +6.4 | 2e-08 | 13/28 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +6.0 | 2e-07 | 2/9 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +5.9 | 2e-07 | 15/43 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.4 | 4e-06 | 12/32 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +5.4 | 4e-06 | 1/9 (HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.3 | 8e-04 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.030 | 2/42 (HOP62, J82) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.1 | 0.077 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.080 | 4/41 (J82, SHP-77, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (HEC-1-A 0.0870×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0486×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (J82 0.0676×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.73 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0870× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 2.78 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0676× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 1.74 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0486× (z -8.6) |
| [[A-172 (line)]] | wt | 0.879 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.694 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.594 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.779 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.726 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.780 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.523 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGFR4]] | +0.52 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[FBXO46]] | +0.52 | +0.42 / +0.39 | both halves | 6e-05 |  |
| [[LMTK3]] | +0.52 | +0.32 / +0.32 | both halves | 2e-04 |  |
| [[SLC66A2]] | +0.51 | +0.24 / +0.41 | both halves | 4e-04 |  |
| [[DNAAF3]] | +0.51 | +0.22 / +0.40 | both halves | 6e-04 |  |
| [[ALDH4A1]] | +0.51 | +0.36 / +0.40 | both halves | 9e-05 |  |
| [[PI4KAP1]] | +0.50 | +0.18 / +0.42 | ⚠ not reproduced | 9e-04 |  |
| [[RHPN1]] | +0.50 | +0.27 / +0.35 | both halves | 3e-04 |  |
| [[SHF]] | +0.50 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[FOXO6]] | +0.49 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[EPHA1]] | +0.49 | +0.46 / +0.31 | both halves | 2e-04 |  |
| [[FCHO1]] | +0.49 | +0.21 / +0.35 | both halves | 6e-04 |  |
| [[SEMA3F]] | +0.48 | +0.32 / +0.35 | both halves | 2e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 33 of them with an alert (⚠; 33 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH6-DT]] | -0.53 | -0.20 / -0.30 | ⚠ not reproduced | 8e-04 |  |
| [[SPRY3]] | -0.51 | -0.24 / -0.27 | both halves | 4e-04 |  |
| [[CHD1-DT]] | -0.50 | -0.12 / -0.35 | ⚠ not reproduced | 0.002 |  |
| [[CSTF3]] | -0.49 | -0.14 / -0.32 | ⚠ not reproduced | 0.002 |  |
| [[UHMK1]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[LINC01004]] | -0.48 | -0.11 / -0.37 | ⚠ not reproduced | 0.002 |  |
| [[ACYP2]] | -0.48 | -0.15 / -0.36 | ⚠ not reproduced | 0.001 |  |
| [[LINC01376]] | -0.47 | -0.20 / -0.32 | ⚠ not reproduced | 7e-04 |  |
| [[ANKRD17-DT]] | -0.47 | -0.10 / -0.30 | ⚠ not reproduced | 0.003 |  |
| [[CBR4]] | -0.47 | -0.28 / -0.26 | both halves | 4e-04 |  |
| [[SBDS]] | -0.47 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[CHRAC1]] | -0.46 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[SNHG14]] | -0.46 | -0.24 / -0.28 | both halves | 4e-04 |  |
| [[NT5DC1]] | -0.46 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[RBM3]] | -0.46 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[TRIM66]] | -0.43 | -0.25 / -0.24 | both halves | 4e-04 |  |
| [[TMEM106B]] | -0.43 | -0.26 / -0.41 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.6, 1.0); signed map (-24.4, 29.3). **Vector** length 31.6, 2.73% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.7 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.7 | +8.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.5 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +0.4 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +0.8 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | lipase E, hormone sensitive type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,401,514-42,427,388 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSL |
| Gene groups (HGNC) | Lipases |
| Hallmark sets | BILE_ACID_METABOLISM, ADIPOGENESIS |
| Reactome | 8 pathways, smallest: Triglyceride catabolism; Triglyceride metabolism; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05469](https://www.uniprot.org/uniprotkb/Q05469) (Hormone-sensitive lipase):

> Lipase with broad substrate specificity, catalyzing the hydrolysis of triacylglycerols (TAGs), diacylglycerols (DAGs), monoacylglycerols (MAGs), cholesteryl esters and retinyl esters. Shows a preferential hydrolysis of DAGs over TAGs and MAGs and preferentially hydrolyzes the fatty acid (FA) esters at the sn-3 position of the glycerol backbone in DAGs. Preferentially hydrolyzes FA esters at the sn-1 and sn-2 positions of the glycerol backbone in TAGs (By similarity). Catalyzes the hydrolysis of …

**Summary**, from NCBI Gene [3991](https://www.ncbi.nlm.nih.gov/gene/3991):

> The protein encoded by this gene has a long and a short form, generated by use of alternative translational start codons. The long form is expressed in steroidogenic tissues such as testis, where it converts cholesteryl esters to free cholesterol for steroid hormone production. The short form is expressed in adipose tissue, among others, where it hydrolyzes stored triglycerides to free fatty acids. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6621) · Entrez [3991](https://www.ncbi.nlm.nih.gov/gene/3991) · UniProt [Q05469](https://www.uniprot.org/uniprotkb/Q05469) · Ensembl [ENSG00000079435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079435)

## Data

Gene col 1257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1257); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1257]; `tensor/DDL_lfc|DDL_z.npy` [1257]; `embed/gene_vectors.npy` [1257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1257 or target_col == 1257). Every well: [[LIPE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIPE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
