---
symbol: "ACLY"
type: "gene"
col: 5215
ensembl_id: "ENSG00000131473"
name: "ATP citrate lyase"
location: "17q21.2"
module: 12
arm: "-"
pooled_cpm: 83.4
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ACLY

*ATP citrate lyase* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.22× (z +29.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.597× (z -9.1, q 8e-17, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.684× (z -6.7, q 5e-09, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FASN]] (+0.72, fdr 7e-06), [[BLTP2]] (+0.63, fdr 7e-06), [[PTDSS1]] (+0.63, fdr 1e-05); moves opposite to [[SEC62]] (-0.64, fdr 1e-05), [[COIL]] (-0.62, fdr 2e-05), [[SMIM26]] (-0.60, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPS18B]] (-0.60, fdr 2e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.22×** | +29.0 | 0e+00 | 48/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.63×** | +16.3 | 0e+00 | 41/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.46×** | +15.8 | 0e+00 | 46/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +13.5 | 3e-39 | 44/50 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +12.5 | 5e-34 | 41/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.91×** | +10.5 | 1e-23 | 37/45 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.42×** | +8.6 | 5e-16 | 39/48 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.59×** | +8.1 | 4e-14 | 37/48 (CFPAC-1, HT-29, …) | two highest doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +6.7 | 1e-09 | 34/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | **1.31×** | +6.6 | 3e-09 | 34/49 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.45×** | +6.5 | 5e-09 | 28/48 (CFPAC-1, HT-29, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.38×** | +5.7 | 7e-07 | 27/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +5.4 | 3e-06 | 26/48 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.36×** | +5.2 | 1e-05 | 27/47 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 22/48 (HEC-1-A, Panc 03.27, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.032 | 18/48 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.032 | 19/48 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.042 | 13/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Lopinavir (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.065 | 9/48 (NCI-H2347, SW480, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.097 | 17/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -9.1 | 8e-17 | 37/48 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.684×** | -6.7 | 5e-09 | 29/48 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.685×** | -6.7 | 5e-09 | 28/48 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -5.9 | 7e-07 | 31/48 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.715×** | -5.7 | 2e-06 | 28/48 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.786×** | -4.3 | 0.002 | 24/48 (C32, RPMI-7951, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.851× | -4.0 | 0.004 | 15/48 (LoVo, Panc 03.27, …) | rises with dose | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.788×** | -4.0 | 0.005 | 24/48 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.806×** | -3.8 | 0.009 | 24/48 (A-172, A-427, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.873× | -3.4 | 0.037 | 14/48 (PANC-1, SNU-1, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.874× | -3.4 | 0.037 | 19/48 (C32, hTERT-HPNE, …) | all doses, flat | low cells (technical?) |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.831×** | -3.3 | 0.048 | 13/48 (KATO III, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.825×** | -3.3 | 0.048 | 23/47 (SNU-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.2 | 0.052 | 22/48 (A-427, A-172, …) | all doses, flat | composition shift |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.886× | -3.0 | 0.089 | 7/49 (KATO III, SNU-423, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.888× | -3.0 | 0.096 | 8/49 (HEC-1-A, HS-578T, …) | all doses, flat |  |
| [[Tolcapone (drug)]] 5 µM |  | 0.889× | -2.9 | 0.096 | 4/49 (SW48, SW 900, …) | top dose only | position effect removed |
| [[AZD-8055 (drug)]] 5 µM |  | **0.728×** | -2.9 | 0.096 | 11/49 (HEC-1-A, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.848× | -2.9 | 0.096 | 14/48 (J82, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 145 | 3 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -16.1) |
| [[HT-29 (line)]] | alt | 66.7 | 8 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +22.0) | — |
| [[NCI-H23 (line)]] | alt | 77.4 | 6 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +14.4) | [[Harringtonine (drug)]] 5 µM 0.305× (z -11.5) |
| [[BT-474 (line)]] | alt | 92.1 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 43.4 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +23.6) | — |
| [[HEC-1-A (line)]] | alt | 80.8 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +26.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 86.8 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +27.8) | — |
| [[NCI-H460 (line)]] | wt | 63.3 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +28.3) | — |
| [[Panc 03.27 (line)]] | alt | 61.2 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +27.7) | — |
| [[PANC-1 (line)]] | alt | 56.8 | 3 (2 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +18.2) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -12.2) |
| [[HOP62 (line)]] | alt | 75.1 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 110 | 5 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.471× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 48.7 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +14.9) | — |
| [[SW480 (line)]] | alt | 65.8 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +27.9) | — |
| [[C32 (line)]] | wt | 130 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -11.9) |
| [[J82 (line)]] | alt | 82.3 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 58.0 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +14.2) | — |
| [[SW1417 (line)]] | alt | 70.4 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +18.6) | — |
| [[C-33 A (line)]] | alt | 102 | 4 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 3.29× (z +14.8) | — |
| [[LS 180 (line)]] | wt | 52.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +18.0) | — |
| [[NCI-H2030 (line)]] | alt | 143 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +16.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 60.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 55.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +14.3) | — |
| [[A-427 (line)]] | wt | 143 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -20.7) |
| [[A549 (line)]] | wt | 165 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 42.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +17.8) | — |
| [[SHP-77 (line)]] | alt | 67.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 142 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.381× (z -10.8) |
| [[A498 (line)]] | wt | 185 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 36.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +13.6) | — |
| [[H4 (line)]] | wt | 67.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 53.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 129 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.7) | — |
| [[KATO III (line)]] | alt | 88.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +17.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -9.1) |
| [[LoVo (line)]] | wt | 52.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +22.0) | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +18.7) | — |
| [[NCI-H596 (line)]] | alt | 70.5 | 1 | 1 (1 ⚠) | [[Atazanavir (sulfate) (drug)]] 0.05 µM 4.44× (z +11.4) | [[Pentoxifylline (drug)]] 0.05 µM 0.281× (z -9.9) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 73.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 62.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +11.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -10.3) |
| [[SW 1271 (line)]] | alt | 61.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +9.8) | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0809× (z -9.0) |
| [[AN3 CA (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.242× (z -8.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 27.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +15.5) | — |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 68.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +16.4) | — |
| [[NCI-H661 (line)]] | alt | 71.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0811× (z -11.0) |
| [[RKO (line)]] | wt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +18.1) | — |
| [[SW48 (line)]] | wt | 69.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +14.7) | — |
| [[NCI-H2122 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FASN]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 | same gene group; pathway: ChREBP activates metabolic gene expression; STRING 994 |
| [[BLTP2]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PTDSS1]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[FADS2]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 514 |
| [[AKT1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 | STRING 711 |
| [[BPNT2]] | +0.61 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[COLGALT1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[G6PD]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 785 |
| [[PPIA]] | +0.59 | +0.53 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ADAM15]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[NSDHL]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 | STRING 415 |

## Genes that move opposite

*47 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC62]] | -0.64 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[COIL]] | -0.62 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | -0.60 | -0.53 / -0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18B]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[MRPS18C]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[CROCCP2-1]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[LIPT1]] | -0.59 | -0.47 / -0.65 | both halves | 2e-05 | same gene group |
| [[SRSF11]] ⚠ | -0.59 | -0.50 / -0.60 | both halves | 1e-05 | STRING 411; ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[RAB9A]] | -0.59 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[KRT10]] ⚠ | -0.59 | -0.50 / -0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAT2]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[VAMP2]] | -0.58 | -0.46 / -0.59 | both halves | 2e-05 | pathway: Integration of energy metabolism |
| [[MAP2K7]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ATP5MC2]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (20.5, -50.8); signed map (-51.0, 30.8). **Vector** length 138, 45.9% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +29.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +13.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.8 | +16.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +5.4 | +8.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.7 | +6.6 |
|  | [[Posaconazole (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.3 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.2 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -0.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ATP citrate lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,866,917-41,930,542 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPCL, CLATP, ACL |
| Gene groups (HGNC) | Acyltransferases |
| Hallmark sets | ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: ChREBP activates metabolic gene expression; Fatty acyl-CoA biosynthesis; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P53396](https://www.uniprot.org/uniprotkb/P53396) (ATP-citrate synthase):

> Catalyzes the cleavage of citrate into oxaloacetate and acetyl-CoA, the latter serving as common substrate in multiple biochemical reactions in protein, carbohydrate and lipid metabolism.

**Summary**, from NCBI Gene [47](https://www.ncbi.nlm.nih.gov/gene/47):

> ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several important biosynthetic pathways, including lipogenesis and cholesterogenesis. In nervous tissue, ATP …

**Accessions** — [HGNC:115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:115) · Entrez [47](https://www.ncbi.nlm.nih.gov/gene/47) · UniProt [P53396](https://www.uniprot.org/uniprotkb/P53396) · Ensembl [ENSG00000131473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131473)

## Data

Gene col 5215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5215); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5215]; `tensor/DDL_lfc|DDL_z.npy` [5215]; `embed/gene_vectors.npy` [5215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5215 or target_col == 5215). Every well: [[ACLY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACLY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
