---
symbol: "EZR"
type: "gene"
col: 1707
ensembl_id: "ENSG00000092820"
name: "ezrin"
location: "6q25.3"
module: 31
arm: "+"
pooled_cpm: 546.13
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 30
direction_downstream: 17
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# EZR

*ezrin* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +12.8, q 7e-35, up in 32 of 45 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.64× (z +8.6, q 2e-15, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.609× (z -12.2, q 1e-31, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF2]] (+0.73, fdr 7e-06), [[RHOB]] (+0.63, fdr 1e-05), [[LMO7]] (+0.63, fdr 7e-06); moves opposite to [[LINC01139]] (-0.56, fdr 2e-05), [[TRAPPC13]] (-0.56, fdr 3e-05), [[SNRNP40]] (-0.55, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[MISP]] → it (grade B ⚠); 17 go from it, the strongest it → cells under [[Sonidegib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.68×** | +12.8 | 7e-35 | 32/45 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.64×** | +8.6 | 2e-15 | 33/44 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.56×** | +7.4 | 2e-11 | 32/44 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.2 | 6e-08 | 27/46 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.43×** | +6.0 | 2e-07 | 25/45 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.41×** | +6.0 | 2e-07 | 32/45 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +4.8 | 2e-04 | 21/45 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +4.5 | 4e-04 | 25/45 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 4e-04 | 26/45 (MIA PaCa-2, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.3 | 9e-04 | 18/45 (HepG2/C3A, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **1.29×** | +4.3 | 9e-04 | 22/41 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.27×** | +4.2 | 0.002 | 22/45 (SNU-1, A-427, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.006 | 22/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.009 | 18/45 (MIA PaCa-2, SHP-77, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.010 | 19/45 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.049 | 20/44 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.072 | 20/45 (SK-MEL-2, A-427, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.079 | 16/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -12.2 | 1e-31 | 36/46 (SW48, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -5.8 | 2e-06 | 33/45 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.725×** | -5.6 | 4e-06 | 32/45 (HCT15, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.727×** | -5.3 | 1e-05 | 28/44 (SW48, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -5.2 | 2e-05 | 25/45 (SW48, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.811×** | -5.2 | 2e-05 | 24/45 (SW48, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.748×** | -5.1 | 3e-05 | 33/45 (LoVo, HCT15, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -4.4 | 1e-03 | 26/47 (SW48, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.800×** | -3.9 | 0.006 | 24/45 (SW48, SNU-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.857× | -3.8 | 0.008 | 10/45 (SW480, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.863× | -3.6 | 0.015 | 19/45 (SW48, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.034 | 23/45 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.871× | -3.4 | 0.034 | 17/45 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.813×** | -3.3 | 0.034 | 21/45 (HCT15, LoVo, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.056 | 19/45 (SW48, HOP62, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.840× | -3.0 | 0.075 | 15/45 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.845× | -2.9 | 0.097 | 19/45 (SW 900, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 1,011 | 4 (3 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +12.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.94× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -28.0) |
| [[SNU-1 (line)]] | wt | 1,110 | 5 (4 ⚠) | 5 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.45× (z +15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.43× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -15.5) |
| [[SW48 (line)]] | wt | 1,352 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -29.2) |
| [[A-427 (line)]] | wt | 421 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +20.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.43× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 1,791 | 3 (3 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.7) ⚠ cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -23.3) |
| [[SK-MEL-2 (line)]] | alt | 330 | 5 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +11.5) | [[Selinexor (drug)]] 5 µM 0.589× (z -10.2) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.6) |
| [[HOP62 (line)]] | alt | 208 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +18.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.67× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 1,209 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 1,132 | 2 (1 ⚠) | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.11× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -24.0) |
| [[PANC-1 (line)]] | alt | 243 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +22.9) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HCT15 (line)]] | alt | 791 | 3 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.51× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -16.6) |
| [[LS 180 (line)]] | wt | 921 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.4) |
| [[RKO (line)]] | wt | 223 | 4 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.01× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.3) |
| [[SNU-423 (line)]] | alt | 300 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.28× (z +9.5) | — |
| [[A549 (line)]] | wt | 380 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.8) ⚠ cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -14.7) |
| [[Hs 766T (line)]] | wt | 634 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -14.5) |
| [[LoVo (line)]] | wt | 1,206 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -20.0) |
| [[NCI-H2030 (line)]] | alt | 276 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +12.3) | — |
| [[NCI-H460 (line)]] | wt | 527 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.4) ⚠ cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -16.6) |
| [[SW1417 (line)]] | alt | 1,012 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -24.9) |
| [[A498 (line)]] | wt | 140 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[CFPAC-1 (line)]] | alt | 1,047 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 161 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.48× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 164 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.77× (z +9.5) | — |
| [[SW480 (line)]] | alt | 894 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -16.1) |
| [[BT-474 (line)]] | alt | 384 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -15.2) |
| [[J82 (line)]] | alt | 236 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 1,148 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 261 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +16.2) ⚠ cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 538 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.0) |
| [[SHP-77 (line)]] | alt | 145 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.02× (z +10.7) | — |
| [[A-172 (line)]] | wt | 308 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.13× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 685 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 532 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -17.5) |
| [[HepG2_C3A (line)]] | wt | 195 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 196 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H1573 (line)]] | alt | 409 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.3) |
| [[AN3 CA (line)]] | alt | 325 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 133 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 98.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 139 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 115 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 659 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 488 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 292 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF2]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[RHOB]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LMO7]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ANXA2]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 | STRING 725 |
| [[SPTAN1]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 655 |
| [[RDH13]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MISP]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 | STRING 582 |
| [[TES]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PPL]] | +0.59 | +0.47 / +0.51 | both halves | 2e-05 | STRING 957 |
| [[KLF5]] | +0.59 | +0.57 / +0.59 | both halves | 8e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01139]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TRAPPC13]] | -0.56 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SNRNP40]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[C2orf42]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[FBXO22]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[DHX35]] | -0.53 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[STARD7-AS1]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZCCHC4]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MIR762HG]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[FAHD2A]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[COA6]] | -0.50 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CDC23]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 30, C 0. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MISP]] | B | MISP activity raises EZR's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without MISP | 1e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[ANXA3]] | B | ANXA3 activity raises EZR's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 2.93× lower at baseline in the lines without ANXA3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[ITGB4]] | B | ITGB4 activity raises EZR's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.01× lower at baseline in the lines without ITGB4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[C1orf116]] | B | C1orf116 activity raises EZR's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.39× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MYO5B]] | B | MYO5B activity raises EZR's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[KRT19]] | B | KRT19 activity raises EZR's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.78× lower at baseline in the lines without KRT19 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[CDH1]] | B | CDH1 activity raises EZR's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[SH2D3A]] | B | SH2D3A activity raises EZR's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[GPRC5A]] | B | GPRC5A activity raises EZR's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.99× lower at baseline in the lines without GPRC5A | 0.004 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[PCDH1]] | B | PCDH1 activity raises EZR's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without PCDH1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[CLDN4]] | B | CLDN4 activity raises EZR's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.64× lower at baseline in the lines without CLDN4 | 0.007 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[SULT2B1]] | B | SULT2B1 activity raises EZR's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.64× lower at baseline in the lines without SULT2B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Sonidegib (drug)]] 5 µM | C | EZR, [[TMC7]] activity raises the cells' numbers under Sonidegib 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.69× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| [[PARD6B]] | C | EZR, [[TMC7]] activity raises PARD6B's level | lines that do not express EZR, TMC7 (3) vs lines expressing them (47) | 4.35× lower at baseline in the lines without EZR, TMC7 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[DTP3 (drug)]] 5 µM | C | EZR, [[TMC7]] activity raises the cells' numbers under DTP3 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.61× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Peretinoin (drug)]] 5 µM | C | EZR, [[TMC7]] activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.72× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Daptomycin (drug)]] 0.5 µM | C | EZR, [[TMC7]] activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.63× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; cell counts less trustworthy; co-absent genes |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | C | EZR, [[TMC7]] activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.70× the cells of the other lines | 0.039 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| [[TUFT1]] | C | EZR activity raises TUFT1's level | lines that do not express EZR (3) vs lines expressing it (47) | 3.86× lower at baseline in the lines without EZR | 0.040 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent |
| cells under [[Pasireotide (acetate) (drug)]] 5 µM | C | EZR, [[TMC7]] activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.81× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Artesunate (drug)]] 0.5 µM | C | EZR, [[TMC7]] activity lowers the cells' numbers under Artesunate 0.5 µM (makes them more sensitive) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 1.29× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[vincristine (drug)]] 5 µM | C | EZR, [[TMC7]] activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.53× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | EZR, [[TMC7]] activity lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 1.33× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| [[CYSTM1]] | C | EZR activity raises CYSTM1's level | lines that do not express EZR (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without EZR | 0.082 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.3, 57.8); signed map (-0.2, 23.8). **Vector** length 151, 52.1% of its response variance represented; |z| ≥ 3 in 1,616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +7.1 | +12.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +6.5 | +8.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.1 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.7 | +3.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -5.7 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | -5.0 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -4.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | -3.2 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | ezrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,765,741-158,819,368 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously VIL2 |
| Gene groups (HGNC) | A-kinase anchoring proteins; FERM domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 9 pathways, smallest: Netrin-1 signaling; Recycling pathway of L1; Sensory processing of sound by outer hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [P15311](https://www.uniprot.org/uniprotkb/P15311) (Ezrin):

> Probably involved in connections of major cytoskeletal structures to the plasma membrane. In epithelial cells, required for the formation of microvilli and membrane ruffles on the apical pole. Along with PLEKHG6, required for normal macropinocytosis.

**Summary**, from NCBI Gene [7430](https://www.ncbi.nlm.nih.gov/gene/7430):

> The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human cancers. A pseudogene located on chromosome 3 has been identified for this gene. Alternatively …

**Accessions** — [HGNC:12691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12691) · Entrez [7430](https://www.ncbi.nlm.nih.gov/gene/7430) · UniProt [P15311](https://www.uniprot.org/uniprotkb/P15311) · Ensembl [ENSG00000092820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092820)

## Data

Gene col 1707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1707); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1707]; `tensor/DDL_lfc|DDL_z.npy` [1707]; `embed/gene_vectors.npy` [1707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1707 or target_col == 1707). Every well: [[EZR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EZR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
