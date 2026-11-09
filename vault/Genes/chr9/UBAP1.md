---
symbol: "UBAP1"
type: "gene"
col: 9053
ensembl_id: "ENSG00000165006"
name: "ubiquitin associated protein 1"
location: "9p13.3"
module: 20
arm: "-"
pooled_cpm: 180.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# UBAP1

*ubiquitin associated protein 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.83× (z +13.5, q 5e-39, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.431× (z -18.8, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.708× (z -7.7, q 1e-12, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELF1]] (+0.61, fdr 4e-05), [[DUSP16]] (+0.56, fdr 3e-04), [[TMEM265]] (+0.56, fdr 1e-03, ⚠ one half only (not replicated)), [[USP53]] (+0.54, fdr 3e-05); moves opposite to [[ELAVL1]] (-0.57, fdr 1e-04), [[IPO5]] (-0.51, fdr 7e-05), [[PRKDC]] (-0.50, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TYMP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +13.5 | 5e-39 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +8.7 | 1e-15 | 38/48 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +8.1 | 8e-14 | 33/49 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.8 | 1e-12 | 34/48 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +7.7 | 2e-12 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +7.0 | 3e-10 | 36/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +6.3 | 3e-08 | 27/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.0 | 4e-05 | 28/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +5.0 | 4e-05 | 26/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 4e-05 | 26/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +4.2 | 0.002 | 21/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.008 | 20/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.5 | 0.023 | 13/49 (HT-29, LS 180, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.4 | 0.026 | 17/48 (KATO III, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -18.8 | 0e+00 | 45/49 (A-427, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -16.8 | 0e+00 | 41/44 (SW 900, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.499×** | -14.3 | 4e-44 | 41/45 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.550×** | -13.3 | 3e-38 | 44/48 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.562×** | -12.8 | 2e-35 | 42/48 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.655×** | -9.4 | 5e-19 | 40/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -7.7 | 1e-12 | 39/48 (NCI-H23, SW 900, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.784×** | -7.6 | 2e-12 | 30/49 (A549, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -6.7 | 1e-09 | 37/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.763×** | -6.0 | 1e-07 | 36/48 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.779×** | -5.5 | 1e-06 | 26/48 (NCI-H1792, BT-474, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.787×** | -5.3 | 5e-06 | 32/48 (BT-474, A549, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.844× | -5.3 | 5e-06 | 16/48 (CFPAC-1, NCI-H1792, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -5.0 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.809×** | -4.5 | 2e-04 | 26/50 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.825×** | -4.3 | 7e-04 | 23/48 (BT-474, KATO III, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.705×** | -4.1 | 0.002 | 26/49 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.828×** | -4.0 | 0.002 | 22/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.835× | -4.0 | 0.002 | 23/48 (NCI-H661, HCT15, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.873× | -3.0 | 0.070 | 11/48 (COLO 205, NCI-H1792, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.908× | -3.0 | 0.070 | 8/48 (NCI-H23, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.875× | -2.9 | 0.076 | 11/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.910× | -2.9 | 0.077 | 10/48 (SW 1271, A-172, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.877× | -2.9 | 0.082 | 7/48 (LoVo, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 164 | 8 (3 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -11.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 169 | 9 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 272 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.537× (z -12.2) |
| [[HT-29 (line)]] | alt | 189 | 4 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.94× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -14.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 195 | 1 | 8 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 201 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -18.2) |
| [[A-172 (line)]] | wt | 281 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -15.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.553× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 173 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -15.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 209 | 1 | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -15.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 232 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -23.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 266 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 170 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -8.8) |
| [[SW 900 (line)]] | alt | 277 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.432× (z -10.9) |
| [[A498 (line)]] | wt | 275 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 177 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.532× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 237 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 388 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 213 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 159 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -16.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 124 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -12.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 303 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -22.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 163 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.474× (z -8.9) |
| [[KATO III (line)]] | alt | 140 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -13.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 110 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +16.7) | — |
| [[NCI-H2030 (line)]] | alt | 138 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 229 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 126 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 153 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.81× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0716× (z -29.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 97.5 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.12× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -22.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -18.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -12.3) |
| [[SNU-1 (line)]] | wt | 139 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.6) | — |
| [[SW480 (line)]] | alt | 146 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.1) | — |
| [[C32 (line)]] | wt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -10.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 222 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.257× (z -9.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.458× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 141 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.230× (z -11.6) |
| [[AN3 CA (line)]] | alt | 161 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF1]] | +0.61 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[DUSP16]] | +0.56 | +0.29 / +0.66 | both halves | 3e-04 |  |
| [[TMEM265]] | +0.56 | +0.18 / +0.62 | ⚠ one half (not replicated) | 1e-03 |  |
| [[USP53]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SCAND1]] | +0.53 | +0.28 / +0.47 | both halves | 3e-04 |  |
| [[TYMP]] | +0.51 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[PNRC1]] | +0.51 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[WSB1]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[PAFAH1B1]] | +0.51 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[FAM53C]] | +0.50 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[SAP18]] | +0.50 | +0.27 / +0.48 | both halves | 3e-04 |  |
| [[WIPF2]] | +0.50 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[OFD1]] | +0.50 | +0.27 / +0.52 | both halves | 3e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAVL1]] | -0.57 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[IPO5]] | -0.51 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[PRKDC]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TXNDC5]] | -0.50 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[MACROH2A1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[GCN1]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[NSUN2]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[FAM120A]] | -0.48 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[CCAR2]] | -0.48 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[GMPS]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[RFT1]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DPYSL2]] | -0.46 | -0.14 / -0.48 | ⚠ not reproduced | 0.002 |  |
| [[FKBP9]] | -0.46 | -0.21 / -0.46 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TYMP]] | B | TYMP activity raises UBAP1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.29× lower at baseline in the lines without TYMP | 0.013 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[ADGRF4]] | B | ADGRF4 activity raises UBAP1's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without ADGRF4 | 0.051 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (31.9, -33.5); signed map (42.4, -4.0). **Vector** length 95.7, 33.4% of its response variance represented; |z| ≥ 3 in 1,416 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -7.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +5.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.0 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,179,005-34,252,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously UBAP |
| Gene groups (HGNC) | ESCRT-I |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ09](https://www.uniprot.org/uniprotkb/Q9NZ09) (Ubiquitin-associated protein 1):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process. Binds to ubiquitinated cargo proteins and is required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies (MVBs). Plays a role in the proteasomal degradation of ubiquitinated cell-surface proteins, such as EGFR and BST2.

**Summary**, from NCBI Gene [51271](https://www.ncbi.nlm.nih.gov/gene/51271):

> This gene is a member of the UBA domain family, whose members include proteins having connections to ubiquitin and the ubiquitination pathway. The ubiquitin associated domain is thought to be a non-covalent ubiquitin binding domain consisting of a compact three helix bundle. This particular protein originates from a gene locus in a refined region on chromosome 9 undergoing loss of heterozygosity in nasopharyngeal carcinoma (NPC). Taking into account its cytogenetic location, this UBA domain …

**Accessions** — [HGNC:12461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12461) · Entrez [51271](https://www.ncbi.nlm.nih.gov/gene/51271) · UniProt [Q9NZ09](https://www.uniprot.org/uniprotkb/Q9NZ09) · Ensembl [ENSG00000165006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165006)

## Data

Gene col 9053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9053); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9053]; `tensor/DDL_lfc|DDL_z.npy` [9053]; `embed/gene_vectors.npy` [9053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9053 or target_col == 9053). Every well: [[UBAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
