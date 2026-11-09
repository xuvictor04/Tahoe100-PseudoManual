---
symbol: "RACGAP1"
type: "gene"
col: 8453
ensembl_id: "ENSG00000161800"
name: "Rac GTPase activating protein 1"
location: "12q13.12"
module: 22
arm: "+"
pooled_cpm: 66.23
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# RACGAP1

*Rac GTPase activating protein 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.37× (z +13.0, q 5e-36, up in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.73× (z +4.3, q 8e-04, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (PANC-1 3.47×, RKO 5.63×, Panc 03.27 4.18×, A549 4.52×, …; ⚠ cell-cycle shift, explains ~96% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (LoVo 4.37×, KATO III 3.80×, NCI-H460 3.64×, NCI-H23 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (KATO III 5.01×, LoVo 5.12×, NCI-H460 3.89×; ⚠ cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.532× (z -9.6, q 6e-19, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.705× (z -7.5, q 1e-11, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC5]] (+0.93, fdr 7e-06), [[NCAPH]] (+0.92, fdr 7e-06), [[TPX2]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 14 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (PANC-1 3.47×, RKO 5.63×, Panc 03.27 4.18×, A549 4.52×, …; ⚠ cell-cycle shift, explains ~96% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (LoVo 4.37×, KATO III 3.80×, NCI-H460 3.64×, NCI-H23 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (KATO III 5.01×, LoVo 5.12×, NCI-H460 3.89×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.37×** | +13.0 | 5e-36 | 44/47 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.74×** | +11.8 | 1e-29 | 36/47 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.81×** | +8.9 | 8e-17 | 38/47 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.78×** | +8.7 | 5e-16 | 36/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.69×** | +7.6 | 3e-12 | 40/47 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.58×** | +6.9 | 4e-10 | 27/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.49×** | +6.0 | 1e-07 | 29/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.51×** | +6.0 | 1e-07 | 31/46 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.48×** | +5.9 | 3e-07 | 29/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.93×** | +5.2 | 1e-05 | 33/46 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +4.3 | 8e-04 | 23/47 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.3 | 9e-04 | 2/47 (NCI-H2030, HOP62) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.29×** | +3.9 | 0.005 | 20/47 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.26×** | +3.5 | 0.021 | 17/47 (PANC-1, C32, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.2 | 0.047 | 13/47 (NCI-H23, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.532×** | -9.6 | 6e-19 | 42/47 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.667×** | -8.7 | 1e-15 | 33/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -7.5 | 1e-11 | 31/47 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.727×** | -6.8 | 1e-09 | 30/47 (A498, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.635×** | -6.5 | 9e-09 | 36/47 (A-427, SW480, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -6.3 | 4e-08 | 34/47 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -5.6 | 1e-06 | 29/47 (SHP-77, A498, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.771×** | -5.6 | 2e-06 | 28/47 (A498, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.711×** | -5.2 | 1e-05 | 31/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.710×** | -5.0 | 3e-05 | 24/46 (H4, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.538×** | -4.9 | 5e-05 | 30/44 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.746×** | -4.5 | 4e-04 | 24/47 (A498, H4, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.751×** | -4.2 | 0.001 | 21/47 (KATO III, A498, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.772×** | -3.9 | 0.003 | 23/47 (LOX-IMVI, LoVo, …) | all doses, flat | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.833× | -3.9 | 0.003 | 22/47 (AsPC-1, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.854× | -3.4 | 0.022 | 14/47 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.801×** | -3.4 | 0.023 | 14/47 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 0.867× | -3.1 | 0.059 | 13/47 (Hs 766T, SW 1271, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.068 | 18/47 (AN3 CA, A498, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.759×** | -3.0 | 0.073 | 12/47 (CFPAC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.824×** | -2.9 | 0.079 | 17/47 (SHP-77, C-33 A, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.825×** | -2.9 | 0.081 | 7/47 (AsPC-1, C-33 A, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.7 | 6 (6 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.0) ⚠ cell-cycle shift, explains ~96% of this change | [[Selinexor (drug)]] 5 µM 0.407× (z -11.2) ⚠ cell-cycle shift, explains ~83% of this change |
| [[A498 (line)]] | wt | 84.3 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.305× (z -16.2) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.344× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 77.2 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.9) ⚠ cell-cycle shift, explains ~96% of this change | [[Selinexor (drug)]] 5 µM 0.304× (z -12.7) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.387× (z -10.1) |
| [[A-172 (line)]] | wt | 55.4 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.359× (z -12.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.474× (z -9.4) |
| [[H4 (line)]] | wt | 79.3 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.256× (z -10.8) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -10.5) |
| [[HOP62 (line)]] | alt | 62.7 | 2 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.2) ⚠ cell-cycle shift, explains ~96% of this change | [[Auranofin (drug)]] 5 µM 0.356× (z -9.1) |
| [[LoVo (line)]] | wt | 40.7 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.12× (z +14.2) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[LS 180 (line)]] | wt | 42.5 | 2 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +9.6) ⚠ cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.9) |
| [[PANC-1 (line)]] | alt | 69.5 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +19.0) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[KATO III (line)]] | alt | 62.6 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +14.3) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 95.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.54× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Selinexor (drug)]] 5 µM 0.505× (z -8.5) ⚠ cell-cycle shift, explains ~83% of this change |
| [[A-427 (line)]] | wt | 136 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.208× (z -20.4) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.482× (z -9.5) |
| [[C32 (line)]] | wt | 49.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.3) ⚠ cell-cycle shift, explains ~96% of this change | [[Selinexor (drug)]] 5 µM 0.335× (z -10.2) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HEC-1-A (line)]] | alt | 84.6 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.5) ⚠ cell-cycle shift, explains ~96% of this change | [[Auranofin (drug)]] 5 µM 0.407× (z -10.7) |
| [[SHP-77 (line)]] | alt | 119 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -9.2) |
| [[A549 (line)]] | wt | 57.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +16.6) ⚠ cell-cycle shift, explains ~96% of this change | [[Selinexor (drug)]] 0.5 µM 0.336× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SNU-1 (line)]] | wt | 73.0 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.162× (z -10.1) ⚠ cell-cycle shift, explains ~96% of this change |
| [[SW1417 (line)]] | alt | 68.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.3) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[AsPC-1 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +8.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[COLO 205 (line)]] | alt | 26.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0632× (z -14.2) |
| [[Hs 766T (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.195× (z -15.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HS-578T (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.9) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +8.8) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[J82 (line)]] | alt | 92.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.0) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[NCI-H2030 (line)]] | alt | 99.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +15.6) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[NCI-H2347 (line)]] | alt | 88.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.9) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0970× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 64.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +17.7) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[RKO (line)]] | wt | 53.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +17.9) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[SNU-423 (line)]] | alt | 63.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.8) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[SW 1271 (line)]] | alt | 98.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.8) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[SW480 (line)]] | alt | 91.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC5]] | +0.93 | +0.91 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 827 |
| [[NCAPH]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | STRING 660 |
| [[TPX2]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 864 |
| [[NCAPG]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | STRING 864 |
| [[KIF4A]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 907 |
| [[KIF11]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 978 |
| [[CCNA2]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 856 |
| [[CDK1]] | +0.91 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 960 |
| [[KIF23]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[SPAG5]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 771 |
| [[TOP2A]] | +0.90 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 882 |
| [[CIT]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 639 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RACGAP1's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises RACGAP1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without PIMREG | 0.069 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises RACGAP1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without AURKB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises RACGAP1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without PBK | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NOPCHAP1]] | C | NOPCHAP1's natural level strengthens RACGAP1's drug response | NOPCHAP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.06; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[CDC20]] | C | CDC20 activity raises RACGAP1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.63× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.941). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.9, -54.8); signed map (-48.4, -42.9). **Vector** length 146, 53.6% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.83 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.73 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.73 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +6.2 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +5.7 | +11.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.4 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +4.0 | +7.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +1.0 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.2 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -0.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -8.9 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -8.2 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -7.1 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.0 | -2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Rac GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,976,923-50,033,136 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MgcRacGAP, CYK4 |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 24 pathways, smallest: Kinesins; RHOD GTPase cycle; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0H5](https://www.uniprot.org/uniprotkb/Q9H0H5) (Rac GTPase-activating protein 1):

> Component of the centralspindlin complex that serves as a microtubule-dependent and Rho-mediated signaling required for the myosin contractile ring formation during the cell cycle cytokinesis. Required for proper attachment of the midbody to the cell membrane during cytokinesis. Sequentially binds to ECT2 and RAB11FIP3 which regulates cleavage furrow ingression and abscission during cytokinesis. Plays key roles in controlling cell growth and differentiation of hematopoietic cells through …

**Summary**, from NCBI Gene [29127](https://www.ncbi.nlm.nih.gov/gene/29127):

> This gene encodes a GTPase-activating protein (GAP) that is a compoment of the centralspindlin complex. This protein binds activated forms of Rho GTPases and stimulates GTP hydrolysis, which results in negative regulation of Rho-mediated signals. This protein plays a regulatory role in cytokinesis, cell growth, and differentiation. Alternatively spliced transcript variants have been found for this gene. There is a pseudogene for this gene on chromosome 12. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:9804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9804) · Entrez [29127](https://www.ncbi.nlm.nih.gov/gene/29127) · UniProt [Q9H0H5](https://www.uniprot.org/uniprotkb/Q9H0H5) · Ensembl [ENSG00000161800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161800)

## Data

Gene col 8453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8453); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8453]; `tensor/DDL_lfc|DDL_z.npy` [8453]; `embed/gene_vectors.npy` [8453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8453 or target_col == 8453). Every well: [[RACGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RACGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
