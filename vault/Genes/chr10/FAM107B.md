---
symbol: "FAM107B"
type: "gene"
col: 805
ensembl_id: "ENSG00000065809"
name: "family with sequence similarity 107 member B"
location: "10p13"
module: 81
arm: "+"
pooled_cpm: 226.68
n_lines_expressing: 39
n_dd_up: 13
n_dd_down: 42
n_dd_up_clean: 9
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 33
direction_downstream: 45
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# FAM107B

*family with sequence similarity 107 member B* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +11.9, q 8e-30, up in 22 of 37 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +10.7, q 3e-24, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (13 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.573× (z -11.4, q 2e-27, down in 31 of 36 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.623× (z -9.1, q 2e-17, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WNT7B]] (+0.71, fdr 7e-06), [[AADACP1]] (+0.70, fdr 7e-06), [[EHD1]] (+0.70, fdr 7e-06); moves opposite to [[LTBR]] (-0.56, fdr 1e-05), [[ARMC8]] (-0.55, fdr 1e-05), [[LARP1]] (-0.53, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[SERPINE2]] → it (grade B ⚠); 45 go from it, the strongest it → [[EXT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +11.9 | 8e-30 | 22/37 (HOP62, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +10.7 | 3e-24 | 31/37 (SW1417, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +10.5 | 1e-23 | 24/37 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +9.0 | 3e-17 | 25/37 (SW1417, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +6.4 | 1e-08 | 20/37 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +6.3 | 3e-08 | 22/36 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +5.7 | 7e-07 | 24/37 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 7e-07 | 24/38 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 6e-06 | 25/37 (LoVo, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +5.0 | 4e-05 | 19/37 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +5.0 | 4e-05 | 21/36 (SW 900, PANC-1, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.55×** | +4.6 | 2e-04 | 23/37 (RKO, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.017 | 15/36 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.17× | +3.5 | 0.022 | 14/37 (BT-474, LS 180, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.4 | 0.022 | 16/37 (LoVo, HCT15, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.039 | 13/37 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.085 | 13/38 (SW480, COLO 205, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.100 | 4/38 (Panc 03.27, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM | ⚠ position correction uncertain | **0.573×** | -11.4 | 2e-27 | 31/36 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.618×** | -9.2 | 9e-18 | 28/37 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.623×** | -9.1 | 2e-17 | 22/37 (A549, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.659×** | -8.9 | 7e-17 | 32/36 (NCI-H2347, HCT15, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM | ⚠ position correction uncertain | **0.665×** | -8.7 | 4e-16 | 23/37 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.667×** | -8.7 | 5e-16 | 23/37 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -8.4 | 4e-15 | 23/36 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dexamethasone (drug)]] 5 µM | ⚠ position correction uncertain | **0.681×** | -8.2 | 2e-14 | 25/37 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.677×** | -7.7 | 9e-13 | 23/36 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.704×** | -7.5 | 4e-12 | 27/37 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -7.3 | 2e-11 | 23/34 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.697×** | -7.1 | 5e-11 | 23/37 (NCI-H2347, HCT15, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.799×** | -6.8 | 6e-10 | 20/37 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -6.7 | 7e-10 | 26/37 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.730×** | -6.7 | 7e-10 | 24/38 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.731×** | -6.7 | 8e-10 | 22/37 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.731×** | -6.7 | 8e-10 | 23/37 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.739×** | -6.5 | 3e-09 | 21/37 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.739×** | -6.4 | 3e-09 | 22/37 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -6.2 | 2e-08 | 21/37 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.740×** | -6.2 | 2e-08 | 24/37 (NCI-H2347, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.750×** | -6.0 | 5e-08 | 22/39 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 407 | 2 (2 ⚠) | 19 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.35× (z +10.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Triamcinolone (drug)]] 5 µM 0.507× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 193 | 0 | 20 (3 ⚠) | — | [[Budesonide (drug)]] 5 µM 0.296× (z -13.5) |
| [[A549 (line)]] | wt | 799 | 0 | 18 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -19.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.434× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 289 | 0 | 17 (7 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.310× (z -12.7) ⚠ position correction uncertain · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.383× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 798 | 0 | 16 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0733× (z -29.6) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.369× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 556 | 1 (1 ⚠) | 12 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Dexamethasone (drug)]] 0.05 µM 0.391× (z -10.6) ⚠ position correction uncertain · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.398× (z -10.4) |
| [[LoVo (line)]] | wt | 104 | 11 (6 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.68× (z +13.7) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.79× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 809 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -19.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.517× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 341 | 0 | 6 (2 ⚠) | — | [[Dexamethasone (drug)]] 5 µM 0.490× (z -9.6) ⚠ position correction uncertain · without an alert: [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.491× (z -9.5) |
| [[SW1417 (line)]] | alt | 203 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.59× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 672 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[Hs 766T (line)]] | wt | 245 | 0 | 5 (2 ⚠) | — | [[Dexamethasone (drug)]] 5 µM 0.342× (z -9.5) ⚠ position correction uncertain · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.362× (z -9.0) |
| [[RKO (line)]] | wt | 102 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.43× (z +9.1) | — |
| [[SW480 (line)]] | alt | 81.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +10.8) | — |
| [[KATO III (line)]] | alt | 177 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +11.1) | — |
| [[A-172 (line)]] | wt | 353 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -11.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 404 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -11.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 170 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +19.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.374× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 255 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 125 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.66× (z +9.3) | — |
| [[SW48 (line)]] | wt | 199 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.61× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 62.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +14.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 185 | 0 | 2 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.331× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 59.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 150 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.336× (z -12.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 278 | 0 | 2 (1 ⚠) | — | [[Dexamethasone (drug)]] 5 µM 0.421× (z -9.8) ⚠ position correction uncertain · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.435× (z -9.5) |
| [[SW 900 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 59.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.0) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[CHP-212 (line)]] | wt | 293 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.376× (z -8.6) ⚠ position correction uncertain |
| [[HS-578T (line)]] | alt | 241 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 32.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 33.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT7B]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[AADACP1]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[EHD1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[PKIA]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[DPF3]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[SHB]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GRK5]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FGD6]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SLC35F3]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBR]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ARMC8]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[LARP1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TAF8]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[NFIC]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[BATF]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 31, C 2. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE2]] | B | SERPINE2 activity raises FAM107B's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 3.25× lower at baseline in the lines without SERPINE2 | 0.003 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[PTHLH]] | B | PTHLH activity raises FAM107B's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.83× lower at baseline in the lines without PTHLH | 0.004 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[WNT7B]] | B | WNT7B activity raises FAM107B's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.41× lower at baseline in the lines without WNT7B | 0.004 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[SOX9]] | B | SOX9 activity raises FAM107B's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 4.82× lower at baseline in the lines without SOX9 | 0.007 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[AADACP1]] | B | AADACP1 activity raises FAM107B's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 3.08× lower at baseline in the lines without AADACP1 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[GABRE]] | B | GABRE activity raises FAM107B's level | lines that do not express GABRE (20) vs lines expressing it (30) | 3.05× lower at baseline in the lines without GABRE | 0.008 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[LAMC2]] | B | LAMC2 activity raises FAM107B's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without LAMC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[SMOX]] | B | SMOX activity raises FAM107B's level | lines that do not express SMOX (6) vs lines expressing it (44) | 5.90× lower at baseline in the lines without SMOX | 0.012 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[F3]] | B | F3 activity raises FAM107B's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.76× lower at baseline in the lines without F3 | 0.016 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[MAP2K1]] | B | MAP2K1 activity raises FAM107B's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[NHS]] | B | NHS activity raises FAM107B's level | lines that do not express NHS (17) vs lines expressing it (33) | 3.10× lower at baseline in the lines without NHS | 0.021 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[SERPIND1]] | B | SERPIND1 activity raises FAM107B's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without SERPIND1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 43, C 2. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXT1]] | B | FAM107B activity raises EXT1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without FAM107B | 0.003 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[WNT7B]] | B | FAM107B activity raises WNT7B's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.80× lower at baseline in the lines without FAM107B | 0.009 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[ITGA2]] | B | FAM107B activity raises ITGA2's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 4.31× lower at baseline in the lines without FAM107B | 0.011 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[PTHLH]] | B | FAM107B activity raises PTHLH's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without FAM107B | 0.012 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[SOX9]] | B | FAM107B activity raises SOX9's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.38× lower at baseline in the lines without FAM107B | 0.014 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[SMOX]] | B | FAM107B activity raises SMOX's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without FAM107B | 0.015 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[ADAM19]] | B | FAM107B activity raises ADAM19's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without FAM107B | 0.016 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[F3]] | B | FAM107B activity raises F3's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.89× lower at baseline in the lines without FAM107B | 0.020 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[NHS]] | B | FAM107B activity raises NHS's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.14× lower at baseline in the lines without FAM107B | 0.023 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[DUSP5]] | B | FAM107B activity raises DUSP5's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.11× lower at baseline in the lines without FAM107B | 0.024 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[ACVR1]] | B | FAM107B activity raises ACVR1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without FAM107B | 0.026 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[PLAUR]] | B | FAM107B activity raises PLAUR's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.90× lower at baseline in the lines without FAM107B | 0.027 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.2, -0.2); signed map (2.0, 44.9). **Vector** length 144, 45.4% of its response variance represented; |z| ≥ 3 in 1,614 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +5.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.4 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +10.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | +4.1 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +6.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.8 | -1.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.7 | +2.9 |
| fall | [[Clobetasol propionate (drug)]] 0.5 µM |  | -7.3 | -9.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -7.1 | -6.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -6.9 | -7.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -6.4 | -6.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -6.3 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 107 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:14,518,557-14,774,897 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45505, MGC11034, HITS; previously C10orf45 |
| Matched by | ensembl_id |

UniProt [Q9H098](https://www.uniprot.org/uniprotkb/Q9H098) carries no function annotation.

**Summary**, from NCBI Gene [83641](https://www.ncbi.nlm.nih.gov/gene/83641):

> Predicted to act upstream of or within sensory perception of sound. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23726) · Entrez [83641](https://www.ncbi.nlm.nih.gov/gene/83641) · UniProt [Q9H098](https://www.uniprot.org/uniprotkb/Q9H098) · Ensembl [ENSG00000065809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065809)

## Data

Gene col 805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 805); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 805]; `tensor/DDL_lfc|DDL_z.npy` [805]; `embed/gene_vectors.npy` [805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 805 or target_col == 805). Every well: [[FAM107B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM107B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
