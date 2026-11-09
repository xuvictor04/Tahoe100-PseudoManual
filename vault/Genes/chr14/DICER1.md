---
symbol: "DICER1"
type: "gene"
col: 2011
ensembl_id: "ENSG00000100697"
name: "dicer 1, ribonuclease III"
location: "14q32.13"
module: 1
arm: "+"
pooled_cpm: 125.67
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DICER1

*dicer 1, ribonuclease III* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.99× (z +13.2, q 6e-37, up in 41 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H460 3.07×, HT-29 2.40×, NCI-H2030 1.55×, SW48 1.82×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 2.43×, Panc 03.27 3.23×, BT-474 3.83×, NCI-H460 2.40×); [[PH-797804 (drug)]] 5 µM in 3 lines (SW480 2.22×, MIA PaCa-2 3.23×, RKO 3.15×); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (NCI-H460 1.72×, MIA PaCa-2 1.79×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.586× (z -19.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMAD1]] (+0.64, fdr 1e-05), [[KLHL42]] (+0.60, fdr 3e-05), [[PAIP1]] (+0.60, fdr 1e-05); moves opposite to [[MKNK1]] (-0.57, fdr 1e-05), [[LMTK3]] (-0.53, fdr 6e-05), [[MAGT1]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2011.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H460 3.07×, HT-29 2.40×, NCI-H2030 1.55×, SW48 1.82×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 2.43×, Panc 03.27 3.23×, BT-474 3.83×, NCI-H460 2.40×); [[PH-797804 (drug)]] 5 µM in 3 lines (SW480 2.22×, MIA PaCa-2 3.23×, RKO 3.15×); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (NCI-H460 1.72×, MIA PaCa-2 1.79×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +13.2 | 6e-37 | 41/49 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +8.5 | 5e-15 | 33/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +7.8 | 2e-12 | 27/47 (LoVo, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +7.3 | 3e-11 | 24/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.1 | 1e-10 | 20/38 (PANC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +7.0 | 2e-10 | 16/49 (LoVo, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.20× | +6.4 | 2e-08 | 24/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +5.7 | 7e-07 | 22/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +4.5 | 4e-04 | 19/45 (C-33 A, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.09× | +4.4 | 7e-04 | 16/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +4.0 | 0.003 | 8/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.11× | +3.8 | 0.007 | 13/48 (MIA PaCa-2, NCI-H2030, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.10× | +3.6 | 0.013 | 12/48 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.10× | +3.5 | 0.016 | 9/47 (LoVo, SW480, …) | all doses, flat |  |
| [[Infigratinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.028 | 11/48 (NCI-H1792, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.054 | 15/48 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.06× | +3.1 | 0.054 | 5/49 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.08× | +3.0 | 0.089 | 10/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | 1.17× | +3.0 | 0.090 | 11/48 (MIA PaCa-2, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.586×** | -19.6 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.601×** | -18.7 | 0e+00 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.680×** | -14.2 | 2e-43 | 43/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -8.4 | 6e-15 | 21/48 (SW480, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -8.3 | 8e-15 | 28/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.838× | -6.5 | 7e-09 | 22/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -5.1 | 2e-05 | 17/49 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.909× | -5.0 | 5e-05 | 13/48 (SNU-1, HOP62, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.810×** | -4.0 | 0.003 | 20/45 (SNU-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.967× | -4.0 | 0.004 | 0/50 | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.904× | -3.7 | 0.010 | 8/49 (C32, NCI-H2347, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.05 µM |  | 0.908× | -3.3 | 0.045 | 8/47 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[SBI-0640756 (drug)]] 5 µM |  | 0.844× | -3.3 | 0.048 | 14/48 (LoVo, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 0.848× | -3.2 | 0.063 | 17/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.919× | -3.1 | 0.069 | 10/48 (BT-474, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 236 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -19.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.408× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 131 | 7 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +30.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.72× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.431× (z -16.1) |
| [[LoVo (line)]] | wt | 131 | 4 (4 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.416× (z -16.5) |
| [[BT-474 (line)]] | alt | 288 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.83× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 167 | 3 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.11× (z +11.0) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 3.23× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.422× (z -12.7) |
| [[SW480 (line)]] | alt | 150 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.43× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -20.6) |
| [[A549 (line)]] | wt | 152 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.407× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 156 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.461× (z -14.2) |
| [[J82 (line)]] | alt | 140 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.481× (z -12.4) |
| [[RKO (line)]] | wt | 154 | 1 | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.15× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.496× (z -10.3) |
| [[SHP-77 (line)]] | alt | 126 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.466× (z -11.5) |
| [[LS 180 (line)]] | wt | 153 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.450× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 154 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.23× (z +9.7) | [[Lonafarnib (drug)]] 5 µM 0.300× (z -9.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.563× (z -9.0) |
| [[SW1417 (line)]] | alt | 122 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -14.8) |
| [[SW48 (line)]] | wt | 189 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.24× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.491× (z -10.9) |
| [[A498 (line)]] | wt | 78.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[COLO 205 (line)]] | alt | 91.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HT-29 (line)]] | alt | 94.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.2) ⚠ cell-cycle shift, explains ~45% of this change | [[Auranofin (drug)]] 5 µM 0.413× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -16.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.519× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.537× (z -11.4) |
| [[AN3 CA (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[C-33 A (line)]] | alt | 85.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.22× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 90.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.648× (z -9.6) |
| [[HS-578T (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.624× (z -8.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 94.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.483× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.644× (z -9.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H2030 (line)]] | alt | 201 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +11.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H23 (line)]] | alt | 88.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.10× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -9.2) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -12.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-1 (line)]] | wt | 139 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.462× (z -12.4) |
| [[SW 900 (line)]] | alt | 128 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.536× (z -8.7) |
| [[A-427 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 130 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD1]] | +0.64 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.60 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[PAIP1]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 | pathway: M-decay: degradation of maternal mRNAs by maternally stored factors |
| [[NUDT19]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RBM17]] | +0.57 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CCNJ]] | +0.57 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[USP46]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[TDRD3]] | +0.56 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[CCT6P1]] | +0.55 | +0.57 / +0.33 | both halves | 1e-04 |  |
| [[OTUD4]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ZFR]] | +0.55 | +0.46 / +0.45 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK1]] | -0.57 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[LMTK3]] | -0.53 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[MAGT1]] | -0.52 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[VRK3]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[VMP1]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 | same gene group |
| [[ATG2A]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 | same gene group |
| [[GIPR]] | -0.50 | -0.37 / -0.46 | both halves | 8e-05 | same gene group |
| [[GP6-AS1]] | -0.50 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PLEKHO2]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[WDR26]] | -0.49 | -0.51 / -0.46 | both halves | 2e-05 | same gene group |
| [[TMEM92]] | -0.49 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[POFUT2]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DICER1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.8, 10.6); signed map (22.2, -37.8). **Vector** length 106, 26.3% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.0 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.9 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +8.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -18.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -19.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -8.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.7 | -4.0 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | dicer 1, ribonuclease III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.13 — chr14:95,086,228-95,158,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Dicer, KIAA0928, K12H4.8-LIKE, HERNA; previously MNG1 |
| Gene groups (HGNC) | Endoribonucleases; MicroRNA protein coding host genes; RISC loading complex subunits |
| Reactome | 9 pathways, smallest: tRNA-derived small RNA (tsRNA or tRNA-related fragment, tRF) biogenesis; Small interfering RNA (siRNA) biogenesis; Regulation of MITF-M-dependent genes involved in apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPY3](https://www.uniprot.org/uniprotkb/Q9UPY3) (Endoribonuclease Dicer):

> Double-stranded RNA (dsRNA) endoribonuclease playing a central role in short dsRNA-mediated post-transcriptional gene silencing. Cleaves naturally occurring long dsRNAs and short hairpin pre-microRNAs (miRNA) into fragments of twenty-one to twenty-three nucleotides with 3' overhang of two nucleotides, producing respectively short interfering RNAs (siRNA) and mature microRNAs. SiRNAs and miRNAs serve as guide to direct the RNA-induced silencing complex (RISC) to complementary RNAs to degrade …

**Summary**, from NCBI Gene [23405](https://www.ncbi.nlm.nih.gov/gene/23405):

> This gene encodes a protein possessing an RNA helicase motif containing a DEXH box in its amino terminus and an RNA motif in the carboxy terminus. The encoded protein functions as a ribonuclease and is required by the RNA interference and small temporal RNA (stRNA) pathways to produce the active small RNA component that represses gene expression. This protein also acts as a strong antiviral agent with activity against RNA viruses, including the Zika and SARS-CoV-2 viruses. Alternative splicing …

**Accessions** — [HGNC:17098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17098) · Entrez [23405](https://www.ncbi.nlm.nih.gov/gene/23405) · UniProt [Q9UPY3](https://www.uniprot.org/uniprotkb/Q9UPY3) · Ensembl [ENSG00000100697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100697)

## Data

Gene col 2011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2011); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2011]; `tensor/DDL_lfc|DDL_z.npy` [2011]; `embed/gene_vectors.npy` [2011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2011 or target_col == 2011). Every well: [[DICER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DICER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
