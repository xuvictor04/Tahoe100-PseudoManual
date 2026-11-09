---
symbol: "SBDSP1-1"
type: "gene"
col: 16610
ensembl_id: "ENSG00000291152"
name: ""
location: ""
module: 7
arm: "+"
pooled_cpm: 4.09
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SBDSP1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.49× (z +19.8, q 0e+00, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Methotrexate (drug)]] 0.5 µM: 0.673× (z -3.7, q 0.091, down in 6 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.05 µM in 1 line (J82 0.0713×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBDSP1]] (+0.76, fdr 7e-06, ⚠ same locus), [[AUP1]] (+0.68, fdr 1e-05), [[CCT6P3]] (+0.66, fdr 3e-05), [[FLII]] (+0.59, fdr 3e-05); moves opposite to [[IGFBP2]] (-0.59, fdr 3e-05), [[COX6A1]] (-0.57, fdr 5e-05), [[UBL5]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.49×** | +19.8 | 0e+00 | 34/35 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.33×** | +14.7 | 0e+00 | 6/8 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.45×** | +13.9 | 1e-41 | 21/21 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.02×** | +13.0 | 3e-36 | 34/35 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.58×** | +11.2 | 5e-27 | 39/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +9.5 | 2e-19 | 10/12 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +7.7 | 8e-13 | 18/26 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.19×** | +7.3 | 2e-11 | 29/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +7.1 | 6e-11 | 28/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.0 | 1e-10 | 19/36 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +6.9 | 4e-10 | 24/42 (SW480, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +6.6 | 2e-09 | 25/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +6.4 | 6e-09 | 11/22 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.01×** | +6.1 | 4e-08 | 19/41 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +5.7 | 5e-07 | 21/43 (PANC-1, A498, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +5.4 | 2e-06 | 7/46 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.8 | 6e-05 | 17/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.42×** | +4.6 | 1e-04 | 11/44 (NCI-H2030, H4, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.009 | 13/42 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.06×** | +3.5 | 0.010 | 2/42 (A498, SW480) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.010 | 11/43 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16610.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.05 µM in 1 line (J82 0.0713×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Methotrexate (drug)]] 0.5 µM |  | **0.673×** | -3.7 | 0.091 | 6/43 (Hs 766T, HepG2/C3A, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **0.681×** | -3.6 | 0.091 | 11/44 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.87 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.5) | — |
| [[A498 (line)]] | wt | 7.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 5.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +9.9) | — |
| [[J82 (line)]] | alt | 4.02 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0713× (z -9.3) |
| [[KATO III (line)]] | alt | 5.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +9.0) | — |
| [[LoVo (line)]] | wt | 3.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 2.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 4.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 2.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 3.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +10.6) | — |
| [[A-172 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBDSP1]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[AUP1]] | +0.68 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[CCT6P3]] | +0.66 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[FLII]] | +0.59 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[ZNF213]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ZNF197]] | +0.59 | +0.70 / +0.36 | both halves | 9e-05 |  |
| [[MRPL9]] | +0.59 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TAF9]] | +0.59 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[ACTR8]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[DXO]] | +0.58 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[ZNF181]] | +0.57 | +0.67 / +0.30 | both halves | 2e-04 |  |
| [[BRPF3]] | +0.57 | +0.58 / +0.37 | both halves | 8e-05 |  |
| [[ZNF621]] | +0.57 | +0.62 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP2]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.57 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[UBL5]] | -0.55 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[KIAA2013]] | -0.54 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[UQCRQ]] ⚠ | -0.53 | -0.43 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCRH]] | -0.52 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[COX6C]] | -0.51 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[SBNO1]] | -0.51 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[RABGEF1P1]] | -0.51 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SPCS1]] | -0.50 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[NEDD8]] | -0.49 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD13D]] | -0.49 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[MLEC]] | -0.49 | -0.55 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.356). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-27.2, 9.1); signed map (11.3, -22.0). **Vector** length 47.1, 5.65% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +0.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.4 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -1.4 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.1 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | +0.7 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

> [!warning] No registry record
> SBDSP1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16610); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16610]; `tensor/DDL_lfc|DDL_z.npy` [16610]; `embed/gene_vectors.npy` [16610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16610 or target_col == 16610). Every well: [[SBDSP1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBDSP1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
