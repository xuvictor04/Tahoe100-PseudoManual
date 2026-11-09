---
symbol: "IP6K1"
type: "gene"
col: 10680
ensembl_id: "ENSG00000176095"
name: "inositol hexakisphosphate kinase 1"
location: "3p21.31"
module: 149
arm: "+"
pooled_cpm: 67.65
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# IP6K1

*inositol hexakisphosphate kinase 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.88× (z +15.4, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.350× (z -21.9, q 0e+00, down in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.783× (z -7.5, q 7e-12, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAU2]] (+0.69, fdr 7e-06), [[GPATCH8]] (+0.66, fdr 7e-06), [[SPOP]] (+0.64, fdr 7e-06); moves opposite to [[GLO1]] (-0.56, fdr 3e-05), [[METAP1]] (-0.54, fdr 3e-05), [[TFRC]] (-0.54, fdr 2e-05).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +15.4 | 0e+00 | 46/49 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +13.4 | 2e-38 | 37/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +9.7 | 4e-20 | 38/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +7.3 | 4e-11 | 32/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 2e-09 | 35/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 6e-04 | 24/48 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.021 | 23/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.031 | 12/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.034 | 8/50 (NCI-H460, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.050 | 17/48 (COLO 205, NCI-H460, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.063 | 18/47 (HEC-1-A, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.350×** | -21.9 | 0e+00 | 40/43 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.372×** | -21.4 | 0e+00 | 46/49 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -13.6 | 5e-40 | 42/45 (HepG2/C3A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.621×** | -10.3 | 7e-23 | 39/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.635×** | -9.9 | 7e-21 | 40/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -7.5 | 7e-12 | 32/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.750×** | -6.2 | 4e-08 | 30/48 (NCI-H1792, HepG2/C3A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.790×** | -4.9 | 6e-05 | 28/50 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.801×** | -4.8 | 9e-05 | 25/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.860× | -4.6 | 2e-04 | 22/49 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.811×** | -4.4 | 7e-04 | 22/47 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -4.3 | 8e-04 | 19/48 (NCI-H1792, H4, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.823×** | -4.2 | 0.001 | 23/49 (HCT15, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.826×** | -4.2 | 0.001 | 22/48 (CHP-212, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.708×** | -3.9 | 0.003 | 17/44 (SK-MEL-2, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.859× | -3.3 | 0.037 | 15/48 (SNU-423, SW 1271, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.863× | -3.2 | 0.046 | 12/48 (SW480, J82, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.816×** | -3.1 | 0.046 | 11/47 (SHP-77, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | 0.866× | -3.1 | 0.048 | 10/48 (HEC-1-A, LS 180, …) | top dose only | position effect removed |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 0.904× | -3.1 | 0.053 | 3/49 (HS-578T, AN3 CA, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.871× | -3.0 | 0.073 | 14/48 (COLO 205, NCI-H1792, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.073 | 13/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.872× | -2.9 | 0.095 | 19/48 (PANC-1, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 85.3 | 2 | 9 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 4.72× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.582× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 96.5 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -17.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 81.1 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.38× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -16.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 86.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0441× (z -25.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 59.3 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 96.6 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 61.2 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -14.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 139 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.86× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -15.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 66.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0597× (z -28.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 84.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0981× (z -23.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 76.7 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.21× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 71.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -19.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 55.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -15.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 68.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.87× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -13.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 66.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -10.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 57.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0489× (z -22.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 74.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -18.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 44.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.87× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 79.4 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.61× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -9.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[PANC-1 (line)]] | alt | 52.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -19.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 68.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -14.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 92.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -18.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 84.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -21.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 62.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0802× (z -26.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 59.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0628× (z -13.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 49.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.9) | — |
| [[H4 (line)]] | wt | 29.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.5) | [[AZD2858 (drug)]] 0.5 µM 0.0889× (z -9.8) ⚠ toxic |
| [[HCT15 (line)]] | alt | 65.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -17.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 42.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.01× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 48.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -10.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 72.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 67.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -15.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 75.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -12.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 78.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -14.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) | — |
| [[NCI-H661 (line)]] | alt | 74.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -21.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 84.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -17.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAU2]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[GPATCH8]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SPOP]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[NAA60]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[TRIM4]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PPP6R2]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RBX1]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[MTG2]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ZNF3]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLO1]] | -0.56 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[METAP1]] | -0.54 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[TFRC]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TPM3]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PAICS]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.8, 4.8); signed map (-3.8, -10.5). **Vector** length 106, 30.4% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +7.0 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +13.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +9.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.7 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.4 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | -5.0 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -21.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | inositol hexakisphosphate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,724,294-49,786,542 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0263; previously IHPK1 |
| Gene groups (HGNC) | Inositol hexakisphosphate kinase family |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 3 pathways, smallest: Synthesis of IPs in the nucleus; Synthesis of pyrophosphates in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92551](https://www.uniprot.org/uniprotkb/Q92551) (Inositol hexakisphosphate kinase 1):

> Converts inositol hexakisphosphate (InsP6) to diphosphoinositol pentakisphosphate (InsP7/PP-InsP5). Converts 1,3,4,5,6-pentakisphosphate (InsP5) to PP-InsP4.

**Summary**, from NCBI Gene [9807](https://www.ncbi.nlm.nih.gov/gene/9807):

> This gene encodes a member of the inositol phosphokinase family. The encoded protein may be responsible for the conversion of inositol hexakisphosphate (InsP6) to diphosphoinositol pentakisphosphate (InsP7/PP-InsP5). It may also convert 1,3,4,5,6-pentakisphosphate (InsP5) to PP-InsP4. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:18360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18360) · Entrez [9807](https://www.ncbi.nlm.nih.gov/gene/9807) · UniProt [Q92551](https://www.uniprot.org/uniprotkb/Q92551) · Ensembl [ENSG00000176095](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176095)

## Data

Gene col 10680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10680); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10680]; `tensor/DDL_lfc|DDL_z.npy` [10680]; `embed/gene_vectors.npy` [10680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10680 or target_col == 10680). Every well: [[IP6K1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IP6K1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
