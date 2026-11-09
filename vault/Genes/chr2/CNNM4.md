---
symbol: "CNNM4"
type: "gene"
col: 8137
ensembl_id: "ENSG00000158158"
name: "cyclin and CBS domain divalent metal cation transport mediator 4"
location: "2q11.2"
module: 3
arm: "+"
pooled_cpm: 56.4
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CNNM4

*cyclin and CBS domain divalent metal cation transport mediator 4* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.25× (z +17.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.400× (z -10.7, q 5e-24, down in 29 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Berbamine (drug)]] 0.05 µM: 0.731× (z -3.8, q 0.012, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFMID]] (+0.76, fdr 7e-06), [[FAM53C]] (+0.68, fdr 7e-06), [[ZNF10]] (+0.68, fdr 7e-06); moves opposite to [[XRCC5]] (-0.71, fdr 7e-06), [[TMX3]] (-0.68, fdr 7e-06), [[CAPRIN1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.25×** | +17.6 | 0e+00 | 48/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.63×** | +15.7 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +14.3 | 4e-44 | 40/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.99×** | +13.3 | 3e-38 | 46/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +9.4 | 7e-19 | 45/48 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.78×** | +6.5 | 7e-09 | 44/48 (NCI-H2347, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +6.0 | 2e-07 | 35/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +5.8 | 4e-07 | 32/48 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.5 | 2e-06 | 31/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.56×** | +5.4 | 4e-06 | 30/49 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.0 | 2e-05 | 27/49 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 4e-04 | 31/49 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.4 | 5e-04 | 30/48 (J82, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 28/48 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.012 | 23/49 (LOX-IMVI, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.013 | 25/48 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -10.7 | 5e-24 | 29/38 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.436×** | -9.3 | 3e-18 | 33/41 (SW48, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.489×** | -8.7 | 6e-16 | 38/48 (NCI-H23, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.9 | 0.012 | 1/49 (CHP-212) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.731×** | -3.8 | 0.012 | 29/48 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.801×** | -3.8 | 0.012 | 29/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -3.8 | 0.012 | 25/48 (LS 180, COLO 205, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.736×** | -3.7 | 0.014 | 28/48 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.738×** | -3.7 | 0.014 | 25/48 (SW1417, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.586×** | -3.4 | 0.038 | 22/49 (HS-578T, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.766×** | -3.2 | 0.063 | 19/49 (RPMI-7951, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.839× | -3.0 | 0.12 | 14/48 (A498, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.8 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 76.0 | 6 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.13× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -10.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.1 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -16.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 68.3 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 122 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -15.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 66.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.98× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -18.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 40.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.26× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 106 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 36.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.98× (z +13.1) | — |
| [[RKO (line)]] | wt | 33.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.42× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 49.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.0865× (z -16.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +17.2) | — |
| [[A-172 (line)]] | wt | 37.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +11.2) | — |
| [[A-427 (line)]] | wt | 28.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.81× (z +12.7) | — |
| [[C-33 A (line)]] | alt | 44.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 58.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +21.1) | — |
| [[HEC-1-A (line)]] | alt | 72.3 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 40.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.69× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 51.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 55.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 87.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -16.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 80.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.0715× (z -19.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 41.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.99× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 90.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0805× (z -11.1) |
| [[HS-578T (line)]] | alt | 28.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.86× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -10.5) |
| [[LS 180 (line)]] | wt | 96.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -13.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 67.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.8) | — |
| [[C32 (line)]] | wt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.12× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 41.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.00× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 67.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.35× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 44.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 27.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0814× (z -17.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFMID]] | +0.76 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[FAM53C]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ZNF10]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[RAB11FIP1]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[BIK]] | +0.67 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[WIPF2]] | +0.67 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[SNHG7]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[AHDC1]] | +0.66 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[SIRT2]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[BCORL1]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[CTR9]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC5]] | -0.71 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[TMX3]] | -0.68 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.66 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[PSME3]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.65 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[SSU72]] | -0.63 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[SRFBP1]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[NUP155]] | -0.62 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[BTBD1]] | -0.62 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SOCS4]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[XRCC6]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity raises CNNM4's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.62× lower at baseline in the lines without MPZL3 | 0.009 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[IRF6]] | B | IRF6 activity raises CNNM4's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.55× lower at baseline in the lines without IRF6 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[RNF223]] | B | RNF223 activity raises CNNM4's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without RNF223 | 0.060 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[BIK]] | B | BIK activity raises CNNM4's level | lines that do not express BIK (15) vs lines expressing it (35) | 1.54× lower at baseline in the lines without BIK | 0.089 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (12.7, -6.6); signed map (-27.4, 13.3). **Vector** length 124, 39.6% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +15.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.5 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +6.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.0 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.5 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.9 | -9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | cyclin and CBS domain divalent metal cation transport mediator 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,760,902-96,811,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC70A4, KIAA1592; previously ACDP4 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 70, cyclin and CBS domain divalent metal cation transport mediators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4Q7](https://www.uniprot.org/uniprotkb/Q6P4Q7) (Metal transporter CNNM4):

> Probable metal transporter. The interaction with the metal ion chaperone COX11 suggests that it may play a role in sensory neuron functions (By similarity). May play a role in biomineralization and retinal function.

**Summary**, from NCBI Gene [26504](https://www.ncbi.nlm.nih.gov/gene/26504):

> This gene encodes a member of the ancient conserved domain containing protein family. Members of this protein family contain a cyclin box motif and have structural similarity to the cyclins. The encoded protein may play a role in metal ion transport. Mutations in this gene are associated with Jalili syndrome which consists of cone-rod dystrophy and amelogenesis imperfecta. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:105) · Entrez [26504](https://www.ncbi.nlm.nih.gov/gene/26504) · UniProt [Q6P4Q7](https://www.uniprot.org/uniprotkb/Q6P4Q7) · Ensembl [ENSG00000158158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158158)

## Data

Gene col 8137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8137); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8137]; `tensor/DDL_lfc|DDL_z.npy` [8137]; `embed/gene_vectors.npy` [8137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8137 or target_col == 8137). Every well: [[CNNM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNNM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
