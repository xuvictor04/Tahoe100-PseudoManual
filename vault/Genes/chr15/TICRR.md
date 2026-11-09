---
symbol: "TICRR"
type: "gene"
col: 6426
ensembl_id: "ENSG00000140534"
name: "TOPBP1 interacting checkpoint and replication regulator"
location: "15q26.1"
module: 67
arm: "+"
pooled_cpm: 29.14
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# TICRR

*TOPBP1 interacting checkpoint and replication regulator* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.52× (z +11.9, q 5e-30, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.77× (z +9.0, q 4e-17, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.473× (z -9.7, q 1e-19, down in 33 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.677× (z -5.1, q 4e-05, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPC25]] (+0.89, fdr 7e-06), [[NCAPD3]] (+0.86, fdr 7e-06), [[KIF22]] (+0.86, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.52×** | +11.9 | 5e-30 | 39/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **2.42×** | +11.4 | 2e-27 | 39/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.31×** | +10.8 | 8e-25 | 37/45 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.20×** | +10.2 | 4e-22 | 38/46 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.77×** | +9.0 | 4e-17 | 40/46 (RKO, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.97×** | +8.8 | 2e-16 | 31/45 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.98×** | +8.4 | 3e-15 | 31/45 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.89×** | +8.2 | 2e-14 | 34/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.26×** | +8.0 | 1e-13 | 36/45 (A-172, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.80×** | +7.6 | 2e-12 | 37/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.77×** | +7.1 | 7e-11 | 33/46 (NCI-H23, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.61×** | +6.1 | 4e-08 | 25/45 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.38×** | +5.9 | 2e-07 | 22/46 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.45×** | +4.8 | 7e-05 | 23/45 (HT-29, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.45×** | +4.8 | 8e-05 | 22/46 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.006 | 16/44 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.025 | 14/45 (MIA PaCa-2, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.031 | 16/46 (A549, LOX-IMVI, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.047 | 15/46 (A549, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.473×** | -9.7 | 1e-19 | 33/41 (HCT15, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -9.6 | 3e-19 | 25/35 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.554×** | -7.7 | 3e-12 | 33/46 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.670×** | -7.4 | 2e-11 | 28/46 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -5.1 | 4e-05 | 27/45 (C32, Panc 03.27, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -4.9 | 1e-04 | 22/46 (A498, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.731×** | -4.1 | 0.004 | 23/46 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -4.0 | 0.004 | 19/46 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.734×** | -3.9 | 0.007 | 18/46 (NCI-H1573, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.747×** | -3.8 | 0.008 | 22/46 (A-427, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.590×** | -3.6 | 0.017 | 18/45 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.767×** | -3.3 | 0.040 | 15/45 (NCI-H661, A498, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.778×** | -3.3 | 0.045 | 21/45 (NCI-H460, LOX-IMVI, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **0.781×** | -3.2 | 0.048 | 14/45 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.051 | 17/44 (A549, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.052 | 15/45 (NCI-H661, NCI-H460, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.786×** | -3.0 | 0.089 | 15/46 (Hs 766T, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.84 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.4 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.28× (z +13.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 38.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -13.8) |
| [[A498 (line)]] | wt | 27.9 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.143× (z -19.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.321× (z -11.5) |
| [[H4 (line)]] | wt | 34.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0553× (z -13.4) |
| [[A549 (line)]] | wt | 39.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.09× (z +9.0) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 49.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.2) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 22.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.57× (z +9.6) ⚠ cell-cycle shift, explains ~65% of this change | [[Selinexor (drug)]] 5 µM 0.355× (z -9.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.380× (z -8.7) |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.136× (z -14.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.306× (z -8.8) |
| [[SW480 (line)]] | alt | 24.9 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +9.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 25.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 41.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.364× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.256× (z -9.4) |
| [[KATO III (line)]] | alt | 27.3 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.31× (z +11.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +8.7) ⚠ cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -19.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0610× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 23.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +8.7) ⚠ cell-cycle shift, explains ~62% of this change | [[Selinexor (drug)]] 5 µM 0.417× (z -8.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[RKO (line)]] | wt | 31.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -13.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.277× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H2030 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.332× (z -9.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SHP-77 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPC25]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[NCAPD3]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[KIF22]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 |  |
| [[STIL]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 | STRING 430 |
| [[BARD1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SPC24]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 |  |
| [[KIFC1]] | +0.84 | +0.84 / +0.84 | both halves | 7e-06 | STRING 447 |
| [[PBK]] | +0.84 | +0.88 / +0.83 | both halves | 7e-06 | STRING 553 |
| [[MELK]] | +0.83 | +0.85 / +0.81 | both halves | 7e-06 | STRING 506 |
| [[POLQ]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | STRING 565 |
| [[NEIL3]] | +0.83 | +0.83 / +0.83 | both halves | 7e-06 | STRING 408 |
| [[SPAG5]] | +0.83 | +0.85 / +0.81 | both halves | 7e-06 | STRING 484 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises TICRR's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.46× lower at baseline in the lines without E2F8 | 0.009 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises TICRR's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.18× lower at baseline in the lines without PIMREG | 0.012 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises TICRR's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without DSCC1 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises TICRR's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.98× lower at baseline in the lines without PBK | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[CDCA3]] | C | CDCA3 activity raises TICRR's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.65× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises TICRR's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.08× lower at baseline in the lines without MELK, TK1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.891). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.9, -50.8); signed map (-43.5, -41.2). **Vector** length 133, 42.5% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.79 to 12); *G2/M checkpoint* (hallmark, mean cos +0.79 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.75 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.8 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.7 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.3 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.0 | +10.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.8 | +11.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +8.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +1.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.6 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.6 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -8.3 | -7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -7.4 | -7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.8 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.2 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TOPBP1 interacting checkpoint and replication regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,575,469-89,631,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45866, FLJ41618, Treslin, SLD3; previously C15orf42 |
| Reactome | 5 pathways, smallest: Cyclin A/B1/B2 associated events during G2/M transition; G2/M Transition; Mitotic G2-G2/M phases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2Z1](https://www.uniprot.org/uniprotkb/Q7Z2Z1) (Treslin):

> Regulator of DNA replication and S/M and G2/M checkpoints. Regulates the triggering of DNA replication initiation via its interaction with TOPBP1 by participating in CDK2-mediated loading of CDC45L onto replication origins. Required for the transition from pre-replication complex (pre-RC) to pre-initiation complex (pre-IC). Required to prevent mitotic entry after treatment with ionizing radiation.

**Summary**, from NCBI Gene [90381](https://www.ncbi.nlm.nih.gov/gene/90381):

> Enables chromatin binding activity. Involved in regulation of DNA-templated DNA replication initiation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28704) · Entrez [90381](https://www.ncbi.nlm.nih.gov/gene/90381) · UniProt [Q7Z2Z1](https://www.uniprot.org/uniprotkb/Q7Z2Z1) · Ensembl [ENSG00000140534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140534)

## Data

Gene col 6426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6426); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6426]; `tensor/DDL_lfc|DDL_z.npy` [6426]; `embed/gene_vectors.npy` [6426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6426 or target_col == 6426). Every well: [[TICRR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TICRR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
