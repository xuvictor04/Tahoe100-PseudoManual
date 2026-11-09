---
symbol: "FAM174B"
type: "gene"
col: 11678
ensembl_id: "ENSG00000185442"
name: "family with sequence similarity 174 member B"
location: "15q26.1"
module: 35
arm: "+"
pooled_cpm: 16.92
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 20
n_dd_up_clean: 19
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# FAM174B

*family with sequence similarity 174 member B* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.51× (z +28.9, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.525× (z -9.9, q 3e-20, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.80, fdr 1e-05), [[TMEM202-AS1]] (+0.80, fdr 1e-05), [[PBLD]] (+0.79, fdr 1e-05); moves opposite to [[NBPF3]] (-0.67, fdr 1e-05), [[MAST3]] (-0.66, fdr 3e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GOLGA2P5-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.51×** | +28.9 | 0e+00 | 43/45 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +13.0 | 5e-36 | 32/43 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +11.9 | 4e-30 | 36/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +10.7 | 1e-24 | 24/39 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +9.4 | 9e-19 | 28/45 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +8.4 | 6e-15 | 22/33 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +7.8 | 7e-13 | 27/45 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.3 | 2e-11 | 13/23 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +6.3 | 2e-08 | 20/46 (HEC-1-A, SW48, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.36×** | +4.6 | 3e-04 | 16/46 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.5 | 3e-04 | 19/46 (MIA PaCa-2, COLO 205, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.8 | 0.006 | 3/47 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.009 | 8/45 (MIA PaCa-2, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.013 | 6/42 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.032 | 13/47 (MIA PaCa-2, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.033 | 3/42 (SW 900, PANC-1, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.033 | 10/46 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.048 | 15/46 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.064 | 8/46 (A549, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.525×** | -9.9 | 3e-20 | 37/46 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.564×** | -8.8 | 4e-16 | 32/46 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.587×** | -8.7 | 6e-16 | 30/46 (J82, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.637×** | -6.9 | 6e-10 | 27/46 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -6.7 | 3e-09 | 23/45 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.668×** | -6.2 | 6e-08 | 23/44 (PANC-1, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -5.9 | 3e-07 | 23/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -5.7 | 9e-07 | 22/46 (HT-29, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.515×** | -5.7 | 9e-07 | 19/46 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.713×** | -5.5 | 2e-06 | 21/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -5.5 | 2e-06 | 22/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -5.1 | 2e-05 | 16/45 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.598×** | -4.4 | 5e-04 | 14/42 (Panc 03.27, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.647×** | -3.7 | 0.008 | 10/44 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.798×** | -3.7 | 0.008 | 15/46 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.666×** | -3.5 | 0.016 | 6/42 (NCI-H23, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.024 | 13/46 (A-427, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 38.3 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -11.8) |
| [[LoVo (line)]] | wt | 13.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +18.8) | — |
| [[J82 (line)]] | alt | 54.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0978× (z -15.3) |
| [[PANC-1 (line)]] | alt | 21.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.356× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -8.7) |
| [[C32 (line)]] | wt | 11.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.0) | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0505× (z -12.6) |
| [[HOP62 (line)]] | alt | 10.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 32.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 19.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.89 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +12.0) | [[Clofarabine (drug)]] 5 µM 0.127× (z -9.0) |
| [[SW480 (line)]] | alt | 23.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.1) | — |
| [[A498 (line)]] | wt | 6.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +8.9) | — |
| [[A549 (line)]] | wt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 6.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 9.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 7.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 8.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +8.9) | — |
| [[KATO III (line)]] | alt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 9.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.6) | — |
| [[A-172 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.80 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.80 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[PBLD]] | +0.79 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[SIAH2-AS1]] | +0.79 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.79 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[MYLK4]] | +0.78 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.78 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[PSMD7-DT]] | +0.77 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | +0.77 | +0.72 / +0.38 | both halves | 7e-05 |  |
| [[INTS6-AS1]] | +0.76 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[SPEN-AS1]] | +0.76 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[MALINC1]] | +0.74 | +0.66 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.67 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[MAST3]] | -0.66 | -0.53 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOLGA2P5-1]] | B | GOLGA2P5-1 activity raises FAM174B's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without GOLGA2P5-1 | 0.023 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FAM174B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STOX1]] | B | STOX1 activity raises FAM174B's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.64× lower at baseline in the lines without STOX1 | 0.064 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers FAM174B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ARHGEF17]] | C | ARHGEF17 activity lowers FAM174B's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.55× higher at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.825). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.3, 18.9); signed map (26.0, -4.2). **Vector** length 89.2, 18.3% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +28.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +6.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | +4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.6 | -9.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 174 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:92,617,448-92,809,884 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC400451, MGC102891 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3ZCQ3](https://www.uniprot.org/uniprotkb/Q3ZCQ3) (Membrane protein FAM174B):

> Essential for Golgi structural integrity.

**Summary**, from NCBI Gene [400451](https://www.ncbi.nlm.nih.gov/gene/400451):

> Involved in Golgi organization. Located in Golgi apparatus and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34339) · Entrez [400451](https://www.ncbi.nlm.nih.gov/gene/400451) · UniProt [Q3ZCQ3](https://www.uniprot.org/uniprotkb/Q3ZCQ3) · Ensembl [ENSG00000185442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185442)

## Data

Gene col 11678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11678); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11678]; `tensor/DDL_lfc|DDL_z.npy` [11678]; `embed/gene_vectors.npy` [11678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11678 or target_col == 11678). Every well: [[FAM174B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM174B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
