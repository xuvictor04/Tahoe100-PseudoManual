---
symbol: "PLK4"
type: "gene"
col: 6651
ensembl_id: "ENSG00000142731"
name: "polo like kinase 4"
location: "4q28.1"
module: 22
arm: "+"
pooled_cpm: 22.28
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PLK4

*polo like kinase 4* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.42× (z +13.8, q 2e-40, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.97× (z +8.9, q 8e-17, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.700× (z -7.8, q 2e-12, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.742× (z -6.6, q 6e-09, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKA3]] (+0.90, fdr 7e-06), [[KIF15]] (+0.89, fdr 7e-06), [[NCAPG]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.42×** | +13.8 | 2e-40 | 43/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.24×** | +12.6 | 7e-34 | 36/46 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.79×** | +9.1 | 1e-17 | 33/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.79×** | +9.1 | 1e-17 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +8.9 | 8e-17 | 36/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +7.7 | 1e-12 | 30/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.66×** | +7.6 | 3e-12 | 29/46 (LoVo, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.56×** | +6.9 | 4e-10 | 27/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +6.1 | 9e-08 | 26/47 (NCI-H2030, RKO, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.40×** | +5.1 | 2e-05 | 21/48 (RKO, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.38×** | +5.0 | 2e-05 | 22/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.77×** | +4.7 | 2e-04 | 15/47 (NCI-H2347, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.20× | +4.0 | 0.003 | 14/48 (HS-578T, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.700×** | -7.8 | 2e-12 | 27/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.592×** | -7.4 | 4e-11 | 30/48 (LS 180, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.644×** | -6.9 | 1e-09 | 23/42 (HCT15, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.742×** | -6.6 | 6e-09 | 25/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -6.1 | 1e-07 | 24/48 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.696×** | -5.3 | 9e-06 | 23/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.756×** | -4.4 | 0.001 | 18/48 (A498, COLO 205, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.690×** | -4.1 | 0.003 | 13/48 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.772×** | -4.0 | 0.003 | 16/47 (HEC-1-A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.004 | 14/48 (HEC-1-A, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.764×** | -4.0 | 0.004 | 13/48 (Panc 03.27, HT-29, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.776×** | -3.9 | 0.004 | 14/48 (HEC-1-A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.781×** | -3.8 | 0.005 | 19/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.005 | 16/48 (J82, SW 900, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.005 | 14/47 (RKO, SW480, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.630×** | -3.8 | 0.006 | 16/46 (NCI-H23, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.716×** | -3.7 | 0.007 | 14/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.010 | 14/47 (PANC-1, SW 1271, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.870× | -3.1 | 0.057 | 14/48 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.827×** | -3.0 | 0.075 | 10/45 (SW48, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.829×** | -2.9 | 0.081 | 17/48 (C-33 A, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 18.4 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.95× (z +10.9) ⚠ cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 0.5 µM 0.0805× (z -12.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HEC-1-A (line)]] | alt | 55.1 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.51× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.448× (z -8.9) |
| [[LoVo (line)]] | wt | 15.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.56× (z +12.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 19.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.315× (z -10.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-427 (line)]] | wt | 37.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.230× (z -15.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.418× (z -9.4) |
| [[H4 (line)]] | wt | 24.6 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0419× (z -12.5) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.207× (z -9.7) |
| [[KATO III (line)]] | alt | 20.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.89× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 20.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +9.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -12.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.141× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0911× (z -8.9) ⚠ toxic |
| [[J82 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +11.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[RKO (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 26.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.152× (z -9.3) |
| [[AN3 CA (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA3]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | STRING 525 |
| [[KIF15]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 850 |
| [[NCAPG]] | +0.88 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 860 |
| [[POLQ]] | +0.87 | +0.89 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 506 |
| [[SHCBP1]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | STRING 513 |
| [[SPC25]] | +0.87 | +0.87 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 450 |
| [[KIF11]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 912 |
| [[MELK]] | +0.86 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 847 |
| [[NCAPH]] | +0.86 | +0.88 / +0.87 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 672 |
| [[FOXM1]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 | pathway: G2/M Transition; STRING 634 |
| [[KIF22]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ZGRF1]] | +0.85 | +0.86 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises PLK4's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without E2F8 | 0.025 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises PLK4's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without NDC80 | 0.053 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises PLK4's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without PBK | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises PLK4's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without MYBL2 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises PLK4's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.51× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[PBK]] | C | PBK activity strengthens PLK4's drug response | lines that do not express PBK (4) vs lines expressing it (44) | the lines without PBK respond 0.46× as strongly (z diff +1.81); strongest at PH-797804 5 µM: 0.67x vs 2.44x (z diff +2.7) | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -51.5); signed map (-45.0, -44.3). **Vector** length 118, 33.4% of its response variance represented; |z| ≥ 3 in 1,206 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.66 to 28); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.62 to 41); *Mitotic Anaphase* (reactome, mean cos +0.61 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.7 | +4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.5 | +6.9 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.9 | +13.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | -0.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.0 | +1.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.4 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.3 | -7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -4.2 | -7.8 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.6 | -4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | -3.2 | -3.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -1.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | polo like kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:127,880,893-127,899,224 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sak; previously STK18 |
| Gene groups (HGNC) | Polo like kinase family |
| Hallmark sets | MYC_TARGETS_V2, ESTROGEN_RESPONSE_LATE, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O00444](https://www.uniprot.org/uniprotkb/O00444) (Serine/threonine-protein kinase PLK4):

> Serine/threonine-protein kinase that plays a central role in centriole duplication. Able to trigger procentriole formation on the surface of the parental centriole cylinder, leading to the recruitment of centriole biogenesis proteins such as SASS6, CPAP, CCP110, CEP135 and gamma-tubulin. When overexpressed, it is able to induce centrosome amplification through the simultaneous generation of multiple procentrioles adjoining each parental centriole during S phase. Phosphorylates 'Ser-151' of …

**Summary**, from NCBI Gene [10733](https://www.ncbi.nlm.nih.gov/gene/10733):

> This gene encodes a member of the polo family of serine/threonine protein kinases. The protein localizes to centrioles, complex microtubule-based structures found in centrosomes, and regulates centriole duplication during the cell cycle. Three alternatively spliced transcript variants that encode different protein isoforms have been found for this gene. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:11397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11397) · Entrez [10733](https://www.ncbi.nlm.nih.gov/gene/10733) · UniProt [O00444](https://www.uniprot.org/uniprotkb/O00444) · Ensembl [ENSG00000142731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142731)

## Data

Gene col 6651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6651); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6651]; `tensor/DDL_lfc|DDL_z.npy` [6651]; `embed/gene_vectors.npy` [6651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6651 or target_col == 6651). Every well: [[PLK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
