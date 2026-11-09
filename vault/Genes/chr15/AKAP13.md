---
symbol: "AKAP13"
type: "gene"
col: 10002
ensembl_id: "ENSG00000170776"
name: "A-kinase anchoring protein 13"
location: "15q25.3"
module: 97
arm: "+"
pooled_cpm: 535.92
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# AKAP13

*A-kinase anchoring protein 13* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.85× (z +15.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.521× (z -22.9, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D8]] (+0.70, fdr 7e-06), [[ERGIC1]] (+0.67, fdr 1e-05), [[DENND3]] (+0.66, fdr 1e-05); moves opposite to [[LINC02100]] (-0.62, fdr 2e-05), [[GALNT7-DT]] (-0.61, fdr 1e-04), [[KLRA1P]] (-0.57, fdr 5e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +15.2 | 0e+00 | 44/48 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +13.9 | 3e-41 | 44/48 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +11.8 | 7e-30 | 42/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +7.3 | 5e-11 | 28/48 (A-172, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +6.3 | 3e-08 | 33/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +5.6 | 3e-06 | 30/47 (C32, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.25×** | +5.4 | 6e-06 | 26/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.48×** | +5.1 | 3e-05 | 37/49 (J82, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.9 | 5e-05 | 34/49 (A-172, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +4.8 | 9e-05 | 36/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +4.7 | 2e-04 | 24/48 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +4.5 | 3e-04 | 23/47 (hTERT-HPNE, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +4.4 | 5e-04 | 23/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +4.3 | 8e-04 | 20/48 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.006 | 19/50 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.009 | 21/48 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.521×** | -22.9 | 0e+00 | 44/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -21.3 | 0e+00 | 42/44 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.447×** | -19.9 | 0e+00 | 46/49 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -15.6 | 0e+00 | 41/45 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -13.4 | 4e-39 | 44/47 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -12.0 | 3e-31 | 40/48 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.733×** | -7.7 | 1e-12 | 40/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.750×** | -7.1 | 6e-11 | 36/48 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.756×** | -6.6 | 3e-09 | 34/48 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.757×** | -6.5 | 3e-09 | 28/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -6.5 | 4e-09 | 29/48 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -6.0 | 1e-07 | 29/50 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -5.5 | 1e-06 | 24/48 (HOP62, A-172, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.694×** | -4.7 | 8e-05 | 33/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -4.7 | 1e-04 | 23/48 (BT-474, SNU-423, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.701×** | -4.6 | 1e-04 | 34/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.888× | -4.2 | 8e-04 | 0/49 | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.732×** | -4.1 | 0.001 | 25/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.852× | -3.7 | 0.006 | 16/47 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.866× | -3.6 | 0.009 | 14/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 406 | 18 | 10 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -20.4) |
| [[SK-MEL-2 (line)]] | alt | 415 | 14 | 7 (5 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 1.94× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.346× (z -18.4) |
| [[HS-578T (line)]] | alt | 282 | 13 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -15.6) |
| [[C32 (line)]] | wt | 309 | 6 (2 ⚠) | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.33× (z +17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.20× (z +13.4) | [[Trametinib (drug)]] 0.5 µM 0.587× (z -10.4) |
| [[A-172 (line)]] | wt | 293 | 7 (2 ⚠) | 6 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.34× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -14.3) |
| [[A498 (line)]] | wt | 422 | 8 (3 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +20.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.86× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 755 | 1 | 12 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.71× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -29.0) |
| [[Hs 766T (line)]] | wt | 733 | 4 | 6 (5 ⚠) | [[Budesonide (drug)]] 5 µM 1.99× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 519 | 3 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -19.0) |
| [[RPMI-7951 (line)]] | alt | 428 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -14.1) |
| [[SNU-423 (line)]] | alt | 473 | 3 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.07× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -21.9) |
| [[SW1417 (line)]] | alt | 487 | 4 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -16.5) |
| [[KATO III (line)]] | alt | 715 | 3 | 6 (5 ⚠) | [[Belinostat (drug)]] 5 µM 2.05× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 318 | 3 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.464× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 749 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -22.9) |
| [[PANC-1 (line)]] | alt | 572 | 4 (4 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.43× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.312× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -18.5) |
| [[AsPC-1 (line)]] | alt | 977 | 3 | 5 (4 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 1.81× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 1,104 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -28.6) |
| [[HEC-1-A (line)]] | alt | 276 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.95× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.500× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 551 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -18.0) |
| [[J82 (line)]] | alt | 339 | 4 | 4 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.46× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 687 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -26.0) |
| [[SHP-77 (line)]] | alt | 309 | 7 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 384 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.08× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -13.1) |
| [[HCT15 (line)]] | alt | 387 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 276 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -16.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 688 | 1 | 6 (5 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 1.80× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -13.5) |
| [[SW48 (line)]] | wt | 550 | 2 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.80× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.8) |
| [[H4 (line)]] | wt | 341 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 356 | 4 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.35× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 984 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 968 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -30.1) |
| [[NCI-H23 (line)]] | alt | 292 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.76× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -13.3) |
| [[SW480 (line)]] | alt | 440 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -11.9) |
| [[A549 (line)]] | wt | 809 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -30.7) |
| [[COLO 205 (line)]] | alt | 816 | 3 (2 ⚠) | 2 (1 ⚠) | [[Peretinoin (drug)]] 5 µM 2.41× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -13.2) |
| [[HT-29 (line)]] | alt | 757 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.6) |
| [[LS 180 (line)]] | wt | 537 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -12.4) |
| [[RKO (line)]] | wt | 269 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.19× (z +11.5) | [[Auranofin (drug)]] 5 µM 0.512× (z -9.8) |
| [[A-427 (line)]] | wt | 229 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -15.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 284 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.10× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 729 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -11.1) |
| [[AN3 CA (line)]] | alt | 282 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.398× (z -8.9) |
| [[C-33 A (line)]] | alt | 270 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 342 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.5) |
| [[SNU-1 (line)]] | wt | 219 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.07× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 453 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -8.7) |
| [[CHP-212 (line)]] | wt | 347 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 853 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 529 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D8]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ERGIC1]] | +0.67 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[DENND3]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TANC2]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[NCOA3]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TOX2]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PTPN12]] | +0.64 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[FOXO1]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[MT1X]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ATP2B4]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MT2A]] | +0.62 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02100]] | -0.62 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[GALNT7-DT]] | -0.61 | -0.55 / -0.32 | both halves | 1e-04 |  |
| [[KLRA1P]] | -0.57 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[LINC01134]] | -0.55 | -0.41 / -0.32 | both halves | 1e-04 |  |
| [[TSTD3]] | -0.54 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[MAIP1]] | -0.54 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[CSTF3]] | -0.53 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[PNISR-AS1]] | -0.53 | -0.45 / -0.21 | both halves | 7e-04 |  |
| [[OXA1L-DT]] | -0.52 | -0.49 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[MR1]] | -0.52 | -0.47 / -0.22 | both halves | 6e-04 | same gene group |
| [[HOXD3]] | -0.52 | -0.30 / -0.30 | both halves | 2e-04 |  |
| [[CASS4]] | -0.52 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[C5orf15]] | -0.52 | -0.32 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises AKAP13's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without TBC1D8 | 0.005 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[DENND3]] | B | DENND3 activity raises AKAP13's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without DENND3 | 0.011 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[ABLIM3]] | B | ABLIM3 activity raises AKAP13's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without ABLIM3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[MYO1E]] | B | MYO1E activity raises AKAP13's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without MYO1E | 0.019 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[EPAS1]] | B | EPAS1 activity raises AKAP13's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without EPAS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[DENND3]] | B | DENND3 activity strengthens AKAP13's drug response | lines that do not express DENND3 (7) vs lines expressing it (42) | the lines without DENND3 respond 0.85× as strongly (z diff +1.11); strongest at Dinaciclib 0.5 µM: 0.72x vs 0.42x (z diff +5.4) | 0.039 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NIBAN2]] | B | NIBAN2 activity raises AKAP13's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without NIBAN2 | 0.063 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent |
| [[CCDC68]] | B | CCDC68 activity raises AKAP13's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without CCDC68 | 0.066 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[PAG1]] | B | PAG1 activity raises AKAP13's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.36× lower at baseline in the lines without PAG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[ATP2B4]] | B | ATP2B4 activity raises AKAP13's level | lines that do not express ATP2B4 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without ATP2B4 | 0.071 | ⚠ within organs, on part of the lines; also absent: PROCR, ARSJ, LAMB1 |
| [[DUSP1]] | B | DUSP1 activity raises AKAP13's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.61× lower at baseline in the lines without DUSP1 | 0.081 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[FLNB]] | C | FLNB activity raises AKAP13's level | lines that do not express FLNB (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, 11.7); signed map (12.4, 34.0). **Vector** length 152, 59.4% of its response variance represented; |z| ≥ 3 in 2,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +12.6 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +12.4 | +15.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +12.1 | +13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.5 | +6.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +6.4 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.1 | +2.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.7 | +3.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +5.4 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.2 | -22.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.4 | -13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -8.0 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.7 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.4 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -12.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -5.7 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.3 — chr15:85,380,571-85,749,358 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ht31, BRX, AKAP-Lbc, c-lbc, PROTO-LB, HA-3, ARHGEF13; previously LBC |
| Gene groups (HGNC) | A-kinase anchoring proteins; Pleckstrin homology domain containing; Dbl family Rho GEFs; Minor histocompatibility antigens; MicroRNA protein coding host genes |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 13 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12802](https://www.uniprot.org/uniprotkb/Q12802) (A-kinase anchor protein 13):

> Scaffold protein that plays an important role in assembling signaling complexes downstream of several types of G protein-coupled receptors. Activates RHOA in response to signaling via G protein-coupled receptors via its function as Rho guanine nucleotide exchange factor. May also activate other Rho family members. Part of a kinase signaling complex that links ADRA1A and ADRA1B adrenergic receptor signaling to the activation of downstream p38 MAP kinases, such as MAPK11 and MAPK14. Part of a …

**Summary**, from NCBI Gene [11214](https://www.ncbi.nlm.nih.gov/gene/11214):

> The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. Alternative splicing of this gene results in multiple transcript variants encoding different isoforms containing c-terminal dbl oncogene homology (DH) and pleckstrin homology (PH) domains. The DH domain is …

**Accessions** — [HGNC:371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:371) · Entrez [11214](https://www.ncbi.nlm.nih.gov/gene/11214) · UniProt [Q12802](https://www.uniprot.org/uniprotkb/Q12802) · Ensembl [ENSG00000170776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170776)

## Data

Gene col 10002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10002); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10002]; `tensor/DDL_lfc|DDL_z.npy` [10002]; `embed/gene_vectors.npy` [10002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10002 or target_col == 10002). Every well: [[AKAP13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
