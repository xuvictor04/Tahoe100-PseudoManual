---
symbol: "ANKRD12"
type: "gene"
col: 2167
ensembl_id: "ENSG00000101745"
name: "ankyrin repeat domain 12"
location: "18p11.22"
module: 74
arm: "+"
pooled_cpm: 485.04
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# ANKRD12

*ankyrin repeat domain 12* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +26.3, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.539× (z -18.0, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.857× (z -6.6, q 3e-09, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSF1]] (+0.74, fdr 7e-06), [[KMT2A]] (+0.69, fdr 7e-06), [[PNRC1]] (+0.65, fdr 7e-06); moves opposite to [[ZNF587B]] (-0.67, fdr 7e-06), [[AHSA1]] (-0.67, fdr 7e-06), [[GCN1]] (-0.65, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SOX4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +26.3 | 0e+00 | 43/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +12.2 | 1e-31 | 37/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.49×** | +11.8 | 8e-30 | 40/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.33×** | +8.7 | 4e-16 | 27/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +7.9 | 3e-13 | 31/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +7.8 | 8e-13 | 38/49 (COLO 205, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +7.4 | 1e-11 | 29/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +4.7 | 2e-04 | 18/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.9 | 0.006 | 7/48 (AsPC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.09× | +3.8 | 0.010 | 3/48 (KATO III, AN3 CA, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.10× | +3.3 | 0.057 | 7/49 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.068 | 21/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.073 | 20/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.09× | +3.0 | 0.098 | 7/50 (AsPC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2167.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -18.0 | 0e+00 | 39/44 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.579×** | -15.9 | 0e+00 | 42/47 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.593×** | -15.8 | 0e+00 | 43/49 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.567×** | -11.4 | 9e-28 | 40/45 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.721×** | -9.9 | 4e-21 | 41/48 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.738×** | -8.2 | 3e-14 | 35/48 (NCI-H1792, MIA PaCa-2, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.646×** | -6.9 | 3e-10 | 39/45 (HOP62, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.649×** | -6.8 | 5e-10 | 28/38 (C32, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.851× | -6.8 | 5e-10 | 23/49 (A549, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.854× | -6.7 | 1e-09 | 19/48 (C32, SNU-423, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -6.6 | 3e-09 | 17/48 (HOP62, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.817×** | -6.1 | 5e-08 | 26/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | **0.822×** | -5.7 | 6e-07 | 24/47 (HOP62, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.701×** | -5.6 | 7e-07 | 36/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.733×** | -4.9 | 3e-05 | 34/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.874× | -4.1 | 0.002 | 15/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.877× | -3.9 | 0.002 | 20/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.004 | 26/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.899× | -3.2 | 0.034 | 7/48 (HT-29, C-33 A, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.931× | -3.0 | 0.058 | 0/49 | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | 0.870× | -3.0 | 0.061 | 9/48 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Megestrol (drug)]] 5 µM |  | 0.935× | -2.8 | 0.097 | 4/49 (HS-578T, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 326 | 11 (7 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +31.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.587× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 1,106 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.614× (z -10.1) |
| [[BT-474 (line)]] | alt | 766 | 5 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -12.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 614 | 2 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +17.6) | [[Selinexor (drug)]] 5 µM 0.581× (z -14.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HT-29 (line)]] | alt | 725 | 4 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +21.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -20.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 352 | 7 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +26.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.450× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 449 | 6 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +22.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.555× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 452 | 5 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +25.4) | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 519 | 3 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +20.9) | [[Dinaciclib (drug)]] 0.5 µM 0.542× (z -11.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 536 | 3 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +23.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.471× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 505 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -16.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 430 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +22.7) | [[Selinexor (drug)]] 5 µM 0.621× (z -11.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[MIA PaCa-2 (line)]] | alt | 693 | 1 (1 ⚠) | 6 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 1.72× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -22.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 1,040 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -18.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 608 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -22.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 443 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.561× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1,482 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -20.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 405 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +25.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.562× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 831 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -17.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 430 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +18.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.507× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 547 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.262× (z -20.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 415 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.551× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 324 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +29.9) | — |
| [[SNU-423 (line)]] | alt | 433 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -16.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 334 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +31.4) | — |
| [[Hs 766T (line)]] | wt | 424 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +19.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.500× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 318 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +30.3) | — |
| [[SW 900 (line)]] | alt | 417 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +21.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.407× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 367 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -23.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H1792 (line)]] | alt | 346 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.457× (z -11.0) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 254 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +14.7) | — |
| [[SW480 (line)]] | alt | 341 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.543× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 168 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +23.5) | — |
| [[H4 (line)]] | wt | 424 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 510 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.535× (z -11.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 298 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +15.0) | — |
| [[RPMI-7951 (line)]] | alt | 534 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +16.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -15.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 335 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +27.4) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 564 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -13.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 432 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -12.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 544 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.510× (z -10.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[CHP-212 (line)]] | wt | 418 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -9.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H2030 (line)]] | alt | 432 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.386× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 389 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 427 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 550 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 529 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 737 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 451 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSF1]] | +0.74 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[KMT2A]] | +0.69 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[PNRC1]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CHD2]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[SMDT1]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[OFD1]] | +0.64 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[CEP350]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TXNIP]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[BTG1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PIM3]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[YY1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF587B]] | -0.67 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[AHSA1]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[GCN1]] | -0.65 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[RPSA]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[NSUN2]] | -0.62 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[NIPA2]] | -0.62 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[TXNDC5]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[NUP205]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[METTL3]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[NAA50]] | -0.60 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[DPAGT1]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.59 | -0.59 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX4]] | B | SOX4 activity lowers ANKRD12's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without SOX4 | 0.089 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.3, -44.8); signed map (-6.9, 10.3). **Vector** length 161, 58.8% of its response variance represented; |z| ≥ 3 in 1,495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.5 | +26.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.9 | +11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.1 | +12.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.7 | +7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.2 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -9.8 | -15.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.5 | -8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -8.9 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -8.0 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -7.4 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.2 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.2 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:9,136,228-9,285,985 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0874, FLJ20053, GAC-1, ANCO-2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UB98](https://www.uniprot.org/uniprotkb/Q6UB98) (Ankyrin repeat domain-containing protein 12):

> May recruit HDACs to the p160 coactivators/nuclear receptor complex to inhibit ligand-dependent transactivation.

**Summary**, from NCBI Gene [23253](https://www.ncbi.nlm.nih.gov/gene/23253):

> This gene encodes a member of the ankyrin repeats-containing cofactor family. These proteins may inhibit the transcriptional activity of nuclear receptors through the recruitment of histone deacetylases. The encoded protein interacts with p160 coactivators and also represses transcription mediated by the coactivator alteration/deficiency in activation 3 (ADA3). Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:29135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29135) · Entrez [23253](https://www.ncbi.nlm.nih.gov/gene/23253) · UniProt [Q6UB98](https://www.uniprot.org/uniprotkb/Q6UB98) · Ensembl [ENSG00000101745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101745)

## Data

Gene col 2167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2167); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2167]; `tensor/DDL_lfc|DDL_z.npy` [2167]; `embed/gene_vectors.npy` [2167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2167 or target_col == 2167). Every well: [[ANKRD12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
