---
symbol: "NLRP2"
type: "gene"
col: 334
ensembl_id: "ENSG00000022556"
name: "NLR family pyrin domain containing 2"
location: "19q13.42"
module: 23
arm: "-"
pooled_cpm: 6.85
n_lines_expressing: 17
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# NLRP2

*NLR family pyrin domain containing 2* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.45× (z +18.0, q 0e+00, up in 0 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +8.5, q 2e-15, up in 4 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.908× (z -4.2, q 0.010, down in 0 of 15 measured lines) ⚠ position not correctable. The strongest without an alert is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM: 0.709× (z -4.1, q 0.010, down in 0 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.210×, C-33 A 0.237×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.385×, J82 0.291×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.304×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPYL5]] (+0.60, fdr 1e-04), [[ZNF445]] (+0.55, fdr 3e-04), [[SNAP47]] (+0.53, fdr 4e-05); moves opposite to [[NIFK-AS1]] (-0.53, fdr 2e-04), [[DNAI4]] (-0.52, fdr 2e-04), [[CHD1-DT]] (-0.50, fdr 7e-04).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.45×** | +18.0 | 0e+00 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +13.5 | 3e-39 | 2/10 (BT-474, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +9.5 | 3e-19 | 2/13 (NCI-H23, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +8.5 | 2e-15 | 4/15 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.0 | 2e-10 | 0/15 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.4 | 1e-08 | 10/15 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +6.0 | 1e-07 | 3/14 (HOP62, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.56×** | +5.4 | 5e-06 | 1/15 (SHP-77) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.7 | 1e-04 | 1/14 (HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.70×** | +4.6 | 3e-04 | 3/14 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.4 | 5e-04 | 1/15 (BT-474) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.4 | 6e-04 | 0/14 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.2 | 0.001 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.1 | 0.002 | 2/14 (A549, NCI-H1792) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.40×** | +4.1 | 0.002 | 1/14 (HOP62) | top dose only | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.003 | 0/15 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.004 | 12/15 (A549, J82, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.005 | 4/15 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.008 | 0/15 | inconsistent across doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.023 | 0/14 | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.032 | 0/15 | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.055 | 1/14 (HCT15) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.19× | +2.9 | 0.078 | 5/15 (C-33 A, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.210×, C-33 A 0.237×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.385×, J82 0.291×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.304×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.2 | 0.010 | 0/15 | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.709×** | -4.1 | 0.010 | 0/15 | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.597× | -3.3 | 0.22 | 0/15 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | 0.612× | -3.1 | 0.28 | 1/15 (SK-MEL-2) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.619× | -3.0 | 0.28 | 0/15 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 42.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -12.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.6) |
| [[A-172 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.813 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.634 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPYL5]] | +0.60 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[ZNF445]] | +0.55 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[SNAP47]] | +0.53 | +0.43 / +0.44 | both halves | 4e-05 |  |
| [[AGK]] | +0.52 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[RNF212]] | +0.52 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[FSD1]] | +0.51 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[RNF40]] | +0.51 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[COG2]] | +0.51 | +0.22 / +0.51 | both halves | 6e-04 |  |
| [[LINC00540]] | +0.50 | +0.26 / +0.43 | both halves | 3e-04 |  |
| [[GRIA2]] | +0.50 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[DDX19B]] | +0.49 | +0.28 / +0.39 | both halves | 3e-04 |  |
| [[DCAF1]] | +0.49 | +0.37 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK-AS1]] | -0.53 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[DNAI4]] | -0.52 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[CHD1-DT]] | -0.50 | -0.21 / -0.40 | both halves | 7e-04 |  |
| [[SPESP1]] | -0.50 | -0.34 / -0.27 | both halves | 3e-04 |  |
| [[PSMD6-AS2]] | -0.50 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[ANKRD17-DT]] | -0.50 | -0.24 / -0.37 | both halves | 4e-04 |  |
| [[CCDC30]] | -0.49 | -0.21 / -0.38 | both halves | 7e-04 |  |
| [[ANXA2R-OT1]] | -0.49 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[DARS1-AS1]] | -0.48 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[SAP30L-AS1]] | -0.48 | -0.33 / -0.25 | both halves | 4e-04 |  |
| [[PELO-AS1]] | -0.48 | -0.24 / -0.30 | both halves | 4e-04 |  |
| [[EPM2A-DT]] | -0.48 | -0.23 / -0.33 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-34.9, 20.5); signed map (-15.0, -28.3). **Vector** length 24.1, 4.14% of its response variance represented; |z| ≥ 3 in 262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +4.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NLR family pyrin domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,953,130-55,001,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20510, PYPAF2, NBS1, PAN1, CLR19.9; previously NALP2 |
| Gene groups (HGNC) | NLR family; Pyrin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX02](https://www.uniprot.org/uniprotkb/Q9NX02) (NACHT, LRR and PYD domains-containing protein 2):

> Component of cytoplasmic lattices, which consist in fibrous structures found in the cytoplasm of oocytes and preimplantation embryos. Cytoplasmic lattices are required to store maternal proteins critical for embryonic development, such as ribosomal proteins, cytoskeletal tubulins and proteins controlling epigenetic reprogramming of the preimplantation embryo, in a poised but restrained state, regulating their availability for early embryonic development. Suppresses TNF- and CD40-induced NFKB1 …

**Summary**, from NCBI Gene [55655](https://www.ncbi.nlm.nih.gov/gene/55655):

> This gene is a member of the nucleotide-binding and leucine-rich repeat receptor (NLR) family, and is predicted to contain an N-terminal pyrin effector domain (PYD), a centrally-located nucleotide-binding and oligomerization domain (NACHT) and C-terminal leucine-rich repeats (LRR). Members of this gene family are thought to be important regulators of immune responses. This gene product interacts with components of the IkB kinase (IKK) complex, and can regulate both caspase-1 and NF-kB (nuclear …

**Accessions** — [HGNC:22948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22948) · Entrez [55655](https://www.ncbi.nlm.nih.gov/gene/55655) · UniProt [Q9NX02](https://www.uniprot.org/uniprotkb/Q9NX02) · Ensembl [ENSG00000022556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000022556)

## Data

Gene col 334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 334); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 334]; `tensor/DDL_lfc|DDL_z.npy` [334]; `embed/gene_vectors.npy` [334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 334 or target_col == 334). Every well: [[NLRP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLRP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
