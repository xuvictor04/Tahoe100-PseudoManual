---
symbol: "FASTKD3"
type: "gene"
col: 4515
ensembl_id: "ENSG00000124279"
name: "FASTK mitochondrial RNA regulator 3"
location: "5p15.31"
module: 107
arm: "+"
pooled_cpm: 4.47
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# FASTKD3

*FASTK mitochondrial RNA regulator 3* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +8.8, q 9e-16, up in 22 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.544× (z -8.0, q 7e-13, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPUSD2]] (+0.67, fdr 7e-06), [[ALKBH3]] (+0.66, fdr 1e-05), [[ZNF777]] (+0.65, fdr 7e-06); moves opposite to [[PEAK1]] (-0.56, fdr 4e-05), [[JOSD1]] (-0.54, fdr 1e-05), [[LIMS1]] (-0.52, fdr 2e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.8 | 9e-16 | 22/39 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.49×** | +8.6 | 2e-15 | 29/42 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +8.5 | 4e-15 | 17/25 (SW480, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.97×** | +7.5 | 1e-11 | 17/36 (SW480, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +7.0 | 4e-10 | 13/46 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.67×** | +6.7 | 2e-09 | 22/46 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.65×** | +6.6 | 4e-09 | 18/47 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.51×** | +5.4 | 5e-06 | 16/47 (LoVo, SNU-423, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +4.9 | 5e-05 | 2/11 (LoVo, A-427) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +4.8 | 8e-05 | 9/33 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.3 | 8e-04 | 1/46 (NCI-H2347) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.41×** | +4.2 | 0.001 | 3/14 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 5/45 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.50×** | +3.8 | 0.006 | 1/15 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.3 | 0.032 | 8/27 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +3.1 | 0.059 | 5/46 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.098 | 9/36 (Hs 766T, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -8.0 | 7e-13 | 24/46 (NCI-H2030, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -5.7 | 3e-06 | 16/47 (AN3 CA, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -5.7 | 3e-06 | 17/36 (SW1417, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rifaximin (drug)]] 5 µM |  | **0.731×** | -4.0 | 0.010 | 6/43 (J82, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.776×** | -3.3 | 0.095 | 11/44 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.77 | 0 | 2 (1 ⚠) | — | [[Orlistat (drug)]] 0.05 µM 0.0986× (z -8.7) |
| [[PANC-1 (line)]] | alt | 4.83 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[SHP-77 (line)]] | alt | 7.84 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0885× (z -9.9) |
| [[A-172 (line)]] | wt | 4.00 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.114× (z -8.5) |
| [[A498 (line)]] | wt | 4.25 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0936× (z -10.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 3.98 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0671× (z -10.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 4.79 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0700× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 5.93 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[NCI-H460 (line)]] | wt | 4.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 6.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0760× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD2]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZNF2]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RRN3]] | +0.64 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[DDX55]] | +0.63 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MRPL44]] | +0.62 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ZNF16]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.62 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ELP3]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SLC25A38]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MRPS11]] | +0.61 | +0.68 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.56 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[JOSD1]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[LIMS1]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.7, 6.0); signed map (-10.7, -16.8). **Vector** length 48.1, 5.41% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.5 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +4.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -5.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | FASTK mitochondrial RNA regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:7,859,159-7,869,037 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5297, FLJ23274 |
| Gene groups (HGNC) | FASTK mitochondrial RNA binding family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CZ7](https://www.uniprot.org/uniprotkb/Q14CZ7) (FAST kinase domain-containing protein 3, mitochondrial):

> Required for normal mitochondrial respiration. Increases steady-state levels and half-lives of a subset of mature mitochondrial mRNAs MT-ND2, MT-ND3, MT-CYTB, MT-CO2, and MT-ATP8/6. Promotes MT-CO1 mRNA translation and increases mitochondrial complex IV assembly and activity.

**Summary**, from NCBI Gene [79072](https://www.ncbi.nlm.nih.gov/gene/79072):

> This gene encodes a member of a small family of Fas-activated serine/threonine kinase domain (FASTKD) containing proteins that share an amino terminal mitochondrial targeting domain and multiple carboxy terminal FAST domains as well as a putative RNA-binding RAP domain. The members of this family are ubiquitously expressed and are generally most abundant in mitochondria-enriched tissues such as heart, skeletal muscle and brown-adipose tissue. Some members of this protein family may play a role …

**Accessions** — [HGNC:28758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28758) · Entrez [79072](https://www.ncbi.nlm.nih.gov/gene/79072) · UniProt [Q14CZ7](https://www.uniprot.org/uniprotkb/Q14CZ7) · Ensembl [ENSG00000124279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124279)

## Data

Gene col 4515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4515); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4515]; `tensor/DDL_lfc|DDL_z.npy` [4515]; `embed/gene_vectors.npy` [4515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4515 or target_col == 4515). Every well: [[FASTKD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FASTKD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
