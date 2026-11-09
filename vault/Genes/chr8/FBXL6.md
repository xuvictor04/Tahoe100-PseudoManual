---
symbol: "FBXL6"
type: "gene"
col: 11275
ensembl_id: "ENSG00000182325"
name: "F-box and leucine rich repeat protein 6"
location: "8q24.3"
module: 29
arm: "-"
pooled_cpm: 2.71
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# FBXL6

*F-box and leucine rich repeat protein 6* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.35× (z +12.7, q 6e-34, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.573× (z -4.2, q 0.011, down in 15 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (RKO 0.0486×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG11]] (+0.73, fdr 7e-06), [[WASHC1]] (+0.72, fdr 7e-06), [[SURF2]] (+0.70, fdr 7e-06); moves opposite to [[PPT1]] (-0.70, fdr 7e-06), [[TMEM30A]] (-0.65, fdr 7e-06), [[CRTAP]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.35×** | +12.7 | 6e-34 | 32/34 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.41×** | +8.7 | 7e-16 | 1/2 (NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.13×** | +8.4 | 6e-15 | 13/15 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.07×** | +8.0 | 2e-13 | 32/39 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +7.7 | 2e-12 | 23/34 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.77×** | +7.2 | 4e-11 | 13/17 (A-427, A498, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.25×** | +5.3 | 9e-06 | 2/6 (SW1417, PANC-1) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.1 | 2e-05 | 16/35 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.96×** | +5.0 | 5e-05 | 17/44 (LOX-IMVI, Hs 766T, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.97×** | +4.8 | 8e-05 | 11/24 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.81×** | +4.4 | 6e-04 | 6/43 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.78×** | +4.3 | 1e-03 | 6/15 (A498, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 0.001 | 13/41 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.74×** | +4.1 | 0.002 | 5/25 (NCI-H2030, SK-MEL-2, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +3.7 | 0.009 | 6/29 (HS-578T, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.69×** | +3.4 | 0.021 | 6/27 (RKO, A549, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.023 | 9/29 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.37×** | +3.4 | 0.023 | 3/24 (A498, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.057 | 4/26 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.057 | 6/27 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.49×** | +2.9 | 0.081 | 4/43 (PANC-1, SW1417, …) | all doses, flat | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +2.9 | 0.092 | 6/26 (LS 180, A498, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (RKO 0.0486×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -4.2 | 0.011 | 15/42 (RKO, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.577×** | -4.1 | 0.011 | 10/45 (hTERT-HPNE, LoVo, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.629× | -3.1 | 0.39 | 6/43 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +8.5) | — |
| [[RKO (line)]] | wt | 6.16 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0486× (z -10.6) |
| [[A-172 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.896 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG11]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.72 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[SURF2]] | +0.70 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[LIME1]] | +0.68 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[RNF166]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | +0.65 | +0.49 / +0.73 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GFUS]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[NT5C]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[ZNF316]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.62 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SEMA4C]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[KLF16]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NSUN5P1-1]] | +0.62 | +0.51 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | -0.70 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[TMEM30A]] | -0.65 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[CRTAP]] | -0.64 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[TMX1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[LAMP2]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[PRDX3]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.59 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.58 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[SCARB2]] | -0.58 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[ILRUN]] | -0.57 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[SUMO1]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-36.6, -14.9); signed map (1.7, -11.1). **Vector** length 48.2, 6.74% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +7.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +1.9 | +4.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +4.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,355,431-144,359,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBL6 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N531](https://www.uniprot.org/uniprotkb/Q8N531) (F-box/LRR-repeat protein 6):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [26233](https://www.ncbi.nlm.nih.gov/gene/26233):

> This gene encodes a member of a family of proteins that are characterized by an F-box motif. The encoded protein also contains leucine-rich repeats. F-box-containing proteins comprise one of the subunits of the SCF (SKP1-cullin-F-box) complex, which functions in phosphorylation-dependent ubiquitination. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:13603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13603) · Entrez [26233](https://www.ncbi.nlm.nih.gov/gene/26233) · UniProt [Q8N531](https://www.uniprot.org/uniprotkb/Q8N531) · Ensembl [ENSG00000182325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182325)

## Data

Gene col 11275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11275); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11275]; `tensor/DDL_lfc|DDL_z.npy` [11275]; `embed/gene_vectors.npy` [11275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11275 or target_col == 11275). Every well: [[FBXL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
