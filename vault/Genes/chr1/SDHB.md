---
symbol: "SDHB"
type: "gene"
col: 3875
ensembl_id: "ENSG00000117118"
name: "succinate dehydrogenase complex iron sulfur subunit B"
location: "1p36.13"
module: 57
arm: "+"
pooled_cpm: 51.09
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# SDHB

*succinate dehydrogenase complex iron sulfur subunit B* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.20× (z +12.3, q 5e-32, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.919× (z -4.8, q 9e-04, down in 0 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.828× (z -4.4, q 0.004, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.465×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1C]] (+0.76, fdr 7e-06), [[NDUFB7]] (+0.73, fdr 7e-06), [[MED23]] (+0.72, fdr 1e-05); moves opposite to [[MEPCE]] (-0.66, fdr 1e-05), [[ERCC6L2]] (-0.63, fdr 5e-05), [[DDX5]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.20×** | +12.3 | 5e-32 | 47/49 (SW480, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.73×** | +9.0 | 5e-17 | 38/47 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.69×** | +8.5 | 4e-15 | 34/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.70×** | +8.3 | 1e-14 | 29/41 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.63×** | +7.4 | 1e-11 | 31/44 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.50×** | +6.4 | 2e-08 | 32/47 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.47×** | +6.3 | 2e-08 | 37/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +5.8 | 4e-07 | 37/48 (SW480, NCI-H23, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.33×** | +4.7 | 2e-04 | 26/48 (SW480, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.33×** | +4.7 | 2e-04 | 27/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.31×** | +4.4 | 5e-04 | 25/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 25/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.8 | 0.008 | 21/47 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.012 | 22/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **1.24×** | +3.6 | 0.012 | 20/47 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.018 | 21/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.018 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.025 | 12/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.036 | 12/48 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.054 | 9/48 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +2.9 | 0.083 | 9/48 (Hs 766T, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3875.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.465×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -4.8 | 9e-04 | 0/49 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.828×** | -4.4 | 0.004 | 22/48 (A-427, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 44.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 54.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.39× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 42.6 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.0) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[PANC-1 (line)]] | alt | 71.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.20× (z +9.2) | — |
| [[SW480 (line)]] | alt | 53.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.91× (z +10.3) | — |
| [[A-427 (line)]] | wt | 69.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.2) |
| [[KATO III (line)]] | alt | 47.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.12× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 58.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.07× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 39.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.78× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H23 (line)]] | alt | 70.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.64× (z +9.5) | — |
| [[RKO (line)]] | wt | 62.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.65× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 54.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.62× (z +8.5) | — |
| [[A-172 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1C]] | +0.76 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 968 |
| [[NDUFB7]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 865 |
| [[MED23]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.71 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.71 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.70 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.69 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[USPL1]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NCK1]] | +0.68 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[ELP1]] | +0.68 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SDHAF3]] | +0.68 | +0.66 / +0.51 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 930 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEPCE]] | -0.66 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.63 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[DDX5]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.62 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.62 | -0.67 / -0.34 | both halves | 1e-04 |  |
| [[SKIL]] | -0.60 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[LINC01004]] | -0.60 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[USP11]] | -0.59 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[KDM6B]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 | STRING 437 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.0, -11.6); signed map (-33.0, -11.4). **Vector** length 75.1, 17.4% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +12.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.8 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.7 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | -0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | +1.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex iron sulfur subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:17,018,664-17,054,151 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SDH1, SDH |
| Gene groups (HGNC) | Mitochondrial complex II: succinate dehydrogenase subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P21912](https://www.uniprot.org/uniprotkb/P21912) (Succinate dehydrogenase):

> Iron-sulfur protein (IP) subunit of the succinate dehydrogenase complex (mitochondrial respiratory chain complex II), responsible for transferring electrons from succinate to ubiquinone (coenzyme Q). SDH also oxidizes malate to the non-canonical enol form of oxaloacetate, enol-oxaloacetate (By similarity). Enol-oxaloacetate, which is a potent inhibitor of the succinate dehydrogenase activity, is further isomerized into keto-oxaloacetate (By similarity).

**Summary**, from NCBI Gene [6390](https://www.ncbi.nlm.nih.gov/gene/6390):

> This tumor suppressor gene encodes the iron-sulfur protein subunit of the succinate dehydrogenase (SDH) enzyme complex which plays a critical role in mitochondria. The SDH enzyme complex is composed of four nuclear-encoded subunits. This enzyme complex converts succinate to fumarate which releases electrons as part of the citric acid cycle, and the enzyme complex additionally provides an attachment site for released electrons to be transferred to the oxidative phosphorylation pathway. The SDH …

**Accessions** — [HGNC:10681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10681) · Entrez [6390](https://www.ncbi.nlm.nih.gov/gene/6390) · UniProt [P21912](https://www.uniprot.org/uniprotkb/P21912) · Ensembl [ENSG00000117118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117118)

## Data

Gene col 3875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3875); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3875]; `tensor/DDL_lfc|DDL_z.npy` [3875]; `embed/gene_vectors.npy` [3875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3875 or target_col == 3875). Every well: [[SDHB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
