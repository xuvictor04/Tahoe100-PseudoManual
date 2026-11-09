---
symbol: "RERE"
type: "gene"
col: 6634
ensembl_id: "ENSG00000142599"
name: "arginine-glutamic acid dipeptide repeats"
location: "1p36.23"
module: 134
arm: "+"
pooled_cpm: 511.14
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# RERE

*arginine-glutamic acid dipeptide repeats* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.42× (z +7.5, q 4e-11, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.433× (z -17.1, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.572× (z -11.9, q 3e-30, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1958]] (+0.67, fdr 7e-06), [[SLC2A3]] (+0.65, fdr 1e-05), [[FAM117B]] (+0.62, fdr 1e-05); moves opposite to [[JHY]] (-0.58, fdr 5e-05), [[ANKLE2]] (-0.57, fdr 2e-05), [[SLC9A8]] (-0.56, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +7.5 | 4e-11 | 34/48 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.2 | 1e-10 | 36/48 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 2e-06 | 30/48 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.5 | 6e-06 | 26/48 (A-172, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 1.19× | +5.2 | 3e-05 | 20/48 (A-427, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.009 | 32/49 (A498, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +3.6 | 0.028 | 21/49 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.052 | 21/48 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.084 | 29/48 (LS 180, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -17.1 | 0e+00 | 43/44 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.466×** | -16.2 | 0e+00 | 48/49 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.476×** | -12.4 | 4e-33 | 41/45 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -11.9 | 3e-30 | 43/48 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -10.6 | 3e-24 | 42/48 (A-427, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -9.9 | 2e-21 | 43/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.621×** | -9.7 | 2e-20 | 39/48 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.653×** | -9.0 | 1e-17 | 40/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.777×** | -7.6 | 2e-12 | 29/48 (A549, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.705×** | -7.4 | 6e-12 | 37/48 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -7.3 | 1e-11 | 42/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.723×** | -6.9 | 2e-10 | 39/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.762×** | -5.6 | 1e-06 | 33/47 (LoVo, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.784×** | -5.2 | 9e-06 | 32/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.787×** | -5.1 | 1e-05 | 32/48 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -4.7 | 7e-05 | 33/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.700×** | -3.6 | 0.008 | 30/48 (NCI-H1792, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.846× | -3.6 | 0.010 | 19/47 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.896× | -3.3 | 0.020 | 5/49 (NCI-H460, HepG2/C3A, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.020 | 18/48 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.730×** | -3.2 | 0.029 | 27/49 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.770×** | -3.2 | 0.029 | 26/47 (HCT15, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.878× | -3.2 | 0.029 | 14/48 (NCI-H1792, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -3.2 | 0.032 | 28/48 (NCI-H1792, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.754×** | -2.9 | 0.078 | 26/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 464 | 0 | 17 (13 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.239× (z -19.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.260× (z -18.8) |
| [[SW 900 (line)]] | alt | 567 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -20.9) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 427 | 3 | 8 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.76× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.401× (z -14.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.524× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 1,358 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -24.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.541× (z -8.8) |
| [[J82 (line)]] | alt | 242 | 4 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.399× (z -14.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[LoVo (line)]] | wt | 474 | 4 (1 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.551× (z -10.3) |
| [[PANC-1 (line)]] | alt | 863 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -13.0) |
| [[C32 (line)]] | wt | 540 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.418× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 882 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 358 | 6 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.524× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.529× (z -8.9) |
| [[A-427 (line)]] | wt | 769 | 1 (1 ⚠) | 6 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.53× (z +9.6) ⚠ cell-cycle shift, explains ~85% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -14.9) |
| [[A498 (line)]] | wt | 224 | 4 (1 ⚠) | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.00× (z +11.6) | [[Harringtonine (drug)]] 0.5 µM 0.505× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 255 | 1 (1 ⚠) | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +12.6) ⚠ cell-cycle shift, explains ~8% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -13.1) |
| [[C-33 A (line)]] | alt | 1,052 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -31.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 490 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -16.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -10.9) |
| [[Hs 766T (line)]] | wt | 490 | 3 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -12.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 408 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.445× (z -11.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 768 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 667 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.441× (z -13.8) |
| [[A549 (line)]] | wt | 367 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -25.0) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -15.4) |
| [[HOP62 (line)]] | alt | 558 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 727 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 334 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -15.0) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.469× (z -11.4) |
| [[SW480 (line)]] | alt | 660 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.534× (z -10.9) |
| [[AN3 CA (line)]] | alt | 559 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.456× (z -9.3) |
| [[HT-29 (line)]] | alt | 476 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.442× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 287 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.468× (z -12.8) |
| [[SHP-77 (line)]] | alt | 605 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -15.5) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -13.8) |
| [[SW1417 (line)]] | alt | 289 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.481× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.587× (z -9.2) |
| [[SW48 (line)]] | wt | 465 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -8.8) |
| [[A-172 (line)]] | wt | 201 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.64× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.519× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 424 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.78× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -18.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 643 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -14.0) |
| [[SNU-423 (line)]] | alt | 406 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -11.7) |
| [[COLO 205 (line)]] | alt | 437 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 1.76× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -13.2) |
| [[H4 (line)]] | wt | 506 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -20.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 518 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -16.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 388 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -12.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 362 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.75× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.541× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 336 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.564× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 603 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 989 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -9.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 500 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -14.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -11.8) |
| [[CHP-212 (line)]] | wt | 266 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 364 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 465 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 533 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 392 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 316 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SLC2A3]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[FAM117B]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SNX25]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MAML3]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TRPT1]] | +0.54 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[ZFYVE28]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[AP1S1]] | +0.53 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[FMNL2]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SNX14]] | +0.53 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[GLRX]] | +0.53 | +0.47 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JHY]] | -0.58 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ANKLE2]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SLC9A8]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LIG4]] | -0.55 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TAPBPL]] | -0.51 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[CLIP1]] | -0.51 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[PHF11]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[BRPF3]] | -0.51 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ZXDA]] | -0.50 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[BTC]] | -0.50 | -0.53 / -0.24 | both halves | 4e-04 |  |
| [[FGF2]] | -0.50 | -0.50 / -0.26 | both halves | 3e-04 |  |
| [[LINC01725]] | -0.50 | -0.48 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RERE's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RERE's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.0, -12.5); signed map (-35.1, 27.9). **Vector** length 105, 39.9% of its response variance represented; |z| ≥ 3 in 1,633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | -0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.3 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -10.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -7.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.2 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.0 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | arginine-glutamic acid dipeptide repeats |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:8,352,397-8,848,921 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0458, ARP, ARG, DNB1, ATN2; previously ATN1L |
| Gene groups (HGNC) | GATA zinc finger domain containing; Myb/SANT domain containing; Atrophins; RERE complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2R6](https://www.uniprot.org/uniprotkb/Q9P2R6) (Arginine-glutamic acid dipeptide repeats protein):

> Plays a role as a transcriptional repressor during development. May play a role in the control of cell survival. Overexpression of RERE recruits BAX to the nucleus particularly to POD and triggers caspase-3 activation, leading to cell death.

**Summary**, from NCBI Gene [473](https://www.ncbi.nlm.nih.gov/gene/473):

> This gene encodes a member of the atrophin family of arginine-glutamic acid (RE) dipeptide repeat-containing proteins. The encoded protein co-localizes with a transcription factor in the nucleus, and its overexpression triggers apoptosis. A similar protein in mouse associates with histone deacetylase and is thought to function as a transcriptional co-repressor during embryonic development. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:9965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9965) · Entrez [473](https://www.ncbi.nlm.nih.gov/gene/473) · UniProt [Q9P2R6](https://www.uniprot.org/uniprotkb/Q9P2R6) · Ensembl [ENSG00000142599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142599)

## Data

Gene col 6634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6634); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6634]; `tensor/DDL_lfc|DDL_z.npy` [6634]; `embed/gene_vectors.npy` [6634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6634 or target_col == 6634). Every well: [[RERE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RERE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
