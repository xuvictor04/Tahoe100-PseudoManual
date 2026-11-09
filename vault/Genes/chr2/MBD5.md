---
symbol: "MBD5"
type: "gene"
col: 12869
ensembl_id: "ENSG00000204406"
name: "methyl-CpG binding domain protein 5"
location: "2q23.1"
module: 74
arm: "+"
pooled_cpm: 354.64
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 48
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# MBD5

*methyl-CpG binding domain protein 5* — 2q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.28× (z +4.3, q 0.008, up in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.27×; ⚠ position not correctable); [[Cobimetinib (drug)]] 5 µM in 1 line (SK-MEL-2 1.99×).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (24 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.337× (z -19.2, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.533× (z -16.3, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC8]] (+0.62, fdr 9e-06), [[ARFIP1]] (+0.59, fdr 9e-06), [[TBCK]] (+0.57, fdr 4e-05); moves opposite to [[CAMKK2]] (-0.56, fdr 2e-05), [[FAM124A]] (-0.53, fdr 4e-05), [[MPP3]] (-0.51, fdr 4e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM124A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.27×; ⚠ position not correctable); [[Cobimetinib (drug)]] 5 µM in 1 line (SK-MEL-2 1.99×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.008 | 33/47 (SK-MEL-2, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 25 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.337×** | -19.2 | 0e+00 | 43/44 (A-427, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.335×** | -17.3 | 0e+00 | 47/49 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.514×** | -17.2 | 0e+00 | 40/48 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.369×** | -16.9 | 0e+00 | 44/45 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.533×** | -16.3 | 0e+00 | 46/49 (CHP-212, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.416×** | -15.5 | 0e+00 | 47/47 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.454×** | -13.9 | 4e-42 | 45/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -12.7 | 4e-35 | 40/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.567×** | -10.0 | 9e-22 | 40/48 (COLO 205, SW 900, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.618×** | -8.8 | 8e-17 | 46/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.628×** | -8.5 | 8e-16 | 41/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.632×** | -8.4 | 2e-15 | 36/48 (HCT15, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.638×** | -8.2 | 8e-15 | 41/48 (HCT15, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.646×** | -8.0 | 5e-14 | 39/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -7.7 | 7e-13 | 43/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -7.3 | 7e-12 | 34/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.639×** | -7.1 | 5e-11 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.769×** | -6.8 | 3e-10 | 42/49 (CFPAC-1, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.731×** | -5.7 | 3e-07 | 34/48 (SW480, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -5.6 | 6e-07 | 36/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.750×** | -5.3 | 3e-06 | 39/48 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.724×** | -5.1 | 7e-06 | 38/47 (MIA PaCa-2, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.587×** | -5.0 | 1e-05 | 38/48 (SW 900, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.780×** | -4.3 | 3e-04 | 25/48 (KATO III, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.636×** | -4.2 | 4e-04 | 37/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.788×** | -4.2 | 5e-04 | 30/48 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.728×** | -4.1 | 5e-04 | 33/48 (SK-MEL-2, NCI-H23, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 453 | 0 | 19 (14 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -14.6) |
| [[H4 (line)]] | wt | 559 | 0 | 18 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -19.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -14.1) |
| [[SW480 (line)]] | alt | 373 | 0 | 17 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 503 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -13.4) |
| [[A-172 (line)]] | wt | 385 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -26.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -21.2) |
| [[C32 (line)]] | wt | 366 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -28.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -22.8) |
| [[SW 900 (line)]] | alt | 618 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -30.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -16.9) |
| [[HCT15 (line)]] | alt | 637 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.8) |
| [[HOP62 (line)]] | alt | 416 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -21.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -14.6) |
| [[HT-29 (line)]] | alt | 464 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -13.4) |
| [[KATO III (line)]] | alt | 267 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 313 | 0 | 12 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.190× (z -25.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 317 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -23.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -15.5) |
| [[COLO 205 (line)]] | alt | 467 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0816× (z -30.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 413 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -24.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 399 | 0 | 11 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.193× (z -17.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.249× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 426 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.475× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 255 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -24.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 348 | 0 | 10 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -20.2) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.273× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 408 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -30.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -17.6) |
| [[SNU-423 (line)]] | alt | 289 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -13.1) |
| [[BT-474 (line)]] | alt | 198 | 0 | 9 (8 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0618× (z -17.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 446 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -12.2) |
| [[PANC-1 (line)]] | alt | 322 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.519× (z -9.9) |
| [[A498 (line)]] | wt | 482 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 277 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 670 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -19.5) |
| [[LoVo (line)]] | wt | 243 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -19.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.467× (z -12.1) |
| [[LS 180 (line)]] | wt | 496 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.9) |
| [[SW1417 (line)]] | alt | 252 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -15.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -11.0) |
| [[CHP-212 (line)]] | wt | 689 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -21.1) |
| [[SK-MEL-2 (line)]] | alt | 232 | 1 | 5 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.99× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 298 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -17.2) |
| [[C-33 A (line)]] | alt | 390 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.9) |
| [[Hs 766T (line)]] | wt | 249 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.322× (z -12.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 251 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.0) |
| [[A-427 (line)]] | wt | 342 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0794× (z -29.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 179 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -11.8) |
| [[AN3 CA (line)]] | alt | 382 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -10.1) |
| [[RKO (line)]] | wt | 258 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -15.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 344 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.398× (z -10.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -13.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 577 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -9.8) |
| [[SW 1271 (line)]] | alt | 413 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 188 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.380× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 416 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 347 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC8]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[ARFIP1]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[TBCK]] | +0.57 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[NIPBL]] | +0.55 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TNKS]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 | pathway: Deubiquitination |
| [[UBR3]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ANKHD1]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[DCP1A]] | +0.54 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GALK2]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CHMP2A]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[XRN1]] | +0.53 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[BBS9]] | +0.53 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMKK2]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[FAM124A]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[MPP3]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SDC3]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PVR]] | -0.49 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[KCNC4]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ADCY3]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TTL]] | -0.48 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[NBEAL2]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[GFOD1]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MIR17HG]] | -0.47 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[SMAGP]] | -0.47 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM124A]] | B | FAM124A activity raises MBD5's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without FAM124A | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.486). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-26.3, -6.8); signed map (-8.1, -6.5). **Vector** length 90.9, 42.3% of its response variance represented; |z| ≥ 3 in 1,855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +8.1 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.0 | -7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +3.2 | -8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.2 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.0 | -0.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -15.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.9 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.8 | -7.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.4 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -16.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.9 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.2 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | methyl-CpG binding domain protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.1 — chr2:148,021,011-148,516,971 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11113, KIAA1461 |
| Gene groups (HGNC) | Methyl-CpG binding domain containing; PWWP domain containing |
| Reactome | 2 pathways, smallest: UCH proteinases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P267](https://www.uniprot.org/uniprotkb/Q9P267) (Methyl-CpG-binding domain protein 5):

> Non-catalytic component of the polycomb repressive deubiquitinase (PR-DUB) complex, a complex that specifically mediates deubiquitination of histone H2A monoubiquitinated at 'Lys-120' (H2AK119ub1). Important for stability of PR-DUB components and stimulating its ubiquitinase activity. As part of the PR-DUB complex, associates with chromatin enriched in histone marks H3K4me1, H3K4me3, and H3K27Ac, but not in H3K27me3. The PR-DUB complex is an epigenetic regulator of gene expression, including …

**Summary**, from NCBI Gene [55777](https://www.ncbi.nlm.nih.gov/gene/55777):

> This gene encodes a member of the methyl-CpG-binding domain (MBD) family. The MBD consists of about 70 residues and is the minimal region required for a methyl-CpG-binding protein binding specifically to methylated DNA. In addition to the MBD domain, this protein contains a PWWP domain (Pro-Trp-Trp-Pro motif), which consists of 100-150 amino acids and is found in numerous proteins that are involved in cell division, growth and differentiation. Mutations in this gene cause an autosomal dominant …

**Accessions** — [HGNC:20444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20444) · Entrez [55777](https://www.ncbi.nlm.nih.gov/gene/55777) · UniProt [Q9P267](https://www.uniprot.org/uniprotkb/Q9P267) · Ensembl [ENSG00000204406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204406)

## Data

Gene col 12869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12869); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12869]; `tensor/DDL_lfc|DDL_z.npy` [12869]; `embed/gene_vectors.npy` [12869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12869 or target_col == 12869). Every well: [[MBD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
