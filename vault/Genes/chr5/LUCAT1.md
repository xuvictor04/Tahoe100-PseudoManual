---
symbol: "LUCAT1"
type: "gene"
col: 14531
ensembl_id: "ENSG00000248323"
name: "lung cancer associated transcript 1"
location: "5q14.3"
module: 101
arm: "+"
pooled_cpm: 326.33
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 66
n_dd_up_clean: 12
n_dd_down_clean: 50
in_vector_space: true
direction_upstream: 19
direction_downstream: 9
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# LUCAT1

*lung cancer associated transcript 1* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +9.7, q 2e-19, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 66 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.514× (z -14.3, q 2e-43, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH2L]] (+0.69, fdr 7e-06), [[TPT1-AS1]] (+0.67, fdr 8e-06), [[OSMR-DT]] (+0.63, fdr 9e-06); moves opposite to [[CHPT1]] (-0.59, fdr 1e-05), [[EHMT2]] (-0.56, fdr 1e-05), [[RAVER2]] (-0.56, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TM4SF19]], [[TM4SF19-DYNLT2B]] → it (grade B ⚠); 9 go from it, the strongest it → [[GPAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14531.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +9.7 | 2e-19 | 32/40 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +9.1 | 4e-17 | 31/40 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +8.6 | 2e-15 | 32/40 (SHP-77, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +7.9 | 4e-13 | 35/41 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.8 | 2e-04 | 20/41 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.7 | 2e-04 | 25/40 (Hs 766T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.002 | 28/39 (NCI-H23, RKO, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.1 | 0.003 | 20/40 (SW48, RKO, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +3.9 | 0.006 | 21/39 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.007 | 21/40 (COLO 205, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.043 | 19/41 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.045 | 18/39 (SHP-77, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.090 | 16/40 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.10 | 19/42 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 78 in all, 20 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 66 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -14.3 | 2e-43 | 30/40 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.383×** | -14.0 | 2e-42 | 38/39 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.410×** | -13.5 | 2e-39 | 35/40 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.201×** | -12.8 | 3e-35 | 38/40 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -12.7 | 1e-34 | 37/40 (H4, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.427×** | -12.4 | 2e-33 | 34/39 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.227×** | -11.8 | 3e-30 | 38/41 (CFPAC-1, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.516×** | -10.0 | 8e-22 | 36/40 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.318×** | -9.1 | 5e-18 | 40/40 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.656×** | -9.0 | 1e-17 | 29/40 (A-172, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -8.5 | 1e-15 | 33/40 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.584×** | -8.2 | 2e-14 | 26/41 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.590×** | -8.0 | 6e-14 | 31/40 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.605×** | -7.6 | 1e-12 | 30/40 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -7.4 | 6e-12 | 28/40 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.604×** | -7.3 | 7e-12 | 31/41 (H4, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.617×** | -7.3 | 9e-12 | 31/40 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.621×** | -7.2 | 2e-11 | 32/40 (H4, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.637×** | -6.8 | 3e-10 | 29/40 (H4, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 743 | 0 | 30 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -39.2) |
| [[NCI-H460 (line)]] | wt | 426 | 0 | 23 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -31.2) |
| [[NCI-H1573 (line)]] | alt | 2,046 | 0 | 21 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -15.4) |
| [[BT-474 (line)]] | alt | 103 | 1 | 17 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.25× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 572 | 0 | 18 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.164× (z -18.8) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.256× (z -14.7) |
| [[COLO 205 (line)]] | alt | 841 | 4 (1 ⚠) | 12 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0870× (z -20.4) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0602× (z -12.8) |
| [[HCT15 (line)]] | alt | 196 | 1 | 15 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.03× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -24.6) |
| [[RKO (line)]] | wt | 355 | 1 | 15 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.83× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 398 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -23.7) |
| [[SW480 (line)]] | alt | 197 | 3 | 12 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.81× (z +16.0) | [[Binimetinib (drug)]] 0.5 µM 0.442× (z -10.8) |
| [[C32 (line)]] | wt | 138 | 3 | 10 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.262× (z -14.4) |
| [[HOP62 (line)]] | alt | 866 | 0 | 13 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -20.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -13.5) |
| [[Hs 766T (line)]] | wt | 160 | 11 (4 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +16.7) | [[Selinexor (drug)]] 5 µM 0.468× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 299 | 1 | 11 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +9.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.219× (z -16.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 516 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -25.3) |
| [[HEC-1-A (line)]] | alt | 210 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -26.1) |
| [[NCI-H23 (line)]] | alt | 536 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0358× (z -35.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 356 | 1 | 10 (7 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +10.8) | [[Lonafarnib (drug)]] 5 µM 0.108× (z -13.0) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.477× (z -11.7) |
| [[A549 (line)]] | wt | 365 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -24.9) |
| [[PANC-1 (line)]] | alt | 95.7 | 3 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.04× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -14.7) |
| [[SW 1271 (line)]] | alt | 1,121 | 1 | 9 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.13× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.125× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -15.0) |
| [[A-172 (line)]] | wt | 279 | 1 | 8 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.50× (z +10.5) | [[Selinexor (drug)]] 5 µM 0.190× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 247 | 3 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -25.2) |
| [[AsPC-1 (line)]] | alt | 180 | 6 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +19.2) | [[Dexamethasone (drug)]] 0.5 µM 0.374× (z -8.9) |
| [[HS-578T (line)]] | alt | 412 | 1 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.04× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -14.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -12.0) |
| [[HT-29 (line)]] | alt | 123 | 4 (1 ⚠) | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.27× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.274× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.444× (z -8.8) |
| [[SHP-77 (line)]] | alt | 289 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 6.91× (z +18.6) | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -16.0) |
| [[SNU-423 (line)]] | alt | 291 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.6) |
| [[LoVo (line)]] | wt | 88.7 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.38× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 6.89× (z +14.9) | [[Cobimetinib (drug)]] 0.5 µM 0.332× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 163 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.4) | [[PH-797804 (drug)]] 5 µM 0.0615× (z -12.0) |
| [[SW 900 (line)]] | alt | 262 | 3 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.3) | [[TAK-901 (drug)]] 5 µM 0.161× (z -9.1) |
| [[J82 (line)]] | alt | 288 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.218× (z -15.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 203 | 3 | 1 | [[Auranofin (drug)]] 5 µM 3.69× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.6) |
| [[SW 1088 (line)]] | alt | 725 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 128 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +12.2) | — |
| [[A-427 (line)]] | wt | 173 | 1 | 1 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.01× (z +10.0) | [[PH-797804 (drug)]] 5 µM 0.192× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.285× (z -10.4) |
| [[A498 (line)]] | wt | 374 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.235× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 401 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.8) |
| [[SW48 (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.54× (z +10.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[AN3 CA (line)]] | alt | 67.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 46.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 45.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 57.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 450 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 408 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 50.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 50.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2L]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TPT1-AS1]] | +0.67 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[OSMR-DT]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[NIT1]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[BACH1]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[HOMER1]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PPP1R14B-AS1]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CCNYL1]] | +0.61 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[HMGN2P46]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ISG20]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[POU2F2]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ITGA2-AS1]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.59 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[EHMT2]] | -0.56 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[RAVER2]] | -0.56 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[ALDH7A1]] | -0.56 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[SORT1]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[HADH]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CCDC6]] | -0.54 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[FLVCR2]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[LUC7L2]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.51 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[SORBS2]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 16, C 3. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity raises LUCAT1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 3.79× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[IGFBP3]] | B | IGFBP3 activity raises LUCAT1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without IGFBP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[CRLF2]] | B | CRLF2 activity raises LUCAT1's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 3.44× lower at baseline in the lines without CRLF2 | 0.011 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[WFDC3]] | B | WFDC3 activity raises LUCAT1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without WFDC3 | 0.019 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[DELEC1]] | B | DELEC1 activity raises LUCAT1's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 3.41× lower at baseline in the lines without DELEC1 | 0.033 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises LUCAT1's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without CLDN14-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[HRH1]] | B | HRH1 activity raises LUCAT1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.25× lower at baseline in the lines without HRH1 | 0.047 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[PLAUR]] | B | PLAUR activity raises LUCAT1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without PLAUR | 0.050 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises LUCAT1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without ITGB1-DT | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[SHB]] | B | SHB activity raises LUCAT1's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.62× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[GPAT3]] | B | GPAT3 activity raises LUCAT1's level | lines that do not express GPAT3 (7) vs lines expressing it (43) | 2.51× lower at baseline in the lines without GPAT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: HLA-H, ABCA5, ISG20; maybe low, not absent; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers LUCAT1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPAT3]] | B | LUCAT1 activity raises GPAT3's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 2.45× lower at baseline in the lines without LUCAT1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[ITGA2-AS1]] | B | LUCAT1 activity raises ITGA2-AS1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without LUCAT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[PAIP1]] | B | LUCAT1 activity lowers PAIP1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.28× higher at baseline in the lines without LUCAT1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[EHMT2]] | B | LUCAT1 activity lowers EHMT2's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.71× higher at baseline in the lines without LUCAT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[HBEGF]] | B | LUCAT1 activity raises HBEGF's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without LUCAT1 | 0.077 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[NOP14-AS1]] | B | LUCAT1 activity raises NOP14-AS1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without LUCAT1 | 0.077 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[NFIA]] | B | LUCAT1 activity lowers NFIA's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 4.39× higher at baseline in the lines without LUCAT1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[BCAN-AS1]] | B | LUCAT1 activity raises BCAN-AS1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without LUCAT1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[PDE2A]] | C | LUCAT1 activity raises PDE2A's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without LUCAT1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16; co-absent with the target |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.6, -5.7); signed map (-0.3, 31.1). **Vector** length 155, 58.4% of its response variance represented; |z| ≥ 3 in 2,301 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.3 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +10.8 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.4 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.7 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +2.1 |
| fall | [[NG25 (drug)]] 5 µM |  | -9.0 | -9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.5 | -10.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -7.3 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.6 | -9.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -6.6 | -7.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.5 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -12.8 |

## What is on record

|  |  |
|---|---|
| Name | lung cancer associated transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.3 — chr5:91,054,834-91,314,547 (-) |
| Ensembl biotype | lncRNA |
| Also known as | SCAL1, SCAT5 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48498) · Entrez [100505994](https://www.ncbi.nlm.nih.gov/gene/100505994) · Ensembl [ENSG00000248323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248323)

## Data

Gene col 14531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14531); `tables/drug_effects.parquet` (92 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14531]; `tensor/DDL_lfc|DDL_z.npy` [14531]; `embed/gene_vectors.npy` [14531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14531 or target_col == 14531). Every well: [[LUCAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LUCAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
