---
symbol: "CCDC171"
type: "gene"
col: 9052
ensembl_id: "ENSG00000164989"
name: "coiled-coil domain containing 171"
location: "9p22.3"
module: 10
arm: "+"
pooled_cpm: 29.7
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 13
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 9
direction_downstream: 9
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CCDC171

*coiled-coil domain containing 171* — 9p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.77× (z +6.2, q 4e-07, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.190× (z -17.8, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WWOX]] (+0.59, fdr 1e-05), [[FAM172A]] (+0.52, fdr 4e-05), [[CASC2]] (+0.50, fdr 4e-05); moves opposite to [[PHLDB3]] (-0.44, fdr 8e-05), [[EML2]] (-0.43, fdr 1e-04), [[CIAO2B]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[FRG1-DT]] → it (grade B ⚠); 9 go from it, the strongest it → [[WWOX]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +6.2 | 4e-07 | 34/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 0.001 | 29/44 (SW480, KATO III, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.59×** | +4.5 | 0.001 | 26/44 (NCI-H460, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.005 | 28/45 (KATO III, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.046 | 17/45 (LoVo, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.046 | 19/44 (SW480, LoVo, …) | two highest doses |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.047 | 15/45 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.050 | 17/45 (NCI-H1573, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.056 | 20/45 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.070 | 13/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.070 | 12/45 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.079 | 13/45 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.079 | 14/45 (SW480, C-33 A, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.71× | +3.0 | 0.10 | 13/44 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.190×** | -17.8 | 0e+00 | 45/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.338×** | -16.4 | 0e+00 | 41/44 (COLO 205, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.255×** | -14.6 | 0e+00 | 41/43 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.266×** | -14.2 | 2e-43 | 43/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.272×** | -13.9 | 7e-42 | 44/45 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.351×** | -11.2 | 5e-27 | 38/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.347×** | -10.9 | 1e-25 | 42/45 (SNU-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.388×** | -10.1 | 3e-22 | 38/45 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.435×** | -8.9 | 3e-17 | 35/45 (KATO III, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.436×** | -8.9 | 4e-17 | 31/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.222×** | -8.4 | 2e-15 | 41/45 (HOP62, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.236×** | -8.1 | 4e-14 | 36/43 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -6.8 | 6e-10 | 30/42 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.509×** | -6.6 | 2e-09 | 28/45 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.539×** | -6.2 | 2e-08 | 30/45 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.619×** | -5.1 | 1e-05 | 27/45 (COLO 205, HOP62, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -4.5 | 2e-04 | 22/45 (A-427, SNU-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.690×** | -4.0 | 0.002 | 20/44 (NCI-H23, SK-MEL-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.003 | 25/45 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.719×** | -3.5 | 0.010 | 22/45 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 100.0 | 0 | 10 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.173× (z -15.1) |
| [[PANC-1 (line)]] | alt | 30.0 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -15.6) |
| [[COLO 205 (line)]] | alt | 54.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0590× (z -24.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.120× (z -13.0) |
| [[KATO III (line)]] | alt | 58.7 | 1 | 8 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 2.93× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.0913× (z -18.9) |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -13.3) |
| [[HOP62 (line)]] | alt | 50.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0812× (z -15.7) |
| [[NCI-H23 (line)]] | alt | 43.1 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0835× (z -17.6) |
| [[SNU-1 (line)]] | wt | 64.1 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0703× (z -15.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0953× (z -14.6) |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.196× (z -10.4) |
| [[H4 (line)]] | wt | 61.9 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0565× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 44.9 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0420× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -13.7) |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0675× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0880× (z -13.0) |
| [[RKO (line)]] | wt | 52.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -12.1) |
| [[SW480 (line)]] | alt | 19.8 | 1 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.2) ⚠ cell-cycle shift, explains ~22% of this change | [[Digitoxin (drug)]] 0.5 µM 0.185× (z -10.9) |
| [[A498 (line)]] | wt | 29.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -11.3) |
| [[J82 (line)]] | alt | 24.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.155× (z -11.6) |
| [[LoVo (line)]] | wt | 33.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.118× (z -16.0) |
| [[SNU-423 (line)]] | alt | 27.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -8.6) |
| [[LS 180 (line)]] | wt | 34.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.9) |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.173× (z -11.5) |
| [[SW48 (line)]] | wt | 54.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -9.1) |
| [[A-172 (line)]] | wt | 22.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 27.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0546× (z -15.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.223× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.301× (z -8.5) |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.136× (z -10.6) ⚠ toxic |
| [[A549 (line)]] | wt | 20.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -9.6) |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -9.2) |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WWOX]] | +0.59 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[FAM172A]] | +0.52 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[CASC2]] | +0.50 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[C5]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[HCCS-DT]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZRANB2-DT]] | +0.49 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[CNOT1]] | +0.49 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[TARS1]] | +0.47 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[HNRNPA1L3]] | +0.47 | +0.39 / +0.38 | both halves | 6e-05 |  |
| [[ANP32B]] | +0.46 | +0.39 / +0.39 | both halves | 5e-05 |  |
| [[PRKN]] | +0.46 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PSAT1]] | +0.46 | +0.38 / +0.57 | both halves | 6e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDB3]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[EML2]] | -0.43 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[CIAO2B]] | -0.43 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[RMND5B]] | -0.42 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[UBE2J2]] | -0.42 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[BCAR1]] | -0.41 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[TMEM184B]] | -0.41 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[ACOT8]] | -0.40 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[MN1]] | -0.40 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[ARVCF]] | -0.40 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[ZBTB43]] | -0.40 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[GTF2A2]] | -0.39 | -0.25 / -0.40 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1-DT]] | B | FRG1-DT activity raises CCDC171's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without FRG1-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[WWOX]] | B | WWOX activity raises CCDC171's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.63× lower at baseline in the lines without WWOX | 0.010 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[KATNAL2]] | B | KATNAL2 activity raises CCDC171's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without KATNAL2 | 0.011 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[CNTLN]] | B | CNTLN activity raises CCDC171's level | lines that do not express CNTLN (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without CNTLN | 0.036 | ⚠ within organs, on part of the lines; also absent: SRGAP2D, PRKAR2B, WDR54 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CCDC171's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[PRKN]] | B | PRKN activity raises CCDC171's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.41× lower at baseline in the lines without PRKN | 0.062 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[ANKS1B]] | B | ANKS1B activity raises CCDC171's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without ANKS1B | 0.065 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[LINC00466]] | B | LINC00466 activity raises CCDC171's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.74× lower at baseline in the lines without LINC00466 | 0.072 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[FRG1-DT]] | B | FRG1-DT activity strengthens CCDC171's drug response | lines that do not express FRG1-DT (6) vs lines expressing it (39) | the lines without FRG1-DT respond 0.83× as strongly (z diff +1.78); strongest at Digitoxin 5 µM: 0.50x vs 0.19x (z diff +5.3) | 0.086 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWOX]] | C | CCDC171 activity raises WWOX's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 3.53× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[CASC2]] | C | CCDC171 activity raises CASC2's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 3.37× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TBC1D32]] | C | CCDC171 activity raises TBC1D32's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[CARF]] | C | CCDC171, [[RFX3-DT]] activity raises CARF's level | lines that do not express CCDC171, RFX3-DT (3) vs lines expressing them (47) | 2.33× lower at baseline in the lines without CCDC171, RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p; co-absent genes |
| [[PRIMPOL]] | C | CCDC171 activity raises PRIMPOL's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[CCDC7]] | C | CCDC171 activity raises CCDC7's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 1.43× lower at baseline in the lines without CCDC171 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[EIF1B-AS1]] | C | CCDC171, [[DUSP19]], [[RFX3-DT]] activity raises EIF1B-AS1's level | lines that do not express CCDC171, DUSP19, RFX3-DT (3) vs lines expressing them (47) | 2.62× lower at baseline in the lines without CCDC171, DUSP19, RFX3-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p; co-absent genes |
| [[ALMS1]] | C | CCDC171 activity raises ALMS1's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without CCDC171 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[VLDLR-AS1]] | C | CCDC171 activity raises VLDLR-AS1's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 2.61× lower at baseline in the lines without CCDC171 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.313). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.7, -39.3); signed map (3.2, 6.0). **Vector** length 75.5, 20.7% of its response variance represented; |z| ≥ 3 in 1,327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | +2.5 | -5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +6.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +4.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | -6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 171 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.3 — chr9:15,553,043-16,061,663 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39267, FLJ46740, Em:AL513423.1, bA778P13.1, bA536D16.1; previously C9orf93 |
| Matched by | ensembl_id |

UniProt [Q6TFL3](https://www.uniprot.org/uniprotkb/Q6TFL3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29828) · Entrez [203238](https://www.ncbi.nlm.nih.gov/gene/203238) · UniProt [Q6TFL3](https://www.uniprot.org/uniprotkb/Q6TFL3) · Ensembl [ENSG00000164989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164989)

## Data

Gene col 9052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9052); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9052]; `tensor/DDL_lfc|DDL_z.npy` [9052]; `embed/gene_vectors.npy` [9052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9052 or target_col == 9052). Every well: [[CCDC171 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC171.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
