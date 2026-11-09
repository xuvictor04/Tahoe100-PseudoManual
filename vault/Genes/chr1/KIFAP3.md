---
symbol: "KIFAP3"
type: "gene"
col: 1138
ensembl_id: "ENSG00000075945"
name: "kinesin associated protein 3"
location: "1q24.2"
module: 17
arm: "+"
pooled_cpm: 65.57
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# KIFAP3

*kinesin associated protein 3* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.62× (z +10.8, q 2e-24, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.418× (z -19.4, q 0e+00, down in 43 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.439× (z -18.3, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC1I2]] (+0.61, fdr 1e-05), [[MOCS2]] (+0.61, fdr 1e-05), [[STAM2]] (+0.57, fdr 2e-05); moves opposite to [[TLCD3A]] (-0.58, fdr 2e-04), [[PRDM15]] (-0.56, fdr 5e-05), [[NINJ2]] (-0.55, fdr 0.001, ⚠ not reproduced), [[ZNF460-AS1]] (-0.54, fdr 4e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +10.8 | 2e-24 | 40/47 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +9.4 | 1e-18 | 39/47 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +9.0 | 3e-17 | 36/47 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.3 | 1e-05 | 24/47 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +5.2 | 2e-05 | 24/46 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +4.4 | 9e-04 | 18/49 (NCI-H1573, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 9e-04 | 19/46 (HOP62, SHP-77, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.001 | 18/49 (NCI-H2030, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.14× | +4.3 | 0.001 | 12/47 (NCI-H1792, SW480, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.010 | 18/47 (LS 180, RKO, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.010 | 16/48 (A498, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.010 | 18/48 (HT-29, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.015 | 10/47 (A-172, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.018 | 12/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.3 | 0.032 | 4/47 (LOX-IMVI, A549, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.032 | 11/47 (A-172, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.2 | 0.042 | 15/47 (SW1417, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.044 | 12/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.044 | 11/47 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -19.4 | 0e+00 | 43/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.439×** | -18.3 | 0e+00 | 41/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -17.9 | 0e+00 | 37/47 (CFPAC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -15.0 | 0e+00 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.555×** | -13.1 | 5e-37 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.597×** | -10.8 | 2e-25 | 41/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.694×** | -8.1 | 4e-14 | 35/46 (PANC-1, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.542×** | -7.1 | 8e-11 | 28/47 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.719×** | -7.0 | 1e-10 | 28/46 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.550×** | -6.9 | 2e-10 | 33/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.566×** | -6.6 | 2e-09 | 33/47 (H4, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -6.5 | 3e-09 | 24/47 (HOP62, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.574×** | -6.4 | 5e-09 | 31/47 (Hs 766T, A549, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.581×** | -6.3 | 1e-08 | 30/47 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.853× | -5.0 | 3e-05 | 21/47 (NCI-H1792, Hs 766T, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.813×** | -4.6 | 1e-04 | 20/47 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.814×** | -4.6 | 1e-04 | 21/47 (H4, SW48, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.750×** | -4.5 | 2e-04 | 24/47 (A-172, LOX-IMVI, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.868× | -4.4 | 2e-04 | 15/47 (HOP62, Hs 766T, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.757×** | -4.4 | 3e-04 | 20/47 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 75.9 | 3 | 9 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.241× (z -18.4) |
| [[HOP62 (line)]] | alt | 45.7 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.209× (z -15.0) |
| [[Hs 766T (line)]] | wt | 53.6 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -15.4) |
| [[LoVo (line)]] | wt | 31.1 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -11.6) |
| [[H4 (line)]] | wt | 67.3 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 78.4 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -15.0) |
| [[LS 180 (line)]] | wt | 39.8 | 1 (1 ⚠) | 5 (2 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.78× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0705× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -14.5) |
| [[PANC-1 (line)]] | alt | 55.3 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.81× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.405× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.481× (z -10.5) |
| [[A-172 (line)]] | wt | 260 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 111 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 54.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.377× (z -10.4) |
| [[SNU-423 (line)]] | alt | 38.1 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -13.2) |
| [[SW 900 (line)]] | alt | 80.2 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.4) |
| [[SW480 (line)]] | alt | 33.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.226× (z -16.4) |
| [[A498 (line)]] | wt | 158 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.4) |
| [[A549 (line)]] | wt | 83.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 85.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 37.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.415× (z -9.0) |
| [[J82 (line)]] | alt | 48.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 52.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 65.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.431× (z -9.1) |
| [[SW1417 (line)]] | alt | 39.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +11.1) | — |
| [[CHP-212 (line)]] | wt | 75.1 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0832× (z -12.4) |
| [[HT-29 (line)]] | alt | 34.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.4 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -9.7) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 91.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.2) |
| [[RKO (line)]] | wt | 34.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.162× (z -13.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 70.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.362× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.421× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 71.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.134× (z -10.8) |
| [[A-427 (line)]] | wt | 73.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.199× (z -8.8) ⚠ cell-cycle shift, explains ~93% of this change |
| [[C-33 A (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 69.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -18.7) |
| [[COLO 205 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -11.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 99.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -17.9) |
| [[NCI-H2030 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.400× (z -9.1) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1I2]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[MOCS2]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[STAM2]] | +0.57 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[TBC1D19]] | +0.55 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CAST]] | +0.55 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[PHF6]] | +0.54 | +0.37 / +0.41 | both halves | 7e-05 |  |
| [[DLD]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[OSBPL9]] | +0.53 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[UBL7]] | +0.53 | +0.42 / +0.34 | both halves | 1e-04 |  |
| [[DMXL1]] | +0.52 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[STX7]] | +0.52 | +0.41 / +0.33 | both halves | 1e-04 |  |
| [[DYNLT3]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD3A]] | -0.58 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[PRDM15]] | -0.56 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[NINJ2]] | -0.55 | -0.41 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[ZNF460-AS1]] | -0.54 | -0.46 / -0.24 | both halves | 4e-04 |  |
| [[TMEM11-DT]] | -0.52 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[RAI1]] | -0.52 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SUZ12P1]] | -0.51 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[DEAF1]] | -0.51 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | -0.51 | -0.39 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[SYCE2]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[RBM15]] | -0.50 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[PRDM10]] | -0.50 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[TNPO2]] | -0.50 | -0.42 / -0.30 | both halves | 2e-04 | same gene group |
| [[MIA]] | -0.49 | -0.43 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-20.5, -0.6); signed map (-23.6, -20.2). **Vector** length 104, 28.3% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +9.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.4 | -17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -10.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -19.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.2 | -13.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -7.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | kinesin associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,921,326-170,085,208 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMAP, KAP3, FLA3, KAP-1 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 18 pathways, smallest: Intraflagellar transport; Kinesins; Translocation of SLC2A4 (GLUT4) to the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92845](https://www.uniprot.org/uniprotkb/Q92845) (Kinesin-associated protein 3):

> Involved in tethering the chromosomes to the spindle pole and in chromosome movement. Binds to the tail domain of the KIF3A/KIF3B heterodimer to form a heterotrimeric KIF3 complex and may regulate the membrane binding of this complex (By similarity).

**Summary**, from NCBI Gene [22920](https://www.ncbi.nlm.nih.gov/gene/22920):

> The small G protein GDP dissociation stimulator (smg GDS) is a regulator protein having two activities on a group of small G proteins including the Rho and Rap1 family members and Ki-Ras; one is to stimulate their GDP/GTP exchange reactions, and the other is to inhibit their interactions with membranes. The protein encoded by this gene contains 9 'Armadillo' repeats and interacts with the smg GDS protein through these repeats. This protein, which is highly concentrated around the endoplasmic …

**Accessions** — [HGNC:17060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17060) · Entrez [22920](https://www.ncbi.nlm.nih.gov/gene/22920) · UniProt [Q92845](https://www.uniprot.org/uniprotkb/Q92845) · Ensembl [ENSG00000075945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075945)

## Data

Gene col 1138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1138); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1138]; `tensor/DDL_lfc|DDL_z.npy` [1138]; `embed/gene_vectors.npy` [1138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1138 or target_col == 1138). Every well: [[KIFAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIFAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
