---
symbol: "CDK7"
type: "gene"
col: 5505
ensembl_id: "ENSG00000134058"
name: "cyclin dependent kinase 7"
location: "5q13.2"
module: 41
arm: "+"
pooled_cpm: 89.7
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# CDK7

*cyclin dependent kinase 7* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +14.0, q 4e-42, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.489× (z -9.1, q 7e-17, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Busulfan (drug)]] 0.05 µM: 0.761× (z -3.6, q 0.043, down in 25 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54]] (+0.72, fdr 7e-06), [[EXOC1]] (+0.68, fdr 7e-06), [[TGDS]] (+0.68, fdr 7e-06); moves opposite to [[REEP3]] (-0.68, fdr 7e-06), [[ANAPC7]] (-0.66, fdr 7e-06), [[IPO9]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +14.0 | 4e-42 | 43/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.1 | 2e-13 | 38/49 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +7.6 | 5e-12 | 37/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.86×** | +7.2 | 8e-11 | 48/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +7.0 | 2e-10 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.0 | 3e-10 | 37/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.9 | 5e-10 | 36/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +5.1 | 2e-05 | 37/48 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.6 | 2e-04 | 32/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +4.6 | 2e-04 | 32/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.6 | 3e-04 | 32/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 30/48 (A-427, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.020 | 27/48 (KATO III, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +3.3 | 0.034 | 22/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.078 | 24/49 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.078 | 18/49 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.078 | 21/48 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.090 | 27/50 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -9.1 | 7e-17 | 36/43 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.603×** | -5.4 | 2e-05 | 35/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -5.1 | 5e-05 | 29/45 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.761×** | -3.6 | 0.043 | 25/49 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.058 | 26/48 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -3.4 | 0.058 | 20/48 (AsPC-1, A498, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.777×** | -3.3 | 0.068 | 26/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -3.2 | 0.093 | 20/48 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.783× | -3.1 | 0.11 | 23/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.850× | -3.1 | 0.12 | 18/48 (NCI-H2347, SW 1088, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.795× | -3.0 | 0.12 | 24/49 (A498, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 89.4 | 10 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +25.4) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 84.1 | 10 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.91× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 83.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 121 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 229 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.493× (z -9.2) |
| [[A549 (line)]] | wt | 97.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +15.1) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 54.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0579× (z -25.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 80.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 57.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.0) | — |
| [[LoVo (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.86× (z +10.9) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.8) | — |
| [[SW48 (line)]] | wt | 77.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.3) | — |
| [[SW480 (line)]] | alt | 85.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +14.0) | — |
| [[A-427 (line)]] | wt | 91.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 65.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.7) | — |
| [[C32 (line)]] | wt | 89.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -10.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.8) | — |
| [[CHP-212 (line)]] | wt | 70.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -10.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 92.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.261× (z -8.8) |
| [[HCT15 (line)]] | alt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -20.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 53.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 71.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 66.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.0) | — |
| [[J82 (line)]] | alt | 81.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 76.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 75.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 70.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 67.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 82.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.8) | — |
| [[SNU-423 (line)]] | alt | 96.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 134 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 73.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[EXOC1]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TGDS]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.68 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[DPM1]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[FBXL15]] | +0.66 | +0.40 / +0.74 | both halves | 4e-05 |  |
| [[SNHG7]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[DCAF5]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.65 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[AFTPH]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP3]] | -0.68 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.66 | -0.60 / -0.63 | both halves | 7e-06 | pathway: S Phase |
| [[IPO9]] | -0.65 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[TARDBP]] | -0.64 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[VMA21]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 | pathway: HALLMARK_PEROXISOME |
| [[HNRNPAB]] | -0.63 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.63 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.63 | -0.47 / -0.65 | both halves | 2e-05 | pathway: G2/M Transition |
| [[SAE1]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PSME3]] | -0.63 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[ZNF8]] | -0.62 | -0.63 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.4, -31.1); signed map (-14.8, 2.2). **Vector** length 102, 34.9% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +8.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.9 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.4 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.9 | +7.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +0.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,234,795-69,277,430 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAK1, CDKN7, MO15, STK1, CAK |
| Gene groups (HGNC) | Cyclin dependent kinases; CDK activating kinase complex |
| Hallmark sets | PEROXISOME |
| Reactome | 56 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [P50613](https://www.uniprot.org/uniprotkb/P50613) (Cyclin-dependent kinase 7):

> Serine/threonine kinase involved in cell cycle control and in RNA polymerase II-mediated RNA transcription. As a cyclin-dependent kinase, CDK7 is activated by the binding to cyclin-H/CCNH and the CDK-activating kinase assembly factor MAT1. Catalytic subunit of the CDK-activating kinase (CAK) complex, a master regulator of CDK activity by catalyzing the activating threonine phosphorylation of CDKs. CAK activates major mediators of cell cycle control, including CDK1, CDK2, CDK4 and CDK6, and …

**Summary**, from NCBI Gene [1022](https://www.ncbi.nlm.nih.gov/gene/1022):

> The protein encoded by this gene is a member of the cyclin-dependent protein kinase (CDK) family. CDK family members are highly similar to the gene products of Saccharomyces cerevisiae cdc28, and Schizosaccharomyces pombe cdc2, and are known to be important regulators of cell cycle progression. This protein forms a trimeric complex with cyclin H and MAT1, which functions as a Cdk-activating kinase (CAK). It is an essential component of the transcription factor TFIIH, that is involved in …

**Accessions** — [HGNC:1778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1778) · Entrez [1022](https://www.ncbi.nlm.nih.gov/gene/1022) · UniProt [P50613](https://www.uniprot.org/uniprotkb/P50613) · Ensembl [ENSG00000134058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134058)

## Data

Gene col 5505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5505); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5505]; `tensor/DDL_lfc|DDL_z.npy` [5505]; `embed/gene_vectors.npy` [5505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5505 or target_col == 5505). Every well: [[CDK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
