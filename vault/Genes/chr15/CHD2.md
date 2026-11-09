---
symbol: "CHD2"
type: "gene"
col: 10405
ensembl_id: "ENSG00000173575"
name: "chromodomain helicase DNA binding protein 2"
location: "15q26.1"
module: 69
arm: "+"
pooled_cpm: 841.81
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CHD2

*chromodomain helicase DNA binding protein 2* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +19.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.349× (z -24.0, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.682× (z -8.8, q 1e-16, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REL]] (+0.71, fdr 7e-06), [[RSF1]] (+0.69, fdr 7e-06), [[YTHDC1]] (+0.68, fdr 7e-06); moves opposite to [[POP1]] (-0.64, fdr 7e-06), [[NSUN2]] (-0.61, fdr 1e-05), [[CHCHD6]] (-0.60, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GALNT14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +19.0 | 0e+00 | 44/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.14×** | +17.4 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +11.3 | 3e-27 | 43/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +11.0 | 4e-26 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +10.9 | 9e-26 | 44/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +10.2 | 2e-22 | 45/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +9.1 | 9e-18 | 32/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +8.9 | 4e-17 | 46/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +6.5 | 5e-09 | 43/48 (C32, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 3e-05 | 26/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.15× | +4.5 | 4e-04 | 16/48 (A498, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.4 | 6e-04 | 4/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 7e-04 | 24/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.13× | +3.9 | 0.003 | 12/48 (SNU-1, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.19× | +3.9 | 0.004 | 20/48 (SNU-1, A-427, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.009 | 31/49 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.015 | 27/48 (SK-MEL-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.022 | 13/49 (HOP62, hTERT-HPNE, …) | rises with dose | plate-row cell shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.026 | 11/47 (KATO III, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.349×** | -24.0 | 0e+00 | 48/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.351×** | -23.9 | 0e+00 | 48/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.455×** | -18.0 | 0e+00 | 47/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.444×** | -17.8 | 0e+00 | 43/44 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.486×** | -15.8 | 0e+00 | 47/47 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.507×** | -15.5 | 0e+00 | 48/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.659×** | -13.5 | 2e-39 | 40/49 (A549, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.681×** | -8.8 | 1e-16 | 43/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.682×** | -8.8 | 1e-16 | 45/48 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.694×** | -8.4 | 4e-15 | 36/48 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.697×** | -7.6 | 1e-12 | 35/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -6.6 | 3e-09 | 33/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.775×** | -5.8 | 2e-07 | 30/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.631×** | -5.5 | 2e-06 | 36/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.784×** | -5.4 | 3e-06 | 36/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -5.0 | 2e-05 | 17/48 (A549, HCT15, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.692×** | -4.4 | 3e-04 | 34/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.711×** | -4.1 | 0.001 | 32/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.726×** | -3.8 | 0.003 | 32/49 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.848× | -3.8 | 0.004 | 19/49 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.848× | -3.8 | 0.004 | 20/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.005 | 28/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.032 | 13/48 (RKO, Panc 03.27, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.912× | -3.0 | 0.054 | 8/48 (BT-474, A549, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.883× | -2.8 | 0.075 | 6/47 (C32, SW48, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.884× | -2.8 | 0.080 | 9/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 1,221 | 10 (2 ⚠) | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[LOX-IMVI (line)]] | wt | 686 | 8 (1 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +24.2) | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -20.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.663× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 1,800 | 2 | 14 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.19× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.435× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 544 | 13 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.68× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 1,281 | 4 (1 ⚠) | 10 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -20.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.599× (z -8.5) |
| [[SNU-1 (line)]] | wt | 882 | 9 (3 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +24.0) | [[Panobinostat (drug)]] 5 µM 0.308× (z -16.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 839 | 6 (1 ⚠) | 8 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -23.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 622 | 7 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +32.2) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -17.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 916 | 4 (1 ⚠) | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.238× (z -24.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.546× (z -10.5) |
| [[HOP62 (line)]] | alt | 655 | 6 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.348× (z -17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.587× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 778 | 6 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -22.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 862 | 5 (1 ⚠) | 8 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -18.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 1,013 | 6 (1 ⚠) | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +19.7) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 853 | 4 | 9 (9 ⚠) | [[Harringtonine (drug)]] 5 µM 2.39× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.230× (z -25.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 677 | 8 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +21.3) | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -16.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 947 | 4 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +21.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -29.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.663× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 984 | 5 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.200× (z -27.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Brivudine (drug)]] 5 µM 0.389× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 657 | 4 | 8 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.439× (z -16.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 832 | 4 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.254× (z -23.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.580× (z -9.3) |
| [[A-172 (line)]] | wt | 555 | 5 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +26.3) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CFPAC-1 (line)]] | alt | 1,271 | 1 | 10 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.190× (z -31.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.636× (z -8.6) |
| [[CHP-212 (line)]] | wt | 915 | 4 | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 1,413 | 5 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +16.8) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -20.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 472 | 5 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.318× (z -19.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 1,440 | 2 | 9 (9 ⚠) | [[TAK-901 (drug)]] 5 µM 2.90× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 1,046 | 2 | 9 (9 ⚠) | [[TAK-901 (drug)]] 5 µM 2.87× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -28.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 945 | 4 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +20.3) | [[Panobinostat (drug)]] 5 µM 0.283× (z -19.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 740 | 3 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.522× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 547 | 3 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.536× (z -9.7) |
| [[SW1417 (line)]] | alt | 965 | 3 (1 ⚠) | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -21.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 670 | 3 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.84× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Hs 766T (line)]] | wt | 698 | 2 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 470 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +22.3) | [[Panobinostat (drug)]] 5 µM 0.515× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 792 | 3 | 6 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.39× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -18.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 839 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -18.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.502× (z -10.4) |
| [[SW48 (line)]] | wt | 932 | 6 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 575 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.302× (z -14.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 565 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 1,217 | 1 | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -17.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 872 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 416 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.493× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 589 | 2 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.23× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 496 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 426 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.485× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 1271 (line)]] | alt | 1,199 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.311× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 615 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.465× (z -11.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H661 (line)]] | alt | 622 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 669 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2122 (line)]] | alt | 1,454 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 922 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REL]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[RSF1]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[YTHDC1]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SIRT1]] | +0.66 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ZBTB10]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CUTALP]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[KMT2E]] | +0.63 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[COL11A2]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[NSUN2]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[GMPS]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TMEM201]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ZNF496]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.58 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[NUP93]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TEX2]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[FBXW2]] | -0.58 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT14]] | B | GALNT14 activity raises CHD2's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.23× lower at baseline in the lines without GALNT14 | 0.065 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises CHD2's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without MTUS1-DT | 0.080 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[LGALS3]] | B | LGALS3 activity raises CHD2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without LGALS3 | 0.096 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.3, -31.6); signed map (-7.3, 9.2). **Vector** length 122, 55.4% of its response variance represented; |z| ≥ 3 in 2,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +8.2 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +19.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.3 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +11.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.9 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.0 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -1.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.6 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:92,886,203-93,027,996 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38614, DKFZp547I1315, DKFZp781D1727, DKFZp686E01200 |
| Gene groups (HGNC) | Helicases; SNF2 related family; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; ATP-dependent chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [O14647](https://www.uniprot.org/uniprotkb/O14647) (ATP-dependent chromatin remodeler CHD2):

> ATP-dependent chromatin-remodeling factor that specifically binds to the promoter of target genes, leading to chromatin remodeling, possibly by promoting deposition of histone H3.3. Involved in myogenesis via interaction with MYOD1: binds to myogenic gene regulatory sequences and mediates incorporation of histone H3.3 prior to the onset of myogenic gene expression, promoting their expression (By similarity).

**Summary**, from NCBI Gene [1106](https://www.ncbi.nlm.nih.gov/gene/1106):

> The CHD family of proteins is characterized by the presence of chromo (chromatin organization modifier) domains and SNF2-related helicase/ATPase domains. CHD genes alter gene expression possibly by modification of chromatin structure thus altering access of the transcriptional apparatus to its chromosomal DNA template. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1917) · Entrez [1106](https://www.ncbi.nlm.nih.gov/gene/1106) · UniProt [O14647](https://www.uniprot.org/uniprotkb/O14647) · Ensembl [ENSG00000173575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173575)

## Data

Gene col 10405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10405); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10405]; `tensor/DDL_lfc|DDL_z.npy` [10405]; `embed/gene_vectors.npy` [10405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10405 or target_col == 10405). Every well: [[CHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
