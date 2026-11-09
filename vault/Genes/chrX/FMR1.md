---
symbol: "FMR1"
type: "gene"
col: 2211
ensembl_id: "ENSG00000102081"
name: "fragile X messenger ribonucleoprotein 1"
location: "Xq27.3"
module: 130
arm: "+"
pooled_cpm: 109.45
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# FMR1

*fragile X messenger ribonucleoprotein 1* — Xq27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +22.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.636× (z -11.2, q 2e-26, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAG2]] (+0.66, fdr 1e-05), [[TRANK1]] (+0.64, fdr 1e-05), [[PAXIP1-AS2]] (+0.63, fdr 1e-05); moves opposite to [[ZNF215]] (-0.63, fdr 1e-05), [[RBAK-RBAKDN]] (-0.62, fdr 1e-05), [[DAP3]] (-0.61, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02985]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +22.5 | 0e+00 | 43/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +14.1 | 9e-43 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +12.6 | 4e-34 | 40/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +10.7 | 9e-25 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +10.0 | 2e-21 | 34/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +9.6 | 6e-20 | 32/48 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +7.3 | 3e-11 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +7.1 | 7e-11 | 28/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.4 | 1e-08 | 28/49 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.4 | 3e-06 | 19/48 (J82, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +5.3 | 6e-06 | 24/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +5.2 | 1e-05 | 24/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.19× | +4.3 | 8e-04 | 19/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 21/44 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.9 | 0.003 | 15/49 (KATO III, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.008 | 11/48 (RKO, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.019 | 13/48 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.025 | 8/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[crizotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.028 | 14/48 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.028 | 16/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.028 | 17/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.040 | 13/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.636×** | -11.2 | 2e-26 | 41/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.655×** | -10.5 | 3e-23 | 37/48 (A549, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.742×** | -7.4 | 3e-11 | 32/48 (NCI-H23, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.782×** | -5.9 | 6e-07 | 25/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -5.7 | 1e-06 | 26/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.744×** | -3.8 | 0.013 | 19/48 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.865× | -3.6 | 0.027 | 16/48 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.904× | -3.5 | 0.029 | 12/49 (A549, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.4 | 0.037 | 14/49 (SK-MEL-2, MIA PaCa-2, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.869× | -3.4 | 0.037 | 18/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.773×** | -3.3 | 0.045 | 16/48 (NCI-H23, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 0.791× | -3.0 | 0.11 | 15/47 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.11 | 10/48 (HEC-1-A, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 92.6 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +23.2) | — |
| [[PANC-1 (line)]] | alt | 130 | 9 (4 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +22.5) | [[Panobinostat (drug)]] 5 µM 0.573× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.607× (z -8.6) |
| [[SW480 (line)]] | alt | 78.6 | 4 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.531× (z -9.8) |
| [[HOP62 (line)]] | alt | 65.5 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.467× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.482× (z -8.5) |
| [[J82 (line)]] | alt | 102 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.0) | — |
| [[KATO III (line)]] | alt | 146 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.554× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 154 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 101 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.1) | — |
| [[LoVo (line)]] | wt | 88.4 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.554× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 113 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.491× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 153 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.1) | [[Auranofin (drug)]] 5 µM 0.423× (z -9.3) |
| [[BT-474 (line)]] | alt | 67.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.3) | — |
| [[H4 (line)]] | wt | 76.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 120 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 113 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 122 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 62.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.9) | — |
| [[RKO (line)]] | wt | 81.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 124 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +17.4) | — |
| [[A-172 (line)]] | wt | 144 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +10.5) | — |
| [[C32 (line)]] | wt | 64.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +17.9) | — |
| [[HS-578T (line)]] | alt | 59.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 57.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 73.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.419× (z -12.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 96.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.8) | — |
| [[A-427 (line)]] | wt | 118 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.87× (z +14.8) | — |
| [[A498 (line)]] | wt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.410× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 61.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 181 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 60.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.484× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 171 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 259 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.1) | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG2]] | +0.66 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[TRANK1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PAXIP1-AS2]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NR1D2]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MAT2B]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RBM33]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PATL1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[HMGN2]] | +0.61 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[CHASERR]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TXNDC16]] | +0.60 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[RAB21]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF215]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[DAP3]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[C11orf24]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RABEPK]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[EPS15L1]] | -0.59 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[DGKD]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[NLK]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[POLR3A]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02985]] | B | LINC02985 activity lowers FMR1's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 1.22× higher at baseline in the lines without LINC02985 | 0.059 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |
| [[DAPK2]] | B | DAPK2 activity raises FMR1's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 1.25× lower at baseline in the lines without DAPK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises FMR1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF544]] | B | ZNF544 activity lowers FMR1's level | lines that do not express ZNF544 (6) vs lines expressing it (44) | 1.30× higher at baseline in the lines without ZNF544 | 0.099 | ⚠ within organs, on part of the lines; also absent: LPIN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.6, -9.3); signed map (31.1, -26.7). **Vector** length 125, 39.7% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +22.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +12.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.9 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.3 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.3 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.8 | -2.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | fragile X messenger ribonucleoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq27.3 — chrX:147,911,919-147,951,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FMRP, FRAXA, MGC87458; previously POF1, POF |
| Gene groups (HGNC) | FMR1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06787](https://www.uniprot.org/uniprotkb/Q06787) (Fragile X messenger ribonucleoprotein 1):

> Multifunctional polyribosome-associated RNA-binding protein that plays a central role in neuronal development and synaptic plasticity through the regulation of alternative mRNA splicing, mRNA stability, mRNA dendritic transport and postsynaptic local protein synthesis of target mRNAs. Acts as an mRNA regulator by mediating formation of some phase-separated membraneless compartment: undergoes liquid-liquid phase separation upon binding to target mRNAs, leading to assemble mRNAs into cytoplasmic …

**Summary**, from NCBI Gene [2332](https://www.ncbi.nlm.nih.gov/gene/2332):

> The protein encoded by this gene binds RNA and is associated with polysomes. The encoded protein may be involved in mRNA trafficking from the nucleus to the cytoplasm. A trinucleotide repeat (CGG) in the 5' UTR is normally found at 6-53 copies, but an expansion to 55-230 repeats is the cause of fragile X syndrome. Expansion of the trinucleotide repeat may also cause one form of premature ovarian failure (POF1). Multiple alternatively spliced transcript variants that encode different protein …

**Accessions** — [HGNC:3775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3775) · Entrez [2332](https://www.ncbi.nlm.nih.gov/gene/2332) · UniProt [Q06787](https://www.uniprot.org/uniprotkb/Q06787) · Ensembl [ENSG00000102081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102081)

## Data

Gene col 2211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2211); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2211]; `tensor/DDL_lfc|DDL_z.npy` [2211]; `embed/gene_vectors.npy` [2211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2211 or target_col == 2211). Every well: [[FMR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
