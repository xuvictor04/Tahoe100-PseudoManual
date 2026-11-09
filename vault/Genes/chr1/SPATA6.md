---
symbol: "SPATA6"
type: "gene"
col: 5275
ensembl_id: "ENSG00000132122"
name: "spermatogenesis associated 6"
location: "1p33"
module: 80
arm: "+"
pooled_cpm: 32.28
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 40
n_dd_up_clean: 17
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# SPATA6

*spermatogenesis associated 6* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.89× (z +9.6, q 3e-19, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.247× (z -21.1, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6]] (+0.69, fdr 1e-05), [[ALAD]] (+0.66, fdr 4e-05), [[POT1]] (+0.66, fdr 2e-05); moves opposite to [[LINC01829]] (-0.68, fdr 1e-05), [[ZHX2]] (-0.67, fdr 1e-05), [[LTO1]] (-0.66, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MGLL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +9.6 | 3e-19 | 38/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +9.3 | 3e-18 | 38/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +8.0 | 2e-13 | 35/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +7.7 | 2e-12 | 34/46 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +6.1 | 1e-07 | 31/46 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.5 | 7e-04 | 25/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.001 | 23/46 (SW480, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.004 | 20/46 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.005 | 22/46 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.013 | 18/45 (LoVo, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.018 | 15/45 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.018 | 15/46 (HEC-1-A, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.018 | 10/46 (NCI-H1573, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.036 | 14/46 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.041 | 16/46 (AsPC-1, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.247×** | -21.1 | 0e+00 | 43/46 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.426×** | -18.2 | 0e+00 | 40/46 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.308×** | -17.8 | 0e+00 | 43/45 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.343×** | -16.1 | 0e+00 | 41/46 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.351×** | -15.8 | 0e+00 | 45/46 (C-33 A, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.377×** | -14.7 | 0e+00 | 39/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.426×** | -12.9 | 5e-36 | 41/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -12.6 | 2e-34 | 39/46 (HS-578T, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.489×** | -10.4 | 2e-23 | 37/46 (HOP62, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -9.6 | 7e-20 | 37/46 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -8.9 | 4e-17 | 31/46 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -8.3 | 7e-15 | 36/45 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.658×** | -6.3 | 1e-08 | 31/45 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.661×** | -6.2 | 2e-08 | 27/45 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -6.0 | 6e-08 | 33/46 (HEC-1-A, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -6.0 | 6e-08 | 31/46 (C32, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.754×** | -6.0 | 7e-08 | 31/46 (C32, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.679×** | -5.8 | 2e-07 | 33/46 (CHP-212, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -5.7 | 4e-07 | 26/46 (C32, SNU-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.519×** | -5.1 | 1e-05 | 27/46 (NCI-H1573, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.5 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.163× (z -15.1) |
| [[C32 (line)]] | wt | 104 | 0 | 13 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0295× (z -28.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.199× (z -13.6) |
| [[SW480 (line)]] | alt | 25.5 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0552× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -17.8) |
| [[HOP62 (line)]] | alt | 28.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.211× (z -12.0) |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 75.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -22.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 45.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -16.2) |
| [[PANC-1 (line)]] | alt | 62.0 | 1 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -14.3) |
| [[SW 900 (line)]] | alt | 38.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.266× (z -9.8) |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0858× (z -19.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0459× (z -16.8) |
| [[AN3 CA (line)]] | alt | 102 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -16.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 29.9 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -12.2) |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -13.3) |
| [[J82 (line)]] | alt | 15.7 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belzutifan (drug)]] 5 µM 0.0600× (z -9.5) |
| [[SHP-77 (line)]] | alt | 114 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.7) |
| [[SNU-1 (line)]] | wt | 69.8 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -14.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -11.5) |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0296× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.149× (z -11.7) |
| [[C-33 A (line)]] | alt | 107 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.265× (z -12.5) |
| [[H4 (line)]] | wt | 30.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -11.8) |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0443× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -13.3) |
| [[A498 (line)]] | wt | 19.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.23× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 26.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0844× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CFPAC-1 (line)]] | alt | 22.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.3) |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.150× (z -10.2) |
| [[LoVo (line)]] | wt | 20.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -13.9) |
| [[RKO (line)]] | wt | 25.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.184× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 64.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.248× (z -11.1) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -8.7) |
| [[A-427 (line)]] | wt | 64.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.380× (z -9.2) |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0539× (z -13.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0644× (z -8.5) |
| [[KATO III (line)]] | alt | 25.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -8.7) |
| [[SW48 (line)]] | wt | 24.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | +0.69 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ALAD]] | +0.66 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[POT1]] | +0.66 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[HACE1]] | +0.66 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.66 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.64 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[NDRG3]] | +0.64 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[DYNC2H1]] | +0.63 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[MNS1]] | +0.62 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[ARRB2]] | +0.62 | +0.38 / +0.40 | both halves | 6e-05 |  |
| [[KCTD6]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ELP1]] | +0.61 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01829]] | -0.68 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZHX2]] | -0.67 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[LTO1]] | -0.66 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[PXDC1]] | -0.66 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ATXN1L]] | -0.65 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.65 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | -0.64 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SIAH2-AS1]] | -0.64 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[GCNT4]] | -0.64 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[TMEM217]] | -0.64 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[C1S]] | -0.63 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SLC13A3]] | -0.63 | -0.50 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGLL]] | B | MGLL activity lowers SPATA6's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.93× higher at baseline in the lines without MGLL | 0.046 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[ZHX2]] | B | ZHX2 activity lowers SPATA6's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 2.33× higher at baseline in the lines without ZHX2 | 0.074 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[TBC1D32]] | C | TBC1D32 activity raises SPATA6's level | lines that do not express TBC1D32 (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without TBC1D32 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ACOT12, ENSG00000271590, ENSG00000288545; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction -0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.3, 9.6); signed map (-27.6, -10.6). **Vector** length 76.3, 20.0% of its response variance represented; |z| ≥ 3 in 1,448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -5.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -16.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:48,295,373-48,472,208 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRF1, FLJ10007, SRF-1 |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWH7](https://www.uniprot.org/uniprotkb/Q9NWH7) (Spermatogenesis-associated protein 6):

> Required for formation of the sperm connecting piece during spermiogenesis. Sperm connecting piece is essential for linking the developing flagellum to the head during late spermiogenesis. May be involved in myosin-based microfilament transport through interaction with myosin subunits.

**Summary**, from NCBI Gene [54558](https://www.ncbi.nlm.nih.gov/gene/54558):

> Predicted to enable myosin light chain binding activity. Predicted to be involved in motile cilium assembly and spermatogenesis. Predicted to be located in extracellular region and motile cilium. Predicted to be active in sperm head-tail coupling apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18309) · Entrez [54558](https://www.ncbi.nlm.nih.gov/gene/54558) · UniProt [Q9NWH7](https://www.uniprot.org/uniprotkb/Q9NWH7) · Ensembl [ENSG00000132122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132122)

## Data

Gene col 5275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5275); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5275]; `tensor/DDL_lfc|DDL_z.npy` [5275]; `embed/gene_vectors.npy` [5275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5275 or target_col == 5275). Every well: [[SPATA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
