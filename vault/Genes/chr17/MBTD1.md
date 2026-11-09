---
symbol: "MBTD1"
type: "gene"
col: 230
ensembl_id: "ENSG00000011258"
name: "mbt domain containing 1"
location: "17q21.33"
module: 156
arm: "+"
pooled_cpm: 137.58
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# MBTD1

*mbt domain containing 1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 2.41× (z +8.8, q 6e-16, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.655× (z -13.3, q 2e-37, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.608× (z -11.1, q 4e-26, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QRICH1]] (+0.63, fdr 1e-05), [[ZNF263]] (+0.62, fdr 9e-06), [[GPBP1L1]] (+0.61, fdr 1e-05); moves opposite to [[EFR3A]] (-0.55, fdr 5e-05), [[FLNC]] (-0.53, fdr 3e-05), [[OCRL]] (-0.51, fdr 3e-05).
> It is in [[Module 156]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +8.8 | 6e-16 | 38/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.5 | 3e-08 | 25/49 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.4 | 0.002 | 27/49 (NCI-H23, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | 1.13× | +4.0 | 0.009 | 15/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.086 | 19/49 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 1.37× | +3.2 | 0.12 | 12/49 (KATO III, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.12 | 7/48 (SW1417, hTERT-HPNE, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.12 | 11/48 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.12 | 10/48 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.36× | +3.1 | 0.12 | 13/50 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.12 | 10/49 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.0 | 0.12 | 20/48 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.655×** | -13.3 | 2e-37 | 36/48 (SW480, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.551×** | -13.2 | 2e-37 | 41/49 (SK-MEL-2, KATO III, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -11.1 | 4e-26 | 44/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.599×** | -11.0 | 9e-26 | 34/44 (CHP-212, KATO III, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -10.9 | 2e-25 | 43/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.615×** | -10.0 | 2e-21 | 39/45 (SW48, A-172, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.647×** | -9.3 | 1e-18 | 35/48 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.666×** | -9.0 | 2e-17 | 39/48 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.708×** | -7.4 | 1e-11 | 30/47 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.738×** | -6.7 | 1e-09 | 32/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -6.6 | 2e-09 | 35/48 (PANC-1, CFPAC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -6.5 | 5e-09 | 33/48 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.748×** | -6.4 | 6e-09 | 31/48 (H4, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.753×** | -6.3 | 1e-08 | 30/48 (SW 900, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.771×** | -5.8 | 3e-07 | 36/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.783×** | -5.0 | 2e-05 | 28/47 (A549, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.853× | -4.9 | 2e-05 | 18/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.801×** | -4.9 | 3e-05 | 26/48 (CFPAC-1, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.807×** | -4.5 | 2e-04 | 25/48 (MIA PaCa-2, NCI-H1792, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.651×** | -4.3 | 5e-04 | 27/48 (NCI-H1792, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.662×** | -4.1 | 1e-03 | 25/48 (SK-MEL-2, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.671×** | -4.0 | 0.002 | 27/48 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.892× | -3.6 | 0.008 | 3/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.817×** | -3.2 | 0.029 | 21/48 (NCI-H1792, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.879× | -2.8 | 0.079 | 12/47 (CFPAC-1, H4, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 173 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -20.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -13.0) |
| [[PANC-1 (line)]] | alt | 187 | 1 | 9 (7 ⚠) | [[PH-797804 (drug)]] 5 µM 3.63× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.498× (z -11.0) |
| [[SW 900 (line)]] | alt | 138 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -18.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -14.5) |
| [[A-172 (line)]] | wt | 122 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.408× (z -11.2) |
| [[A498 (line)]] | wt | 120 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.363× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 177 | 1 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.32× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 196 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.434× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 181 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.88× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.514× (z -9.7) |
| [[C32 (line)]] | wt | 90.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -13.2) |
| [[COLO 205 (line)]] | alt | 184 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 171 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.449× (z -11.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.495× (z -10.2) |
| [[HOP62 (line)]] | alt | 173 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -11.4) |
| [[KATO III (line)]] | alt | 215 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H1792 (line)]] | alt | 147 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -15.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.488× (z -10.2) |
| [[SNU-423 (line)]] | alt | 171 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -11.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.471× (z -8.7) |
| [[CHP-212 (line)]] | wt | 350 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0360× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 188 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 84.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -11.2) |
| [[SW1417 (line)]] | alt | 129 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 168 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.522× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 94.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.387× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 148 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 104 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.383× (z -10.4) |
| [[SW48 (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0726× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.512× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 121 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.8) | — |
| [[LoVo (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.551× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 87.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.430× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 159 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 116 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -17.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF263]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[GPBP1L1]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ING4]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[CDK13]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ZNF75D]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[APPBP2]] | +0.59 | +0.49 / +0.62 | both halves | 2e-05 |  |
| [[ZNF394]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PRPF40B]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ILF3-DT]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TRUB2]] | +0.56 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[PDPR]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFR3A]] | -0.55 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[FLNC]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[OCRL]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ALAS1]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[DNAJB5]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TFE3]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CSRP1]] | -0.48 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[TRIM68]] | -0.48 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TACC1]] | -0.47 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[DUSP8]] | -0.47 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[RALB]] | -0.46 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[RFK]] | -0.46 | -0.37 / -0.54 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.5, -10.0); signed map (-2.5, -2.4). **Vector** length 121, 41.0% of its response variance represented; |z| ≥ 3 in 1,203 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.7 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +9.3 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -0.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.1 | +3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.3 | -13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -9.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mbt domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:51,177,425-51,260,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SA49P01, FLJ20055 |
| Gene groups (HGNC) | MBT domain containing; Tip60/Nua4 histone acetyltransferase complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05BQ5](https://www.uniprot.org/uniprotkb/Q05BQ5) (MBT domain-containing protein 1):

> Chromatin reader component of the NuA4 histone acetyltransferase complex, a multiprotein complex involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. The NuA4 complex plays a direct role in repair of DNA double-strand breaks (DSBs) by promoting homologous recombination (HR). MBTD1 specifically recognizes and binds monomethylated and dimethylated 'Lys-20' on histone H4 (H4K20me1 and H4K20me2, respectively). In the NuA4 complex, …

**Summary**, from NCBI Gene [54799](https://www.ncbi.nlm.nih.gov/gene/54799):

> Enables NuA4 histone acetyltransferase complex binding activity; histone H4K20me1 reader activity; and histone H4K20me2 reader activity. Involved in double-strand break repair via homologous recombination; positive regulation of double-strand break repair via homologous recombination; and regulation of cell cycle. Located in nucleoplasm. Part of NuA4 histone acetyltransferase complex. Is active in site of double-strand break. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19866) · Entrez [54799](https://www.ncbi.nlm.nih.gov/gene/54799) · UniProt [Q05BQ5](https://www.uniprot.org/uniprotkb/Q05BQ5) · Ensembl [ENSG00000011258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011258)

## Data

Gene col 230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 230); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 230]; `tensor/DDL_lfc|DDL_z.npy` [230]; `embed/gene_vectors.npy` [230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 230 or target_col == 230). Every well: [[MBTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
