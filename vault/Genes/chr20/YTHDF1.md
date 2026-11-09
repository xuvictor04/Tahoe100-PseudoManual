---
symbol: "YTHDF1"
type: "gene"
col: 7402
ensembl_id: "ENSG00000149658"
name: "YTH N6-methyladenosine RNA binding protein F1"
location: "20q13.33"
module: 3
arm: "+"
pooled_cpm: 40.67
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# YTHDF1

*YTH N6-methyladenosine RNA binding protein F1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +17.4, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.585× (z -8.8, q 6e-16, down in 26 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.791× (z -5.7, q 3e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXR2]] (+0.64, fdr 1e-05), [[SCYL1]] (+0.63, fdr 1e-05), [[RTCB]] (+0.61, fdr 1e-05); moves opposite to [[GLS]] (-0.60, fdr 1e-05), [[TEX14]] (-0.56, fdr 1e-04), [[EPB41L2]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +17.4 | 0e+00 | 44/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +12.0 | 6e-31 | 41/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +11.5 | 4e-28 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +10.2 | 5e-22 | 43/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +9.1 | 1e-17 | 38/48 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +8.8 | 1e-16 | 41/48 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.3 | 1e-14 | 37/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.45×** | +8.0 | 7e-14 | 34/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +7.6 | 2e-12 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +7.6 | 2e-12 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.2 | 4e-11 | 35/47 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +7.0 | 1e-10 | 37/48 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.7 | 9e-10 | 32/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +6.3 | 9e-09 | 32/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.9 | 2e-07 | 34/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.6 | 1e-04 | 26/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 2e-04 | 20/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.007 | 21/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -8.8 | 6e-16 | 26/39 (SHP-77, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.600×** | -8.7 | 7e-16 | 32/47 (RKO, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -5.7 | 3e-06 | 26/48 (SW1417, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -5.3 | 2e-05 | 3/48 (SNU-1, NCI-H661, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.798×** | -3.9 | 0.012 | 18/48 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.820×** | -3.4 | 0.066 | 15/48 (SNU-1, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.827×** | -3.3 | 0.086 | 15/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.086 | 19/48 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.833× | -3.1 | 0.11 | 10/48 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.835× | -3.1 | 0.12 | 11/48 (SW48, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 45.1 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 55.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.2) | — |
| [[LoVo (line)]] | wt | 38.3 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 43.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.9) | [[Selinexor (drug)]] 5 µM 0.388× (z -10.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 65.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 24.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +16.4) | — |
| [[PANC-1 (line)]] | alt | 26.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 39.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -11.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 45.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.5) | [[Omeprazole (drug)]] 0.5 µM 0.296× (z -9.1) |
| [[KATO III (line)]] | alt | 64.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 36.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 94.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.3) |
| [[A-172 (line)]] | wt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.1) | — |
| [[A498 (line)]] | wt | 51.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.9) | — |
| [[A549 (line)]] | wt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 32.9 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0786× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 42.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.1) | — |
| [[RKO (line)]] | wt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -15.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -14.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.8) | — |
| [[SW 1271 (line)]] | alt | 48.8 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0682× (z -9.1) |
| [[SW48 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXR2]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 | STRING 505 |
| [[SCYL1]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[RTCB]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ALG2]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[NECAP1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ZNF567]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TMEM216]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[WRAP73]] | +0.55 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[NUBP2]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[COG3]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[TEX14]] | -0.56 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[EPB41L2]] | -0.52 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[FKBP3]] | -0.51 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[ATP11C]] | -0.50 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[AP2B1]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[DOCK7]] | -0.49 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[BHLHE40-AS1]] | -0.48 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[CCDC200]] | -0.47 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[PGRMC1]] | -0.47 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[PRDM2]] | -0.47 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[LAMC1]] | -0.47 | -0.29 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.347). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-7.6, -55.0); signed map (-28.1, 3.3). **Vector** length 78.1, 17.5% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | +4.7 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +12.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | -0.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.9 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | YTH N6-methyladenosine RNA binding protein F1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,195,429-63,216,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20391; previously C20orf21 |
| Gene groups (HGNC) | YTH domain containing N6-methyladenosine readers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYJ9](https://www.uniprot.org/uniprotkb/Q9BYJ9) (YTH domain-containing family protein 1):

> Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability. M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing. Acts as a regulator of mRNA stability by promoting degradation of m6A-containing mRNAs via interaction with the CCR4-NOT complex. The YTHDF paralogs (YTHDF1, YTHDF2 and YTHDF3) shares m6A-containing mRNAs targets and act redundantly to mediate mRNA …

**Summary**, from NCBI Gene [54915](https://www.ncbi.nlm.nih.gov/gene/54915):

> Enables N6-methyladenosine-containing RNA reader activity and ribosome binding activity. Involved in mRNA destabilization; positive regulation of translational initiation; and stress granule assembly. Located in P-body and cytoplasmic stress granule. Implicated in colorectal cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15867) · Entrez [54915](https://www.ncbi.nlm.nih.gov/gene/54915) · UniProt [Q9BYJ9](https://www.uniprot.org/uniprotkb/Q9BYJ9) · Ensembl [ENSG00000149658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149658)

## Data

Gene col 7402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7402); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7402]; `tensor/DDL_lfc|DDL_z.npy` [7402]; `embed/gene_vectors.npy` [7402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7402 or target_col == 7402). Every well: [[YTHDF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YTHDF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
