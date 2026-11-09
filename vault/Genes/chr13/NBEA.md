---
symbol: "NBEA"
type: "gene"
col: 10314
ensembl_id: "ENSG00000172915"
name: "neurobeachin"
location: "13q13.3"
module: 207
arm: "-"
pooled_cpm: 136.1
n_lines_expressing: 43
n_dd_up: 15
n_dd_down: 43
n_dd_up_clean: 14
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# NBEA

*neurobeachin* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.86× (z +9.1, q 6e-17, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.512× (z -13.7, q 6e-40, down in 36 of 42 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC3P1]] (+0.60, fdr 4e-05), [[ZBTB20]] (+0.58, fdr 1e-05), [[TTBK2]] (+0.57, fdr 1e-04); moves opposite to [[RECQL5]] (-0.52, fdr 4e-05), [[PIGG]] (-0.50, fdr 6e-05), [[ACAD9]] (-0.50, fdr 1e-04).
> It sits in the **-** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 2 go from it, the strongest it → [[AIG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +9.1 | 6e-17 | 28/41 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +9.0 | 6e-17 | 31/41 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +7.6 | 4e-12 | 32/42 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +6.9 | 6e-10 | 26/41 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +6.4 | 1e-08 | 26/41 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +6.1 | 1e-07 | 27/41 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +5.6 | 2e-06 | 28/42 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +5.5 | 2e-06 | 31/40 (SW480, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.003 | 26/40 (SW480, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.050 | 20/41 (J82, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.057 | 19/41 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.072 | 18/43 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.25×** | +3.1 | 0.078 | 21/43 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.078 | 20/41 (LS 180, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.078 | 16/42 (LS 180, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.098 | 12/41 (SW480, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -13.7 | 6e-40 | 36/42 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.440×** | -11.5 | 6e-28 | 35/40 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.592×** | -10.7 | 1e-24 | 26/41 (NCI-H460, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.514×** | -9.6 | 7e-20 | 34/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.505×** | -9.2 | 6e-18 | 26/39 (C-33 A, AN3 CA, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.511×** | -8.3 | 1e-14 | 32/42 (SNU-1, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.594×** | -7.3 | 3e-11 | 27/39 (C-33 A, SNU-1, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -6.2 | 3e-08 | 37/42 (SNU-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.650×** | -6.2 | 3e-08 | 30/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.656×** | -6.1 | 6e-08 | 30/41 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -5.9 | 2e-07 | 34/41 (HEC-1-A, SNU-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -5.8 | 2e-07 | 30/43 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.675×** | -5.7 | 6e-07 | 30/41 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **0.678×** | -5.6 | 9e-07 | 32/41 (H4, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.682×** | -5.5 | 1e-06 | 26/41 (NCI-H460, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.660×** | -5.1 | 9e-06 | 31/41 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -5.0 | 2e-05 | 29/41 (NCI-H1573, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -4.4 | 3e-04 | 21/42 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.747×** | -4.2 | 6e-04 | 23/41 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 8e-04 | 29/41 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.596×** | -3.9 | 0.002 | 27/41 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.705×** | -3.6 | 0.007 | 24/41 (BT-474, MIA PaCa-2, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.623×** | -3.6 | 0.007 | 25/41 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.782×** | -3.5 | 0.008 | 22/41 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.784×** | -3.5 | 0.009 | 18/41 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 209 | 0 | 13 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -24.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SNU-1 (line)]] | wt | 1,192 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -19.8) |
| [[J82 (line)]] | alt | 134 | 5 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.06× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -15.5) |
| [[AN3 CA (line)]] | alt | 533 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 200 | 1 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.71× (z +9.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 177 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 35.3 | 7 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.60× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 246 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 180 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -20.8) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 111 | 2 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.51× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.3) |
| [[A-172 (line)]] | wt | 134 | 1 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[BT-474 (line)]] | alt | 114 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.310× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.4) |
| [[C32 (line)]] | wt | 303 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.0) |
| [[PANC-1 (line)]] | alt | 60.5 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -10.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.428× (z -8.8) |
| [[A549 (line)]] | wt | 225 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -13.7) |
| [[C-33 A (line)]] | alt | 361 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.8) |
| [[HCT15 (line)]] | alt | 93.8 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.20× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 508 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 187 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -8.6) |
| [[SW 900 (line)]] | alt | 247 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -14.9) |
| [[A-427 (line)]] | wt | 154 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CHP-212 (line)]] | wt | 454 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -16.0) |
| [[HOP62 (line)]] | alt | 113 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[LS 180 (line)]] | wt | 68.8 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.69× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -8.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Hs 766T (line)]] | wt | 172 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 171 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW 1271 (line)]] | alt | 293 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 74.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.45× (z +12.3) | — |
| [[H4 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.305× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HepG2_C3A (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0978× (z -14.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.275× (z -8.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC3P1]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[ZBTB20]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TTBK2]] | +0.57 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[MPDZ]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 | STRING 588 |
| [[TTC28]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PCNX2]] | +0.53 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[KMT2C]] | +0.52 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[STAU2]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MIR181A1HG]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[GKAP1]] | +0.51 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FGGY]] | +0.51 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[LINC02484]] | +0.51 | +0.34 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL5]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PIGG]] | -0.50 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[ACAD9]] | -0.50 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[DUS2]] | -0.50 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[SHPK]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CWF19L1]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP1]] | -0.48 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PTCD1]] | -0.46 | -0.23 / -0.34 | both halves | 5e-04 |  |
| [[GLE1]] | -0.46 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[DPY19L3-DT]] | -0.45 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[RAB27A]] | -0.45 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[ZNF710]] | -0.45 | -0.27 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers NBEA's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[TTC28]] | B | TTC28 activity strengthens NBEA's drug response | lines that do not express TTC28 (9) vs lines expressing it (33) | the lines without TTC28 respond 0.82× as strongly (z diff +1.71); strongest at Homoharringtonine 5 µM: 0.99x vs 0.56x (z diff +6.3) | 0.098 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AIG1]] | B | NBEA activity raises AIG1's level | lines that do not express NBEA (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without NBEA | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HDGFL3, HLTF, FERMT2 |
| [[LYPLAL1]] | B | NBEA activity raises LYPLAL1's level | lines that do not express NBEA (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without NBEA | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HDGFL3, HLTF, FERMT2 |

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **-** arm (projection on the module's main direction -0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-21.5, 29.2); signed map (-7.3, 12.6). **Vector** length 101, 34.6% of its response variance represented; |z| ≥ 3 in 1,432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +9.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.0 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -0.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | neurobeachin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:34,942,270-35,673,022 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1544, BCL8B, FLJ10197, LYST2 |
| Gene groups (HGNC) | WD repeat domain containing; A-kinase anchoring proteins; BEACH domain containing ; Armadillo like helical domain containing |
| Reactome | 21 pathways, smallest: PKA activation; PKA-mediated phosphorylation of CREB; CaM pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFP9](https://www.uniprot.org/uniprotkb/Q8NFP9) (Neurobeachin):

> Binds to type II regulatory subunits of protein kinase A and anchors/targets them to the membrane. May anchor the kinase to cytoskeletal and/or organelle-associated proteins (By similarity).

**Summary**, from NCBI Gene [26960](https://www.ncbi.nlm.nih.gov/gene/26960):

> This gene encodes a member of a large, diverse group of A-kinase anchor proteins that target the activity of protein kinase A to specific subcellular sites by binding to its type II regulatory subunits. Brain-specific expression and coat protein-like membrane recruitment of a highly similar protein in mouse suggest an involvement in neuronal post-Golgi membrane traffic. Mutations in this gene may be associated with a form of autism. This gene and its expression are frequently disrupted in …

**Accessions** — [HGNC:7648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7648) · Entrez [26960](https://www.ncbi.nlm.nih.gov/gene/26960) · UniProt [Q8NFP9](https://www.uniprot.org/uniprotkb/Q8NFP9) · Ensembl [ENSG00000172915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172915)

## Data

Gene col 10314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10314); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10314]; `tensor/DDL_lfc|DDL_z.npy` [10314]; `embed/gene_vectors.npy` [10314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10314 or target_col == 10314). Every well: [[NBEA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBEA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
