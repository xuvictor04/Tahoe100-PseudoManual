---
symbol: "TVP23C"
type: "gene"
col: 10563
ensembl_id: "ENSG00000175106"
name: "trans-golgi network vesicle protein 23 homolog C"
location: "17p12"
module: 56
arm: "+"
pooled_cpm: 140.98
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 39
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TVP23C

*trans-golgi network vesicle protein 23 homolog C* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.23× (z +4.6, q 0.002, up in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 3 lines (SHP-77 2.53×, HT-29 2.59×, SW1417 1.91×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 2.24×); [[Artesunate (drug)]] 5 µM in 1 line (SW480 1.50×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -20.1, q 0e+00, down in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.591× (z -16.4, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TVP23C-CDRT4]] (+0.82, fdr 7e-06, ⚠ same locus), [[CDRT4]] (+0.76, fdr 7e-06, ⚠ same locus), [[PGM3]] (+0.68, fdr 7e-06), [[COPA]] (+0.68, fdr 7e-06), [[COG6]] (+0.67, fdr 7e-06); moves opposite to [[THAP12]] (-0.57, fdr 3e-05), [[YAP1]] (-0.54, fdr 4e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RABGEF1P3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10563.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 3 lines (SHP-77 2.53×, HT-29 2.59×, SW1417 1.91×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 2.24×); [[Artesunate (drug)]] 5 µM in 1 line (SW480 1.50×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.6 | 0.002 | 23/46 (SHP-77, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.23×** | +4.5 | 0.002 | 28/47 (RPMI-7951, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +4.4 | 0.002 | 25/46 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.048 | 18/47 (SW480, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 25 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.525×** | -20.1 | 0e+00 | 39/46 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -16.4 | 0e+00 | 35/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.494×** | -15.6 | 0e+00 | 40/47 (A498, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.501×** | -14.7 | 0e+00 | 34/42 (Panc 03.27, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.502×** | -14.1 | 7e-43 | 35/43 (SNU-423, A-172, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.526×** | -13.6 | 3e-40 | 40/46 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.622×** | -10.5 | 1e-23 | 33/46 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -9.7 | 1e-20 | 36/46 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.648×** | -9.5 | 9e-20 | 30/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.443×** | -9.4 | 3e-19 | 39/47 (HS-578T, SNU-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -9.0 | 9e-18 | 36/45 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.669×** | -8.8 | 5e-17 | 35/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.672×** | -8.7 | 9e-17 | 31/46 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.674×** | -8.7 | 1e-16 | 41/46 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.677×** | -8.3 | 6e-15 | 37/46 (HOP62, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -7.6 | 1e-12 | 26/46 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.718×** | -7.3 | 9e-12 | 33/46 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.637×** | -5.2 | 4e-06 | 28/47 (RPMI-7951, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -4.8 | 4e-05 | 24/46 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.821×** | -4.3 | 3e-04 | 22/46 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.827×** | -4.1 | 6e-04 | 22/46 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.828×** | -4.1 | 6e-04 | 23/46 (BT-474, Hs 766T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.830×** | -4.1 | 8e-04 | 21/46 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.002 | 22/46 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.840× | -3.8 | 0.002 | 17/46 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.830×** | -3.8 | 0.003 | 20/45 (C32, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.847× | -3.3 | 0.012 | 17/46 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 225 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -25.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -19.6) |
| [[A-172 (line)]] | wt | 176 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -30.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -20.3) |
| [[HOP62 (line)]] | alt | 267 | 0 | 12 (11 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -18.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 187 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -21.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -17.9) |
| [[A549 (line)]] | wt | 214 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -24.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -19.2) |
| [[PANC-1 (line)]] | alt | 82.6 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -21.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.370× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 164 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -18.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -10.2) |
| [[SNU-423 (line)]] | alt | 156 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -23.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -13.8) |
| [[A498 (line)]] | wt | 199 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -22.3) |
| [[NCI-H1792 (line)]] | alt | 137 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -26.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 167 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -16.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -12.5) |
| [[H4 (line)]] | wt | 162 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.2) |
| [[Hs 766T (line)]] | wt | 140 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -13.6) |
| [[KATO III (line)]] | alt | 187 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -16.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 201 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -14.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 74.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -14.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.276× (z -12.7) |
| [[J82 (line)]] | alt | 171 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -17.2) |
| [[LS 180 (line)]] | wt | 132 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -13.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -18.1) |
| [[SW 900 (line)]] | alt | 132 | 0 | 5 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.375× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -8.9) |
| [[SW480 (line)]] | alt | 128 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.8) |
| [[LoVo (line)]] | wt | 224 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 84.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -15.5) |
| [[HCT15 (line)]] | alt | 325 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[hTERT-HPNE (line)]] | wt | 97.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 96.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-1 (line)]] | wt | 157 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -12.1) |
| [[A-427 (line)]] | wt | 62.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[CHP-212 (line)]] | wt | 133 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[Panc 03.27 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[RKO (line)]] | wt | 136 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +9.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 150 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.53× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.4) |
| [[BT-474 (line)]] | alt | 83.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.364× (z -8.9) |
| [[C-33 A (line)]] | alt | 74.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HT-29 (line)]] | alt | 70.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.59× (z +9.1) | — |
| [[SW 1271 (line)]] | alt | 296 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SW1417 (line)]] | alt | 81.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.91× (z +8.5) | — |
| [[SW48 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 236 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TVP23C-CDRT4]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CDRT4]] | +0.76 | +0.73 / +0.77 | both halves | 7e-06 | STRING 742; ⚠ same locus (26.5 kb, same strand: neighbours can correlate without regulation) |
| [[PGM3]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[COPA]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[COG6]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[UFM1]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SERP1]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SEC24D]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[FAM114A1]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ZNF841]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[COPB1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP12]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[YAP1]] | -0.54 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RABGEF1P3]] | B | RABGEF1P3 activity raises TVP23C's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.1, -33.7); signed map (-55.9, 16.7). **Vector** length 116, 39.7% of its response variance represented; |z| ≥ 3 in 1,515 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.56 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.57 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.57 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -9.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.9 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.5 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | trans-golgi network vesicle protein 23 homolog C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,502,264-15,563,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8763; previously FAM18B2 |
| Matched by | ensembl_id |

UniProt [Q96ET8](https://www.uniprot.org/uniprotkb/Q96ET8) carries no function annotation.

**Summary**, from NCBI Gene [201158](https://www.ncbi.nlm.nih.gov/gene/201158):

> Predicted to be involved in protein secretion and vesicle-mediated transport. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30453) · Entrez [201158](https://www.ncbi.nlm.nih.gov/gene/201158) · UniProt [Q96ET8](https://www.uniprot.org/uniprotkb/Q96ET8) · Ensembl [ENSG00000175106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175106)

## Data

Gene col 10563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10563); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10563]; `tensor/DDL_lfc|DDL_z.npy` [10563]; `embed/gene_vectors.npy` [10563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10563 or target_col == 10563). Every well: [[TVP23C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TVP23C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
