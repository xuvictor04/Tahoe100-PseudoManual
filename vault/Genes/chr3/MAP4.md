---
symbol: "MAP4"
type: "gene"
col: 525
ensembl_id: "ENSG00000047849"
name: "microtubule associated protein 4"
location: "3p21.31"
module: 211
arm: "+"
pooled_cpm: 401.4
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# MAP4

*microtubule associated protein 4* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.31× (z +10.1, q 5e-21, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.659× (z -21.8, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP1B]] (+0.65, fdr 7e-06), [[KIF1B]] (+0.62, fdr 7e-06), [[ECPAS]] (+0.61, fdr 7e-06); moves opposite to [[KBTBD2]] (-0.55, fdr 3e-05), [[CCNT1]] (-0.54, fdr 3e-05), [[ZG16B]] (-0.53, fdr 2e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[UCHL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +10.1 | 5e-21 | 29/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +9.5 | 9e-19 | 34/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +8.8 | 3e-16 | 20/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.27×** | +8.7 | 6e-16 | 26/47 (HCT15, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +8.2 | 4e-14 | 31/47 (LoVo, A-427, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +8.0 | 1e-13 | 25/46 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +7.8 | 7e-13 | 12/47 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +7.7 | 1e-12 | 26/47 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.23×** | +7.1 | 1e-10 | 25/47 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +6.5 | 3e-09 | 23/47 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.20×** | +6.5 | 4e-09 | 22/46 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.20×** | +6.4 | 5e-09 | 22/44 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +6.4 | 8e-09 | 20/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +6.3 | 1e-08 | 23/47 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +6.2 | 3e-08 | 19/46 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.13× | +4.9 | 2e-05 | 15/48 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.14× | +4.9 | 3e-05 | 16/48 (NCI-H460, A-427, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +4.9 | 3e-05 | 15/46 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +4.4 | 3e-04 | 4/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.28×** | +4.4 | 3e-04 | 23/47 (NCI-H460, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.10× | +4.2 | 6e-04 | 14/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.12× | +4.0 | 0.001 | 17/47 (NCI-H460, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.659×** | -21.8 | 0e+00 | 42/47 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.545×** | -21.6 | 0e+00 | 44/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.607×** | -18.5 | 0e+00 | 46/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.617×** | -17.9 | 0e+00 | 44/47 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.630×** | -17.1 | 0e+00 | 47/47 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.687×** | -13.3 | 1e-38 | 36/47 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -12.1 | 6e-32 | 30/47 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.794×** | -12.1 | 9e-32 | 26/48 (A549, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -11.3 | 6e-28 | 29/47 (NCI-H2347, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.746×** | -10.8 | 2e-25 | 37/47 (A-172, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -8.2 | 1e-14 | 35/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -7.7 | 9e-13 | 27/47 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.817×** | -7.5 | 3e-12 | 24/47 (SW1417, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.807×** | -7.4 | 8e-12 | 28/46 (HS-578T, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.829×** | -7.0 | 1e-10 | 25/47 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.828×** | -6.6 | 1e-09 | 22/46 (RKO, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.892× | -6.0 | 6e-08 | 9/47 (A549, J82, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.902× | -5.4 | 2e-06 | 9/47 (A-172, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.865× | -5.4 | 2e-06 | 22/47 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.864× | -5.0 | 1e-05 | 15/46 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.883× | -4.6 | 9e-05 | 13/48 (HOP62, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.919× | -4.5 | 2e-04 | 9/47 (LoVo, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 551 | 1 (1 ⚠) | 12 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.63× (z +9.4) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -27.8) |
| [[HS-578T (line)]] | alt | 741 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -26.2) |
| [[SK-MEL-2 (line)]] | alt | 692 | 5 (2 ⚠) | 8 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.70× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.537× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.549× (z -12.3) |
| [[C32 (line)]] | wt | 300 | 9 (4 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.23× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.88× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.510× (z -11.9) |
| [[A-172 (line)]] | wt | 670 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -23.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -22.8) |
| [[LOX-IMVI (line)]] | wt | 488 | 1 (1 ⚠) | 10 (5 ⚠) | [[Trametinib (drug)]] 5 µM 1.59× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -40.3) |
| [[NCI-H460 (line)]] | wt | 355 | 5 (1 ⚠) | 6 (3 ⚠) | [[Trametinib (drug)]] 5 µM 1.68× (z +11.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 1.72× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.411× (z -17.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.593× (z -14.8) |
| [[LoVo (line)]] | wt | 360 | 3 (1 ⚠) | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.71× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.547× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.597× (z -10.8) |
| [[PANC-1 (line)]] | alt | 371 | 2 (1 ⚠) | 8 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.55× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.632× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 644 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -19.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.655× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 156 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 446 | 2 (1 ⚠) | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.61× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -22.5) |
| [[RKO (line)]] | wt | 361 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 586 | 1 (1 ⚠) | 8 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.73× (z +9.5) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -20.2) |
| [[SW480 (line)]] | alt | 305 | 6 (3 ⚠) | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +18.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.555× (z -12.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.628× (z -10.2) |
| [[A549 (line)]] | wt | 345 | 1 (1 ⚠) | 7 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.54× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -19.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.613× (z -10.6) |
| [[J82 (line)]] | alt | 585 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -17.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.499× (z -16.0) |
| [[LS 180 (line)]] | wt | 399 | 3 (1 ⚠) | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.535× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.560× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 473 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.84× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.367× (z -19.3) |
| [[A-427 (line)]] | wt | 383 | 1 (1 ⚠) | 4 (1 ⚠) | [[Trametinib (drug)]] 5 µM 1.63× (z +9.4) ⚠ cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -29.8) |
| [[A498 (line)]] | wt | 433 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.526× (z -15.2) |
| [[BT-474 (line)]] | alt | 266 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.580× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 494 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.526× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 290 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -16.1) |
| [[SW48 (line)]] | wt | 470 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 183 | 1 | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.54× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -11.9) |
| [[H4 (line)]] | wt | 427 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.506× (z -10.4) |
| [[HT-29 (line)]] | alt | 267 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.581× (z -9.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 500 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.451× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 316 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -23.6) |
| [[SNU-1 (line)]] | wt | 469 | 1 | 3 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.63× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -14.4) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.648× (z -9.9) |
| [[SNU-423 (line)]] | alt | 523 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -14.1) |
| [[SW1417 (line)]] | alt | 477 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.442× (z -16.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.638× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 402 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -12.8) ⚠ cell-cycle shift, explains ~22% of this change |
| [[AsPC-1 (line)]] | alt | 287 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -18.8) |
| [[HepG2_C3A (line)]] | wt | 328 | 2 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.68× (z +10.8) | — |
| [[KATO III (line)]] | alt | 236 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -12.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.576× (z -12.0) |
| [[HCT15 (line)]] | alt | 445 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.537× (z -10.2) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 324 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.127× (z -14.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 345 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 418 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 326 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 275 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 572 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 477 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 274 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP1B]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 | STRING 570 |
| [[KIF1B]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ECPAS]] | +0.61 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ERC1]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[RHOA]] | +0.60 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[XPOT]] | +0.59 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[EXOC6B]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SANBR]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[STX2]] | +0.58 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[RHOQ]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[NLN]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[AAK1]] | +0.57 | +0.68 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD2]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CCNT1]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ZG16B]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[NR4A2]] | -0.50 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[ABT1]] | -0.50 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MAML2]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[HNMT]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[SPRED1]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[HES1]] | -0.49 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CSTF1]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DUSP4]] | -0.49 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[PNRC2]] | -0.48 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UCHL1]] | B | UCHL1 activity raises MAP4's level | lines that do not express UCHL1 (29) vs lines expressing it (21) | 1.16× lower at baseline in the lines without UCHL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: NEFL, ADD2, CDH4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.2, 11.1); signed map (-12.7, 19.0). **Vector** length 147, 55.1% of its response variance represented; |z| ≥ 3 in 1,946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +10.8 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.9 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +9.5 | +7.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.7 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.6 | +7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.8 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +7.7 | +6.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.6 | -21.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.9 | -17.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.4 | -11.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -8.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.8 | -7.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.2 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.6 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,850,690-48,089,272 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [P27816](https://www.uniprot.org/uniprotkb/P27816) (Microtubule-associated protein 4):

> Non-neuronal microtubule-associated protein. Promotes microtubule assembly.

**Summary**, from NCBI Gene [4134](https://www.ncbi.nlm.nih.gov/gene/4134):

> The protein encoded by this gene is a major non-neuronal microtubule-associated protein. This protein contains a domain similar to the microtubule-binding domains of neuronal microtubule-associated protein (MAP2) and microtubule-associated protein tau (MAPT/TAU). This protein promotes microtubule assembly, and has been shown to counteract destabilization of interphase microtubule catastrophe promotion. Cyclin B was found to interact with this protein, which targets cell division cycle 2 (CDC2) …

**Accessions** — [HGNC:6862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6862) · Entrez [4134](https://www.ncbi.nlm.nih.gov/gene/4134) · UniProt [P27816](https://www.uniprot.org/uniprotkb/P27816) · Ensembl [ENSG00000047849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047849)

## Data

Gene col 525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 525); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 525]; `tensor/DDL_lfc|DDL_z.npy` [525]; `embed/gene_vectors.npy` [525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 525 or target_col == 525). Every well: [[MAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
