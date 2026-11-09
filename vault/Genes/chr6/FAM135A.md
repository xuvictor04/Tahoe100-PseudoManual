---
symbol: "FAM135A"
type: "gene"
col: 1343
ensembl_id: "ENSG00000082269"
name: "family with sequence similarity 135 member A"
location: "6q13"
module: 18
arm: "+"
pooled_cpm: 105.15
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FAM135A

*family with sequence similarity 135 member A* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.35× (z +9.0, q 9e-17, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.593× (z -15.9, q 0e+00, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.583× (z -6.1, q 1e-07, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.129×, LoVo 0.193×, KATO III 0.182×, PANC-1 0.233×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 0.0785×, KATO III 0.144×, HepG2/C3A 0.170×, NCI-H2030 0.222×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 0.216×, C32 0.217×, PANC-1 0.396×; ⚠ cell-cycle shift, explains ~54% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.309×); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.302×); [[Decitabine (drug)]] 0.05 µM in 1 line (SW 1271 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM164]] (+0.61, fdr 1e-05), [[CAMKMT]] (+0.60, fdr 1e-05), [[PHKA1]] (+0.59, fdr 1e-05); moves opposite to [[TEF]] (-0.56, fdr 1e-05), [[GORAB]] (-0.52, fdr 4e-05), [[GNL1]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[AFF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +9.0 | 9e-17 | 32/46 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.48×** | +8.0 | 3e-13 | 34/45 (NCI-H23, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +7.9 | 4e-13 | 29/46 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.27×** | +7.3 | 4e-11 | 25/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.1 | 1e-10 | 29/45 (HOP62, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.7 | 2e-09 | 33/46 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +6.5 | 6e-09 | 25/46 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +5.6 | 1e-06 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.6 | 1e-06 | 20/46 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +5.4 | 5e-06 | 23/47 (HEC-1-A, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 6e-06 | 21/47 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 9e-06 | 24/46 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 9e-05 | 22/46 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.52×** | +4.7 | 1e-04 | 21/41 (NCI-H23, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.23×** | +4.5 | 3e-04 | 21/46 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 4e-04 | 22/46 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +4.3 | 4e-04 | 20/46 (Hs 766T, NCI-H2030, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 4e-04 | 19/46 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 19/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.005 | 20/45 (Hs 766T, NCI-H2030, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.13× | +3.7 | 0.005 | 17/46 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.011 | 19/45 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.014 | 15/46 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1343.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.129×, LoVo 0.193×, KATO III 0.182×, PANC-1 0.233×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 0.0785×, KATO III 0.144×, HepG2/C3A 0.170×, NCI-H2030 0.222×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 0.216×, C32 0.217×, PANC-1 0.396×; ⚠ cell-cycle shift, explains ~54% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.309×); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.302×); [[Decitabine (drug)]] 0.05 µM in 1 line (SW 1271 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.593×** | -15.9 | 0e+00 | 36/46 (HepG2/C3A, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.481×** | -15.7 | 0e+00 | 40/47 (SHP-77, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -11.4 | 1e-27 | 34/42 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.604×** | -10.0 | 1e-21 | 31/43 (NCI-H2030, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.704×** | -7.6 | 4e-12 | 30/45 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.710×** | -7.1 | 1e-10 | 26/46 (AN3 CA, C32, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -6.1 | 1e-07 | 31/47 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.5 | 5e-04 | 20/46 (Panc 03.27, HT-29, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.817×** | -4.4 | 8e-04 | 22/46 (PANC-1, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.831×** | -4.0 | 0.003 | 18/46 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.708×** | -3.9 | 0.005 | 19/45 (KATO III, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.8 | 0.007 | 1/48 (NCI-H2122) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.861× | -3.2 | 0.051 | 18/46 (BT-474, A498, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.900× | -3.2 | 0.051 | 11/46 (PANC-1, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.863× | -3.2 | 0.055 | 15/46 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.821×** | -3.0 | 0.085 | 16/46 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.908× | -3.0 | 0.097 | 2/47 (Panc 03.27, COLO 205) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 465 | 0 | 13 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -22.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.309× (z -12.4) |
| [[PANC-1 (line)]] | alt | 211 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.302× (z -8.8) |
| [[KATO III (line)]] | alt | 324 | 1 | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.23× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -24.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 89.7 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -20.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[COLO 205 (line)]] | alt | 75.2 | 3 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.40× (z +11.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.51× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HT-29 (line)]] | alt | 303 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +10.3) ⚠ cell-cycle shift, explains ~93% of this change | [[Dinaciclib (drug)]] 5 µM 0.327× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 173 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -21.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 215 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -20.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 73.6 | 2 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AN3 CA (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0685× (z -18.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[LOX-IMVI (line)]] | wt | 81.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -24.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 96.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 119 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 164 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -16.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SK-MEL-2 (line)]] | alt | 90.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -18.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 72.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.356× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 90.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -12.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -14.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 57.7 | 2 | 0 | [[Budesonide (drug)]] 5 µM 3.06× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 35.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +15.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 81.7 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.87× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0785× (z -31.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 76.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 55.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AsPC-1 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 92.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HCT15 (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 70.0 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.24× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.39× (z +13.6) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW 1271 (line)]] | alt | 77.9 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.101× (z -8.5) |
| [[SW480 (line)]] | alt | 86.7 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 25.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM164]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CAMKMT]] | +0.60 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[PHKA1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[STIM1]] | +0.57 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[SGPP1]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[HS2ST1]] | +0.55 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TXN]] | +0.54 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[AHCYL2]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MEMO1]] | +0.54 | +0.62 / +0.40 | both halves | 4e-05 |  |
| [[PPP2R5E]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[RHBDD1]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[KIAA0232]] | +0.53 | +0.54 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEF]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[GORAB]] | -0.52 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[GNL1]] | -0.51 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[ZNF548]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TP53BP1]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[AFF3]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZNF20]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[FNBP1P1]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ZFHX2]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[AXL]] | -0.48 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[GRIK4]] | -0.48 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[SYNGAP1]] | -0.47 | -0.55 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFF3]] | B | AFF3 activity lowers FAM135A's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 2.18× higher at baseline in the lines without AFF3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[TOP2A]] | B | TOP2A activity lowers FAM135A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GCLC]] | C | GCLC activity raises FAM135A's level | lines that do not express GCLC (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without GCLC | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRC8B; maybe low, not absent |
| [[ARHGEF11]] | C | ARHGEF11's natural level strengthens FAM135A's drug response | ARHGEF11's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.12; direction clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.2, -8.2); signed map (-46.4, -6.8). **Vector** length 122, 35.5% of its response variance represented; |z| ≥ 3 in 1,379 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.1 | +8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.8 | +5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.3 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +9.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.9 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.6 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.4 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -12.6 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -7.4 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.1 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +0.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 135 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:70,412,941-70,561,174 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20176; previously KIAA1411 |
| Reactome | 4 pathways, smallest: RND1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

UniProt [Q9P2D6](https://www.uniprot.org/uniprotkb/Q9P2D6) carries no function annotation.

**Summary**, from NCBI Gene [57579](https://www.ncbi.nlm.nih.gov/gene/57579):

> Predicted to be involved in lipid metabolic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21084) · Entrez [57579](https://www.ncbi.nlm.nih.gov/gene/57579) · UniProt [Q9P2D6](https://www.uniprot.org/uniprotkb/Q9P2D6) · Ensembl [ENSG00000082269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082269)

## Data

Gene col 1343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1343); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1343]; `tensor/DDL_lfc|DDL_z.npy` [1343]; `embed/gene_vectors.npy` [1343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1343 or target_col == 1343). Every well: [[FAM135A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM135A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
