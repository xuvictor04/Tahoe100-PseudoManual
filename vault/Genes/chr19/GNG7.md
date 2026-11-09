---
symbol: "GNG7"
type: "gene"
col: 10728
ensembl_id: "ENSG00000176533"
name: "G protein subunit gamma 7"
location: "19p13.3"
module: 191
arm: "+"
pooled_cpm: 15.14
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# GNG7

*G protein subunit gamma 7* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.35× (z +33.2, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.722× (z -5.4, q 4e-05, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALN1]] (+0.69, fdr 7e-06), [[SYP]] (+0.61, fdr 1e-05), [[ZNF815P]] (+0.60, fdr 1e-05); moves opposite to [[CCNJ]] (-0.59, fdr 4e-05), [[PGAP4]] (-0.56, fdr 8e-05), [[ATR]] (-0.54, fdr 9e-05).
> It is in [[Module 191]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.35×** | +33.2 | 0e+00 | 46/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.33×** | +30.7 | 0e+00 | 47/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +27.7 | 0e+00 | 35/45 (SW1417, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **4.27×** | +24.2 | 0e+00 | 45/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +20.4 | 0e+00 | 43/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.36×** | +20.2 | 0e+00 | 40/46 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +15.0 | 0e+00 | 17/27 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +14.3 | 1e-44 | 22/32 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +13.8 | 1e-41 | 27/39 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +13.0 | 6e-37 | 35/47 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +10.2 | 1e-22 | 30/45 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.69×** | +8.6 | 3e-16 | 30/46 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 2e-06 | 19/43 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.1 | 1e-05 | 13/34 (SW1417, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 6e-05 | 16/43 (C-33 A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 5e-04 | 6/45 (SK-MEL-2, SNU-423, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.004 | 6/46 (SHP-77, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.005 | 10/44 (C32, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.009 | 20/47 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.722×** | -5.4 | 4e-05 | 17/45 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.772×** | -4.3 | 0.005 | 20/47 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.779×** | -4.1 | 0.006 | 17/45 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -4.1 | 0.006 | 20/45 (A-427, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.643×** | -3.8 | 0.014 | 12/43 (SK-MEL-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.785×** | -3.8 | 0.015 | 11/46 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.649×** | -3.7 | 0.015 | 12/42 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.805×** | -3.6 | 0.024 | 17/47 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.029 | 11/46 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.813×** | -3.4 | 0.035 | 16/46 (A-427, SK-MEL-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.052 | 15/42 (SW 900, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.821×** | -3.3 | 0.054 | 14/47 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.822×** | -3.1 | 0.080 | 9/46 (SK-MEL-2, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 33.0 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +22.7) | — |
| [[NCI-H460 (line)]] | wt | 7.84 | 9 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 19.9× (z +16.7) | — |
| [[SK-MEL-2 (line)]] | alt | 73.4 | 2 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -9.9) |
| [[LoVo (line)]] | wt | 28.2 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.24× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.210× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -9.0) |
| [[PANC-1 (line)]] | alt | 9.13 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.9× (z +16.7) | — |
| [[A-172 (line)]] | wt | 19.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +16.8) | — |
| [[HOP62 (line)]] | alt | 6.31 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 20.4× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 12.2× (z +10.8) | — |
| [[KATO III (line)]] | alt | 8.62 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 17.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 12.9× (z +15.0) | — |
| [[SW480 (line)]] | alt | 7.86 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.78× (z +15.0) | — |
| [[A-427 (line)]] | wt | 19.5 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.31× (z +10.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.100× (z -14.4) |
| [[HT-29 (line)]] | alt | 11.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.32× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 24.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +18.1) | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.23× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 38.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +15.4) | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.92× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.61× (z +14.8) | — |
| [[SHP-77 (line)]] | alt | 19.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.53× (z +10.8) | — |
| [[A498 (line)]] | wt | 6.83 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +13.3) | — |
| [[A549 (line)]] | wt | 4.89 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 24.4× (z +11.0) | — |
| [[C32 (line)]] | wt | 47.3 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.22× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 5.47 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 34.2× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 5.32 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 7.06 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 7.03 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 10.8× (z +11.0) | [[Finasteride (drug)]] 5 µM 0.151× (z -8.5) |
| [[RKO (line)]] | wt | 10.4 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 12.8× (z +11.9) | [[Monocrotaline (drug)]] 0.05 µM 0.0741× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 26.3 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.66× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -10.9) |
| [[BT-474 (line)]] | alt | 12.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.55× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 19.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.36× (z +9.7) | — |
| [[H4 (line)]] | wt | 22.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.31× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 7.43 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +8.8) | [[TAK-901 (drug)]] 0.05 µM 0.0558× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 5.61 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 16.2× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 9.79 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.1× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 17.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.87× (z +8.7) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 6.26 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.3× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 9.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 4.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +10.7) | — |
| [[J82 (line)]] | alt | 5.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 25.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALN1]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[SYP]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZNF815P]] | +0.60 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[LINC00624]] | +0.58 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[SPTBN4]] | +0.57 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ATP6V1C2]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SYN3]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 | pathway: Neuronal System |
| [[SHF]] | +0.56 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[ASMTL]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ABHD8]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SRRM3]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[TMEM266]] | +0.55 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNJ]] | -0.59 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[PGAP4]] | -0.56 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ATR]] | -0.54 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[PA2G4]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[GSTCD]] | -0.53 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[TOR3A]] | -0.52 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[MRM1]] | -0.51 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ASH2L]] | -0.51 | -0.39 / -0.44 | both halves | 5e-05 | pathway: Signaling by WNT |
| [[TDRD3]] | -0.51 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.51 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[PANK1]] | -0.51 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[METTL13]] | -0.50 | -0.26 / -0.48 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.5, 34.5); signed map (26.6, 17.3). **Vector** length 94.7, 22.1% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +20.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +8.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,511,219-2,702,694 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00058 |
| Gene groups (HGNC) | G protein subunits gamma |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [O60262](https://www.uniprot.org/uniprotkb/O60262) (Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-7):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems (By similarity). The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction (By similarity). Plays a role in the formation or stabilization of a G protein heterotrimer (G(olf) subunit alpha-beta-gamma-7) that is required for adenylyl cyclase activity in the striatum (By similarity).

**Summary**, from NCBI Gene [2788](https://www.ncbi.nlm.nih.gov/gene/2788):

> Predicted to enable G-protein beta-subunit binding activity. Predicted to be involved in G protein-coupled receptor signaling pathway and regulation of adenylate cyclase activity. Predicted to act upstream of or within behavioral fear response; locomotory behavior; and receptor guanylyl cyclase signaling pathway. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4410) · Entrez [2788](https://www.ncbi.nlm.nih.gov/gene/2788) · UniProt [O60262](https://www.uniprot.org/uniprotkb/O60262) · Ensembl [ENSG00000176533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176533)

## Data

Gene col 10728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10728); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10728]; `tensor/DDL_lfc|DDL_z.npy` [10728]; `embed/gene_vectors.npy` [10728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10728 or target_col == 10728). Every well: [[GNG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
