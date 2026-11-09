---
symbol: "RNF6"
type: "gene"
col: 4838
ensembl_id: "ENSG00000127870"
name: "ring finger protein 6"
location: "13q12.13"
module: 135
arm: "+"
pooled_cpm: 45.22
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 4
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# RNF6

*ring finger protein 6* — 13q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.41× (z +26.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.929× (z -5.0, q 4e-04, down in 1 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.794× (z -4.8, q 4e-04, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO30]] (+0.76, fdr 1e-05), [[POLR2M]] (+0.74, fdr 2e-05), [[ZXDB]] (+0.74, fdr 7e-06); moves opposite to [[METRN]] (-0.75, fdr 1e-05), [[ANAPC11]] (-0.71, fdr 2e-05), [[NUP160]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IGFBP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +26.0 | 0e+00 | 46/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +24.9 | 0e+00 | 45/47 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +18.1 | 0e+00 | 43/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +16.0 | 0e+00 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +15.8 | 0e+00 | 35/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +14.6 | 0e+00 | 47/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +14.3 | 2e-44 | 43/48 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +14.1 | 4e-43 | 44/48 (C32, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.81×** | +12.4 | 2e-33 | 43/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +12.1 | 4e-32 | 40/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +12.0 | 2e-31 | 43/48 (SNU-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +11.7 | 7e-30 | 43/48 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +11.4 | 2e-28 | 42/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +11.1 | 4e-27 | 42/48 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.6 | 8e-25 | 37/47 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.6 | 1e-09 | 26/48 (A-172, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +6.4 | 4e-09 | 28/48 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -5.0 | 4e-04 | 1/49 (NCI-H23) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.794×** | -4.8 | 4e-04 | 21/48 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.802×** | -4.6 | 7e-04 | 24/48 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.822×** | -4.1 | 0.005 | 23/47 (HT-29, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -4.1 | 0.005 | 16/48 (KATO III, SW480, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.838× | -3.7 | 0.023 | 18/48 (NCI-H23, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.731×** | -3.4 | 0.047 | 17/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.845× | -3.4 | 0.047 | 14/47 (RKO, A-427, …) | top dose only |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.901× | -3.1 | 0.12 | 2/49 (HOP62, C-33 A) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.12 | 15/47 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.903× | -3.0 | 0.12 | 4/48 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.759× | -3.0 | 0.12 | 16/48 (SW48, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 69.4 | 8 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +16.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.504× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 36.2 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +18.3) | — |
| [[A-172 (line)]] | wt | 39.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +19.8) | — |
| [[A498 (line)]] | wt | 44.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +17.8) | — |
| [[HOP62 (line)]] | alt | 23.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.4) | — |
| [[J82 (line)]] | alt | 69.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +22.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +18.8) | — |
| [[RKO (line)]] | wt | 91.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +14.7) | — |
| [[Hs 766T (line)]] | wt | 60.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 133 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +17.1) | [[Digitoxin (drug)]] 5 µM 0.490× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.2 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +13.9) | — |
| [[C32 (line)]] | wt | 39.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.14× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 138 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 46.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 33.5 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +13.2) | — |
| [[A549 (line)]] | wt | 28.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 26.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +14.0) | — |
| [[LoVo (line)]] | wt | 61.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 47.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 54.1 | 3 | 0 | [[Selinexor (drug)]] 5 µM 3.04× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 29.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.6) | — |
| [[SW 900 (line)]] | alt | 41.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.7) | — |
| [[A-427 (line)]] | wt | 33.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 61.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 41.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 41.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.7) | — |
| [[H4 (line)]] | wt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 64.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.0) | — |
| [[KATO III (line)]] | alt | 72.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +14.3) | — |
| [[SHP-77 (line)]] | alt | 31.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 51.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO30]] | +0.76 | +0.72 / +0.57 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[POLR2M]] | +0.74 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[ZXDB]] | +0.74 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[EIF5]] | +0.73 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[TDP2]] | +0.72 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[C17orf80]] | +0.71 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ZNF564]] | +0.71 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[HTATIP2]] | +0.70 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[HSPB8]] | +0.69 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.69 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[ZXDA]] | +0.69 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METRN]] | -0.75 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[ANAPC11]] | -0.71 | -0.67 / -0.47 | both halves | 2e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[NUP160]] | -0.67 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[EFHC1]] | -0.66 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.65 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[PI4KAP1-1]] | -0.65 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[SH3GL1]] | -0.65 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[BRAT1]] | -0.64 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[CHEK2]] | -0.64 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[NPHP4]] | -0.64 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[STK32C]] | -0.64 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.63 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP2]] | B | IGFBP2 activity raises RNF6's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without IGFBP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[TOP2A]] | B | TOP2A activity lowers RNF6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MNX1]] | B | MNX1 activity raises RNF6's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without MNX1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |
| [[LINC00857]] | B | LINC00857 activity raises RNF6's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without LINC00857 | 0.045 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.910). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-18.2, 9.0); signed map (8.2, -29.6). **Vector** length 118, 35.2% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.8 | +18.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.1 | +14.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.3 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.9 | +12.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +4.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -8.5 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.5 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -8.3 | -1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.13 — chr13:26,132,115-26,222,314 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686P0776 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y252](https://www.uniprot.org/uniprotkb/Q9Y252) (E3 ubiquitin-protein ligase RNF6):

> E3 ubiquitin-protein ligase mediating 'Lys-48'-linked polyubiquitination of LIMK1 and its subsequent targeting to the proteasome for degradation (By similarity). Negatively regulates axonal outgrowth through regulation of the LIMK1 turnover (By similarity). Mediates 'Lys-6' and 'Lys-27'-linked polyubiquitination of AR/androgen receptor thereby modulating its transcriptional activity. May also bind DNA and function as a transcriptional regulator (By similarity). Mediates polyubiquitination of …

**Summary**, from NCBI Gene [6049](https://www.ncbi.nlm.nih.gov/gene/6049):

> The protein encoded by this gene contains a RING-H2 finger motif. Deletions and mutations in this gene were detected in esophageal squamous cell carcinoma (ESCC), suggesting that this protein may be a potential tumor suppressor. Studies of the mouse counterpart suggested a role of this protein in the transcription regulation that controls germinal differentiation. Multiple alternatively spliced transcript variants encoding the same protein are observed. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10069) · Entrez [6049](https://www.ncbi.nlm.nih.gov/gene/6049) · UniProt [Q9Y252](https://www.uniprot.org/uniprotkb/Q9Y252) · Ensembl [ENSG00000127870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127870)

## Data

Gene col 4838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4838); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4838]; `tensor/DDL_lfc|DDL_z.npy` [4838]; `embed/gene_vectors.npy` [4838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4838 or target_col == 4838). Every well: [[RNF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
