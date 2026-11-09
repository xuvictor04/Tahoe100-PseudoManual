---
symbol: "PPM1B"
type: "gene"
col: 6111
ensembl_id: "ENSG00000138032"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1B"
location: "2p21"
module: 145
arm: "+"
pooled_cpm: 101.86
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# PPM1B

*protein phosphatase, Mg2+/Mn2+ dependent 1B* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +19.5, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.541× (z -12.0, q 2e-30, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.803× (z -6.3, q 6e-08, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELF2]] (+0.65, fdr 7e-06), [[RNF38]] (+0.64, fdr 7e-06), [[RANBP9]] (+0.59, fdr 1e-05); moves opposite to [[TAF1A]] (-0.58, fdr 1e-05), [[BMS1]] (-0.57, fdr 3e-05), [[ULBP3]] (-0.54, fdr 4e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +19.5 | 0e+00 | 44/49 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.30×** | +16.9 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +13.2 | 2e-37 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +12.5 | 1e-33 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.81×** | +12.0 | 3e-31 | 46/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +11.4 | 3e-28 | 41/48 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +10.1 | 5e-22 | 39/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +9.9 | 2e-21 | 41/48 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +9.7 | 2e-20 | 35/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +9.3 | 7e-19 | 38/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.7 | 1e-16 | 33/50 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +8.1 | 2e-14 | 36/48 (A549, A498, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +7.4 | 4e-12 | 35/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.9 | 2e-10 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +5.9 | 1e-07 | 29/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +5.2 | 6e-06 | 25/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +5.1 | 1e-05 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.8 | 0.004 | 15/49 (A-172, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -12.0 | 2e-30 | 31/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.632×** | -9.3 | 3e-18 | 39/49 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -6.3 | 6e-08 | 23/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.728×** | -6.0 | 3e-07 | 30/45 (RKO, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.814×** | -5.9 | 4e-07 | 23/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.791×** | -4.8 | 2e-04 | 27/49 (CHP-212, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.804×** | -4.4 | 7e-04 | 23/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.822×** | -4.0 | 0.005 | 24/49 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.826×** | -3.9 | 0.007 | 22/48 (RPMI-7951, NCI-H661, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.011 | 16/47 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.848× | -3.4 | 0.041 | 20/48 (COLO 205, SNU-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.900× | -3.0 | 0.12 | 8/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 169 | 9 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.0766× (z -31.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 92.1 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +17.3) | — |
| [[PANC-1 (line)]] | alt | 83.5 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +19.5) | — |
| [[SW480 (line)]] | alt | 120 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -15.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 77.4 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +14.8) | — |
| [[LoVo (line)]] | wt | 82.3 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -12.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 82.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +24.7) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 5 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 88.1 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +12.5) | — |
| [[A-427 (line)]] | wt | 149 | 2 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.600× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 137 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 113 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 116 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.2) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 103 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 64.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 149 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -10.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 114 | 2 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -22.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 167 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -12.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 107 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 89.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 123 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -21.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 60.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.61× (z +10.0) | — |
| [[KATO III (line)]] | alt | 101 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 80.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 104 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 88.4 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 84.7 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 90.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 81.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 54.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 58.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 233 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0663× (z -24.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 140 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.5) | — |
| [[SW48 (line)]] | wt | 94.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 84.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 48.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 54.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 121 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 60.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +16.1) | — |
| [[AN3 CA (line)]] | alt | 125 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF2]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[RNF38]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RANBP9]] | +0.59 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SOS2]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PIAS1]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[AMBRA1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PPP2R5E]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[MAP3K3]] | +0.56 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TAPT1]] | +0.55 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ZNRF2]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF1A]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[BMS1]] | -0.57 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[ULBP3]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ZSCAN20]] | -0.54 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[MGA]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[DDX1]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ZKSCAN2]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[HUS1]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ODC1]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MIER2]] | -0.49 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[AGPAT4]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RBAK]] | -0.48 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.9, -19.0); signed map (-18.4, 15.4). **Vector** length 107, 36.4% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +19.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.3 | +9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.0 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -5.9 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:44,167,969-44,244,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPC2BETAX, PP2CB, PP2CBETA |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 8 pathways, smallest: ALK mutants bind TKIs; ISG15 antiviral mechanism; Signaling by ALK fusions and activated point mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [O75688](https://www.uniprot.org/uniprotkb/O75688) (Protein phosphatase 1B):

> Enzyme with a broad specificity. Dephosphorylates CDK2 and CDK6 in vitro. Dephosphorylates PRKAA1 and PRKAA2. Inhibits TBK1-mediated antiviral signaling by dephosphorylating it at 'Ser-172'. Plays an important role in the termination of TNF-mediated NF-kappa-B activation through dephosphorylating and inactivating IKBKB/IKKB.

**Summary**, from NCBI Gene [5495](https://www.ncbi.nlm.nih.gov/gene/5495):

> The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase has been shown to dephosphorylate cyclin-dependent kinases (CDKs), and thus may be involved in cell cycle control. Overexpression of this phosphatase is reported to cause cell-growth arrest or cell death. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:9276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9276) · Entrez [5495](https://www.ncbi.nlm.nih.gov/gene/5495) · UniProt [O75688](https://www.uniprot.org/uniprotkb/O75688) · Ensembl [ENSG00000138032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138032)

## Data

Gene col 6111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6111); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6111]; `tensor/DDL_lfc|DDL_z.npy` [6111]; `embed/gene_vectors.npy` [6111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6111 or target_col == 6111). Every well: [[PPM1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
