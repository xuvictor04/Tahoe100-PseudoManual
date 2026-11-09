---
symbol: "HERC2"
type: "gene"
col: 4918
ensembl_id: "ENSG00000128731"
name: "HECT and RLD domain containing E3 ubiquitin protein ligase 2"
location: "15q13.1"
module: 36
arm: "+"
pooled_cpm: 83.68
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# HERC2

*HECT and RLD domain containing E3 ubiquitin protein ligase 2* — 15q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.93× (z +13.6, q 2e-39, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.600× (z -15.0, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.529× (z -12.7, q 1e-34, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC2P9]] (+0.85, fdr 7e-06), [[HERC2P2]] (+0.80, fdr 7e-06), [[EXOC2]] (+0.80, fdr 7e-06); moves opposite to [[ATP23]] (-0.71, fdr 7e-06), [[FAM117A]] (-0.71, fdr 8e-06), [[RSRP1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TNFRSF10C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +13.6 | 2e-39 | 44/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +11.8 | 1e-29 | 40/48 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +10.9 | 3e-25 | 41/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +9.9 | 6e-21 | 41/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.61×** | +9.9 | 6e-21 | 40/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +9.2 | 3e-18 | 41/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +5.4 | 5e-06 | 31/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +4.4 | 7e-04 | 25/48 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.23×** | +4.0 | 0.003 | 22/44 (A-427, NCI-H23, …) | rises with dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.7 | 0.013 | 22/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.22×** | +3.6 | 0.016 | 21/49 (CFPAC-1, HOP62, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.016 | 19/49 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.016 | 20/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.20×** | +3.4 | 0.031 | 17/48 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.36×** | +3.3 | 0.031 | 16/44 (NCI-H1792, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.061 | 10/47 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.100 | 6/49 (A498, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.600×** | -15.0 | 0e+00 | 42/48 (J82, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -12.7 | 1e-34 | 43/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -12.7 | 1e-34 | 37/49 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -8.8 | 2e-16 | 37/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.674×** | -8.2 | 4e-14 | 36/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.713×** | -7.0 | 2e-10 | 32/48 (A-427, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.772×** | -4.7 | 2e-04 | 27/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.804×** | -4.5 | 4e-04 | 23/48 (BT-474, SW480, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.816×** | -4.2 | 0.002 | 24/48 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -4.1 | 0.002 | 24/48 (SW480, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.823×** | -4.0 | 0.003 | 25/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.003 | 22/49 (NCI-H2030, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.829×** | -3.9 | 0.004 | 25/48 (KATO III, SW 1088, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.6 | 0.011 | 16/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.1 | 0.064 | 14/49 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.899× | -3.1 | 0.064 | 2/48 (NCI-H2030, H4) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.903× | -3.0 | 0.091 | 8/48 (KATO III, SNU-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 82.9 | 3 | 8 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.296× (z -14.2) |
| [[A-172 (line)]] | wt | 86.0 | 3 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -20.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -15.7) |
| [[PANC-1 (line)]] | alt | 106 | 5 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.430× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -11.2) |
| [[SW480 (line)]] | alt | 87.7 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.296× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -17.2) |
| [[HOP62 (line)]] | alt | 69.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 130 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -19.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.413× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 81.8 | 2 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -14.7) |
| [[A549 (line)]] | wt | 100 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.476× (z -8.6) |
| [[BT-474 (line)]] | alt | 74.0 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.308× (z -10.9) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -9.7) |
| [[C32 (line)]] | wt | 76.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -17.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.283× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 62.6 | 2 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.401× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 63.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.66× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 84.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -22.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.404× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 98.0 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.11× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.412× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -12.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 78.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -19.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -14.9) |
| [[J82 (line)]] | alt | 103 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -23.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.320× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 99.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -18.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -15.2) |
| [[SW1417 (line)]] | alt | 89.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -14.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.429× (z -9.6) |
| [[A498 (line)]] | wt | 91.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.4) |
| [[AN3 CA (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.266× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 36.7 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.7) |
| [[COLO 205 (line)]] | alt | 74.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.02× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.391× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.499× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 66.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -12.2) |
| [[SNU-423 (line)]] | alt | 46.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.250× (z -11.6) |
| [[C-33 A (line)]] | alt | 153 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 43.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[H4 (line)]] | wt | 57.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.59× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 57.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 49.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.251× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 81.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.441× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 66.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.420× (z -8.7) |
| [[RKO (line)]] | wt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.4) |
| [[SNU-1 (line)]] | wt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.3) |
| [[SW 900 (line)]] | alt | 65.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.5) | — |
| [[SW48 (line)]] | wt | 101 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.308× (z -9.2) |
| [[CHP-212 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P9]] | +0.85 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[HERC2P2]] | +0.80 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[SPATA5]] | +0.79 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[HERC2P3]] | +0.78 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[HERC2P9-1]] | +0.78 | +0.72 / +0.85 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[DROSHA]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[ERI3]] | +0.73 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[TALDO1]] | +0.72 | +0.70 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP23]] | -0.71 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[FAM117A]] | -0.71 | -0.68 / -0.58 | both halves | 8e-06 |  |
| [[RSRP1]] | -0.69 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ZNF821]] | -0.68 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[UPK2]] | -0.68 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.67 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[FAM200B]] | -0.66 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[KDM5B]] | -0.66 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[HMGCL]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[NDUFV2-AS1]] | -0.63 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[THAP1]] | -0.62 | -0.50 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF10C]] | B | TNFRSF10C activity lowers HERC2's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.40× higher at baseline in the lines without TNFRSF10C | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.4, -31.5); signed map (-15.9, -51.4). **Vector** length 135, 43.5% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.4 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.4 | +9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.9 | +10.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +9.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.3 | -12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -10.1 | -15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -8.3 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.0 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | HECT and RLD domain containing E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.1 — chr15:28,111,040-28,322,179 (-) |
| Ensembl biotype | protein_coding |
| Also known as | jdf2, p528, D15F37S1 |
| Gene groups (HGNC) | Zinc fingers ZZ-type; HECT and RLD domain containing E3 ubiquitin protein ligases; Cytochrome b5 domain containing; Tectonin beta-propeller repeat containing |
| Reactome | 18 pathways, smallest: Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; G2/M DNA damage checkpoint |
| Matched by | ensembl_id |

**Function**, from UniProt [O95714](https://www.uniprot.org/uniprotkb/O95714) (E3 ubiquitin-protein ligase HERC2):

> E3 ubiquitin-protein ligase that ubiquitinates target proteins to control their stability or function, contributing to the DNA damage response, clearance of unassembled protein-complex subunits, and regulation of diverse signaling and metabolic pathways. Regulates ubiquitin-dependent retention of repair proteins on damaged chromosomes by being recruited to sites of DNA damage, where it facilitates assembly of UBE2N and RNF8 and mediates their binding specificity, promoting DNA damage-induced …

**Summary**, from NCBI Gene [8924](https://www.ncbi.nlm.nih.gov/gene/8924):

> This gene belongs to the HERC gene family that encodes a group of unusually large proteins, which contain multiple structural domains. All members have at least 1 copy of an N-terminal region showing homology to the cell cycle regulator RCC1 and a C-terminal HECT (homologous to E6-AP C terminus) domain found in a number of E3 ubiquitin protein ligases. Genetic variations in this gene are associated with skin/hair/eye pigmentation variability. Multiple pseudogenes of this gene are located on …

**Accessions** — [HGNC:4868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4868) · Entrez [8924](https://www.ncbi.nlm.nih.gov/gene/8924) · UniProt [O95714](https://www.uniprot.org/uniprotkb/O95714) · Ensembl [ENSG00000128731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128731)

## Data

Gene col 4918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4918); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4918]; `tensor/DDL_lfc|DDL_z.npy` [4918]; `embed/gene_vectors.npy` [4918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4918 or target_col == 4918). Every well: [[HERC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
