---
symbol: "NOLC1"
type: "gene"
col: 9259
ensembl_id: "ENSG00000166197"
name: "nucleolar and coiled-body phosphoprotein 1"
location: "10q24.32"
module: 5
arm: "+"
pooled_cpm: 116.7
n_lines_expressing: 50
n_dd_up: 55
n_dd_down: 8
n_dd_up_clean: 28
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NOLC1

*nucleolar and coiled-body phosphoprotein 1* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 55 drug-doses (27 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +17.4, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.97× (z +14.1, q 4e-43, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.686× (z -4.8, q 0.001, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.721× (z -4.3, q 0.004, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNO1]] (+0.79, fdr 7e-06), [[EIF4G1]] (+0.77, fdr 7e-06), [[MYBBP1A]] (+0.75, fdr 7e-06); moves opposite to [[NAA38]] (-0.67, fdr 1e-05), [[ZNF821]] (-0.65, fdr 7e-06), [[NPC2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 28 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 55 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **3.83×** | +17.4 | 0e+00 | 49/49 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.39×** | +15.9 | 0e+00 | 42/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **3.27×** | +15.2 | 0e+00 | 48/48 (SNU-423, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **3.38×** | +15.2 | 0e+00 | 44/44 (SNU-423, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.27×** | +14.2 | 1e-43 | 44/45 (NCI-H1573, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.97×** | +14.1 | 4e-43 | 45/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.96×** | +14.1 | 6e-43 | 48/48 (SNU-423, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.86×** | +13.6 | 2e-40 | 48/48 (SNU-423, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.35×** | +11.1 | 1e-26 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.78×** | +10.6 | 3e-24 | 38/49 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **2.25×** | +10.1 | 3e-22 | 43/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +9.9 | 1e-21 | 44/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **2.18×** | +9.7 | 2e-20 | 45/47 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.17×** | +9.6 | 3e-20 | 45/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +8.8 | 6e-17 | 43/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.89×** | +7.2 | 2e-11 | 39/48 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +6.6 | 1e-09 | 41/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +6.0 | 5e-08 | 40/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.08×** | +5.0 | 1e-05 | 40/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.9 | 2e-05 | 28/48 (A-172, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 2e-04 | 31/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.90×** | +4.3 | 3e-04 | 38/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.87×** | +4.2 | 4e-04 | 36/48 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.2 | 5e-04 | 28/48 (Hs 766T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.83×** | +4.1 | 7e-04 | 37/48 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.25×** | +4.0 | 1e-03 | 40/49 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.002 | 36/48 (SW 1271, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.686×** | -4.8 | 0.001 | 37/47 (LoVo, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.721×** | -4.3 | 0.004 | 33/47 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.803×** | -4.0 | 0.012 | 31/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.013 | 28/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.817×** | -3.8 | 0.017 | 28/48 (SHP-77, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.754×** | -3.7 | 0.017 | 27/48 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.754×** | -3.4 | 0.054 | 25/50 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Daidzin (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.088 | 25/48 (NCI-H2347, CHP-212, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.632× | -3.2 | 0.10 | 23/50 (LoVo, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.845× | -3.1 | 0.12 | 18/49 (SW480, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.82 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 117 | 18 (15 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.91× (z +10.3) | — |
| [[A-172 (line)]] | wt | 66.8 | 15 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.00× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 96.3 | 15 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +15.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 89.4 | 15 (13 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +22.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.41× (z +19.1) | — |
| [[HOP62 (line)]] | alt | 75.9 | 14 (13 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +20.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.26× (z +16.9) | — |
| [[NCI-H1792 (line)]] | alt | 53.0 | 14 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +22.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.5× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 66.5 | 14 (13 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +20.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +12.8) | — |
| [[C32 (line)]] | wt | 67.1 | 13 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.25× (z +12.1) | — |
| [[A549 (line)]] | wt | 102 | 12 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +16.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.55× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 69.5 | 12 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +10.2) | — |
| [[LoVo (line)]] | wt | 122 | 9 (8 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.506× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.457× (z -8.5) |
| [[SW 900 (line)]] | alt | 80.6 | 12 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 76.0 | 11 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +19.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.71× (z +15.4) | — |
| [[AsPC-1 (line)]] | alt | 122 | 10 (9 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +13.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 73.7 | 10 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.71× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 80.2 | 10 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.80× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 203 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +13.8) | — |
| [[SW480 (line)]] | alt | 133 | 10 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.43× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 121 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 82.6 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.36× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 8 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +11.8) | [[Adagrasib (drug)]] 0.05 µM 0.663× (z -11.2) ⚠ position not correctable |
| [[SNU-1 (line)]] | wt | 114 | 9 (5 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.63× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 70.6 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.66× (z +10.8) | — |
| [[KATO III (line)]] | alt | 93.1 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 143 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.87× (z +12.4) | — |
| [[J82 (line)]] | alt | 112 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +8.8) | — |
| [[A498 (line)]] | wt | 201 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 76.3 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 136 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[COLO 205 (line)]] | alt | 59.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +10.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[H4 (line)]] | wt | 86.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +12.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.98× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 122 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[LS 180 (line)]] | wt | 81.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.37× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[Selinexor (drug)]] 5 µM 0.387× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 151 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +9.1) | — |
| [[A-427 (line)]] | wt | 189 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[AN3 CA (line)]] | alt | 181 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.39× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 181 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[RPMI-7951 (line)]] | alt | 71.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 77.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +9.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[C-33 A (line)]] | alt | 144 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.62× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[RKO (line)]] | wt | 146 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.53× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 5 µM 0.0617× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNO1]] | +0.79 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.77 | +0.80 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 418 |
| [[MYBBP1A]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 449 |
| [[DDX21]] | +0.73 | +0.77 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 657 |
| [[EBNA1BP2]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 | STRING 776 |
| [[WDR4]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[NOM1]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[NAA15]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[NOL6]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 | STRING 815 |
| [[PUM3]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 | STRING 411 |
| [[GRWD1]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 699 |
| [[IPO4]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA38]] | -0.67 | -0.54 / -0.70 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[ZNF821]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[NPC2]] | -0.65 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[AKAP1-DT]] | -0.64 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[GABARAPL2]] | -0.64 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[NDUFB4]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.62 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[UBE2B]] | -0.62 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[SAT2]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[SMIM27]] | -0.61 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TTI2]] | -0.61 | -0.46 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.0, -33.6); signed map (-5.4, -45.5). **Vector** length 88.0, 40.2% of its response variance represented; |z| ≥ 3 in 1,955 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.51 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.5 | +14.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +3.1 | +15.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +4.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.2 | +15.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -3.6 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.1 | +9.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -1.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar and coiled-body phosphoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,152,176-102,163,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P130, KIAA0035, NOPP140, NOPP130, Srp40 |
| Hallmark sets | MYC_TARGETS_V2, UNFOLDED_PROTEIN_RESPONSE, G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14978](https://www.uniprot.org/uniprotkb/Q14978) (Nucleolar and coiled-body phosphoprotein 1):

> Nucleolar protein that acts as a regulator of RNA polymerase I by connecting RNA polymerase I with enzymes responsible for ribosomal processing and modification. Required for neural crest specification: following monoubiquitination by the BCR(KBTBD8) complex, associates with TCOF1 and acts as a platform to connect RNA polymerase I with enzymes responsible for ribosomal processing and modification, leading to remodel the translational program of differentiating cells in favor of neural crest …

**Summary**, from NCBI Gene [9221](https://www.ncbi.nlm.nih.gov/gene/9221):

> Enables protein heterodimerization activity; protein kinase inhibitor activity; and protein-macromolecule adaptor activity. Involved in mesenchymal cell differentiation and regulation of protein metabolic process. Acts upstream of or within axonogenesis and regulation of synaptic plasticity. Located in fibrillar center. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15608) · Entrez [9221](https://www.ncbi.nlm.nih.gov/gene/9221) · UniProt [Q14978](https://www.uniprot.org/uniprotkb/Q14978) · Ensembl [ENSG00000166197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166197)

## Data

Gene col 9259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9259); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9259]; `tensor/DDL_lfc|DDL_z.npy` [9259]; `embed/gene_vectors.npy` [9259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9259 or target_col == 9259). Every well: [[NOLC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOLC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
