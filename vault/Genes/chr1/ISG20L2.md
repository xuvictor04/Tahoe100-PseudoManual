---
symbol: "ISG20L2"
type: "gene"
col: 6711
ensembl_id: "ENSG00000143319"
name: "interferon stimulated exonuclease gene 20 like 2"
location: "1q23.1"
module: 149
arm: "+"
pooled_cpm: 36.84
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# ISG20L2

*interferon stimulated exonuclease gene 20 like 2* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.00× (z +8.6, q 4e-15, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.725× (z -3.8, q 0.067, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 0.177×, LoVo 0.148×, A-172 0.184×, HepG2/C3A 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.371×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP14]] (+0.72, fdr 7e-06), [[ZNF557]] (+0.71, fdr 7e-06), [[YRDC]] (+0.67, fdr 7e-06); moves opposite to [[NCKAP1]] (-0.64, fdr 7e-06), [[UBQLN1]] (-0.63, fdr 1e-05), [[TNPO1]] (-0.61, fdr 2e-05).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +8.6 | 4e-15 | 35/47 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +8.5 | 4e-15 | 42/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.0 | 2e-13 | 39/48 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.88×** | +7.8 | 8e-13 | 42/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.51×** | +7.2 | 5e-11 | 34/47 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.75×** | +6.7 | 3e-09 | 41/48 (AsPC-1, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.63×** | +6.1 | 1e-07 | 40/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.62×** | +6.0 | 2e-07 | 40/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 3e-07 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.57×** | +5.6 | 1e-06 | 31/46 (BT-474, AsPC-1, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.3 | 5e-06 | 31/48 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +5.2 | 9e-06 | 35/49 (LoVo, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.1 | 2e-05 | 4/48 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +4.6 | 1e-04 | 33/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.45×** | +4.6 | 2e-04 | 26/48 (AsPC-1, BT-474, …) | rises with dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +4.5 | 2e-04 | 34/46 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.003 | 26/46 (H4, RKO, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.005 | 25/46 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.025 | 19/46 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.032 | 17/48 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +3.2 | 0.034 | 19/47 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +3.1 | 0.042 | 17/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.045 | 15/47 (NCI-H23, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.0 | 0.051 | 17/48 (RKO, HS-578T, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.060 | 12/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 0.177×, LoVo 0.148×, A-172 0.184×, HepG2/C3A 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.371×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.725×** | -3.8 | 0.067 | 26/47 (NCI-H23, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.752× | -3.3 | 0.28 | 17/48 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.844× | -3.0 | 0.32 | 13/48 (NCI-H1792, PANC-1, …) | rises with dose | position effect removed |
| [[Pyridoxine (drug)]] 5 µM |  | 0.844× | -3.0 | 0.32 | 16/48 (SNU-423, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 39.3 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.10× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 38.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +8.5) | — |
| [[A-172 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.60× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[CFPAC-1 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.2) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 37.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +8.5) | — |
| [[LoVo (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.7) | — |
| [[A-427 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP14]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |
| [[ZNF557]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[YRDC]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.65 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.64 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[SURF6]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PRPF4]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[BLOC1S4]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TRMT10C]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 | pathway: rRNA processing |
| [[ZNF200]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZKSCAN5]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP1]] | -0.64 | -0.61 / -0.70 | both halves | 7e-06 |  |
| [[UBQLN1]] | -0.63 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[TNPO1]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[RAD23B]] | -0.60 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[EEF1A1P5]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[CNN3]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[DHFR]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[EIF4H]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[TOP2B]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.57 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[MATR3]] | -0.56 | -0.45 / -0.65 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.8, 3.3); signed map (-4.6, -12.9). **Vector** length 99.5, 27.3% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +8.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +3.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.8 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.6 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.6 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | interferon stimulated exonuclease gene 20 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,721,891-156,728,766 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12671 |
| Gene groups (HGNC) | Exonucleases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9L3](https://www.uniprot.org/uniprotkb/Q9H9L3) (Interferon-stimulated 20 kDa exonuclease-like 2):

> 3'-> 5'-exoribonuclease involved in ribosome biogenesis in the processing of the 12S pre-rRNA. Displays a strong specificity for a 3'-end containing a free hydroxyl group.

**Summary**, from NCBI Gene [81875](https://www.ncbi.nlm.nih.gov/gene/81875):

> This gene encodes a 3'-5' exoribonuclease that may be involved in the processing of the 12S pre-rRNA. Pseudogenes have been identified on chromosomes 6 and 11. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:25745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25745) · Entrez [81875](https://www.ncbi.nlm.nih.gov/gene/81875) · UniProt [Q9H9L3](https://www.uniprot.org/uniprotkb/Q9H9L3) · Ensembl [ENSG00000143319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143319)

## Data

Gene col 6711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6711); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6711]; `tensor/DDL_lfc|DDL_z.npy` [6711]; `embed/gene_vectors.npy` [6711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6711 or target_col == 6711). Every well: [[ISG20L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISG20L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
