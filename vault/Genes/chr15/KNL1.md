---
symbol: "KNL1"
type: "gene"
col: 6071
ensembl_id: "ENSG00000137812"
name: "kinetochore scaffold 1"
location: "15q15.1"
module: 22
arm: "+"
pooled_cpm: 79.17
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KNL1

*kinetochore scaffold 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (24 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +11.1, q 1e-25, up in 32 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 1.83× (z +5.3, q 4e-06, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.486× (z -16.8, q 0e+00, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.650× (z -7.3, q 6e-11, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKI67]] (+0.95, fdr 7e-06), [[NDC80]] (+0.94, fdr 7e-06), [[NCAPG]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 26 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +11.1 | 1e-25 | 32/47 (NCI-H2347, NCI-H2030, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.92×** | +10.7 | 5e-24 | 41/47 (PANC-1, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.85×** | +10.5 | 3e-23 | 40/47 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.79×** | +9.9 | 9e-21 | 42/47 (A498, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.78×** | +9.8 | 2e-20 | 39/47 (LoVo, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.71×** | +9.1 | 7e-18 | 41/47 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.63×** | +8.3 | 1e-14 | 35/47 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.42×** | +8.2 | 1e-14 | 40/47 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.48×** | +6.7 | 1e-09 | 32/47 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.48×** | +6.6 | 2e-09 | 32/47 (A-172, NCI-H2347, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.48×** | +6.4 | 7e-09 | 25/43 (NCI-H1792, A-172, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.46×** | +6.4 | 1e-08 | 30/47 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.39×** | +5.6 | 8e-07 | 30/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.83×** | +5.3 | 4e-06 | 29/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +5.1 | 1e-05 | 28/47 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.5 | 3e-04 | 19/47 (RKO, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.005 | 20/47 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.017 | 17/47 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.026 | 14/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.043 | 12/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.049 | 8/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.053 | 14/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 1.19× | +2.9 | 0.063 | 10/47 (KATO III, SW480, …) | top dose only | plate-row cell shift |
| [[Relugolix (drug)]] 0.5 µM |  | 1.18× | +2.8 | 0.072 | 7/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.18× | +2.8 | 0.076 | 9/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.17× | +2.7 | 0.094 | 15/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.17× | +2.7 | 0.095 | 12/47 (HOP62, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.486×** | -16.8 | 0e+00 | 44/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.479×** | -12.4 | 5e-33 | 42/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.645×** | -7.4 | 3e-11 | 40/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -7.3 | 6e-11 | 33/47 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.483×** | -6.4 | 1e-08 | 36/44 (SHP-77, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.595×** | -6.4 | 1e-08 | 34/47 (A-172, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.698×** | -6.0 | 1e-07 | 25/47 (A-172, HT-29, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.649×** | -5.2 | 1e-05 | 29/47 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.635×** | -4.0 | 0.004 | 20/48 (J82, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.643×** | -3.9 | 0.006 | 22/47 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.848× | -3.8 | 0.006 | 20/47 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.803×** | -3.7 | 0.010 | 22/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.804×** | -3.7 | 0.010 | 20/47 (H4, HCT15, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.810×** | -3.5 | 0.015 | 18/47 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.860× | -3.5 | 0.015 | 14/47 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.746×** | -3.5 | 0.016 | 20/47 (A-427, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.705×** | -3.1 | 0.056 | 17/46 (LS 180, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.838× | -3.0 | 0.078 | 12/47 (HEC-1-A, SW 900, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.715×** | -3.0 | 0.078 | 15/47 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.841× | -2.9 | 0.079 | 17/47 (RKO, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 54.6 | 3 (3 ⚠) | 5 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.98× (z +10.0) ⚠ cell-cycle shift, explains ~58% of this change | [[Selinexor (drug)]] 5 µM 0.199× (z -20.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.402× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 81.0 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.261× (z -14.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.286× (z -9.6) |
| [[A-172 (line)]] | wt | 76.1 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.233× (z -16.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.445× (z -9.3) |
| [[RKO (line)]] | wt | 110 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 60.9 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.117× (z -17.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.308× (z -10.0) |
| [[PANC-1 (line)]] | alt | 125 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.550× (z -10.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 54.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.412× (z -10.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[H4 (line)]] | wt | 84.0 | 0 | 4 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.101× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 110 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.282× (z -15.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[KATO III (line)]] | alt | 84.4 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +10.1) ⚠ cell-cycle shift, explains ~88% of this change | — |
| [[LoVo (line)]] | wt | 107 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +11.7) ⚠ cell-cycle shift, explains ~88% of this change | [[Selinexor (drug)]] 5 µM 0.443× (z -10.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 111 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.204× (z -22.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.409× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 110 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +16.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.529× (z -9.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SNU-1 (line)]] | wt | 87.3 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -10.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[C32 (line)]] | wt | 59.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.404× (z -9.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CFPAC-1 (line)]] | alt | 49.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.258× (z -14.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HCT15 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.334× (z -11.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HOP62 (line)]] | alt | 73.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.409× (z -11.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HS-578T (line)]] | alt | 47.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 58.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 118 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.74× (z +9.8) ⚠ cell-cycle shift, explains ~79% of this change | [[Selinexor (drug)]] 5 µM 0.473× (z -10.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H2347 (line)]] | alt | 36.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +17.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 57.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.265× (z -15.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 68.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.342× (z -12.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW1417 (line)]] | alt | 84.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.495× (z -9.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW48 (line)]] | wt | 94.7 | 0 | 2 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.355× (z -10.6) |
| [[SW480 (line)]] | alt | 116 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.38× (z +10.4) ⚠ cell-cycle shift, explains ~79% of this change | [[Selinexor (drug)]] 0.5 µM 0.449× (z -9.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[AN3 CA (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 51.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.259× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 96.2 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.424× (z -8.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 59.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -12.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.200× (z -10.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H1573 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.386× (z -9.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.386× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SHP-77 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0941× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 89.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.475× (z -8.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[AsPC-1 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKI67]] | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 562 |
| [[NDC80]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 995 |
| [[NCAPG]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 652 |
| [[KIF4A]] | +0.93 | +0.92 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 588 |
| [[TPX2]] | +0.91 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 551 |
| [[SMC4]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 566 |
| [[KIF23]] | +0.91 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 762 |
| [[TOP2A]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 711 |
| [[SGO1]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 793 |
| [[DLGAP5]] | +0.90 | +0.88 / +0.89 | both halves | 7e-06 | STRING 748 |
| [[BIRC5]] | +0.90 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 514 |
| [[NCAPH]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 538 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KNL1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without PIMREG | 0.036 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises KNL1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.43× lower at baseline in the lines without PBK | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises KNL1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.59× lower at baseline in the lines without NDC80 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KNL1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without AURKB | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KNL1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.64× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises KNL1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.941). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.8, -55.2); signed map (-49.0, -43.7). **Vector** length 167, 64.4% of its response variance represented; |z| ≥ 3 in 1,532 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.82 to 28); *E2F targets* (hallmark, mean cos +0.72 to 46); *mitotic spindle* (hallmark, mean cos +0.77 to 38).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +6.3 | +9.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | +6.2 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +5.8 | +6.7 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +5.6 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +5.5 | +10.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.7 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.0 | +2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.9 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -13.7 | -16.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -11.7 | -12.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | -9.0 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.8 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -7.6 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.2 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | kinetochore scaffold 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,594,020-40,664,342 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D40, AF15Q14, CT29, KIAA1570, hKNL-1, hSpc105, PPP1R55, Spc7; previously MCPH4, CASC5 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; KNL1 complex |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NG31](https://www.uniprot.org/uniprotkb/Q8NG31) (Outer kinetochore KNL1 complex subunit KNL1):

> Acts as a component of the outer kinetochore KNL1 complex that serves as a docking point for spindle assembly checkpoint components and mediates microtubule-kinetochore interactions. Kinetochores, consisting of a centromere-associated inner segment and a microtubule-contacting outer segment, play a crucial role in chromosome segregation by mediating the physical connection between centromeric DNA and spindle microtubules. The outer kinetochore is made up of the ten-subunit KMN network, …

**Summary**, from NCBI Gene [57082](https://www.ncbi.nlm.nih.gov/gene/57082):

> The protein encoded by this gene is a component of the multiprotein assembly that is required for creation of kinetochore-microtubule attachments and chromosome segregation. The encoded protein functions as a scaffold for proteins that influence the spindle assembly checkpoint during the eukaryotic cell cycle and it interacts with at least five different kinetochore proteins and two checkpoint kinases. In adults, this gene is predominantly expressed in normal testes, various cancer cell lines …

**Accessions** — [HGNC:24054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24054) · Entrez [57082](https://www.ncbi.nlm.nih.gov/gene/57082) · UniProt [Q8NG31](https://www.uniprot.org/uniprotkb/Q8NG31) · Ensembl [ENSG00000137812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137812)

## Data

Gene col 6071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6071); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6071]; `tensor/DDL_lfc|DDL_z.npy` [6071]; `embed/gene_vectors.npy` [6071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6071 or target_col == 6071). Every well: [[KNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
