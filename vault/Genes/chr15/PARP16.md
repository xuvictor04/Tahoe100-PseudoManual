---
symbol: "PARP16"
type: "gene"
col: 6195
ensembl_id: "ENSG00000138617"
name: "poly(ADP-ribose) polymerase family member 16"
location: "15q22.31"
module: 41
arm: "+"
pooled_cpm: 18.6
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# PARP16

*poly(ADP-ribose) polymerase family member 16* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +20.6, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.613× (z -9.4, q 3e-18, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC4]] (+0.61, fdr 1e-05), [[CCDC144NL-1]] (+0.57, fdr 1e-05), [[TRNAU1AP]] (+0.57, fdr 1e-05); moves opposite to [[MTAP]] (-0.56, fdr 2e-05), [[EXT2]] (-0.52, fdr 1e-05), [[NME1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +20.6 | 0e+00 | 43/47 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +15.3 | 0e+00 | 31/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +14.9 | 0e+00 | 34/47 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +13.0 | 2e-36 | 28/47 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +9.6 | 7e-20 | 30/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +6.9 | 3e-10 | 25/48 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 5e-05 | 18/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.7 | 2e-04 | 20/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +4.5 | 4e-04 | 20/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.4 | 6e-04 | 3/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.24×** | +4.2 | 0.002 | 9/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 6/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.6 | 0.014 | 9/47 (NCI-H2030, Hs 766T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.017 | 6/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.038 | 9/48 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.081 | 7/47 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.0 | 0.092 | 8/48 (SK-MEL-2, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -9.4 | 3e-18 | 28/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -9.2 | 2e-17 | 29/47 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -8.3 | 3e-14 | 31/46 (C32, Hs 766T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -6.7 | 3e-09 | 25/47 (NCI-H1792, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -6.7 | 3e-09 | 26/47 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.526×** | -6.5 | 1e-08 | 26/48 (PANC-1, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -6.3 | 3e-08 | 24/47 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.749×** | -5.6 | 2e-06 | 17/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.753×** | -5.5 | 3e-06 | 22/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.774×** | -4.9 | 5e-05 | 15/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.786×** | -4.6 | 2e-04 | 13/47 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.792×** | -4.3 | 7e-04 | 17/48 (A498, A-172, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.793×** | -4.3 | 8e-04 | 14/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.801×** | -4.3 | 8e-04 | 13/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.802×** | -4.1 | 0.002 | 15/47 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.878× | -3.6 | 0.013 | 11/48 (HCT15, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.828×** | -3.4 | 0.020 | 13/48 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.060 | 10/47 (NCI-H23, J82, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.853× | -3.1 | 0.060 | 7/47 (LOX-IMVI, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 36.7 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +25.6) | — |
| [[PANC-1 (line)]] | alt | 28.9 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +26.4) | — |
| [[SW480 (line)]] | alt | 16.1 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 20.5× (z +25.2) | [[Lonafarnib (drug)]] 5 µM 0.136× (z -8.7) ⚠ toxic |
| [[A549 (line)]] | wt | 20.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.4× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 18.9 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +18.5) | — |
| [[HT-29 (line)]] | alt | 12.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 16.3× (z +14.9) | — |
| [[LoVo (line)]] | wt | 16.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +19.5) | — |
| [[SHP-77 (line)]] | alt | 26.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.3× (z +15.6) | — |
| [[SW1417 (line)]] | alt | 15.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +15.1) | — |
| [[SW48 (line)]] | wt | 17.7 | 3 | 1 | [[Auranofin (drug)]] 5 µM 13.1× (z +11.3) | [[Vismodegib (drug)]] 0.5 µM 0.130× (z -9.0) |
| [[A498 (line)]] | wt | 22.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +10.9) | [[Harringtonine (drug)]] 5 µM 0.304× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 28.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +16.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -11.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 16.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.8) | [[PH-797804 (drug)]] 5 µM 0.0753× (z -8.8) |
| [[LS 180 (line)]] | wt | 12.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +13.6) | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 6.58 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +9.5) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0922× (z -9.0) |
| [[H4 (line)]] | wt | 25.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.78× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0868× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 22.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 18.5 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.21× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 16.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.0946× (z -9.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -13.2) |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0938× (z -8.6) |
| [[C-33 A (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.3) | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 43.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0578× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC4]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[CCDC144NL-1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[LRRC27]] | +0.57 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ELOA-AS1]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[FAM161B]] | +0.55 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[MINDY2]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RYR1]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[CFAP43]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[OGA]] | +0.52 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[ZNF77]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ASTE1]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTAP]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[EXT2]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NME1]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[GTF2F2]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[XRN2]] | -0.48 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MRTFB]] | -0.48 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[GMDS]] | -0.47 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[MACROH2A1]] | -0.47 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[EIF4G3]] | -0.47 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[SPATA5]] | -0.47 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[WDR77]] | -0.47 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[HS6ST2]] | -0.47 | -0.39 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.0, -29.3); signed map (-4.8, 1.5). **Vector** length 77.8, 14.2% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.8 | +14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +20.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +0.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,234,460-65,300,618 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20509, FLJ25281, pART15, ARTD15; previously C15orf30 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases; Small nucleolar RNA protein coding host genes |
| Reactome | 12 pathways, smallest: Maturation of nucleoprotein_9683610; Maturation of nucleoprotein_9694631; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5Y8](https://www.uniprot.org/uniprotkb/Q8N5Y8) (Protein mono-ADP-ribosyltransferase PARP16):

> Intracellular mono-ADP-ribosyltransferase that plays a role in different processes, such as protein translation and unfolded protein response (UPR), through the mono-ADP-ribosylation of proteins involved in those processes. Acts as an inhibitor of protein translation by catalyzing mono-ADP-ribosylation of ribosomal subunits, such as RPL14 and RPS6, thereby inhibiting polysome assembly and mRNA loading. Mono-ADP-ribosylation of ribosomal subunits is promoted by NMNAT2. Involved in the unfolded …

**Summary**, from NCBI Gene [54956](https://www.ncbi.nlm.nih.gov/gene/54956):

> Enables kinase binding activity; pentosyltransferase activity; and protein serine/threonine kinase activator activity. Involved in IRE1-mediated unfolded protein response; negative regulation of cytoplasmic translation; and protein auto-ADP-ribosylation. Located in endoplasmic reticulum tubular network and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26040) · Entrez [54956](https://www.ncbi.nlm.nih.gov/gene/54956) · UniProt [Q8N5Y8](https://www.uniprot.org/uniprotkb/Q8N5Y8) · Ensembl [ENSG00000138617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138617)

## Data

Gene col 6195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6195); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6195]; `tensor/DDL_lfc|DDL_z.npy` [6195]; `embed/gene_vectors.npy` [6195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6195 or target_col == 6195). Every well: [[PARP16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
