---
symbol: "DDX1"
type: "gene"
col: 1264
ensembl_id: "ENSG00000079785"
name: "DEAD-box helicase 1"
location: "2p24.3"
module: 28
arm: "+"
pooled_cpm: 133.61
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# DDX1

*DEAD-box helicase 1* — 2p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.35× (z +18.2, q 0e+00, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.21× (z +4.1, q 0.003, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.502× (z -20.6, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1]] (+0.80, fdr 7e-06), [[SLC25A46]] (+0.77, fdr 7e-06), [[SMARCE1]] (+0.71, fdr 7e-06); moves opposite to [[TPTEP2-CSNK1E]] (-0.64, fdr 7e-06), [[HIGD2A]] (-0.63, fdr 1e-05), [[TAF4]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[palbociclib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +18.2 | 0e+00 | 44/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +14.9 | 0e+00 | 41/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +11.4 | 7e-28 | 40/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.58×** | +9.4 | 6e-19 | 39/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +8.9 | 7e-17 | 43/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.29×** | +7.7 | 1e-12 | 34/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +5.7 | 9e-07 | 34/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.003 | 22/48 (PANC-1, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.44×** | +4.0 | 0.004 | 26/47 (A498, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **1.20×** | +3.9 | 0.004 | 23/48 (SW480, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.006 | 22/49 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.006 | 26/48 (KATO III, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.010 | 20/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.016 | 22/48 (NCI-H460, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.023 | 23/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.034 | 15/48 (NCI-H460, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.2 | 0.036 | 15/48 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.086 | 16/48 (PANC-1, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.502×** | -20.6 | 0e+00 | 44/49 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.735×** | -6.5 | 2e-08 | 31/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.748×** | -6.1 | 1e-07 | 36/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.748×** | -6.1 | 1e-07 | 31/48 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.756×** | -5.9 | 3e-07 | 33/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -5.6 | 2e-06 | 31/48 (A498, H4, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.2 | 0.12 | 17/48 (A498, HOP62, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.0 | 0.19 | 14/48 (A498, HOP62, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 110 | 4 (4 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +11.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 131 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +12.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.0) |
| [[A498 (line)]] | wt | 201 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +12.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -20.3) |
| [[HOP62 (line)]] | alt | 128 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -15.0) |
| [[SW480 (line)]] | alt | 130 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +17.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -16.6) |
| [[MIA PaCa-2 (line)]] | alt | 128 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +15.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 87.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 119 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +20.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -14.1) |
| [[A549 (line)]] | wt | 139 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +13.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 87.0 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.3) ⚠ cell-cycle shift, explains ~93% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -14.3) |
| [[Hs 766T (line)]] | wt | 85.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.6) |
| [[HS-578T (line)]] | alt | 84.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 83.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.4) |
| [[J82 (line)]] | alt | 78.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 90.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +17.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -14.0) |
| [[SHP-77 (line)]] | alt | 197 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +12.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 147 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +11.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.2) |
| [[SNU-423 (line)]] | alt | 99.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 107 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.3) |
| [[A-427 (line)]] | wt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +12.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 96.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -19.0) |
| [[C-33 A (line)]] | alt | 75.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +12.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 103 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -12.1) |
| [[HCT15 (line)]] | alt | 141 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.0) |
| [[KATO III (line)]] | alt | 117 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +11.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 71.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +13.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 139 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 87.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -13.0) |
| [[PANC-1 (line)]] | alt | 94.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +17.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 98.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.4) ⚠ cell-cycle shift, explains ~93% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -22.0) |
| [[A-172 (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +11.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 96.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -9.8) |
| [[CHP-212 (line)]] | wt | 6,325 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -14.9) |
| [[COLO 205 (line)]] | alt | 69.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.1) |
| [[H4 (line)]] | wt | 76.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 89.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 91.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +11.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -17.3) |
| [[SNU-1 (line)]] | wt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -18.6) |
| [[SW 900 (line)]] | alt | 86.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.5) |
| [[SW1417 (line)]] | alt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.3) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 | STRING 476 |
| [[SLC25A46]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[SF3A3]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.69 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PWP1]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 | STRING 403 |
| [[NUDT9]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[DBT]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.67 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[SRP72]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[GTF2H3]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP2-CSNK1E]] | -0.64 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[HIGD2A]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[TAF4]] | -0.59 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[WDR20]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CASTOR3P]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.57 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[PDE6D]] | -0.57 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[TMEM41A]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[UBL5]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[COPS9]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[POU2F1]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[NFATC2IP-AS1]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[palbociclib (drug)]] 5 µM | C | DDX1's natural level lowers the cells' numbers under palbociclib 5 µM (makes them more sensitive) | DDX1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.024 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Binimetinib (drug)]] 0.05 µM | C | DDX1's natural level lowers the cells' numbers under Binimetinib 0.05 µM (makes them more sensitive) | DDX1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.2, 3.5); signed map (7.1, -26.0). **Vector** length 120, 36.4% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +9.9 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +7.2 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.2 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.3 | +5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.7 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.9 | -20.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.0 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.1 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.3 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -0.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.2 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.3 — chr2:15,591,178-15,634,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSLIG6, DBP-RB |
| Gene groups (HGNC) | DEAD-box helicases; tRNA splicing ligase complex |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92499](https://www.uniprot.org/uniprotkb/Q92499) (ATP-dependent RNA helicase DDX1):

> Acts as an ATP-dependent RNA helicase, able to unwind both RNA-RNA and RNA-DNA duplexes. Possesses 5' single-stranded RNA overhang nuclease activity. Possesses ATPase activity on various RNA, but not DNA polynucleotides. May play a role in RNA clearance at DNA double-strand breaks (DSBs), thereby facilitating the template-guided repair of transcriptionally active regions of the genome. Together with RELA, acts as a coactivator to enhance NF-kappa-B-mediated transcriptional activation. Acts as a …

**Summary**, from NCBI Gene [1653](https://www.ncbi.nlm.nih.gov/gene/1653):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:2734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2734) · Entrez [1653](https://www.ncbi.nlm.nih.gov/gene/1653) · UniProt [Q92499](https://www.uniprot.org/uniprotkb/Q92499) · Ensembl [ENSG00000079785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079785)

## Data

Gene col 1264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1264); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1264]; `tensor/DDL_lfc|DDL_z.npy` [1264]; `embed/gene_vectors.npy` [1264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1264 or target_col == 1264). Every well: [[DDX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
