---
symbol: "TRIM33"
type: "gene"
col: 12381
ensembl_id: "ENSG00000197323"
name: "tripartite motif containing 33"
location: "1p13.2"
module: 204
arm: "+"
pooled_cpm: 148.14
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# TRIM33

*tripartite motif containing 33* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.88× (z +14.1, q 1e-42, up in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.78× (z +12.9, q 2e-35, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.548× (z -13.5, q 1e-38, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.832× (z -4.2, q 0.004, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-427 0.0526×, SK-MEL-2 0.255×, NCI-H23 0.383×, HEC-1-A 0.369×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SK-MEL-2 0.295×, A-427 0.297×, NCI-H2347 0.350×, C32 0.352×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Panc 03.27 0.312×, NCI-H2347 0.339×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC3]] (+0.72, fdr 7e-06), [[HINT1]] (+0.66, fdr 1e-05), [[ZMYM2]] (+0.66, fdr 7e-06); moves opposite to [[REXO1]] (-0.61, fdr 1e-05), [[ZNF140]] (-0.59, fdr 1e-05), [[CNOT3]] (-0.58, fdr 3e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MFAP3L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +14.1 | 1e-42 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +12.9 | 2e-35 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +10.4 | 4e-23 | 44/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +9.8 | 2e-20 | 41/48 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +7.5 | 1e-11 | 36/48 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +6.4 | 1e-08 | 37/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +6.3 | 2e-08 | 30/48 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +6.3 | 2e-08 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +5.8 | 4e-07 | 33/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +5.4 | 4e-06 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +5.3 | 8e-06 | 33/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.6 | 2e-04 | 27/48 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.5 | 3e-04 | 25/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 7e-04 | 27/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.3 | 8e-04 | 27/45 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 20/50 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.002 | 22/48 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.002 | 14/49 (CFPAC-1, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12381.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-427 0.0526×, SK-MEL-2 0.255×, NCI-H23 0.383×, HEC-1-A 0.369×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SK-MEL-2 0.295×, A-427 0.297×, NCI-H2347 0.350×, C32 0.352×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Panc 03.27 0.312×, NCI-H2347 0.339×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -13.5 | 1e-38 | 46/49 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -11.1 | 5e-26 | 40/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.731×** | -6.5 | 1e-08 | 26/45 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -6.0 | 2e-07 | 33/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.832×** | -4.2 | 0.004 | 22/48 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.893× | -3.6 | 0.026 | 13/48 (SK-MEL-2, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.859× | -3.4 | 0.049 | 19/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.962× | -3.3 | 0.064 | 0/50 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.064 | 18/48 (hTERT-HPNE, SK-MEL-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.867× | -3.2 | 0.071 | 16/48 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.874× | -3.1 | 0.12 | 21/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.876× | -3.0 | 0.13 | 12/48 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 129 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.75× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -15.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 153 | 7 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.19× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.631× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 160 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 155 | 5 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.14× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.600× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 314 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.99× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -15.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 98.0 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.33× (z +13.7) | — |
| [[HepG2_C3A (line)]] | wt | 176 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.41× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -11.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 137 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.530× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 147 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 160 | 2 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.13× (z +9.9) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -38.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 166 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 162 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 198 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -16.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 173 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.91× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -15.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 161 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.70× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -13.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 176 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 107 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.17× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 137 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.26× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.24× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -11.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 84.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 176 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.95× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.91× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -14.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 90.3 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.57× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 193 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 374 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -19.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 72.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.23× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 107 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -12.9) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.27× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 159 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.83× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 173 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC3]] | +0.72 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[HINT1]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[ZMYM2]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SRPK2]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[USP3]] | +0.65 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.63 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[PPP2R5E]] | +0.62 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.60 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SEC61A2]] | +0.59 | +0.69 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REXO1]] | -0.61 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.59 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[CNOT3]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[CELSR3]] | -0.58 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[ZNF614]] | -0.58 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.58 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[SRCAP]] | -0.58 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[MIS12]] | -0.57 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[ZNF646]] | -0.57 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[CYB5D1]] | -0.56 | -0.63 / -0.40 | both halves | 4e-05 |  |
| [[ZNF268]] | -0.56 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[ZNF543]] | -0.56 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFAP3L]] | B | MFAP3L activity raises TRIM33's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.23× lower at baseline in the lines without MFAP3L | 0.070 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.9, -8.3); signed map (-21.2, 15.9). **Vector** length 93.5, 29.0% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | -0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.4 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | +5.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +5.3 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:114,392,790-114,511,203 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIF1GAMMA, FLJ11429, KIAA1113, TIFGAMMA, RFG7, TF1G, TIF1G, PTC7 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; PHD finger proteins; Bromodomain containing; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 6 pathways, smallest: Germ layer formation at gastrulation; Downregulation of SMAD2/3:SMAD4 transcriptional activity; Transcriptional activity of SMAD2/SMAD3:SMAD4 heterotrimer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPN9](https://www.uniprot.org/uniprotkb/Q9UPN9) (E3 ubiquitin-protein ligase TRIM33):

> Acts as an E3 ubiquitin-protein ligase. Promotes SMAD4 ubiquitination, nuclear exclusion and degradation via the ubiquitin proteasome pathway. According to PubMed:16751102, does not promote a decrease in the level of endogenous SMAD4. May act as a transcriptional repressor. Inhibits the transcriptional response to TGF-beta/BMP signaling cascade. Plays a role in the control of cell proliferation. Its association with SMAD2 and SMAD3 stimulates erythroid differentiation of hematopoietic …

**Summary**, from NCBI Gene [51592](https://www.ncbi.nlm.nih.gov/gene/51592):

> The protein encoded by this gene is thought to be a transcriptional corepressor. However, molecules that interact with this protein have not yet been identified. The protein is a member of the tripartite motif family. This motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. Three alternatively spliced transcript variants for this gene have been described, however, the full-length nature of one variant has not been determined. [provided …

**Accessions** — [HGNC:16290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16290) · Entrez [51592](https://www.ncbi.nlm.nih.gov/gene/51592) · UniProt [Q9UPN9](https://www.uniprot.org/uniprotkb/Q9UPN9) · Ensembl [ENSG00000197323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197323)

## Data

Gene col 12381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12381); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12381]; `tensor/DDL_lfc|DDL_z.npy` [12381]; `embed/gene_vectors.npy` [12381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12381 or target_col == 12381). Every well: [[TRIM33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
