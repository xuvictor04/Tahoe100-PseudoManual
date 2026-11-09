---
symbol: "TMTC2"
type: "gene"
col: 10999
ensembl_id: "ENSG00000179104"
name: "transmembrane O-mannosyltransferase targeting cadherins 2"
location: "12q21.31"
module: 127
arm: "+"
pooled_cpm: 240.36
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 41
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# TMTC2

*transmembrane O-mannosyltransferase targeting cadherins 2* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.18× (z +4.8, q 0.001, up in 19 of 43 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.23× (z +4.0, q 0.011, up in 21 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (RKO 3.76×, A498 2.29×, LoVo 1.87×, HOP62 2.40×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.99×, AsPC-1 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.34×, HOP62 2.61×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H460 2.39×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (NCI-H460 2.22×); [[Tucidinostat (drug)]] 5 µM in 1 line (PANC-1 1.75×).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.424× (z -24.3, q 0e+00, down in 38 of 42 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.378× (z -18.8, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLPP1]] (+0.53, fdr 3e-05), [[GLCCI1]] (+0.51, fdr 2e-05), [[NCK1-DT]] (+0.51, fdr 4e-05); moves opposite to [[TOP3B]] (-0.56, fdr 3e-05), [[ZNF502]] (-0.56, fdr 2e-05), [[DMAP1]] (-0.53, fdr 2e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPRC5A]] → it (grade B ⚠); 7 go from it, the strongest it → [[PLEKHG4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10999.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (RKO 3.76×, A498 2.29×, LoVo 1.87×, HOP62 2.40×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.99×, AsPC-1 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.34×, HOP62 2.61×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H460 2.39×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (NCI-H460 2.22×); [[Tucidinostat (drug)]] 5 µM in 1 line (PANC-1 1.75×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.8 | 0.001 | 19/43 (RKO, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.24×** | +4.4 | 0.004 | 22/43 (PANC-1, RKO, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.011 | 21/42 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.031 | 15/44 (CFPAC-1, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.6 | 0.031 | 15/42 (PANC-1, RKO, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.12 | 17/42 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 16/42 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.14 | 12/42 (RPMI-7951, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.424×** | -24.3 | 0e+00 | 38/42 (NCI-H23, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.336×** | -20.3 | 0e+00 | 38/40 (KATO III, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.389×** | -19.0 | 0e+00 | 37/43 (KATO III, NCI-H1792, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.378×** | -18.8 | 0e+00 | 40/42 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.405×** | -18.1 | 0e+00 | 40/42 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -18.0 | 0e+00 | 37/39 (LoVo, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.446×** | -16.2 | 0e+00 | 40/42 (SK-MEL-2, COLO 205, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.457×** | -15.7 | 0e+00 | 39/42 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.468×** | -15.3 | 0e+00 | 39/42 (COLO 205, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.472×** | -15.1 | 0e+00 | 39/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.474×** | -15.0 | 0e+00 | 40/42 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -10.5 | 4e-24 | 33/43 (NCI-H23, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -10.2 | 1e-22 | 32/42 (SW1417, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.608×** | -9.6 | 3e-20 | 32/42 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -9.5 | 8e-20 | 37/42 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.652×** | -8.6 | 3e-16 | 26/42 (COLO 205, HCT15, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.653×** | -8.5 | 5e-16 | 34/42 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -8.1 | 2e-14 | 35/42 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.683×** | -7.2 | 1e-11 | 29/42 (COLO 205, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.747×** | -5.8 | 1e-07 | 28/42 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -5.6 | 6e-07 | 23/42 (A549, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.833×** | -5.2 | 5e-06 | 19/43 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.780×** | -4.8 | 3e-05 | 22/42 (RKO, CFPAC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 408 | 2 | 21 (12 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.39× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -23.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 725 | 0 | 20 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -24.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.127× (z -21.5) |
| [[LOX-IMVI (line)]] | wt | 216 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -21.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.219× (z -19.0) |
| [[BT-474 (line)]] | alt | 286 | 0 | 18 (11 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.173× (z -16.7) |
| [[HCT15 (line)]] | alt | 570 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -28.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 392 | 0 | 17 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -14.3) |
| [[KATO III (line)]] | alt | 505 | 0 | 16 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0816× (z -32.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.393× (z -13.2) |
| [[A549 (line)]] | wt | 249 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -29.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -23.3) |
| [[COLO 205 (line)]] | alt | 384 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -22.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.216× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 265 | 0 | 15 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -13.1) |
| [[HT-29 (line)]] | alt | 547 | 0 | 15 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -16.3) |
| [[LoVo (line)]] | wt | 409 | 1 (1 ⚠) | 14 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -31.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.450× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 190 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -33.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -16.3) |
| [[PANC-1 (line)]] | alt | 89.9 | 1 | 13 (8 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.75× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -18.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.208× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 279 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 176 | 0 | 13 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -17.1) |
| [[C32 (line)]] | wt | 895 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -17.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 229 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 534 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -25.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.240× (z -17.0) |
| [[SW480 (line)]] | alt | 147 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.264× (z -19.5) |
| [[A-427 (line)]] | wt | 190 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -20.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -14.2) |
| [[C-33 A (line)]] | alt | 131 | 0 | 10 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -16.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.341× (z -10.8) |
| [[LS 180 (line)]] | wt | 323 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.363× (z -13.4) |
| [[SW48 (line)]] | wt | 277 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.304× (z -11.7) |
| [[A-172 (line)]] | wt | 146 | 1 (1 ⚠) | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -14.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.275× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 210 | 2 (2 ⚠) | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.424× (z -10.8) |
| [[J82 (line)]] | alt | 144 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -10.6) |
| [[SW1417 (line)]] | alt | 227 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -17.2) ⚠ toxic |
| [[A498 (line)]] | wt | 117 | 1 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.5 µM 0.433× (z -11.4) |
| [[HOP62 (line)]] | alt | 81.5 | 3 (3 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.294× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 148 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -13.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 180 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -27.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.544× (z -9.1) |
| [[Hs 766T (line)]] | wt | 181 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -9.3) |
| [[RKO (line)]] | wt | 71.5 | 3 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.5 µM 0.349× (z -9.3) |
| [[CHP-212 (line)]] | wt | 484 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -8.5) |
| [[H4 (line)]] | wt | 103 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -13.9) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.357× (z -9.7) |
| [[SW 900 (line)]] | alt | 83.3 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.339× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 80.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H661 (line)]] | alt | 317 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 64.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1271 (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 50.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 51.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 47.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLPP1]] | +0.53 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[GLCCI1]] | +0.51 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[NCK1-DT]] | +0.51 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[GPRC5A]] | +0.50 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[KDM4C]] | +0.49 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[EGLN3]] | +0.48 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[IPMK]] | +0.47 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[ZSWIM5]] | +0.46 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[P4HA1]] | +0.46 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[SLC2A1-DT]] | +0.46 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SSR4]] | +0.45 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[LPIN2]] | +0.45 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP3B]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ZNF502]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[DMAP1]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZSCAN20]] | -0.52 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[C19orf44]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MANBAL]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ZNF691]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DRG2]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[DTX3]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZSCAN22]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RBM45]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[EIF2B4]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5A activity raises TMTC2's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.54× lower at baseline in the lines without GPRC5A | 0.022 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[ZNF583]] | B | ZNF583 activity lowers TMTC2's level | lines that do not express ZNF583 (15) vs lines expressing it (35) | 1.61× higher at baseline in the lines without ZNF583 | 0.067 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, SMARCA1, NUDT11 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG4]] | B | TMTC2 activity lowers PLEKHG4's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.84× higher at baseline in the lines without TMTC2 | 0.031 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |
| [[EIF2B4]] | B | TMTC2 activity lowers EIF2B4's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.23× higher at baseline in the lines without TMTC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |
| [[TMEM41A]] | B | TMTC2 activity raises TMEM41A's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without TMTC2 | 0.068 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |
| cells under [[Omeprazole (drug)]] 0.05 µM | B | TMTC2 activity lowers the cells' numbers under Omeprazole 0.05 µM (makes them more sensitive) | lines that do not express TMTC2 (6) vs lines expressing it (42) | the lines without TMTC2: 1.35× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | B | TMTC2 activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express TMTC2 (6) vs lines expressing it (42) | the lines without TMTC2: 0.76× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |
| [[EHHADH]] | B | TMTC2 activity raises EHHADH's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 2.17× lower at baseline in the lines without TMTC2 | 0.090 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |
| [[TTC8]] | B | TMTC2 activity lowers TTC8's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without TMTC2 | 0.095 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction -0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.6, -0.5); signed map (-37.1, 33.1). **Vector** length 104, 36.2% of its response variance represented; |z| ≥ 3 in 1,738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.8 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | -15.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -20.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.5 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -5.0 | -19.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -16.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane O-mannosyltransferase targeting cadherins 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:82,686,880-83,134,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762A217 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Transmembrane O-mannosyltransferase targeting cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N394](https://www.uniprot.org/uniprotkb/Q8N394) (Protein O-mannosyl-transferase TMTC2):

> Transfers mannosyl residues to the hydroxyl group of serine or threonine residues. The 4 members of the TMTC family are O-mannosyl-transferases dedicated primarily to the cadherin superfamily, each member seems to have a distinct role in decorating the cadherin domains with O-linked mannose glycans at specific regions. Also acts as O-mannosyl-transferase on other proteins such as PDIA3.

**Summary**, from NCBI Gene [160335](https://www.ncbi.nlm.nih.gov/gene/160335):

> The protein encoded by this gene is an integral membrane protein localized to the endoplasmic reticulum (ER). The encoded protein contains many tetratricopeptide repeats, sequences known for being involved in protein-protein interactions. This protein binds both the calcium uptake pump SERCA2B and the carbohydrate-binding chaperone calnexin, and it appears to play a role in calcium homeostasis in the ER. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:25440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25440) · Entrez [160335](https://www.ncbi.nlm.nih.gov/gene/160335) · UniProt [Q8N394](https://www.uniprot.org/uniprotkb/Q8N394) · Ensembl [ENSG00000179104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179104)

## Data

Gene col 10999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10999); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10999]; `tensor/DDL_lfc|DDL_z.npy` [10999]; `embed/gene_vectors.npy` [10999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10999 or target_col == 10999). Every well: [[TMTC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMTC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
