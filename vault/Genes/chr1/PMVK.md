---
symbol: "PMVK"
type: "gene"
col: 8670
ensembl_id: "ENSG00000163344"
name: "phosphomevalonate kinase"
location: "1q21.3"
module: 53
arm: "+"
pooled_cpm: 8.83
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PMVK

*phosphomevalonate kinase* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.54× (z +12.6, q 2e-33, up in 27 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +5.4, q 6e-06, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.415× (z -8.8, q 1e-15, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02901]] (+0.61, fdr 3e-05), [[TMPRSS9]] (+0.58, fdr 1e-05), [[RELA-DT]] (+0.57, fdr 6e-05); moves opposite to [[MTM1]] (-0.50, fdr 1e-04).
> It is in [[Module 053]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.54×** | +12.6 | 2e-33 | 27/31 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.87×** | +10.1 | 2e-21 | 12/12 (A498, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.51×** | +8.0 | 2e-13 | 21/26 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.89×** | +6.3 | 3e-08 | 35/47 (A549, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.76×** | +5.6 | 2e-06 | 32/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.4 | 6e-06 | 23/43 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.60×** | +4.6 | 3e-04 | 23/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.4 | 9e-04 | 22/46 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.009 | 16/48 (A-172, A498, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.49×** | +3.8 | 0.009 | 11/35 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.013 | 15/47 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.28×** | +3.4 | 0.029 | 7/48 (LS 180, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.40×** | +3.3 | 0.037 | 11/38 (HT-29, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.064 | 12/48 (CFPAC-1, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.415×** | -8.8 | 1e-15 | 39/47 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.443×** | -8.1 | 1e-13 | 33/46 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.469×** | -7.5 | 9e-12 | 33/46 (COLO 205, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -5.6 | 3e-06 | 25/45 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.582×** | -5.4 | 7e-06 | 24/46 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.671×** | -4.0 | 0.007 | 17/47 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.686×** | -3.6 | 0.022 | 16/43 (LS 180, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.501×** | -3.6 | 0.022 | 16/43 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -10.2) |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0696× (z -11.1) |
| [[HT-29 (line)]] | alt | 7.31 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 4.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0736× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 4.42 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0622× (z -9.2) |
| [[A-172 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02901]] | +0.61 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[TMPRSS9]] | +0.58 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[RELA-DT]] | +0.57 | +0.70 / +0.38 | both halves | 6e-05 |  |
| [[GRAMD2A]] | +0.56 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[GRIK5]] | +0.55 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[C5AR1]] | +0.54 | +0.69 / +0.37 | both halves | 8e-05 |  |
| [[HEATR4]] | +0.54 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[MMP25]] | +0.54 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[PLB1]] | +0.53 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PDE4C]] | +0.53 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R10]] | +0.53 | +0.67 / +0.36 | both halves | 1e-04 |  |
| [[FBXO41]] | +0.53 | +0.72 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTM1]] | -0.50 | -0.67 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, -14.8); signed map (21.6, 12.9). **Vector** length 49.5, 6.68% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.5 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.7 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.3 | +0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -8.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Ciclopirox (drug)]] 0.5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphomevalonate kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,924,740-154,936,719 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMK, PMKA, HUMPMKI |
| Gene groups (HGNC) | Isoprenoid biosynthesis kinases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 6 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15126](https://www.uniprot.org/uniprotkb/Q15126) (Phosphomevalonate kinase):

> Catalyzes the reversible ATP-dependent phosphorylation of mevalonate 5-phosphate to produce mevalonate diphosphate and ADP, a key step in the mevalonic acid mediated biosynthesis of isopentenyl diphosphate and other polyisoprenoid metabolites.

**Summary**, from NCBI Gene [10654](https://www.ncbi.nlm.nih.gov/gene/10654):

> This gene encodes a peroxisomal enzyme that is a member of the galactokinase, homoserine kinase, mevalonate kinase, and phosphomevalonate kinase (GHMP) family of ATP-dependent enzymes. The encoded protein catalyzes the conversion of mevalonate 5-phosphate to mevalonate 5-diphosphate, which is the fifth step in the mevalonate pathway of isoprenoid biosynthesis. Mutations in this gene are linked to certain types of porokeratosis including disseminated superficial porokeratosis. Alternative …

**Accessions** — [HGNC:9141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9141) · Entrez [10654](https://www.ncbi.nlm.nih.gov/gene/10654) · UniProt [Q15126](https://www.uniprot.org/uniprotkb/Q15126) · Ensembl [ENSG00000163344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163344)

## Data

Gene col 8670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8670); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8670]; `tensor/DDL_lfc|DDL_z.npy` [8670]; `embed/gene_vectors.npy` [8670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8670 or target_col == 8670). Every well: [[PMVK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMVK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
