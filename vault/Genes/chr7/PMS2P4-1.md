---
symbol: "PMS2P4-1"
type: "gene"
col: 16612
ensembl_id: "ENSG00000291154"
name: ""
location: ""
module: 207
arm: "+"
pooled_cpm: 82.47
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 42
n_dd_up_clean: 4
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# PMS2P4-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.73× (z +39.8, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.290× (z -25.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLE1]] (+0.72, fdr 7e-06), [[TSNAX-DISC1]] (+0.71, fdr 7e-06), [[RARS2]] (+0.70, fdr 7e-06); moves opposite to [[TMEM185B]] (-0.70, fdr 7e-06), [[PCNX2]] (-0.64, fdr 1e-05), [[SAYSD1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +39.8 | 0e+00 | 49/49 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +17.4 | 0e+00 | 44/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +11.7 | 2e-29 | 40/50 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.34×** | +6.3 | 4e-08 | 33/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +5.3 | 1e-05 | 23/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.4 | 8e-04 | 19/48 (SW1417, BT-474, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.002 | 19/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.20×** | +4.0 | 0.005 | 20/49 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.18× | +3.5 | 0.025 | 16/48 (BT-474, AsPC-1, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.076 | 13/48 (COLO 205, A-427, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.078 | 13/48 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.16× | +3.1 | 0.078 | 11/50 (C32, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 24 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.290×** | -25.4 | 0e+00 | 47/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.496×** | -21.2 | 0e+00 | 41/48 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.414×** | -18.8 | 0e+00 | 46/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.427×** | -18.2 | 0e+00 | 47/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.431×** | -18.0 | 0e+00 | 45/48 (H4, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.446×** | -17.2 | 0e+00 | 45/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.447×** | -17.2 | 0e+00 | 42/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.456×** | -16.1 | 0e+00 | 33/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.465×** | -15.7 | 0e+00 | 40/47 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.463×** | -15.4 | 0e+00 | 43/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.480×** | -14.5 | 1e-45 | 35/44 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.285×** | -14.0 | 5e-43 | 46/49 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.307×** | -13.2 | 5e-38 | 44/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.574×** | -11.1 | 4e-27 | 38/48 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -9.2 | 1e-18 | 41/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -8.3 | 3e-15 | 32/48 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -8.3 | 4e-15 | 36/48 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -8.0 | 3e-14 | 33/48 (H4, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.702×** | -7.5 | 1e-12 | 33/48 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -6.1 | 2e-08 | 28/48 (MIA PaCa-2, AN3 CA, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.756×** | -5.7 | 3e-07 | 26/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.699×** | -5.4 | 1e-06 | 29/48 (HEC-1-A, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.776×** | -5.4 | 1e-06 | 25/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.798×** | -4.8 | 3e-05 | 24/49 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 97.6 | 3 | 16 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +19.8) | [[Harringtonine (drug)]] 0.5 µM 0.128× (z -20.8) |
| [[A-172 (line)]] | wt | 133 | 2 | 13 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +25.7) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.205× (z -17.7) |
| [[H4 (line)]] | wt | 171 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -17.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.107× (z -16.2) |
| [[SW480 (line)]] | alt | 92.4 | 3 | 11 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +23.8) | [[Harringtonine (drug)]] 5 µM 0.239× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 86.9 | 2 | 11 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +13.2) | [[Harringtonine (drug)]] 5 µM 0.115× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 116 | 2 | 11 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +22.1) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -21.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.159× (z -20.6) |
| [[NCI-H1792 (line)]] | alt | 96.3 | 1 | 12 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +21.0) | [[Harringtonine (drug)]] 5 µM 0.0859× (z -24.4) |
| [[NCI-H460 (line)]] | wt | 56.8 | 3 | 10 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +29.1) | [[Harringtonine (drug)]] 0.5 µM 0.248× (z -17.6) |
| [[PANC-1 (line)]] | alt | 102 | 1 | 12 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +17.5) | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -10.3) |
| [[A549 (line)]] | wt | 104 | 1 | 11 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -27.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0990× (z -23.0) |
| [[HEC-1-A (line)]] | alt | 125 | 2 | 10 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +17.9) | [[Harringtonine (drug)]] 0.5 µM 0.297× (z -16.2) |
| [[HOP62 (line)]] | alt | 77.9 | 3 | 9 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +18.5) | [[Harringtonine (drug)]] 5 µM 0.148× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 95.4 | 1 | 11 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -17.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.183× (z -14.5) |
| [[A498 (line)]] | wt | 148 | 2 | 9 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +19.9) | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -28.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0952× (z -24.2) |
| [[SNU-423 (line)]] | alt | 64.8 | 2 | 9 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +20.8) | [[Harringtonine (drug)]] 5 µM 0.174× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 67.1 | 1 | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +23.1) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.271× (z -12.9) |
| [[Hs 766T (line)]] | wt | 134 | 1 | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +16.8) | [[Digitoxin (drug)]] 5 µM 0.190× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.229× (z -13.5) |
| [[SW 900 (line)]] | alt | 61.2 | 2 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +19.2) | [[Digitoxin (drug)]] 5 µM 0.179× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.169× (z -15.1) |
| [[SW1417 (line)]] | alt | 67.0 | 4 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +26.5) | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -17.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 67.2 | 3 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +27.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.301× (z -10.6) |
| [[C32 (line)]] | wt | 64.3 | 3 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +19.8) | [[Harringtonine (drug)]] 0.5 µM 0.194× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 46.1 | 3 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +22.2) | [[Harringtonine (drug)]] 0.5 µM 0.247× (z -13.2) |
| [[LS 180 (line)]] | wt | 46.0 | 3 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +16.9) | [[Harringtonine (drug)]] 5 µM 0.181× (z -15.1) |
| [[HCT15 (line)]] | alt | 154 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 97.9 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.243× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 141 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.267× (z -12.9) |
| [[BT-474 (line)]] | alt | 76.9 | 5 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +24.4) | [[PH-797804 (drug)]] 5 µM 0.194× (z -8.5) |
| [[HT-29 (line)]] | alt | 56.0 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +22.1) | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -8.7) |
| [[LoVo (line)]] | wt | 58.5 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.11× (z +26.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.272× (z -14.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.398× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 61.4 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +24.7) | [[Harringtonine (drug)]] 5 µM 0.280× (z -11.7) |
| [[COLO 205 (line)]] | alt | 63.9 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +16.7) | [[Harringtonine (drug)]] 5 µM 0.234× (z -11.3) |
| [[SW 1088 (line)]] | alt | 222 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0929× (z -10.9) |
| [[AN3 CA (line)]] | alt | 70.8 | 1 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.93× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0662× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.107× (z -12.0) |
| [[J82 (line)]] | alt | 55.8 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +16.0) | [[Harringtonine (drug)]] 5 µM 0.303× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 42.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +13.9) | [[Harringtonine (drug)]] 5 µM 0.237× (z -12.7) |
| [[RKO (line)]] | wt | 32.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +20.7) | — |
| [[SHP-77 (line)]] | alt | 87.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +21.9) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-1 (line)]] | wt | 91.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 43.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.320× (z -11.0) |
| [[C-33 A (line)]] | alt | 81.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.355× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 67.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 82.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 30.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +20.7) | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +15.8) | — |
| [[SW 1271 (line)]] | alt | 91.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.137× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~67% of this change |
| [[CHP-212 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[TSNAX-DISC1]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RARS2]] | +0.70 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[TTC28-AS1]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[COG7]] | +0.69 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[WDR20]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[MFSD8]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SRP54]] | +0.67 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[ZNF248]] | +0.67 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[SOS1]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[LEPR]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.70 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[PCNX2]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[SAYSD1]] | -0.63 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.62 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[N6AMT1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[UBE2E3]] | -0.61 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[COA7]] | -0.60 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[TSPYL5]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.60 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[ZNF518B]] | -0.59 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[AGPS]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[DHX9]] | -0.58 | -0.53 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PMS2P4-1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.837). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-14.3, 24.7); signed map (6.2, 3.5). **Vector** length 121, 44.4% of its response variance represented; |z| ≥ 3 in 1,650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.4 | +39.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.2 | +17.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +11.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +4.4 | +6.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | +3.0 | +4.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | +1.8 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.0 | -8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -8.9 | -16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -8.2 | -17.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.9 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -14.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -13.2 |

## What is on record

> [!warning] No registry record
> PMS2P4-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16612); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16612]; `tensor/DDL_lfc|DDL_z.npy` [16612]; `embed/gene_vectors.npy` [16612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16612 or target_col == 16612). Every well: [[PMS2P4-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMS2P4-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
