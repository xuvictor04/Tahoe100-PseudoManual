---
symbol: "GNPTAB"
type: "gene"
col: 3257
ensembl_id: "ENSG00000111670"
name: "N-acetylglucosamine-1-phosphate transferase subunits alpha and beta"
location: "12q23.2"
module: 188
arm: "+"
pooled_cpm: 58.04
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# GNPTAB

*N-acetylglucosamine-1-phosphate transferase subunits alpha and beta* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.51× (z +13.9, q 6e-41, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Selinexor (drug)]] 0.05 µM: 1.64× (z +11.7, q 2e-29, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -19.1, q 0e+00, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.543× (z -14.5, q 4e-45, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDFIP1]] (+0.65, fdr 7e-06), [[SNX4]] (+0.61, fdr 1e-05), [[LTA4H]] (+0.61, fdr 1e-05); moves opposite to [[CFAP53]] (-0.62, fdr 1e-05), [[ALG13]] (-0.60, fdr 1e-05), [[SLC9A5]] (-0.60, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +13.9 | 6e-41 | 39/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.64×** | +11.7 | 2e-29 | 42/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.61×** | +10.6 | 4e-24 | 40/48 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.6 | 1e-15 | 32/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +7.0 | 4e-10 | 32/48 (C-33 A, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +6.7 | 1e-09 | 29/48 (SW 900, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +6.1 | 1e-07 | 25/48 (SNU-423, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +6.0 | 1e-07 | 27/48 (SW 900, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.8 | 3e-07 | 26/48 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +5.3 | 8e-06 | 20/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +5.3 | 8e-06 | 26/49 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +5.2 | 9e-06 | 20/48 (SW 900, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 3e-05 | 22/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.20× | +4.1 | 0.002 | 20/48 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.19× | +4.0 | 0.002 | 13/49 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.005 | 16/48 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.006 | 13/49 (SK-MEL-2, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.015 | 12/47 (Hs 766T, C32, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.2 | 0.036 | 9/48 (SK-MEL-2, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.566×** | -19.1 | 0e+00 | 37/48 (NCI-H2030, NCI-H23, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.543×** | -14.5 | 4e-45 | 42/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -9.1 | 3e-17 | 30/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -7.2 | 8e-11 | 25/48 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -7.2 | 8e-11 | 24/48 (SNU-423, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.789×** | -5.6 | 2e-06 | 21/47 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.796×** | -5.4 | 5e-06 | 27/47 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -5.3 | 1e-05 | 21/49 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -4.6 | 3e-04 | 19/47 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.831×** | -4.4 | 6e-04 | 16/48 (NCI-H1573, SW1417, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.827×** | -4.3 | 7e-04 | 21/44 (LS 180, NCI-H23, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.853× | -3.8 | 0.008 | 19/48 (NCI-H1573, SW 1271, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.859× | -3.6 | 0.012 | 20/48 (A549, RKO, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | 0.854× | -3.6 | 0.012 | 20/47 (SNU-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | 0.851× | -3.6 | 0.014 | 19/45 (SNU-1, HS-578T, …) | all doses, flat | composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | 0.867× | -3.3 | 0.040 | 11/48 (NCI-H2347, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 66.4 | 1 (1 ⚠) | 5 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.86× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -23.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 75.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -25.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -12.6) |
| [[A549 (line)]] | wt | 72.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -19.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 42.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -18.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.9) |
| [[PANC-1 (line)]] | alt | 74.8 | 2 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.62× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.81× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -20.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 87.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.60× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.297× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 68.6 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.397× (z -10.6) |
| [[LoVo (line)]] | wt | 70.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -22.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.445× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 57.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -18.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -12.5) |
| [[BT-474 (line)]] | alt | 40.3 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.47× (z +8.6) | — |
| [[C32 (line)]] | wt | 77.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -11.7) |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -9.6) |
| [[HS-578T (line)]] | alt | 48.7 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -10.1) ⚠ toxic |
| [[J82 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.3) |
| [[LS 180 (line)]] | wt | 69.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.82× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.0584× (z -33.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 68.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -21.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 80.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -25.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.451× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -10.0) |
| [[SNU-1 (line)]] | wt | 71.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.335× (z -8.8) |
| [[A-172 (line)]] | wt | 39.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.182× (z -8.8) |
| [[H4 (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 57.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.92× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H596 (line)]] | alt | 54.5 | 1 | 0 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 3.56× (z +16.3) | — |
| [[SK-MEL-2 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -13.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 68.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.478× (z -9.2) |
| [[SW48 (line)]] | wt | 70.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 59.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.374× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDFIP1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SNX4]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TM7SF3]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CROT]] | +0.61 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[FAR1]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RAB4A]] | +0.60 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[EXD2]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[STX7]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[C1orf115]] | +0.60 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[TMOD2]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[GRB14]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP53]] | -0.62 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[ALG13]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[SLC9A5]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ZCWPW2]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SCIRT]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TUT7]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[TTC41P]] | -0.58 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[LINC02936]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[C1S]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[LINC01422]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GNPTAB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.1, -6.7); signed map (-33.0, -13.4). **Vector** length 113, 29.1% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +13.4 | +13.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +8.6 | +10.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.0 | +11.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +7.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.3 | -14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.5 | -19.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -7.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylglucosamine-1-phosphate transferase subunits alpha and beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:101,745,499-101,830,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1208, MGC4170; previously GNPTA |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3T906](https://www.uniprot.org/uniprotkb/Q3T906) (N-acetylglucosamine-1-phosphotransferase subunits alpha/beta):

> Catalyzes the formation of mannose 6-phosphate (M6P) markers on high mannose type oligosaccharides in the Golgi apparatus. M6P residues are required to bind to the M6P receptors (MPR), which mediate the vesicular transport of lysosomal enzymes to the endosomal/prelysosomal compartment.

**Summary**, from NCBI Gene [79158](https://www.ncbi.nlm.nih.gov/gene/79158):

> This gene encodes two of three subunit types of the membrane-bound enzyme N-acetylglucosamine-1-phosphotransferase, a heterohexameric complex composed of two alpha, two beta, and two gamma subunits. The encoded protein is proteolytically cleaved at the Lys928-Asp929 bond to yield mature alpha and beta polypeptides while the gamma subunits are the product of a distinct gene (GeneID 84572). In the Golgi apparatus, the heterohexameric complex catalyzes the first step in the synthesis of mannose …

**Accessions** — [HGNC:29670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29670) · Entrez [79158](https://www.ncbi.nlm.nih.gov/gene/79158) · UniProt [Q3T906](https://www.uniprot.org/uniprotkb/Q3T906) · Ensembl [ENSG00000111670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111670)

## Data

Gene col 3257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3257); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3257]; `tensor/DDL_lfc|DDL_z.npy` [3257]; `embed/gene_vectors.npy` [3257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3257 or target_col == 3257). Every well: [[GNPTAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNPTAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
