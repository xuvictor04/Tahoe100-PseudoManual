---
symbol: "STIL"
type: "gene"
col: 4437
ensembl_id: "ENSG00000123473"
name: "STIL centriolar assembly protein"
location: "1p33"
module: 67
arm: "+"
pooled_cpm: 65.41
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 30
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# STIL

*STIL centriolar assembly protein* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.22× (z +12.7, q 2e-34, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.90× (z +4.9, q 4e-05, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.526× (z -10.2, q 8e-22, down in 36 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.618× (z -7.7, q 2e-12, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AURKB]] (+0.88, fdr 7e-06), [[SPC24]] (+0.88, fdr 7e-06), [[KIFC1]] (+0.86, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.22×** | +12.7 | 2e-34 | 41/47 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.21×** | +12.6 | 5e-34 | 43/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.11×** | +11.9 | 1e-30 | 44/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.07×** | +11.6 | 6e-29 | 40/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.96×** | +10.8 | 6e-25 | 39/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.84×** | +9.7 | 3e-20 | 43/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.70×** | +8.5 | 2e-15 | 36/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.50×** | +6.5 | 6e-09 | 27/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.50×** | +6.4 | 7e-09 | 35/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.15×** | +5.8 | 3e-07 | 36/47 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.44×** | +5.8 | 4e-07 | 25/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.42×** | +5.6 | 1e-06 | 26/47 (LoVo, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.9 | 4e-05 | 23/47 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.007 | 18/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.18× | +3.4 | 0.022 | 19/47 (RKO, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.032 | 12/47 (RKO, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.526×** | -10.2 | 8e-22 | 36/47 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -9.6 | 3e-19 | 31/41 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.671×** | -8.4 | 6e-15 | 33/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -7.7 | 2e-12 | 38/47 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.608×** | -7.2 | 5e-11 | 36/47 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.711×** | -5.4 | 5e-06 | 35/47 (Hs 766T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -4.9 | 1e-04 | 28/47 (A-427, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.723×** | -4.7 | 2e-04 | 29/47 (HCT15, CFPAC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.725×** | -4.7 | 2e-04 | 24/47 (COLO 205, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.726×** | -4.7 | 2e-04 | 27/46 (Hs 766T, SW 1271, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.753×** | -4.3 | 7e-04 | 23/46 (HOP62, A-427, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.688×** | -4.2 | 0.001 | 21/45 (Hs 766T, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.761×** | -4.2 | 0.001 | 27/47 (A498, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.753×** | -4.2 | 0.001 | 21/43 (J82, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.823×** | -3.9 | 0.004 | 20/47 (Hs 766T, LS 180, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.830×** | -3.9 | 0.004 | 21/47 (PANC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.799×** | -3.6 | 0.012 | 15/46 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.795×** | -3.5 | 0.014 | 19/46 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.017 | 16/47 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.848× | -3.3 | 0.029 | 15/47 (SW 1271, Hs 766T, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.652×** | -3.3 | 0.029 | 15/46 (A549, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.036 | 11/47 (SW48, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 111 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.386× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 36.5 | 7 (7 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 4.59× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 0.5 µM 0.269× (z -9.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LoVo (line)]] | wt | 39.4 | 6 (6 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.46× (z +13.4) ⚠ cell-cycle shift, explains ~56% of this change | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 47.8 | 2 (2 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.51× (z +9.6) ⚠ cell-cycle shift, explains ~57% of this change | [[Dinaciclib (drug)]] 5 µM 0.194× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 75.9 | 5 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +15.1) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.448× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 143 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.316× (z -13.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.258× (z -12.3) |
| [[KATO III (line)]] | alt | 39.9 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +12.2) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[LS 180 (line)]] | wt | 34.2 | 3 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.86× (z +11.8) ⚠ cell-cycle shift, explains ~46% of this change | [[Selinexor (drug)]] 5 µM 0.231× (z -12.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 101 | 1 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.77× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Dinaciclib (drug)]] 5 µM 0.103× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -8.8) |
| [[RKO (line)]] | wt | 83.3 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 69.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[J82 (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -15.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 51.6 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.235× (z -13.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-172 (line)]] | wt | 44.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -10.6) ⚠ cell-cycle shift, explains ~58% of this change |
| [[AN3 CA (line)]] | alt | 93.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 88.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.300× (z -9.2) |
| [[COLO 205 (line)]] | alt | 84.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0785× (z -12.6) |
| [[Hs 766T (line)]] | wt | 53.0 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.23× (z +8.8) ⚠ cell-cycle shift, explains ~56% of this change | [[XRK3F2 (drug)]] 0.5 µM 0.151× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.1) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 58.9 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0878× (z -9.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 87.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 69.4 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.140× (z -10.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HCT15 (line)]] | alt | 96.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.393× (z -10.6) |
| [[HOP62 (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 81.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 55.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -8.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[BT-474 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AURKB]] | +0.88 | +0.88 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 454 |
| [[SPC24]] | +0.88 | +0.85 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[KIFC1]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.86 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[BARD1]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[TICRR]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 | STRING 430 |
| [[CIT]] | +0.85 | +0.83 / +0.84 | both halves | 7e-06 |  |
| [[KIF22]] | +0.85 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[SPC25]] | +0.84 | +0.87 / +0.86 | both halves | 7e-06 |  |
| [[PBK]] | +0.84 | +0.85 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 471 |
| [[CENPI]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 | STRING 684 |
| [[CDCA5]] | +0.83 | +0.84 / +0.86 | both halves | 7e-06 | STRING 404 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises STIL's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without E2F8 | 0.018 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises STIL's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without TLCD3B | 0.069 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises STIL's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without AURKB | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.910). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.6, -51.5); signed map (-44.3, -40.5). **Vector** length 149, 54.2% of its response variance represented; |z| ≥ 3 in 1,425 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.81 to 12); *Mitotic Prometaphase* (reactome, mean cos +0.76 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.76 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +6.2 | +12.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.3 | +12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.2 | +10.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.0 | +6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.7 | +5.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.1 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.5 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -10.2 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.4 | -7.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -8.0 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.5 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | STIL centriolar assembly protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:47,250,139-47,314,892 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCPH7; previously SIL |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15468](https://www.uniprot.org/uniprotkb/Q15468) (SCL-interrupting locus protein):

> Immediate-early gene. Plays an important role in embryonic development as well as in cellular growth and proliferation; its long-term silencing affects cell survival and cell cycle distribution as well as decreases CDK1 activity correlated with reduced phosphorylation of CDK1. Plays a role as a positive regulator of the sonic hedgehog pathway, acting downstream of PTCH1. Plays an important role in the regulation of centriole duplication. Required for the onset of procentriole formation and …

**Summary**, from NCBI Gene [6491](https://www.ncbi.nlm.nih.gov/gene/6491):

> This gene encodes a cytoplasmic protein implicated in regulation of the mitotic spindle checkpoint, a regulatory pathway that monitors chromosome segregation during cell division to ensure the proper distribution of chromosomes to daughter cells. The protein is phosphorylated in mitosis and in response to activation of the spindle checkpoint, and disappears when cells transition to G1 phase. It interacts with a mitotic regulator, and its expression is required to efficiently activate the …

**Accessions** — [HGNC:10879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10879) · Entrez [6491](https://www.ncbi.nlm.nih.gov/gene/6491) · UniProt [Q15468](https://www.uniprot.org/uniprotkb/Q15468) · Ensembl [ENSG00000123473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123473)

## Data

Gene col 4437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4437); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4437]; `tensor/DDL_lfc|DDL_z.npy` [4437]; `embed/gene_vectors.npy` [4437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4437 or target_col == 4437). Every well: [[STIL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STIL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
