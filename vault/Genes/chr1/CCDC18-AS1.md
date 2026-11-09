---
symbol: "CCDC18-AS1"
type: "gene"
col: 13360
ensembl_id: "ENSG00000223745"
name: "CCDC18 antisense RNA 1"
location: "1p22.1"
module: 15
arm: "+"
pooled_cpm: 124.69
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 41
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CCDC18-AS1

*CCDC18 antisense RNA 1* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.31× (z +4.4, q 0.006, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (22 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.304× (z -19.1, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.319× (z -18.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAGAP-AS1]] (+0.66, fdr 7e-06), [[ZNF862]] (+0.65, fdr 7e-06), [[BET1]] (+0.63, fdr 7e-06); moves opposite to [[API5]] (-0.57, fdr 2e-05), [[CASP2]] (-0.54, fdr 1e-05), [[CBX2]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 0.006 | 29/48 (KATO III, SK-MEL-2, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.008 | 28/48 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.009 | 28/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +3.9 | 0.010 | 29/50 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.010 | 21/49 (SW1417, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.9 | 0.010 | 22/49 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.048 | 17/48 (SW480, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.048 | 20/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.066 | 16/49 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.1 | 0.084 | 11/48 (SNU-1, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.084 | 23/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.084 | 16/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.084 | 21/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.20×** | +3.0 | 0.098 | 20/48 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.10 | 16/48 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 24 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.304×** | -19.1 | 0e+00 | 48/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.319×** | -18.3 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.332×** | -17.7 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.349×** | -16.9 | 0e+00 | 48/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.359×** | -15.8 | 0e+00 | 44/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.439×** | -13.2 | 8e-38 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.431×** | -13.0 | 1e-36 | 46/48 (A549, H4, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.224×** | -12.6 | 2e-34 | 46/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.234×** | -12.2 | 2e-32 | 47/49 (NCI-H23, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.472×** | -12.0 | 1e-31 | 45/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.525×** | -10.3 | 3e-23 | 39/49 (NCI-H23, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.635×** | -10.3 | 5e-23 | 37/48 (A549, HEC-1-A, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.511×** | -10.2 | 1e-22 | 43/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.519×** | -10.1 | 2e-22 | 36/44 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -8.8 | 8e-17 | 36/47 (CHP-212, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -8.0 | 3e-14 | 35/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.677×** | -5.9 | 1e-07 | 33/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.746×** | -4.7 | 6e-05 | 26/48 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.579×** | -4.6 | 9e-05 | 30/48 (NCI-H23, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -4.3 | 4e-04 | 24/49 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.792×** | -3.7 | 0.004 | 23/48 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.797×** | -3.6 | 0.005 | 24/48 (NCI-H2030, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.662×** | -3.4 | 0.009 | 23/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.809×** | -3.4 | 0.012 | 20/48 (HOP62, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 160 | 0 | 18 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.150× (z -21.8) |
| [[HOP62 (line)]] | alt | 179 | 0 | 17 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.185× (z -17.6) |
| [[A549 (line)]] | wt | 161 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -31.8) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 225 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -13.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.158× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 312 | 0 | 14 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -26.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.122× (z -14.9) |
| [[SW480 (line)]] | alt | 118 | 0 | 14 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.133× (z -24.1) |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -18.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.159× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 13 (7 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.213× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 161 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -17.2) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.268× (z -13.8) |
| [[SNU-423 (line)]] | alt | 114 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.5) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.236× (z -14.1) |
| [[HCT15 (line)]] | alt | 225 | 0 | 12 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.211× (z -14.7) |
| [[Hs 766T (line)]] | wt | 154 | 0 | 12 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.150× (z -18.0) |
| [[HS-578T (line)]] | alt | 192 | 0 | 12 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -15.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.295× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 69.4 | 0 | 12 (9 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.252× (z -14.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.281× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 200 | 0 | 11 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -15.0) |
| [[KATO III (line)]] | alt | 119 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.360× (z -10.9) |
| [[LoVo (line)]] | wt | 99.9 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.284× (z -15.2) |
| [[H4 (line)]] | wt | 102 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.169× (z -12.4) |
| [[RKO (line)]] | wt | 113 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.105× (z -12.4) |
| [[SNU-1 (line)]] | wt | 115 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.256× (z -11.3) |
| [[C32 (line)]] | wt | 88.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -13.5) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 155 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -10.3) |
| [[J82 (line)]] | alt | 69.2 | 0 | 8 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.225× (z -14.0) |
| [[COLO 205 (line)]] | alt | 142 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.202× (z -16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.241× (z -14.3) |
| [[HT-29 (line)]] | alt | 87.2 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 7 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.199× (z -15.0) |
| [[BT-474 (line)]] | alt | 139 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.223× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.279× (z -12.4) |
| [[CHP-212 (line)]] | wt | 89.0 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0751× (z -12.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 131 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.238× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 87.3 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.318× (z -10.3) |
| [[C-33 A (line)]] | alt | 177 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0816× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.414× (z -9.5) |
| [[A-172 (line)]] | wt | 88.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.303× (z -10.5) |
| [[A-427 (line)]] | wt | 106 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[A498 (line)]] | wt | 101 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.0) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -8.5) |
| [[SW 1271 (line)]] | alt | 180 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.188× (z -9.9) |
| [[SW 900 (line)]] | alt | 77.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 52.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.326× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.155× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 64.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.199× (z -12.4) |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.253× (z -9.1) |
| [[SW 1088 (line)]] | alt | 237 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -11.9) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SW1417 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 71.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -12.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAGAP-AS1]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF862]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[BET1]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HMGCL]] | +0.62 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[C4orf47]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ZC3H6]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZNF397]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RNF170]] | +0.60 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[KPNB1-DT]] | +0.60 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NIFK-AS1]] | +0.60 | +0.57 / +0.63 | both halves | 9e-06 | same gene group |
| [[POLR1HASP]] | +0.60 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[BRPF3-AS1]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[API5]] | -0.57 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[CASP2]] | -0.54 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[CBX2]] | -0.53 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PRPS1]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SARS2]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[DLAT]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.52 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[STIP1]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[USP14]] | -0.51 | -0.49 / -0.51 | both halves | 2e-05 |  |
| [[CCT2]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[NUP155]] | -0.51 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[POLR3H]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CCDC18-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NR2F2-AS1]] | B | NR2F2-AS1 activity raises CCDC18-AS1's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without NR2F2-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[DDX59-AS1]] | B | DDX59-AS1 activity raises CCDC18-AS1's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without DDX59-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[C4orf47]] | C | C4orf47 activity raises CCDC18-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises CCDC18-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | CCDC18-AS1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | CCDC18-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.017 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Digitoxin (drug)]] 0.05 µM | C | CCDC18-AS1's natural level lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | CCDC18-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.360 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | CCDC18-AS1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | CCDC18-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.472 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | CCDC18-AS1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | CCDC18-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.3, 20.2); signed map (28.6, -7.0). **Vector** length 91.5, 38.1% of its response variance represented; |z| ≥ 3 in 1,772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.6 | -17.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +0.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -8.3 | -10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -6.9 | -10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -5.8 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.8 | -16.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.1 | -6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.0 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -12.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -8.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CCDC18 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p22.1 — chr1:93,262,186-93,346,025 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000440778.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52262) · Entrez [100131564](https://www.ncbi.nlm.nih.gov/gene/100131564) · Ensembl [ENSG00000223745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223745)

## Data

Gene col 13360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13360); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13360]; `tensor/DDL_lfc|DDL_z.npy` [13360]; `embed/gene_vectors.npy` [13360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13360 or target_col == 13360). Every well: [[CCDC18-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC18-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
