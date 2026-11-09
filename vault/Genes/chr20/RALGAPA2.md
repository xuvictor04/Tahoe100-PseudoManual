---
symbol: "RALGAPA2"
type: "gene"
col: 12024
ensembl_id: "ENSG00000188559"
name: "Ral GTPase activating protein catalytic subunit alpha 2"
location: "20p11.23"
module: 83
arm: "-"
pooled_cpm: 228.24
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# RALGAPA2

*Ral GTPase activating protein catalytic subunit alpha 2* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +15.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.446× (z -22.6, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.365× (z -20.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC2A3]] (+0.69, fdr 1e-05), [[KIAA1958]] (+0.68, fdr 1e-05), [[LIFR]] (+0.66, fdr 4e-05); moves opposite to [[PBLD]] (-0.70, fdr 3e-05), [[MAD2L1-DT]] (-0.64, fdr 6e-04), [[MAILR]] (-0.64, fdr 8e-04, ⚠ one half only (not replicated)), [[ANXA2R-OT1]] (-0.64, fdr 3e-04).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +15.1 | 0e+00 | 43/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +11.9 | 2e-30 | 40/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +11.0 | 6e-26 | 38/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.5 | 1e-11 | 34/48 (HS-578T, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.7 | 2e-09 | 34/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +5.6 | 2e-06 | 34/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +4.4 | 1e-03 | 29/49 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.047 | 18/50 (SHP-77, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.11 | 21/47 (AsPC-1, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.446×** | -22.6 | 0e+00 | 44/48 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.365×** | -20.7 | 0e+00 | 48/48 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -19.9 | 0e+00 | 48/49 (HepG2/C3A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.388×** | -19.4 | 0e+00 | 45/49 (COLO 205, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.393×** | -17.7 | 0e+00 | 43/45 (HepG2/C3A, C32, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.458×** | -15.4 | 0e+00 | 45/48 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -14.9 | 0e+00 | 40/44 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.493×** | -13.9 | 3e-42 | 42/47 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -10.1 | 2e-22 | 40/48 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -9.9 | 3e-21 | 41/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -8.3 | 6e-15 | 34/48 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -8.1 | 4e-14 | 40/49 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.678×** | -7.7 | 8e-13 | 36/47 (C32, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.694×** | -7.5 | 3e-12 | 38/48 (HepG2/C3A, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -7.4 | 4e-12 | 35/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -6.4 | 5e-09 | 36/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -5.8 | 2e-07 | 32/48 (MIA PaCa-2, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.754×** | -5.8 | 2e-07 | 32/48 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.5 | 1e-06 | 32/50 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.820×** | -5.4 | 2e-06 | 26/48 (A-172, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.9 | 2e-05 | 30/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.788×** | -4.9 | 2e-05 | 31/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.797×** | -4.6 | 7e-05 | 27/47 (SW480, SNU-423, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 397 | 18 | 5 (3 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.19× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 188 | 1 | 18 (13 ⚠) | [[Panobinostat (drug)]] 5 µM 2.08× (z +9.9) | [[Harringtonine (drug)]] 0.5 µM 0.179× (z -23.3) |
| [[HepG2_C3A (line)]] | wt | 1,020 | 0 | 18 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -29.8) |
| [[LOX-IMVI (line)]] | wt | 232 | 1 | 17 (11 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -22.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -22.0) |
| [[SNU-423 (line)]] | alt | 279 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -32.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -22.5) |
| [[SW480 (line)]] | alt | 255 | 3 | 15 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +16.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -18.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -17.7) |
| [[C32 (line)]] | wt | 271 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -20.0) |
| [[KATO III (line)]] | alt | 631 | 0 | 16 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -21.4) |
| [[HS-578T (line)]] | alt | 202 | 7 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +17.6) | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -18.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 242 | 0 | 15 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -18.4) |
| [[A-172 (line)]] | wt | 197 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -25.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -17.4) |
| [[A549 (line)]] | wt | 179 | 3 | 10 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -30.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -24.0) |
| [[SW1417 (line)]] | alt | 294 | 4 | 9 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 147 | 9 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 344 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -26.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -19.8) |
| [[J82 (line)]] | alt | 129 | 3 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -25.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 228 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -20.5) |
| [[SK-MEL-2 (line)]] | alt | 215 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -22.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -19.6) |
| [[NCI-H1573 (line)]] | alt | 493 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -26.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -23.5) |
| [[RKO (line)]] | wt | 240 | 2 | 9 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.452× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 170 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.0858× (z -33.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -19.5) |
| [[NCI-H2347 (line)]] | alt | 147 | 4 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.7) |
| [[PANC-1 (line)]] | alt | 124 | 3 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +16.7) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -20.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -16.1) |
| [[SW 900 (line)]] | alt | 150 | 3 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -15.0) |
| [[COLO 205 (line)]] | alt | 615 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -20.0) |
| [[A-427 (line)]] | wt | 98.4 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +14.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.0492× (z -39.4) |
| [[HEC-1-A (line)]] | alt | 340 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -16.0) |
| [[Hs 766T (line)]] | wt | 135 | 3 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -15.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -12.8) |
| [[LS 180 (line)]] | wt | 357 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 196 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -14.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.7) |
| [[HCT15 (line)]] | alt | 282 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -9.6) |
| [[HOP62 (line)]] | alt | 96.3 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.07× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -18.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -15.0) |
| [[LoVo (line)]] | wt | 228 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 104 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.5) |
| [[A498 (line)]] | wt | 58.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.14× (z +20.0) | — |
| [[HT-29 (line)]] | alt | 264 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -16.7) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 84.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -10.1) |
| [[SNU-1 (line)]] | wt | 270 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -14.7) |
| [[H4 (line)]] | wt | 142 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.45× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 234 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.121× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 101 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 1088 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 224 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A3]] | +0.69 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[KIAA1958]] | +0.68 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[LIFR]] | +0.66 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[CLMN]] | +0.65 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[EFNA3]] | +0.63 | +0.62 / +0.36 | both halves | 1e-04 |  |
| [[SMYD3]] | +0.63 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[CFD]] | +0.62 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[CARHSP1]] | +0.61 | +0.57 / +0.31 | both halves | 2e-04 |  |
| [[RHPN2]] | +0.61 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[DUSP23]] | +0.61 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[NAA10]] ⚠ | +0.60 | +0.19 / +0.42 | ⚠ not reproduced | 8e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CABIN1]] | +0.60 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[PPP1CC]] | +0.60 | +0.48 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | -0.70 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[MAD2L1-DT]] | -0.64 | -0.51 / -0.22 | both halves | 6e-04 |  |
| [[MAILR]] | -0.64 | -0.52 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ANXA2R-OT1]] | -0.64 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[CSTF3]] | -0.63 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[FIZ1]] | -0.63 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[PCNX4-DT]] | -0.62 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[VPS52]] | -0.62 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[LINC01829]] | -0.60 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[LRRC37A3]] | -0.60 | -0.46 / -0.21 | both halves | 7e-04 |  |
| [[PPP1R3F]] | -0.60 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[ATE1OSP]] | -0.60 | -0.49 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[ZNF621]] | -0.60 | -0.62 / -0.29 | both halves | 3e-04 |  |
| [[ANKRD18B]] | -0.59 | -0.47 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RALGAPA2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RALGAPA2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RALGAPA2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SPATA13]] | C | SPATA13 activity lowers RALGAPA2's level | lines that do not express SPATA13 (4) vs lines expressing it (46) | 1.49× higher at baseline in the lines without SPATA13 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: YBX3, ZNF513, RNF32-DT; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.8, -12.4); signed map (-35.4, 28.1). **Vector** length 118, 45.9% of its response variance represented; |z| ≥ 3 in 1,764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +10.5 | +15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +10.0 | +11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.0 | +11.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.5 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.0 | +0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -19.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.8 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.3 | -20.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.0 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | Ral GTPase activating protein catalytic subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:20,389,530-20,712,644 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1049G11.4, AS250, KIAA1272, RapGAPalpha2; previously C20orf74 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 3 pathways, smallest: Translocation of SLC2A4 (GLUT4) to the plasma membrane; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2PPJ7](https://www.uniprot.org/uniprotkb/Q2PPJ7) (Ral GTPase-activating protein subunit alpha-2):

> Catalytic subunit of the heterodimeric RalGAP2 complex which acts as a GTPase activator for the Ras-like small GTPases RALA and RALB.

**Summary**, from NCBI Gene [57186](https://www.ncbi.nlm.nih.gov/gene/57186):

> Predicted to enable GTPase activator activity and protein heterodimerization activity. Predicted to be involved in activation of GTPase activity. Predicted to act upstream of or within Ral protein signal transduction; regulation of exocyst localization; and regulation of protein localization. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16207) · Entrez [57186](https://www.ncbi.nlm.nih.gov/gene/57186) · UniProt [Q2PPJ7](https://www.uniprot.org/uniprotkb/Q2PPJ7) · Ensembl [ENSG00000188559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188559)

## Data

Gene col 12024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12024); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12024]; `tensor/DDL_lfc|DDL_z.npy` [12024]; `embed/gene_vectors.npy` [12024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12024 or target_col == 12024). Every well: [[RALGAPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALGAPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
