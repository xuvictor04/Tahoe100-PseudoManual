---
symbol: "ACTR3B"
type: "gene"
col: 5458
ensembl_id: "ENSG00000133627"
name: "actin related protein 3B"
location: "7q36.1-q36.2"
module: 5
arm: "+"
pooled_cpm: 24.45
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ACTR3B

*actin related protein 3B* — 7q36.1-q36.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +17.6, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.617× (z -8.7, q 3e-15, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTR1]] (+0.64, fdr 7e-06), [[MECR]] (+0.61, fdr 7e-06), [[ATR]] (+0.61, fdr 7e-06); moves opposite to [[FXR1]] (-0.56, fdr 1e-05), [[ST13]] (-0.53, fdr 8e-05), [[CRYZ]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +17.6 | 0e+00 | 43/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +13.1 | 6e-37 | 42/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.08×** | +13.1 | 1e-36 | 45/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +11.9 | 2e-30 | 39/46 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.89×** | +10.9 | 8e-26 | 36/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.83×** | +10.8 | 4e-25 | 40/48 (A498, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +9.4 | 6e-19 | 27/47 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +9.3 | 1e-18 | 35/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.56×** | +7.6 | 1e-12 | 28/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.47×** | +6.9 | 4e-10 | 27/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.7 | 1e-09 | 22/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.1 | 2e-05 | 21/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.0 | 3e-05 | 21/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 12/48 (A549, C32, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.003 | 15/48 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.008 | 9/47 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.010 | 14/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.5 | 0.014 | 14/48 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.020 | 13/48 (SW480, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.029 | 10/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.029 | 8/48 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.042 | 7/46 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -8.7 | 3e-15 | 32/47 (LoVo, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.635×** | -8.1 | 1e-13 | 28/47 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -7.8 | 9e-13 | 30/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -6.1 | 1e-07 | 25/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.739×** | -5.4 | 7e-06 | 20/44 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.774×** | -4.6 | 4e-04 | 20/48 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.780×** | -4.2 | 0.002 | 17/48 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.786×** | -4.2 | 0.002 | 20/47 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.644×** | -4.1 | 0.002 | 19/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.858× | -3.9 | 0.005 | 13/48 (SHP-77, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.816×** | -3.6 | 0.014 | 13/48 (AN3 CA, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **0.833×** | -3.3 | 0.049 | 13/45 (SW 900, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.827×** | -3.1 | 0.072 | 17/42 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.720×** | -3.1 | 0.084 | 8/45 (C32, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.722×** | -3.1 | 0.084 | 11/41 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 41.3 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.4) | [[Auranofin (drug)]] 5 µM 0.334× (z -12.1) |
| [[C32 (line)]] | wt | 53.6 | 2 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +10.2) | [[Auranofin (drug)]] 5 µM 0.279× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 28.8 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.2) |
| [[A498 (line)]] | wt | 25.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +9.6) | — |
| [[SW480 (line)]] | alt | 35.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -10.8) |
| [[A-427 (line)]] | wt | 36.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -10.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 57.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 14.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.7) | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[LS 180 (line)]] | wt | 18.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 45.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.351× (z -9.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.120× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0586× (z -10.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.209× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW48 (line)]] | wt | 36.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.145× (z -11.4) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTR1]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MECR]] | +0.61 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ATR]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[LSM6]] | +0.59 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[METTL8]] | +0.58 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[HGSNAT]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[WDR75]] | +0.56 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SCLY]] | +0.55 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PUS1]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PKP4]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FAM86HP]] | +0.53 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXR1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ST13]] | -0.53 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[CRYZ]] | -0.52 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SNX3]] | -0.51 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[ARL6IP5]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ANKMY2]] | -0.50 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[MPP1]] | -0.50 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[CALCOCO2]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CYP39A1]] | -0.49 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[THRA]] | -0.49 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[CYB5R4]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LMBRD1]] | -0.49 | -0.59 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity strengthens ACTR3B's drug response | lines that do not express ADD3 (5) vs lines expressing it (43) | the lines without ADD3 respond 0.79× as strongly (z diff +0.94); strongest at Panobinostat 0.5 µM: 1.22x vs 2.26x (z diff +3.1) | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ACTR3B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NT5M]] | B | NT5M activity raises ACTR3B's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without NT5M | 0.045 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[RAB39A]] | B | RAB39A activity raises ACTR3B's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without RAB39A | 0.073 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.9, -31.5); signed map (0.8, -49.7). **Vector** length 86.1, 19.1% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +5.0 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.8 | +9.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1-q36.2 — chr7:152,759,749-152,855,378 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARP11, ARP3beta |
| Gene groups (HGNC) | Actin related proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1U1](https://www.uniprot.org/uniprotkb/Q9P1U1) (Actin-related protein 3B):

> Plays a role in the organization of the actin cytoskeleton. May function as ATP-binding component of the Arp2/3 complex which is involved in regulation of actin polymerization and together with an activating nucleation-promoting factor (NPF) mediates the formation of branched actin networks. May decrease the metastatic potential of tumors.

**Summary**, from NCBI Gene [57180](https://www.ncbi.nlm.nih.gov/gene/57180):

> This gene encodes a member of the actin-related proteins (ARP), which form multiprotein complexes and share 35-55% amino acid identity with conventional actin. The protein encoded by this gene may have a regulatory role in the actin cytoskeleton and induce cell-shape change and motility. Pseudogenes of this gene are located on chromosomes 2, 4, 10, 16, 22 and Y. Alternative splicing results in multiple transcript variants and protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:17256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17256) · Entrez [57180](https://www.ncbi.nlm.nih.gov/gene/57180) · UniProt [Q9P1U1](https://www.uniprot.org/uniprotkb/Q9P1U1) · Ensembl [ENSG00000133627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133627)

## Data

Gene col 5458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5458); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5458]; `tensor/DDL_lfc|DDL_z.npy` [5458]; `embed/gene_vectors.npy` [5458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5458 or target_col == 5458). Every well: [[ACTR3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
