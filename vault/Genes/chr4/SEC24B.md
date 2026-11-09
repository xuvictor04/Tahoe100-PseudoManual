---
symbol: "SEC24B"
type: "gene"
col: 6246
ensembl_id: "ENSG00000138802"
name: "SEC24 homolog B, COPII component"
location: "4q25"
module: 169
arm: "+"
pooled_cpm: 129.02
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# SEC24B

*SEC24 homolog B, COPII component* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.57× (z +10.2, q 1e-21, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.334× (z -23.7, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.691× (z -11.8, q 7e-30, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF5]] (+0.73, fdr 7e-06), [[PPP2R5E]] (+0.73, fdr 7e-06), [[GAPVD1]] (+0.70, fdr 7e-06); moves opposite to [[THOC6]] (-0.69, fdr 1e-05), [[ZNF655]] (-0.60, fdr 2e-05), [[PHF19]] (-0.59, fdr 8e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RPS24]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +10.2 | 1e-21 | 44/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +9.7 | 6e-20 | 45/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +8.9 | 1e-16 | 44/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +8.3 | 1e-14 | 38/49 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +8.1 | 6e-14 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +7.2 | 7e-11 | 37/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +6.9 | 4e-10 | 35/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +6.9 | 4e-10 | 30/38 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +6.1 | 8e-08 | 32/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.3 | 6e-06 | 33/45 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 2e-05 | 37/49 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 3e-04 | 25/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 4e-04 | 26/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 8e-04 | 24/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.005 | 6/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.089 | 13/49 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.334×** | -23.7 | 0e+00 | 42/44 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.359×** | -23.1 | 0e+00 | 48/49 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -14.1 | 5e-43 | 39/45 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.691×** | -11.8 | 7e-30 | 37/48 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.604×** | -11.4 | 8e-28 | 45/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.616×** | -10.9 | 1e-25 | 43/48 (KATO III, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -9.5 | 2e-19 | 37/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.787×** | -7.6 | 2e-12 | 27/49 (A549, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -6.8 | 5e-10 | 27/48 (SNU-1, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.738×** | -6.6 | 3e-09 | 34/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.775×** | -5.7 | 5e-07 | 31/48 (LS 180, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.783×** | -5.5 | 2e-06 | 30/48 (AN3 CA, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.797×** | -5.1 | 2e-05 | 33/48 (NCI-H2347, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.808×** | -4.8 | 6e-05 | 26/48 (NCI-H2347, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.826×** | -4.3 | 7e-04 | 27/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -4.2 | 9e-04 | 14/48 (LOX-IMVI, HepG2/C3A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.855× | -3.5 | 0.015 | 15/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.859× | -3.4 | 0.020 | 15/48 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.863× | -3.3 | 0.029 | 17/47 (SW 900, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.867× | -3.2 | 0.039 | 11/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.870× | -3.1 | 0.046 | 15/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.874× | -3.0 | 0.062 | 5/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 160 | 7 (3 ⚠) | 5 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.50× (z +15.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.573× (z -13.9) |
| [[PANC-1 (line)]] | alt | 81.8 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 145 | 1 | 8 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.23× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.510× (z -14.3) |
| [[LS 180 (line)]] | wt | 172 | 4 (1 ⚠) | 5 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.34× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.73× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 196 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -25.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.518× (z -17.6) |
| [[SW480 (line)]] | alt | 79.3 | 4 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.458× (z -12.3) |
| [[HOP62 (line)]] | alt | 170 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 167 | 5 (2 ⚠) | 3 (2 ⚠) | [[Lonafarnib (drug)]] 5 µM 7.34× (z +15.4) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 3.99× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.530× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 176 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.01× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 127 | 4 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.29× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0968× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.537× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 109 | 2 | 4 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.88× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.591× (z -11.9) |
| [[SW48 (line)]] | wt | 207 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.31× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.343× (z -10.6) |
| [[A549 (line)]] | wt | 131 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 135 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 133 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.510× (z -13.9) |
| [[HS-578T (line)]] | alt | 125 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.8) |
| [[HT-29 (line)]] | alt | 97.3 | 2 | 3 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.07× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.430× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -10.5) |
| [[KATO III (line)]] | alt | 99.2 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.77× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 138 | 1 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 4.44× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 168 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -14.2) |
| [[J82 (line)]] | alt | 93.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 129 | 1 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.05× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -31.8) |
| [[Panc 03.27 (line)]] | alt | 149 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.8) |
| [[RKO (line)]] | wt | 157 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.77× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -10.7) |
| [[SNU-1 (line)]] | wt | 176 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.371× (z -14.2) |
| [[AN3 CA (line)]] | alt | 199 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -12.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.485× (z -9.3) |
| [[SNU-423 (line)]] | alt | 79.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.3) |
| [[SW 900 (line)]] | alt | 107 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.372× (z -15.5) |
| [[SW1417 (line)]] | alt | 108 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.535× (z -8.9) |
| [[A-427 (line)]] | wt | 133 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -17.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.11× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0769× (z -28.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 114 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.483× (z -8.6) |
| [[CHP-212 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0658× (z -16.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -20.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.441× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF5]] | +0.73 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[PPP2R5E]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[GAPVD1]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[SNX4]] | +0.69 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[PIAS1]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[NENF]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SRPK2]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[FHIP2A]] | +0.65 | +0.78 / +0.57 | both halves | 9e-06 |  |
| [[RELCH]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LAMTOR2]] | +0.64 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.69 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.60 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[PHF19]] | -0.59 | -0.72 / -0.37 | both halves | 8e-05 |  |
| [[CYB5D1]] | -0.59 | -0.67 / -0.39 | both halves | 6e-05 |  |
| [[CELSR3]] | -0.59 | -0.67 / -0.44 | both halves | 3e-05 | same gene group |
| [[MIS12]] | -0.58 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[SRSF6]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SKIL]] | -0.58 | -0.71 / -0.46 | both halves | 3e-05 |  |
| [[GNL1]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.57 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.57 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS24]] | C | RPS24's natural level strengthens SEC24B's drug response | RPS24's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.40; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.880). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.2, -8.7); signed map (-35.3, -7.2). **Vector** length 104, 36.1% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | -1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.1 | -11.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | +4.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SEC24 homolog B, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,433,772-109,540,896 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Coat protein complex II |
| Reactome | 19 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Cargo concentration in the ER; Regulation of cholesterol biosynthesis by SREBP (SREBF) |
| Matched by | ensembl_id |

**Function**, from UniProt [O95487](https://www.uniprot.org/uniprotkb/O95487) (Protein transport protein Sec24B):

> Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transport to the Golgi complex. Plays a central role in cargo selection within the COPII complex and together with SEC24A may have a different specificity compared to SEC24C and SEC24D. May package …

**Summary**, from NCBI Gene [10427](https://www.ncbi.nlm.nih.gov/gene/10427):

> The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein is thought to be a cargo-binding component of the COPII vesicle, and is thought to be involved in the transport of secretory proteins from the endoplasmic reticulum to the Golgi apparatus. Mutations in this gene have been associated with neural tube defects, and are thought to be a result of a disruption in interactions with the protein …

**Accessions** — [HGNC:10704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10704) · Entrez [10427](https://www.ncbi.nlm.nih.gov/gene/10427) · UniProt [O95487](https://www.uniprot.org/uniprotkb/O95487) · Ensembl [ENSG00000138802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138802)

## Data

Gene col 6246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6246); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6246]; `tensor/DDL_lfc|DDL_z.npy` [6246]; `embed/gene_vectors.npy` [6246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6246 or target_col == 6246). Every well: [[SEC24B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC24B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
