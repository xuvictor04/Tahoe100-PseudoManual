---
symbol: "HMBOX1"
type: "gene"
col: 7182
ensembl_id: "ENSG00000147421"
name: "homeobox containing 1"
location: "8p21.1-p12"
module: 178
arm: "+"
pooled_cpm: 144.31
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# HMBOX1

*homeobox containing 1* — 8p21.1-p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.58× (z +4.7, q 0.002, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.388× (z -20.0, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.562× (z -12.2, q 2e-32, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNKS]] (+0.67, fdr 7e-06), [[UBE4B]] (+0.63, fdr 1e-05), [[MYL6B]] (+0.59, fdr 3e-05); moves opposite to [[TNFRSF12A]] (-0.57, fdr 1e-04), [[RASGRF1]] (-0.56, fdr 1e-05), [[AKIRIN1]] (-0.55, fdr 3e-05).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LONRF3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.7 | 0.002 | 30/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.037 | 25/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.037 | 27/49 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.37× | +3.2 | 0.13 | 19/49 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.17× | +3.2 | 0.13 | 19/47 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.2 | 0.13 | 17/49 (SHP-77, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.388×** | -20.0 | 0e+00 | 48/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.410×** | -18.8 | 0e+00 | 48/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.437×** | -17.5 | 0e+00 | 48/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.442×** | -17.3 | 0e+00 | 47/49 (SHP-77, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.435×** | -16.9 | 0e+00 | 44/44 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.605×** | -15.0 | 0e+00 | 42/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.529×** | -12.9 | 2e-36 | 46/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.527×** | -12.5 | 5e-34 | 41/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.562×** | -12.2 | 2e-32 | 45/48 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.665×** | -12.2 | 2e-32 | 45/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.593×** | -10.6 | 1e-24 | 41/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.702×** | -10.6 | 2e-24 | 37/49 (A549, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.628×** | -9.8 | 4e-21 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.637×** | -9.1 | 2e-18 | 40/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -8.9 | 2e-17 | 42/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.723×** | -6.9 | 2e-10 | 37/49 (SW 1271, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.784×** | -5.1 | 7e-06 | 32/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.625×** | -4.8 | 4e-05 | 32/49 (RPMI-7951, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.002 | 23/48 (MIA PaCa-2, AN3 CA, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.851× | -3.3 | 0.022 | 21/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.022 | 18/49 (HS-578T, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.731×** | -3.2 | 0.025 | 20/48 (SW48, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.860× | -3.2 | 0.026 | 10/48 (NCI-H661, KATO III, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.750×** | -2.9 | 0.058 | 13/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.873× | -2.9 | 0.071 | 12/49 (NCI-H2347, NCI-H2122, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.865× | -2.8 | 0.076 | 19/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 184 | 0 | 16 (13 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.555× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 207 | 0 | 14 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -18.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.430× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -17.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.451× (z -10.4) |
| [[A-172 (line)]] | wt | 188 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.422× (z -11.2) |
| [[HS-578T (line)]] | alt | 244 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -15.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 220 | 0 | 12 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.353× (z -14.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.533× (z -12.1) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.577× (z -9.7) |
| [[SW 900 (line)]] | alt | 147 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -11.3) |
| [[SW480 (line)]] | alt | 183 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.559× (z -13.3) |
| [[Hs 766T (line)]] | wt | 175 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.630× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 146 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -18.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.528× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 122 | 0 | 10 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.596× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 203 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -21.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -10.7) |
| [[CHP-212 (line)]] | wt | 440 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 155 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -17.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 222 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.436× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -15.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -11.4) |
| [[KATO III (line)]] | alt | 189 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.600× (z -9.1) |
| [[HCT15 (line)]] | alt | 295 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 151 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -17.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.387× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -12.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 138 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 170 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -9.8) |
| [[HOP62 (line)]] | alt | 96.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 78.1 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.376× (z -10.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.459× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SHP-77 (line)]] | alt | 211 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW1417 (line)]] | alt | 61.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.470× (z -8.8) |
| [[A-427 (line)]] | wt | 142 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 59.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 198 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 62.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 98.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-1 (line)]] | wt | 204 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 1271 (line)]] | alt | 72.3 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0438× (z -13.0) |
| [[SW48 (line)]] | wt | 162 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 79.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 187 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNKS]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[UBE4B]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MYL6B]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PPHLN1]] | +0.59 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TENT2]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PIK3C3]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[DNASE2]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SUPV3L1]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ASB7]] | +0.57 | +0.63 / +0.43 | both halves | 3e-05 | STRING 466 |
| [[CDC26]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[DERL1]] | +0.57 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[MARCHF8]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | -0.57 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[RASGRF1]] | -0.56 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[AKIRIN1]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ARNT2]] | -0.54 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[PFN1]] | -0.54 | -0.61 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SKIL]] | -0.53 | -0.66 / -0.39 | both halves | 6e-05 |  |
| [[CCND1]] | -0.53 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[IL4R]] | -0.53 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[MAMLD1]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[EPHB2]] | -0.51 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[IER2]] | -0.50 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[KLF10]] | -0.49 | -0.58 / -0.26 | both halves | 4e-04 |  |
| [[MAP2K3]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LONRF3]] | B | LONRF3 activity lowers HMBOX1's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 1.43× higher at baseline in the lines without LONRF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | HMBOX1's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | HMBOX1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.417 over the table, 0.042 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.1, -12.0); signed map (-21.6, 3.9). **Vector** length 79.1, 26.2% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.9 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +4.6 | -17.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.4 | -16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | -2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.3 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | homeobox containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1-p12 — chr8:28,890,395-29,064,764 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNF1LA, PBHNF, FLJ21616, HOT1 |
| Gene groups (HGNC) | HNF class homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NT76](https://www.uniprot.org/uniprotkb/Q6NT76) (Homeobox-containing protein 1):

> Binds directly to 5'-TTAGGG-3' repeats in telomeric DNA. Associates with the telomerase complex at sites of active telomere processing and positively regulates telomere elongation. Important for TERT binding to chromatin, indicating a role in recruitment of the telomerase complex to telomeres (By similarity). Also plays a role in the alternative lengthening of telomeres (ALT) pathway in telomerase-negative cells where it promotes formation and/or maintenance of ALT-associated promyelocytic …

**Summary**, from NCBI Gene [79618](https://www.ncbi.nlm.nih.gov/gene/79618):

> Enables double-stranded telomeric DNA binding activity; identical protein binding activity; and sequence-specific double-stranded DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II; telomere maintenance via telomerase; and telomere-telomerase complex assembly. Located in chromosome, telomeric region; cytosol; and nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26137) · Entrez [79618](https://www.ncbi.nlm.nih.gov/gene/79618) · UniProt [Q6NT76](https://www.uniprot.org/uniprotkb/Q6NT76) · Ensembl [ENSG00000147421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147421)

## Data

Gene col 7182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7182); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7182]; `tensor/DDL_lfc|DDL_z.npy` [7182]; `embed/gene_vectors.npy` [7182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7182 or target_col == 7182). Every well: [[HMBOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMBOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
