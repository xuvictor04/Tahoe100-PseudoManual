---
symbol: "SCAI"
type: "gene"
col: 10409
ensembl_id: "ENSG00000173611"
name: "suppressor of cancer cell invasion"
location: "9q33.3"
module: 30
arm: "+"
pooled_cpm: 80.28
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SCAI

*suppressor of cancer cell invasion* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.92× (z +14.3, q 2e-43, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.553× (z -18.3, q 0e+00, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.534× (z -13.7, q 9e-41, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.75, fdr 7e-06), [[COG5]] (+0.70, fdr 7e-06), [[NBPF3]] (+0.69, fdr 1e-05); moves opposite to [[C11orf58]] (-0.70, fdr 1e-05), [[TUG1]] (-0.69, fdr 1e-05), [[MIS12]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +14.3 | 2e-43 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +10.8 | 8e-25 | 39/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +9.3 | 3e-18 | 39/48 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +4.2 | 0.003 | 14/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.018 | 21/48 (C32, HepG2/C3A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.023 | 20/49 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.553×** | -18.3 | 0e+00 | 41/48 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.442×** | -17.1 | 0e+00 | 41/48 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.479×** | -16.1 | 0e+00 | 43/49 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.480×** | -15.4 | 0e+00 | 40/44 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -13.7 | 9e-41 | 41/45 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -13.7 | 9e-41 | 40/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -11.2 | 2e-27 | 43/49 (A549, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.617×** | -10.5 | 4e-24 | 39/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.695×** | -7.9 | 1e-13 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.692×** | -7.7 | 7e-13 | 31/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.709×** | -7.5 | 3e-12 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.724×** | -7.0 | 8e-11 | 31/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.726×** | -7.0 | 1e-10 | 30/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.730×** | -6.9 | 3e-10 | 30/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -6.4 | 8e-09 | 26/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -5.6 | 1e-06 | 28/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.817×** | -4.4 | 3e-04 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.702×** | -3.9 | 0.003 | 22/48 (NCI-H1792, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.8 | 0.004 | 24/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Thymol (drug)]] 5 µM |  | 0.888× | -3.6 | 0.007 | 7/48 (A-172, A-427, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -3.5 | 0.012 | 21/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.894× | -3.4 | 0.015 | 13/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.866× | -3.1 | 0.037 | 14/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.867× | -2.9 | 0.079 | 14/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.876× | -2.9 | 0.080 | 8/48 (J82, HEC-1-A, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.877× | -2.8 | 0.086 | 9/47 (SW480, HT-29, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.0 | 1 | 13 (10 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -21.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.243× (z -18.4) |
| [[A-172 (line)]] | wt | 87.3 | 1 | 9 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.56× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -29.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 9 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -9.9) |
| [[PANC-1 (line)]] | alt | 68.3 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -26.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -14.8) |
| [[A498 (line)]] | wt | 72.4 | 1 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -22.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.199× (z -17.6) |
| [[HS-578T (line)]] | alt | 101 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -11.3) |
| [[J82 (line)]] | alt | 108 | 2 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -21.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 67.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -25.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.259× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 76.7 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +11.3) | [[Lonafarnib (drug)]] 5 µM 0.0640× (z -15.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 63.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -8.5) |
| [[SNU-423 (line)]] | alt | 78.0 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -19.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 97.5 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 50.9 | 1 | 3 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 2.83× (z +8.7) | [[Harringtonine (drug)]] 0.5 µM 0.190× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 167 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.78× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -19.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 84.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 35.7 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.220× (z -14.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.278× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 77.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -10.3) |
| [[SW1417 (line)]] | alt | 99.2 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -16.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 52.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -12.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 77.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -10.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 110 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.376× (z -9.1) |
| [[A-427 (line)]] | wt | 66.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 35.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 51.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 81.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[LoVo (line)]] | wt | 68.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.363× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 71.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.1) | [[Harringtonine (drug)]] 5 µM 0.415× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 79.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.227× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 81.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 58.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 73.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -14.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 58.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0720× (z -12.8) |
| [[HCT15 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.345× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 71.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 80.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 91.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 103 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.395× (z -10.8) |
| [[AN3 CA (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.75 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[COG5]] | +0.70 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NBPF3]] | +0.69 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[HSPB11]] | +0.69 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PHAF1]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.68 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ALG9]] | +0.67 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[KCTD7]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.67 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.70 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[TUG1]] | -0.69 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[MIS12]] | -0.67 | -0.64 / -0.61 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[SKIL]] | -0.67 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[TASOR]] | -0.66 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[IL6ST]] | -0.66 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.65 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[MED1]] | -0.65 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[GGPS1]] | -0.65 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[LIG4]] | -0.64 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[CYREN]] | -0.64 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.63 | -0.63 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises SCAI's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without STARD9 | 0.008 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SCAI's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF702P]] | B | ZNF702P activity lowers SCAI's level | lines that do not express ZNF702P (24) vs lines expressing it (26) | 1.21× higher at baseline in the lines without ZNF702P | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33 |
| [[DNMT3B]] | C | DNMT3B activity raises SCAI's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without DNMT3B | 0.051 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[HACE1]] | C | HACE1 activity raises SCAI's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without HACE1 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.757). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.7, -12.3); signed map (-39.2, -0.1). **Vector** length 118, 36.5% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.2 | +14.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.3 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +10.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +4.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -8.8 | -18.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -8.1 | -17.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.0 | -13.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.3 | -11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of cancer cell invasion |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,942,608-125,143,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36664, NET40; previously C9orf126 |
| Reactome | 4 pathways, smallest: RHO GTPases Activate Formins; RHO GTPase Effectors; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9R8](https://www.uniprot.org/uniprotkb/Q8N9R8) (Protein SCAI):

> Tumor suppressor which functions to suppress MRTFA-induced SRF transcriptional activity. May function in the RHOA-DIAPH1 signal transduction pathway and regulate cell migration through transcriptional regulation of ITGB1.

**Summary**, from NCBI Gene [286205](https://www.ncbi.nlm.nih.gov/gene/286205):

> This gene encodes a regulator of cell migration. The encoded protein appears to function in the RhoA (ras homolog gene family, member A)-Dia1 (diaphanous homolog 1) signal transduction pathway. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:26709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26709) · Entrez [286205](https://www.ncbi.nlm.nih.gov/gene/286205) · UniProt [Q8N9R8](https://www.uniprot.org/uniprotkb/Q8N9R8) · Ensembl [ENSG00000173611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173611)

## Data

Gene col 10409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10409); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10409]; `tensor/DDL_lfc|DDL_z.npy` [10409]; `embed/gene_vectors.npy` [10409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10409 or target_col == 10409). Every well: [[SCAI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
