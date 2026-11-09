---
symbol: "STXBP3"
type: "gene"
col: 3784
ensembl_id: "ENSG00000116266"
name: "syntaxin binding protein 3"
location: "1p13.3"
module: 68
arm: "+"
pooled_cpm: 71.23
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# STXBP3

*syntaxin binding protein 3* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +19.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.594× (z -11.5, q 5e-28, down in 32 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.729× (z -7.3, q 3e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFNAR1]] (+0.66, fdr 1e-05), [[BAZ2B]] (+0.63, fdr 1e-05), [[RC3H2]] (+0.62, fdr 2e-05); moves opposite to [[ST6GALNAC6]] (-0.60, fdr 2e-05), [[GFOD2]] (-0.59, fdr 3e-05), [[ST6GALNAC4]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 068]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +19.3 | 0e+00 | 46/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.3 | 4e-18 | 25/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +8.5 | 4e-15 | 31/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.7 | 2e-06 | 24/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +5.0 | 5e-05 | 24/48 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +5.0 | 6e-05 | 26/47 (NCI-H23, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.003 | 20/48 (LoVo, BT-474, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.006 | 21/50 (BT-474, SW 900, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.17× | +3.7 | 0.012 | 8/49 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.016 | 19/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.11× | +3.5 | 0.024 | 2/48 (SHP-77, H4) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.037 | 17/48 (SW48, NCI-H23, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.092 | 11/47 (SK-MEL-2, A549, …) | rises with dose | low cells (technical?) |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.097 | 7/48 (HT-29, SNU-423, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.097 | 10/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.097 | 5/48 (A549, KATO III, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.099 | 10/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.594×** | -11.5 | 5e-28 | 32/43 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.657×** | -9.7 | 1e-19 | 38/49 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -9.6 | 2e-19 | 32/44 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.705×** | -8.1 | 1e-13 | 34/48 (HS-578T, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -7.4 | 2e-11 | 33/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -7.3 | 3e-11 | 33/48 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.761×** | -6.3 | 3e-08 | 27/48 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -5.4 | 4e-06 | 29/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.795×** | -5.3 | 8e-06 | 28/48 (C32, HCT15, …) | all doses, flat | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.739×** | -5.0 | 4e-05 | 24/48 (HCT15, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.673×** | -4.6 | 2e-04 | 24/48 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.823×** | -4.5 | 3e-04 | 22/48 (COLO 205, C32, …) | all doses, flat | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.681×** | -4.5 | 3e-04 | 24/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.688×** | -4.3 | 6e-04 | 23/48 (LS 180, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.778×** | -4.1 | 0.001 | 24/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.019 | 15/48 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.025 | 15/49 (COLO 205, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.752×** | -3.3 | 0.026 | 18/48 (Panc 03.27, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.867× | -3.3 | 0.029 | 16/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.907× | -3.2 | 0.042 | 9/48 (LoVo, SW 1088, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.874× | -3.1 | 0.051 | 19/48 (SW 1271, SNU-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.059 | 12/48 (LS 180, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 87.4 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 90.8 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 73.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 88.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 108 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -12.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 54.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.528× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 130 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +19.9) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -16.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 69.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 164 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 72.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -14.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 54.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.7) | [[Lonafarnib (drug)]] 5 µM 0.117× (z -10.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 85.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 41.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.6) | [[Belinostat (drug)]] 0.5 µM 0.269× (z -9.9) |
| [[Hs 766T (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 90.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 78.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.467× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 71.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 59.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 81.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.6) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A-172 (line)]] | wt | 70.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.7) | — |
| [[A-427 (line)]] | wt | 52.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A549 (line)]] | wt | 65.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 55.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 50.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 75.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.7) | — |
| [[RKO (line)]] | wt | 60.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 65.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.444× (z -8.6) |
| [[SW 1271 (line)]] | alt | 75.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0960× (z -9.3) |
| [[SW48 (line)]] | wt | 81.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.4) | — |
| [[SW480 (line)]] | alt | 74.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -15.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNAR1]] | +0.66 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[RC3H2]] | +0.62 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[NFYB]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SCAF11]] | +0.61 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ZC3H6]] | +0.61 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[CGGBP1]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TMEM35B]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[UNK]] | +0.59 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[SEPSECS]] | +0.58 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RO60]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TIA1]] | +0.57 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | -0.60 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[GFOD2]] | -0.59 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ST6GALNAC6-1]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CALU]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[RRP7BP]] | -0.55 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[GNB1L]] | -0.55 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SLC27A5]] | -0.55 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[EIF3H]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[FTSJ1]] | -0.54 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[ZNF787]] | -0.54 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[ENTPD7]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-1.8, 1.4); signed map (20.9, -18.4). **Vector** length 108, 27.8% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +19.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.2 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:108,746,674-108,809,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNC-18C |
| Gene groups (HGNC) | SM family of SNARE chaperones |
| Reactome | 7 pathways, smallest: Disinhibition of SNARE formation; Translocation of SLC2A4 (GLUT4) to the plasma membrane; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

**Function**, from UniProt [O00186](https://www.uniprot.org/uniprotkb/O00186) (Syntaxin-binding protein 3):

> Together with STX4 and VAMP2, may play a role in insulin-dependent movement of GLUT4 and in docking/fusion of intracellular GLUT4-containing vesicles with the cell surface in adipocytes.

**Summary**, from NCBI Gene [6814](https://www.ncbi.nlm.nih.gov/gene/6814):

> Involved in negative regulation of calcium ion-dependent exocytosis; neutrophil degranulation; and platelet aggregation. Located in cytosol; plasma membrane; and secretory granule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11446) · Entrez [6814](https://www.ncbi.nlm.nih.gov/gene/6814) · UniProt [O00186](https://www.uniprot.org/uniprotkb/O00186) · Ensembl [ENSG00000116266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116266)

## Data

Gene col 3784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3784); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3784]; `tensor/DDL_lfc|DDL_z.npy` [3784]; `embed/gene_vectors.npy` [3784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3784 or target_col == 3784). Every well: [[STXBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
