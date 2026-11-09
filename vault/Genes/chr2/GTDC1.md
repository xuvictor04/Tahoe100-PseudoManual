---
symbol: "GTDC1"
type: "gene"
col: 4310
ensembl_id: "ENSG00000121964"
name: "queuosine-tRNA mannosyltransferase"
location: "2q22.3"
module: 23
arm: "-"
pooled_cpm: 88.01
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GTDC1

*queuosine-tRNA mannosyltransferase* — 2q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +14.4, q 6e-44, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.562× (z -18.8, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R2A]] (+0.62, fdr 1e-05), [[MIPOL1]] (+0.56, fdr 3e-05), [[FGGY]] (+0.55, fdr 1e-04); moves opposite to [[KIAA0753]] (-0.61, fdr 3e-05), [[GPALPP1]] (-0.57, fdr 5e-05), [[ATXN1L]] (-0.56, fdr 8e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +14.4 | 6e-44 | 45/48 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +7.7 | 5e-12 | 33/49 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +7.1 | 3e-10 | 28/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +6.8 | 1e-09 | 27/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +6.3 | 3e-08 | 34/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +4.4 | 0.001 | 24/50 (A-172, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.9 | 0.008 | 17/48 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.018 | 16/47 (C32, H4, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.043 | 14/48 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.086 | 16/47 (SK-MEL-2, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -18.8 | 0e+00 | 42/49 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.467×** | -17.5 | 0e+00 | 45/48 (C32, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.533×** | -13.8 | 4e-41 | 41/49 (A-427, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.548×** | -13.3 | 3e-38 | 35/44 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.717×** | -10.8 | 4e-25 | 29/48 (NCI-H1792, NCI-H1573, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -10.1 | 5e-22 | 38/48 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -9.7 | 2e-20 | 34/50 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.782×** | -8.0 | 9e-14 | 32/48 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.706×** | -7.4 | 8e-12 | 27/44 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -7.2 | 4e-11 | 32/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.732×** | -7.2 | 4e-11 | 31/48 (NCI-H2030, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.746×** | -6.5 | 5e-09 | 28/48 (NCI-H1792, NCI-H23, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.824×** | -6.3 | 1e-08 | 26/48 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.782×** | -5.6 | 7e-07 | 28/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.788×** | -5.5 | 2e-06 | 26/48 (HepG2/C3A, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.794×** | -5.3 | 5e-06 | 27/48 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.716×** | -4.0 | 0.002 | 19/48 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.893× | -3.6 | 0.007 | 9/49 (HOP62, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.861× | -3.4 | 0.015 | 16/48 (SW 900, A498, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.870× | -3.1 | 0.043 | 15/49 (SW1417, KATO III, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.913× | -2.9 | 0.063 | 3/49 (COLO 205, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.825×** | -2.9 | 0.063 | 10/48 (SW 1271, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.878× | -2.8 | 0.079 | 13/48 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.831×** | -2.8 | 0.080 | 9/48 (NCI-H661, HEC-1-A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 82.5 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0945× (z -26.9) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 254 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -21.7) |
| [[NCI-H23 (line)]] | alt | 186 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0775× (z -32.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -19.9) |
| [[A498 (line)]] | wt | 84.7 | 5 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.444× (z -9.7) |
| [[J82 (line)]] | alt | 102 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.375× (z -13.5) |
| [[C32 (line)]] | wt | 104 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.222× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 170 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -18.1) |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 73.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.3) |
| [[PANC-1 (line)]] | alt | 82.0 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.7) |
| [[SW 900 (line)]] | alt | 115 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.2) |
| [[SW480 (line)]] | alt | 53.1 | 1 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.04× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.290× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -18.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.0) |
| [[SW1417 (line)]] | alt | 56.0 | 2 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.32× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.0) |
| [[HS-578T (line)]] | alt | 86.0 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.237× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 67.7 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.42× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -12.7) |
| [[SW48 (line)]] | wt | 75.3 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.244× (z -11.2) |
| [[A-172 (line)]] | wt | 48.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +19.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.90× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 50.1 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.20× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 57.4 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.47× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -11.6) |
| [[A-427 (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 56.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.0) ⚠ cell-cycle shift, explains ~36% of this change | [[Auranofin (drug)]] 5 µM 0.306× (z -12.3) |
| [[HT-29 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.323× (z -11.6) |
| [[LS 180 (line)]] | wt | 80.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.54× (z +15.3) | — |
| [[RKO (line)]] | wt | 41.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.03× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 86.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -9.6) |
| [[A549 (line)]] | wt | 88.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -17.0) |
| [[COLO 205 (line)]] | alt | 81.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 49.6 | 0 | 1 | — | [[DTP3 (drug)]] 5 µM 0.0861× (z -9.0) |
| [[LoVo (line)]] | wt | 45.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.350× (z -10.2) |
| [[SNU-1 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 74.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.1) |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0555× (z -12.7) |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R2A]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MIPOL1]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[FGGY]] | +0.55 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[SMYD3]] | +0.54 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[SPIDR]] | +0.54 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[XPR1]] | +0.53 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[CLYBL]] | +0.51 | +0.34 / +0.40 | both halves | 1e-04 |  |
| [[TRAK1]] | +0.51 | +0.44 / +0.36 | both halves | 9e-05 |  |
| [[FRY]] | +0.50 | +0.26 / +0.42 | both halves | 4e-04 |  |
| [[MRTFA]] | +0.50 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[STK3]] | +0.50 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[NEDD9]] | +0.50 | +0.39 / +0.40 | both halves | 6e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0753]] | -0.61 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[GPALPP1]] | -0.57 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ATXN1L]] | -0.56 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[DVL3]] | -0.52 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[CENPL]] | -0.51 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[ANXA2R-OT1]] | -0.51 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | -0.51 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[IRF3]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[C5orf34]] | -0.50 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ACOX1]] | -0.50 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[C1orf54]] | -0.49 | -0.21 / -0.46 | both halves | 6e-04 |  |
| [[ACAD9]] | -0.49 | -0.20 / -0.44 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GTDC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GTDC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-5.2, 18.3); signed map (-12.9, -52.4). **Vector** length 111, 31.8% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.3 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -18.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -17.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.1 | -6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -8.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.6 | -1.7 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.9 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | queuosine-tRNA mannosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.3 — chr2:143,938,068-144,332,568 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11753, Hmat-Xa; previously GTDC1 |
| Gene groups (HGNC) | Glycosyl transferases group 1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4AE62](https://www.uniprot.org/uniprotkb/Q4AE62) (tRNA-queuosine alpha-mannosyltransferase):

> Glycosyltransferase that specifically catalyzes mannosylation of cytoplasmic tRNA(Asp) modified with queuosine at position 34 (queuosine(34)). Mannosylates the cyclopentene moiety of queuosine(34) in tRNA(Asp) to form mannosyl-queuosine(34). Mannosylation of queuosine(34) in tRNA(Asp) is required to slow-down elongation at cognate codons, GAC and GAU, thereby regulating protein translation.

**Summary**, from NCBI Gene [79712](https://www.ncbi.nlm.nih.gov/gene/79712):

> Enables tRNA-queuosine(34) beta-mannosyltransferase activity. Involved in regulation of translation and tRNA wobble guanine modification. Located in nucleus. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20887) · Entrez [79712](https://www.ncbi.nlm.nih.gov/gene/79712) · UniProt [Q4AE62](https://www.uniprot.org/uniprotkb/Q4AE62) · Ensembl [ENSG00000121964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121964)

## Data

Gene col 4310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4310); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4310]; `tensor/DDL_lfc|DDL_z.npy` [4310]; `embed/gene_vectors.npy` [4310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4310 or target_col == 4310). Every well: [[GTDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
