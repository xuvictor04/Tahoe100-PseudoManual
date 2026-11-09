---
symbol: "JAGN1"
type: "gene"
col: 10059
ensembl_id: "ENSG00000171135"
name: "jagunal vesicle mediated transporter 1"
location: "3p25.3"
module: 7
arm: "+"
pooled_cpm: 5.51
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# JAGN1

*jagunal vesicle mediated transporter 1* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.46× (z +4.6, q 0.003, up in 11 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.414× (z -4.0, q 0.038, down in 16 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (A-427 0.0668×); [[Belinostat (drug)]] 0.5 µM in 1 line (HT-29 0.0728×; ⚠ cell-cycle shift, explains ~5% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.257×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53RK]] (+0.73, fdr 7e-06), [[ZNF155]] (+0.72, fdr 7e-06), [[YTHDF2]] (+0.72, fdr 7e-06); moves opposite to [[SEPTIN2]] (-0.69, fdr 7e-06), [[SETD3]] (-0.64, fdr 7e-06), [[RPA1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.6 | 0.003 | 11/46 (SK-MEL-2, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +4.4 | 0.003 | 22/44 (KATO III, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.2 | 0.004 | 1/9 (J82) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +3.9 | 0.010 | 8/19 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.010 | 16/40 (A-172, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.96×** | +3.9 | 0.010 | 13/42 (HT-29, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.8 | 0.012 | 14/30 (KATO III, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.53×** | +3.7 | 0.016 | 13/46 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.88×** | +3.7 | 0.016 | 15/39 (NCI-H460, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.4 | 0.037 | 7/30 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.041 | 11/47 (HOP62, HS-578T, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.3 | 0.041 | 13/32 (NCI-H2030, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Belzutifan (drug)]] 5 µM |  | **2.03×** | +3.2 | 0.066 | 7/32 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10059.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (A-427 0.0668×); [[Belinostat (drug)]] 0.5 µM in 1 line (HT-29 0.0728×; ⚠ cell-cycle shift, explains ~5% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.257×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -4.0 | 0.038 | 16/44 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.426×** | -3.8 | 0.038 | 19/39 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.686× | -3.2 | 0.21 | 16/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trimetrexate (drug)]] 5 µM |  | 0.770× | -3.2 | 0.21 | 10/46 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.700× | -3.1 | 0.25 | 15/45 (PANC-1, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.96 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0668× (z -11.6) |
| [[HT-29 (line)]] | alt | 5.50 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0728× (z -10.8) ⚠ cell-cycle shift, explains ~5% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.78 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -8.6) |
| [[A-172 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53RK]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ZNF155]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.69 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[UBQLN2]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[MRM3]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[HCCS]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RTL6]] | +0.66 | +0.74 / +0.57 | both halves | 8e-06 |  |
| [[RPP25L]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TMEM70]] | +0.66 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ZNF468]] | +0.66 | +0.74 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN2]] | -0.69 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[SETD3]] | -0.64 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[RPA1]] | -0.62 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.61 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[MLEC]] | -0.59 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SRD5A1]] | -0.59 | -0.66 / -0.40 | both halves | 4e-05 |  |
| [[NOMO2]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[ANAPC5]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PDIA4]] | -0.58 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[RCN2]] | -0.58 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TMEM50B]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.0, 9.8); signed map (0.7, -24.7). **Vector** length 53.9, 7.92% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.7 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Capivasertib (drug)]] 0.5 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | jagunal vesicle mediated transporter 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,890,574-9,894,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GL009, FLJ14602 |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5M9](https://www.uniprot.org/uniprotkb/Q8N5M9) (Protein jagunal homolog 1):

> Endoplasmic reticulum transmembrane protein involved in vesicle-mediated transport, which is required for neutrophil function. Required for vesicle-mediated transport; it is however unclear whether it is involved in early secretory pathway or intracellular protein transport. Acts as a regulator of neutrophil function, probably via its role in vesicle-mediated transport: required for defense against fungal pathogens and for granulocyte colony-stimulating factor (GM-CSF) signaling pathway; …

**Summary**, from NCBI Gene [84522](https://www.ncbi.nlm.nih.gov/gene/84522):

> The protein encoded by this gene is a transmembrane protein. It functions in the early secretory pathway and is necessary for neutrophil differentiation and survival. Mutations in this gene result in severe congenital neutropenia. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:26926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26926) · Entrez [84522](https://www.ncbi.nlm.nih.gov/gene/84522) · UniProt [Q8N5M9](https://www.uniprot.org/uniprotkb/Q8N5M9) · Ensembl [ENSG00000171135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171135)

## Data

Gene col 10059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10059); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10059]; `tensor/DDL_lfc|DDL_z.npy` [10059]; `embed/gene_vectors.npy` [10059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10059 or target_col == 10059). Every well: [[JAGN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAGN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
