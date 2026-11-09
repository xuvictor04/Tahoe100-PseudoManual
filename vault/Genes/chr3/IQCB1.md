---
symbol: "IQCB1"
type: "gene"
col: 10358
ensembl_id: "ENSG00000173226"
name: "IQ motif containing B1"
location: "3q13.33"
module: 40
arm: "+"
pooled_cpm: 95.91
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# IQCB1

*IQ motif containing B1* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.45× (z +11.4, q 2e-27, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.31× (z +8.4, q 5e-15, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -23.0, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.717× (z -10.3, q 7e-23, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF5L]] (+0.73, fdr 7e-06), [[RABEPK]] (+0.72, fdr 7e-06), [[SHQ1]] (+0.69, fdr 7e-06); moves opposite to [[SGO1-AS1]] (-0.69, fdr 7e-06), [[CGGBP1]] (-0.62, fdr 1e-05), [[ERF]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFATC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +11.4 | 2e-27 | 37/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +11.1 | 4e-26 | 38/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +9.0 | 4e-17 | 31/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +8.4 | 5e-15 | 32/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.29×** | +8.0 | 2e-13 | 29/48 (AsPC-1, NCI-H1792, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +7.2 | 7e-11 | 27/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +6.7 | 1e-09 | 25/48 (AsPC-1, NCI-H2347, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +4.9 | 7e-05 | 21/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.42×** | +4.7 | 1e-04 | 19/45 (NCI-H460, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.16× | +4.5 | 3e-04 | 16/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.12× | +4.4 | 5e-04 | 14/48 (A549, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 8e-04 | 13/49 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.001 | 16/48 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 19/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.003 | 17/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 12/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.007 | 14/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.034 | 10/49 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.049 | 3/49 (PANC-1, J82, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.11× | +3.0 | 0.073 | 15/47 (Panc 03.27, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.566×** | -23.0 | 0e+00 | 43/48 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -13.3 | 4e-38 | 35/45 (SK-MEL-2, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.667×** | -12.0 | 5e-31 | 34/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.685×** | -11.7 | 2e-29 | 35/49 (HEC-1-A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -10.4 | 2e-23 | 29/44 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -10.3 | 7e-23 | 32/48 (HEC-1-A, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.725×** | -9.9 | 2e-21 | 28/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -8.1 | 3e-14 | 26/48 (NCI-H2347, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.769×** | -8.1 | 3e-14 | 26/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.770×** | -8.1 | 4e-14 | 30/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.853× | -6.8 | 7e-10 | 18/48 (SW480, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.807×** | -6.6 | 2e-09 | 26/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.744×** | -6.5 | 3e-09 | 27/47 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.844× | -5.3 | 6e-06 | 19/48 (HOP62, LS 180, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -5.2 | 8e-06 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.846× | -4.8 | 6e-05 | 20/47 (SNU-1, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.859× | -4.7 | 8e-05 | 21/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.842× | -3.8 | 0.004 | 12/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.849× | -3.6 | 0.009 | 14/48 (SW 1271, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.902× | -3.2 | 0.036 | 5/49 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.909× | -2.9 | 0.081 | 14/47 (NCI-H2030, SW480, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 85.1 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -17.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 82.4 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -17.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.597× (z -11.2) |
| [[PANC-1 (line)]] | alt | 104 | 1 (1 ⚠) | 6 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.79× (z +10.2) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.420× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 68.5 | 3 (3 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +12.2) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -14.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 94.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -20.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 187 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -15.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.406× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.434× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 131 | 1 (1 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.89× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -17.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.504× (z -8.5) |
| [[A549 (line)]] | wt | 89.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 55.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.4) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 114 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.97× (z +9.3) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 147 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.07× (z +11.2) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 76.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.91× (z +8.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.552× (z -11.4) |
| [[SW480 (line)]] | alt | 114 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.58× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.640× (z -9.0) |
| [[C32 (line)]] | wt | 68.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -16.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 98.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.635× (z -9.4) |
| [[LoVo (line)]] | wt | 113 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -11.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -10.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 71.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.214× (z -8.7) |
| [[COLO 205 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 98.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -16.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 87.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.383× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 64.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 90.3 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.596× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -13.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 1088 (line)]] | alt | 65.7 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.5 µM 0.0666× (z -8.8) |
| [[BT-474 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | +0.73 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[RABEPK]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 | STRING 444 |
| [[SHQ1]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[WRN]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GPR89A]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZW10]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ZNF496]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PIGU]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PHKA2]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[URI1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CDC123]] | +0.64 | +0.72 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1-AS1]] | -0.69 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[CGGBP1]] | -0.62 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ERF]] | -0.62 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[MMRN2]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TFE3]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SKIL]] | -0.61 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[COL28A1]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[UNC79]] | -0.60 | -0.58 / -0.39 | both halves | 5e-05 | same gene group |
| [[DNAH12]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.59 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[PIK3IP1-DT]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC2]] | B | NFATC2 activity lowers IQCB1's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.34× higher at baseline in the lines without NFATC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[TBX20]] | B | TBX20 activity raises IQCB1's level | lines that do not express TBX20 (32) vs lines expressing it (18) | 1.19× lower at baseline in the lines without TBX20 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1 |
| [[TBX20]] | B | TBX20 activity strengthens IQCB1's drug response | lines that do not express TBX20 (32) vs lines expressing it (17) | the lines without TBX20 respond 0.84× as strongly (z diff +0.80); strongest at Harringtonine 5 µM: 0.71x vs 0.58x (z diff +3.0) | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-8.1, -18.1); signed map (-42.9, -19.1). **Vector** length 126, 36.1% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.5 | +11.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.6 | +9.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +5.3 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +8.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.5 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -10.4 | -23.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.3 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -7.8 | -12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.5 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:121,769,761-121,835,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0036, NPHP5, SLSN5 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15051](https://www.uniprot.org/uniprotkb/Q15051) (IQ calmodulin-binding motif-containing protein 1):

> Involved in ciliogenesis. The function in an early step in cilia formation depends on its association with CEP290/NPHP6. Involved in regulation of the BBSome complex integrity, specifically for presence of BBS2 and BBS5 in the complex, and in ciliary targeting of selected BBSome cargos. May play a role in controlling entry of the BBSome complex to cilia possibly implicating CEP290/NPHP6.

**Summary**, from NCBI Gene [9657](https://www.ncbi.nlm.nih.gov/gene/9657):

> This gene encodes a nephrocystin protein that interacts with calmodulin and the retinitis pigmentosa GTPase regulator protein. The encoded protein has a central coiled-coil region and two calmodulin-binding IQ domains. It is localized to the primary cilia of renal epithelial cells and connecting cilia of photoreceptor cells. The protein is thought to play a role in ciliary function. Defects in this gene result in Senior-Loken syndrome type 5. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:28949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28949) · Entrez [9657](https://www.ncbi.nlm.nih.gov/gene/9657) · UniProt [Q15051](https://www.uniprot.org/uniprotkb/Q15051) · Ensembl [ENSG00000173226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173226)

## Data

Gene col 10358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10358); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10358]; `tensor/DDL_lfc|DDL_z.npy` [10358]; `embed/gene_vectors.npy` [10358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10358 or target_col == 10358). Every well: [[IQCB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
