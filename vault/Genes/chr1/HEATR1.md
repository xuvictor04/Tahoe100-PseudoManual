---
symbol: "HEATR1"
type: "gene"
col: 4049
ensembl_id: "ENSG00000119285"
name: "HEAT repeat containing 1"
location: "1q43"
module: 18
arm: "+"
pooled_cpm: 100.85
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# HEATR1

*HEAT repeat containing 1* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.68× (z +13.0, q 8e-36, up in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.83× (z +11.8, q 6e-30, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.768× (z -6.7, q 1e-08, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDN1]] (+0.86, fdr 7e-06), [[PUM3]] (+0.81, fdr 7e-06), [[POLR1A]] (+0.76, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RND1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +13.0 | 8e-36 | 42/48 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.83×** | +11.8 | 6e-30 | 40/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +10.4 | 7e-23 | 40/49 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +9.9 | 8e-21 | 38/48 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +9.8 | 2e-20 | 30/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +9.5 | 3e-19 | 28/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +9.4 | 4e-19 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +9.4 | 6e-19 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +8.9 | 2e-17 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +8.8 | 1e-16 | 38/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +8.7 | 2e-16 | 28/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +7.9 | 1e-13 | 27/48 (SHP-77, AN3 CA, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +7.6 | 1e-12 | 23/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +7.6 | 1e-12 | 32/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.39×** | +7.6 | 2e-12 | 23/45 (NCI-H460, NCI-H1573, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +6.9 | 1e-10 | 27/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.6 | 2e-09 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +5.8 | 2e-07 | 31/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +5.4 | 2e-06 | 29/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +5.0 | 1e-05 | 25/48 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.6 | 9e-05 | 13/49 (A498, SNU-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.46×** | +4.3 | 3e-04 | 23/48 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -6.7 | 1e-08 | 28/49 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -6.6 | 2e-08 | 23/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.823×** | -4.6 | 7e-04 | 22/49 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.835× | -4.6 | 7e-04 | 22/48 (A498, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.865× | -4.2 | 0.002 | 18/48 (LoVo, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.847× | -4.2 | 0.002 | 17/47 (SNU-423, H4, …) | two highest doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -4.0 | 0.006 | 19/48 (SW48, CHP-212, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.723×** | -3.7 | 0.014 | 17/48 (LS 180, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.811×** | -3.7 | 0.014 | 14/48 (H4, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.861× | -3.7 | 0.015 | 16/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.888× | -3.6 | 0.018 | 12/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.820×** | -3.5 | 0.022 | 15/48 (CHP-212, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.868× | -3.5 | 0.023 | 20/47 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.873× | -3.3 | 0.036 | 19/47 (hTERT-HPNE, NCI-H2030, …) | two highest doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.880× | -3.2 | 0.045 | 12/48 (SW 1271, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.883× | -3.2 | 0.056 | 12/49 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.889× | -3.0 | 0.090 | 9/48 (Panc 03.27, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 222 | 12 (9 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 8.98× (z +29.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 8.71× (z +29.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.589× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 52.8 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.45× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 178 | 3 (1 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.78× (z +9.4) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 3.40× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 112 | 6 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.98× (z +20.5) | — |
| [[AsPC-1 (line)]] | alt | 62.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 113 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.19× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 102 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 60.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 59.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.18× (z +8.9) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 70.7 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.05× (z +9.6) | — |
| [[SW48 (line)]] | wt | 122 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 67.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[A549 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 87.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[LS 180 (line)]] | wt | 67.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 79.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 74.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 183 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW1417 (line)]] | alt | 87.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 99.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDN1]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | STRING 579 |
| [[PUM3]] | +0.81 | +0.74 / +0.83 | both halves | 7e-06 | same gene group; STRING 837 |
| [[POLR1A]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 | STRING 938 |
| [[MRPS27]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[NOL10]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 | STRING 998 |
| [[KLHDC4]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[URB1]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 | same gene group; STRING 914 |
| [[TSEN2]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[LRPPRC]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[BCCIP]] | +0.73 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 | same gene group; STRING 973 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RND1]] | B | RND1 activity lowers HEATR1's level | lines that do not express RND1 (9) vs lines expressing it (41) | 1.52× higher at baseline in the lines without RND1 | 0.032 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[DUXAP8]] | B | DUXAP8 activity raises HEATR1's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.53× lower at baseline in the lines without DUXAP8 | 0.067 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[LAMB1]] | B | LAMB1 activity lowers HEATR1's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 1.72× higher at baseline in the lines without LAMB1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[LTBR]] | B | LTBR activity lowers HEATR1's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.53× higher at baseline in the lines without LTBR | 0.092 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.4, -35.9); signed map (-4.5, -50.0). **Vector** length 121, 38.7% of its response variance represented; |z| ≥ 3 in 1,420 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +13.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.0 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.6 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +11.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +5.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -4.4 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | HEAT repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:236,549,005-236,604,516 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10359, BAP28, UTP10 |
| Gene groups (HGNC) | Minor histocompatibility antigens; UTPa subcomplex; Armadillo like helical domain containing |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H583](https://www.uniprot.org/uniprotkb/Q9H583) (HEAT repeat-containing protein 1):

> Ribosome biogenesis factor; required for recruitment of Myc to nucleoli. Involved in nucleolar processing of pre-18S ribosomal RNA. Required for optimal pre-ribosomal RNA transcription by RNA polymerase I. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert …

**Summary**, from NCBI Gene [55127](https://www.ncbi.nlm.nih.gov/gene/55127):

> Enables RNA binding activity. Involved in several processes, including positive regulation of RNA metabolic process; protein localization to nucleolus; and ribosomal small subunit biogenesis. Located in fibrillar center and mitochondrion. Part of small-subunit processome. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25517) · Entrez [55127](https://www.ncbi.nlm.nih.gov/gene/55127) · UniProt [Q9H583](https://www.uniprot.org/uniprotkb/Q9H583) · Ensembl [ENSG00000119285](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119285)

## Data

Gene col 4049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4049); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4049]; `tensor/DDL_lfc|DDL_z.npy` [4049]; `embed/gene_vectors.npy` [4049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4049 or target_col == 4049). Every well: [[HEATR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEATR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
