---
symbol: "KMT2C"
type: "gene"
col: 628
ensembl_id: "ENSG00000055609"
name: "lysine methyltransferase 2C"
location: "7q36.1"
module: 5
arm: "-"
pooled_cpm: 619.8
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KMT2C

*lysine methyltransferase 2C* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +18.3, q 0e+00, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.430× (z -20.0, q 0e+00, down in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.589× (z -13.1, q 7e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKAP2]] (+0.62, fdr 1e-05), [[HCFC1R1]] (+0.59, fdr 3e-05), [[CRIP2]] (+0.58, fdr 2e-05); moves opposite to [[TRNT1]] (-0.59, fdr 2e-05), [[UBIAD1]] (-0.59, fdr 1e-05), [[DCTD]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +18.3 | 0e+00 | 35/48 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +9.9 | 1e-20 | 49/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +9.1 | 3e-17 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +6.2 | 8e-08 | 31/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +6.1 | 2e-07 | 30/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 1e-06 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +5.4 | 5e-06 | 33/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 1e-04 | 26/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 37/48 (CFPAC-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.16× | +3.6 | 0.015 | 20/50 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.16× | +3.5 | 0.023 | 17/47 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.066 | 8/48 (SK-MEL-2, HCT15, …) | rises with dose | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.1 | 0.080 | 11/49 (SNU-423, J82, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.080 | 22/48 (A549, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 628.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.430×** | -20.0 | 0e+00 | 47/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -19.4 | 0e+00 | 44/44 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -19.2 | 0e+00 | 48/49 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.537×** | -14.2 | 2e-43 | 45/45 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.589×** | -13.1 | 7e-37 | 47/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -12.7 | 6e-35 | 39/49 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.777×** | -8.8 | 2e-16 | 31/48 (HS-578T, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.767×** | -6.5 | 5e-09 | 35/48 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.767×** | -6.5 | 5e-09 | 31/48 (BT-474, SW 900, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -5.8 | 4e-07 | 21/48 (AN3 CA, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.794×** | -5.7 | 7e-07 | 29/48 (NCI-H1792, NCI-H2347, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.787×** | -5.7 | 7e-07 | 31/50 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -5.3 | 6e-06 | 0/50 | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.869× | -4.9 | 4e-05 | 3/48 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.826×** | -4.5 | 3e-04 | 25/48 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -3.7 | 0.006 | 21/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.853× | -3.6 | 0.010 | 18/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.865× | -3.4 | 0.018 | 15/48 (J82, NCI-H1792, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.870× | -3.4 | 0.018 | 9/48 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.862× | -3.4 | 0.019 | 14/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.913× | -3.1 | 0.042 | 7/48 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.881× | -3.1 | 0.043 | 13/48 (NCI-H1573, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 779 | 11 (5 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +24.2) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -9.9) |
| [[SW480 (line)]] | alt | 612 | 8 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +18.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.459× (z -15.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 660 | 4 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +20.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -17.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 615 | 1 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -22.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -17.7) |
| [[LS 180 (line)]] | wt | 597 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.600× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 478 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -17.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -10.7) |
| [[PANC-1 (line)]] | alt | 444 | 6 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +25.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.524× (z -12.9) ⚠ toxic |
| [[RKO (line)]] | wt | 726 | 7 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +24.0) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.532× (z -9.6) |
| [[SW 900 (line)]] | alt | 714 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +15.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -18.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.515× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 608 | 2 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.408× (z -15.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -14.5) |
| [[HOP62 (line)]] | alt | 528 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -14.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.454× (z -11.9) |
| [[SW1417 (line)]] | alt | 935 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +19.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -21.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.507× (z -12.6) |
| [[SW48 (line)]] | wt | 806 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 884 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.400× (z -17.8) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -13.7) |
| [[C32 (line)]] | wt | 1,437 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.63× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.559× (z -12.9) |
| [[HT-29 (line)]] | alt | 1,012 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +16.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -19.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.495× (z -11.4) |
| [[KATO III (line)]] | alt | 650 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +18.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -17.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.522× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 839 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -22.6) |
| [[A549 (line)]] | wt | 483 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +18.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -19.7) |
| [[AsPC-1 (line)]] | alt | 624 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -18.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 756 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -24.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.439× (z -13.7) |
| [[COLO 205 (line)]] | alt | 463 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -14.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 603 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.561× (z -13.5) |
| [[J82 (line)]] | alt | 485 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -12.8) |
| [[SNU-1 (line)]] | wt | 517 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 452 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +16.8) | [[Selinexor (drug)]] 5 µM 0.597× (z -12.7) |
| [[HCT15 (line)]] | alt | 729 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.536× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 457 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -12.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 543 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -15.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.572× (z -8.8) |
| [[LoVo (line)]] | wt | 730 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.603× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 615 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 562 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.419× (z -14.6) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.589× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 535 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -26.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.617× (z -11.9) |
| [[A-172 (line)]] | wt | 437 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -11.9) |
| [[A-427 (line)]] | wt | 355 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.537× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 619 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +24.6) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -12.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 859 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.9) |
| [[C-33 A (line)]] | alt | 827 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 354 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.396× (z -14.8) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.648× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 475 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +28.1) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -16.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 529 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.527× (z -12.6) |
| [[H4 (line)]] | wt | 606 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.516× (z -9.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 574 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -13.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 419 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -12.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.585× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 818 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 462 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.577× (z -10.1) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 724 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 733 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 722 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 474 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKAP2]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[HCFC1R1]] | +0.59 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CRIP2]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PAFAH1B1]] | +0.57 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[NBEAL1]] | +0.57 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[GRHL1]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ZNF292]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DCAF6]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.55 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[MAP3K2]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | +0.54 | +0.35 / +0.34 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[GLIS2]] | +0.54 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[PCSK1N]] | +0.54 | +0.51 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNT1]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[UBIAD1]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[DCTD]] | -0.58 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[PIGW]] | -0.57 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[EXOSC3]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins |
| [[ARMC6]] | -0.55 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[WDR4]] | -0.53 | -0.56 / -0.43 | both halves | 3e-05 | STRING 436 |
| [[ANAPC1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[AVEN]] | -0.53 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[RFT1]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZNF124]] | -0.52 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[ALG8]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KMT2C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.6, -43.7); signed map (-18.4, 22.9). **Vector** length 108, 48.1% of its response variance represented; |z| ≥ 3 in 1,534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.9 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.9 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.3 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.3 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.3 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.2 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.2 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.5 | -20.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.5 | -8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.7 | -13.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.0 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:152,134,922-152,436,644 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1506, HALR; previously MLL3 |
| Gene groups (HGNC) | PHD finger proteins; Histone lysine methyltransferases; SET domain containing |
| Reactome | 21 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; PKMTs methylate histone lysines; RUNX1 regulates genes involved in megakaryocyte differentiation and platelet function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEZ4](https://www.uniprot.org/uniprotkb/Q8NEZ4) (Histone-lysine N-methyltransferase 2C):

> Histone methyltransferase that catalyzes methyl group transfer from S-adenosyl-L-methionine to the epsilon-amino group of 'Lys-4' of histone H3 (H3K4). Part of chromatin remodeling machinery predominantly forms H3K4me1 methylation marks at active chromatin sites where transcription and DNA repair take place. Likely plays a redundant role with KMT2D in enriching H3K4me1 mark on primed and active enhancer elements.

**Summary**, from NCBI Gene [58508](https://www.ncbi.nlm.nih.gov/gene/58508):

> This gene is a member of the myeloid/lymphoid or mixed-lineage leukemia (MLL) family and encodes a nuclear protein with an AT hook DNA-binding domain, a DHHC-type zinc finger, six PHD-type zinc fingers, a SET domain, a post-SET domain and a RING-type zinc finger. This protein is a member of the ASC-2/NCOA6 complex (ASCOM), which possesses histone methylation activity and is involved in transcriptional coactivation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13726) · Entrez [58508](https://www.ncbi.nlm.nih.gov/gene/58508) · UniProt [Q8NEZ4](https://www.uniprot.org/uniprotkb/Q8NEZ4) · Ensembl [ENSG00000055609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055609)

## Data

Gene col 628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 628); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 628]; `tensor/DDL_lfc|DDL_z.npy` [628]; `embed/gene_vectors.npy` [628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 628 or target_col == 628). Every well: [[KMT2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
