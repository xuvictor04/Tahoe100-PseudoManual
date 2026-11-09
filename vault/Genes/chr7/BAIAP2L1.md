---
symbol: "BAIAP2L1"
type: "gene"
col: 111
ensembl_id: "ENSG00000006453"
name: "BAR/IMD domain containing adaptor protein 2 like 1"
location: "7q21.3-q22.1"
module: 141
arm: "+"
pooled_cpm: 268.48
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 41
direction_downstream: 2
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# BAIAP2L1

*BAR/IMD domain containing adaptor protein 2 like 1* — 7q21.3-q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.43× (z +18.5, q 0e+00, up in 38 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.01× (z +14.5, q 3e-45, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.629× (z -13.6, q 3e-39, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FA2H]] (+0.69, fdr 7e-06), [[SULT2B1]] (+0.65, fdr 1e-05), [[KIF13B]] (+0.64, fdr 2e-05); moves opposite to [[TSN]] (-0.60, fdr 2e-05), [[NAXD]] (-0.57, fdr 5e-05), [[MAPKAPK5]] (-0.54, fdr 3e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 41 arrows point to it, the strongest [[CBLC]] → it (grade B ⚠); 2 go from it, the strongest it → [[GPRC5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +18.5 | 0e+00 | 38/40 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.01×** | +14.5 | 3e-45 | 37/40 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +11.6 | 5e-29 | 38/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +10.4 | 3e-23 | 25/40 (HEC-1-A, A498, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +10.1 | 1e-21 | 29/40 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +9.5 | 2e-19 | 35/40 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +5.5 | 3e-06 | 23/40 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.57×** | +4.9 | 7e-05 | 26/40 (CFPAC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.3 | 9e-04 | 20/40 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.005 | 15/40 (AsPC-1, A498, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.023 | 13/40 (HepG2/C3A, NCI-H1573, …) | rises with dose | plate-row cell shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +3.3 | 0.051 | 16/41 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.11× | +3.2 | 0.051 | 7/41 (NCI-H1792, SHP-77, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.2 | 0.052 | 13/41 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.052 | 15/40 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.080 | 10/40 (AsPC-1, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | 1.16× | +3.0 | 0.082 | 6/41 (HepG2/C3A, AsPC-1, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -13.6 | 3e-39 | 30/41 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.709×** | -10.1 | 2e-21 | 34/40 (A549, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.684×** | -7.6 | 8e-12 | 28/37 (SK-MEL-2, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.693×** | -7.0 | 3e-10 | 27/38 (BT-474, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.716×** | -6.9 | 5e-10 | 29/40 (LoVo, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -6.5 | 9e-09 | 25/40 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.728×** | -6.3 | 2e-08 | 29/40 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -6.3 | 2e-08 | 22/40 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.738×** | -5.9 | 2e-07 | 26/41 (BT-474, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.754×** | -5.7 | 5e-07 | 26/42 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.761×** | -5.6 | 9e-07 | 24/40 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.773×** | -5.1 | 1e-05 | 24/40 (C32, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.818×** | -5.1 | 2e-05 | 23/40 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.786×** | -5.0 | 3e-05 | 24/40 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.827×** | -4.8 | 6e-05 | 21/40 (HepG2/C3A, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.787×** | -4.8 | 7e-05 | 23/40 (LoVo, BT-474, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.813×** | -4.7 | 9e-05 | 18/41 (LoVo, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.785×** | -4.7 | 9e-05 | 26/40 (LoVo, BT-474, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.844× | -4.4 | 3e-04 | 17/40 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.669×** | -4.4 | 4e-04 | 26/40 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.802×** | -4.3 | 5e-04 | 21/40 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 342 | 4 (1 ⚠) | 12 (5 ⚠) | [[Digitoxin (drug)]] 5 µM 2.96× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.57× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -20.9) |
| [[KATO III (line)]] | alt | 499 | 2 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -28.1) |
| [[NCI-H460 (line)]] | wt | 121 | 10 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.91× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +17.7) | — |
| [[HEC-1-A (line)]] | alt | 205 | 4 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +25.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.17× (z +18.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -22.2) |
| [[Panc 03.27 (line)]] | alt | 258 | 5 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +17.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.38× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -16.5) |
| [[PANC-1 (line)]] | alt | 311 | 6 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +20.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -24.5) |
| [[A-427 (line)]] | wt | 179 | 6 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.18× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.497× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 254 | 3 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.10× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 255 | 7 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.60× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.54× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.0) |
| [[LoVo (line)]] | wt | 355 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.361× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 150 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +13.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.427× (z -9.9) |
| [[SW1417 (line)]] | alt | 236 | 5 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -18.5) |
| [[LS 180 (line)]] | wt | 462 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -24.0) |
| [[NCI-H2030 (line)]] | alt | 317 | 3 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 205 | 5 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.03× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -14.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -12.4) |
| [[A498 (line)]] | wt | 255 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +22.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.35× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 346 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -25.8) |
| [[NCI-H1573 (line)]] | alt | 483 | 4 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.01× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 291 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 2,407 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 328 | 2 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.19× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -15.8) |
| [[H4 (line)]] | wt | 99.0 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.37× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 131 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.09× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.441× (z -12.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HT-29 (line)]] | alt | 523 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -26.6) |
| [[J82 (line)]] | alt | 105 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +17.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 189 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -9.8) |
| [[SW48 (line)]] | wt | 185 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.39× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 68.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.64× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 91.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 94.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 357 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -14.7) |
| [[HCT15 (line)]] | alt | 178 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.27× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 121 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.60× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 91.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -8.9) |
| [[SW480 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.27× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 59.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 56.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 48.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 175 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 44.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 172 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FA2H]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SULT2B1]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.64 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TMC6]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RDH13]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[SH2D3A]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CYSTM1]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[AREG]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R13B]] | +0.61 | +0.49 / +0.53 | both halves | 1e-05 | same gene group |
| [[CBLC]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PLK3]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSN]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[NAXD]] | -0.57 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[MAPKAPK5]] | -0.54 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MRPL9]] | -0.54 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[GATB]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[EIF3F]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[RAE1]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SPAG16]] | -0.52 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[FAM120C]] | -0.52 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TARBP2]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SETD7]] | -0.51 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[ZMPSTE24]] | -0.51 | -0.50 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 40, C 1. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBLC]] | B | CBLC activity raises BAIAP2L1's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without CBLC | 0.001 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[LAMA3]] | B | LAMA3 activity raises BAIAP2L1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[TMPRSS4]] | B | TMPRSS4 activity raises BAIAP2L1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.07× lower at baseline in the lines without TMPRSS4 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[GOLT1A]] | B | GOLT1A activity raises BAIAP2L1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.98× lower at baseline in the lines without GOLT1A | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[SH2D3A]] | B | SH2D3A activity raises BAIAP2L1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.18× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[CLDN7]] | B | CLDN7 activity raises BAIAP2L1's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.01× lower at baseline in the lines without CLDN7 | 0.004 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[S100A14]] | B | S100A14 activity raises BAIAP2L1's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 2.98× lower at baseline in the lines without S100A14 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[GRB7]] | B | GRB7 activity raises BAIAP2L1's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without GRB7 | 0.005 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[SULT2B1]] | B | SULT2B1 activity raises BAIAP2L1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without SULT2B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[CEACAM1]] | B | CEACAM1 activity raises BAIAP2L1's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without CEACAM1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[CYP3A5]] | B | CYP3A5 activity raises BAIAP2L1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without CYP3A5 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[AREG]] | B | AREG activity raises BAIAP2L1's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without AREG | 0.011 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | BAIAP2L1 activity raises GPRC5A's level | lines that do not express BAIAP2L1 (8) vs lines expressing it (42) | 4.26× lower at baseline in the lines without BAIAP2L1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ITPR3, CABLES1, PRKCZ; maybe low, not absent; its own permutation p |
| [[KRT15]] | B | BAIAP2L1 activity raises KRT15's level | lines that do not express BAIAP2L1 (8) vs lines expressing it (42) | 3.36× lower at baseline in the lines without BAIAP2L1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITPR3, CABLES1, PRKCZ; maybe low, not absent |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.8, 48.5); signed map (-0.2, 37.8). **Vector** length 124, 44.0% of its response variance represented; |z| ≥ 3 in 1,484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +1.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +5.6 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | -5.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.3 | -10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | +0.3 |
|  | [[NG25 (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | BAR/IMD domain containing adaptor protein 2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3-q22.1 — chr7:98,291,650-98,401,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IRTKS |
| Gene groups (HGNC) | I-BAR domain containing; SH3 domain containing |
| Reactome | 7 pathways, smallest: RHOF GTPase cycle; RAC2 GTPase cycle; RAC3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHR4](https://www.uniprot.org/uniprotkb/Q9UHR4) (BAR/IMD domain-containing adapter protein 2-like 1):

> May function as adapter protein. Involved in the formation of clusters of actin bundles. Plays a role in the reorganization of the actin cytoskeleton in response to bacterial infection.

**Summary**, from NCBI Gene [55971](https://www.ncbi.nlm.nih.gov/gene/55971):

> This gene encodes a member of the IMD (IRSp53/MIM homology domain) family. Members of this family can be subdivided in two groups, the IRSp53-like and MIM-like, based on the presence or absence of the SH3 (Src homology 3) domain. The protein encoded by this gene contains a conserved IMD, also known as F-actin bundling domain, at the N-terminus, and a canonical SH3 domain near the C-terminus, so it belongs to the IRSp53-like group. This protein is the substrate for insulin receptor tyrosine …

**Accessions** — [HGNC:21649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21649) · Entrez [55971](https://www.ncbi.nlm.nih.gov/gene/55971) · UniProt [Q9UHR4](https://www.uniprot.org/uniprotkb/Q9UHR4) · Ensembl [ENSG00000006453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006453)

## Data

Gene col 111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 111); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 111]; `tensor/DDL_lfc|DDL_z.npy` [111]; `embed/gene_vectors.npy` [111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 111 or target_col == 111). Every well: [[BAIAP2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAIAP2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
