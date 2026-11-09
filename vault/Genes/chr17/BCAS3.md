---
symbol: "BCAS3"
type: "gene"
col: 6506
ensembl_id: "ENSG00000141376"
name: "BCAS3 microtubule associated cell migration factor"
location: "17q23.2"
module: 74
arm: "+"
pooled_cpm: 245.83
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 42
n_dd_up_clean: 23
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# BCAS3

*BCAS3 microtubule associated cell migration factor* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.70× (z +9.6, q 5e-19, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (16 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.328× (z -20.0, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.365× (z -18.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB20]] (+0.65, fdr 7e-06), [[TNRC6B]] (+0.64, fdr 3e-05), [[WDR48]] (+0.63, fdr 2e-04); moves opposite to [[PAX9]] (-0.49, fdr 2e-05), [[PLAAT1]] (-0.48, fdr 1e-03, ⚠ one half only (not replicated)), [[APEX2]] (-0.45, fdr 9e-05), [[ADORA2B]] (-0.44, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +9.6 | 5e-19 | 36/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.29×** | +6.4 | 4e-08 | 28/48 (LoVo, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +6.2 | 1e-07 | 27/48 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 1e-07 | 30/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +5.8 | 9e-07 | 40/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.74×** | +5.2 | 2e-05 | 40/50 (LoVo, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +5.1 | 2e-05 | 36/50 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 4e-05 | 31/48 (SNU-423, H4, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 7e-05 | 35/47 (SW480, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +4.7 | 2e-04 | 24/48 (SW480, BT-474, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +4.4 | 5e-04 | 22/49 (SW480, SHP-77, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +4.1 | 0.002 | 26/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 29/48 (LS 180, KATO III, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 35/49 (SW480, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.004 | 27/49 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 25/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.009 | 25/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.013 | 26/48 (KATO III, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.328×** | -20.0 | 0e+00 | 47/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.365×** | -18.1 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.386×** | -17.1 | 0e+00 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.439×** | -14.2 | 8e-44 | 47/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.512×** | -12.0 | 4e-31 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.516×** | -11.4 | 3e-28 | 34/44 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.540×** | -11.1 | 1e-26 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.548×** | -10.8 | 3e-25 | 36/49 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.331×** | -10.4 | 2e-23 | 46/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.578×** | -9.8 | 4e-21 | 44/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.570×** | -9.7 | 1e-20 | 40/47 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.570×** | -9.7 | 2e-20 | 33/48 (NCI-H1573, A549, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.573×** | -9.5 | 1e-19 | 48/48 (LoVo, SNU-1, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.480×** | -9.4 | 2e-19 | 47/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.376×** | -9.2 | 2e-18 | 46/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.380×** | -9.1 | 4e-18 | 36/49 (C32, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.390×** | -8.8 | 3e-17 | 44/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.397×** | -8.7 | 1e-16 | 45/48 (HEC-1-A, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -7.9 | 8e-14 | 40/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -7.1 | 3e-11 | 34/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.484×** | -6.8 | 2e-10 | 41/48 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.514×** | -6.2 | 9e-09 | 41/48 (PANC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.651×** | -5.5 | 8e-07 | 41/48 (NCI-H23, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.655×** | -5.4 | 1e-06 | 43/49 (NCI-H23, SNU-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 175 | 0 | 23 (13 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.212× (z -23.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 410 | 0 | 19 (15 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -18.0) |
| [[LOX-IMVI (line)]] | wt | 263 | 1 (1 ⚠) | 16 (10 ⚠) | [[Selinexor (drug)]] 5 µM 1.69× (z +9.7) ⚠ cell-cycle shift, explains ~83% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -20.6) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -15.9) |
| [[SW480 (line)]] | alt | 323 | 5 (1 ⚠) | 12 (9 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.30× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -23.0) |
| [[MIA PaCa-2 (line)]] | alt | 321 | 1 | 15 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.224× (z -16.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -12.7) |
| [[HT-29 (line)]] | alt | 219 | 3 (2 ⚠) | 12 (5 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.222× (z -19.4) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -14.5) |
| [[C32 (line)]] | wt | 435 | 0 | 14 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.231× (z -16.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 258 | 0 | 13 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -18.0) |
| [[SNU-1 (line)]] | wt | 246 | 0 | 13 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -19.5) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 448 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.463× (z -11.5) |
| [[A549 (line)]] | wt | 374 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -17.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 330 | 0 | 11 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.231× (z -17.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.400× (z -10.8) |
| [[A-427 (line)]] | wt | 432 | 1 (1 ⚠) | 9 (8 ⚠) | [[Selinexor (drug)]] 5 µM 1.59× (z +9.1) ⚠ cell-cycle shift, explains ~83% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.508× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 268 | 1 | 9 (8 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.241× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -12.9) |
| [[KATO III (line)]] | alt | 260 | 2 (1 ⚠) | 8 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.81× (z +9.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.25× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -16.5) |
| [[LoVo (line)]] | wt | 158 | 6 (3 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.19× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.397× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[EX229 (drug)]] 0.05 µM 0.437× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 247 | 1 (1 ⚠) | 9 (6 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -15.6) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -11.4) |
| [[BT-474 (line)]] | alt | 427 | 5 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Afatinib (drug)]] 5 µM 2.36× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.299× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -12.1) |
| [[LS 180 (line)]] | wt | 178 | 4 (2 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -17.4) |
| [[CFPAC-1 (line)]] | alt | 164 | 2 (1 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.12× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -15.4) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.436× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 208 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.263× (z -18.3) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.240× (z -10.2) |
| [[SHP-77 (line)]] | alt | 320 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -13.7) |
| [[SW1417 (line)]] | alt | 205 | 1 (1 ⚠) | 7 (3 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.174× (z -19.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -12.6) |
| [[HOP62 (line)]] | alt | 217 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -19.6) |
| [[A498 (line)]] | wt | 154 | 1 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.266× (z -13.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AN3 CA (line)]] | alt | 549 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.310× (z -10.2) |
| [[CHP-212 (line)]] | wt | 709 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -10.7) |
| [[COLO 205 (line)]] | alt | 200 | 2 (2 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -15.0) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -13.6) |
| [[SNU-423 (line)]] | alt | 195 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -12.1) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -11.7) |
| [[SW48 (line)]] | wt | 200 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.211× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -11.1) |
| [[A-172 (line)]] | wt | 171 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -12.9) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 486 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.289× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 217 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -14.4) |
| [[HS-578T (line)]] | alt | 193 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.247× (z -15.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.434× (z -9.1) |
| [[J82 (line)]] | alt | 168 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.321× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 451 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.518× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 186 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.202× (z -14.8) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 136 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.82× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -11.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 91.1 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -13.6) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.374× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -10.6) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 0.204× (z -9.0) |
| [[SW 900 (line)]] | alt | 119 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -13.6) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.400× (z -8.6) |
| [[SW 1088 (line)]] | alt | 155 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0646× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Simotinib (drug)]] 0.05 µM 0.0919× (z -9.0) |
| [[SW 1271 (line)]] | alt | 325 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.202× (z -10.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.226× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 82.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[H4 (line)]] | wt | 138 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.409× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 17 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB20]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TNRC6B]] | +0.64 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[WDR48]] | +0.63 | +0.30 / +0.65 | both halves | 2e-04 | same gene group |
| [[FBXL20]] | +0.61 | +0.30 / +0.68 | both halves | 2e-04 |  |
| [[MAP2K5]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[UBXN1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[HBP1]] | +0.58 | +0.29 / +0.61 | both halves | 2e-04 |  |
| [[RB1CC1]] | +0.57 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[RSF1]] | +0.56 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SYF2]] | +0.56 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[NBR1]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAX9]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PLAAT1]] | -0.48 | -0.18 / -0.51 | ⚠ one half (not replicated) | 1e-03 |  |
| [[APEX2]] | -0.45 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[ADORA2B]] | -0.44 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SH3BP1]] | -0.44 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[FAM222A-AS1]] | -0.43 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers BCAS3's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 5.3% of all compounds | 0.026 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, -43.5); signed map (-15.3, 11.1). **Vector** length 108, 48.0% of its response variance represented; |z| ≥ 3 in 2,430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | -18.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.3 | -20.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.0 | -14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -11.9 | -9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -11.6 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.5 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -8.6 | -8.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.6 | -9.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.2 | -10.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.9 | -8.8 |

## What is on record

|  |  |
|---|---|
| Name | BCAS3 microtubule associated cell migration factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:60,677,453-61,392,838 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20128, PHAF2 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6U6](https://www.uniprot.org/uniprotkb/Q9H6U6) (BCAS3 microtubule associated cell migration factor):

> Plays a role in angiogenesis. Participates in the regulation of cell polarity and directional endothelial cell migration by mediating both the activation and recruitment of CDC42 and the reorganization of the actin cytoskeleton at the cell leading edge. Promotes filipodia formation (By similarity). Functions synergistically with PELP1 as a transcriptional coactivator of estrogen receptor-responsive genes. Stimulates histone acetyltransferase activity. Binds to chromatin. Plays a regulatory role …

**Summary**, from NCBI Gene [54828](https://www.ncbi.nlm.nih.gov/gene/54828):

> Enables several functions, including acetyltransferase activator activity; beta-tubulin binding activity; and histone acetyltransferase binding activity. Involved in cellular response to estrogen stimulus; positive regulation of catalytic activity; and positive regulation of transcription by RNA polymerase II. Located in euchromatin; nucleus; and phagophore assembly site. Implicated in Hengel-Maroofian-Schols syndrome. Biomarker of breast cancer. [provided by Alliance of Genome Resources, Jul …

**Accessions** — [HGNC:14347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14347) · Entrez [54828](https://www.ncbi.nlm.nih.gov/gene/54828) · UniProt [Q9H6U6](https://www.uniprot.org/uniprotkb/Q9H6U6) · Ensembl [ENSG00000141376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141376)

## Data

Gene col 6506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6506); `tables/drug_effects.parquet` (95 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6506]; `tensor/DDL_lfc|DDL_z.npy` [6506]; `embed/gene_vectors.npy` [6506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6506 or target_col == 6506). Every well: [[BCAS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
