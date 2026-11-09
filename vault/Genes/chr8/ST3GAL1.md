---
symbol: "ST3GAL1"
type: "gene"
col: 175
ensembl_id: "ENSG00000008513"
name: "ST3 beta-galactoside alpha-2,3-sialyltransferase 1"
location: "8q24.22"
module: 174
arm: "+"
pooled_cpm: 115.65
n_lines_expressing: 39
n_dd_up: 9
n_dd_down: 45
n_dd_up_clean: 9
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 26
direction_downstream: 33
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# ST3GAL1

*ST3 beta-galactoside alpha-2,3-sialyltransferase 1* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +10.2, q 2e-21, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.433× (z -22.9, q 0e+00, down in 33 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN2]] (+0.71, fdr 7e-06), [[PITPNC1]] (+0.70, fdr 7e-06), [[DUSP6]] (+0.70, fdr 7e-06); moves opposite to [[RBM33]] (-0.59, fdr 1e-05), [[FMR1]] (-0.56, fdr 3e-05), [[SH3BGRL]] (-0.54, fdr 4e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[ABHD17C]] → it (grade B ⚠); 33 go from it, the strongest it → [[ACOT7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +10.2 | 2e-21 | 29/37 (RKO, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 3e-04 | 22/38 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.6 | 6e-04 | 19/37 (Hs 766T, SK-MEL-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +4.6 | 6e-04 | 19/37 (LOX-IMVI, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 6e-04 | 17/37 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.002 | 15/36 (LS 180, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 0.002 | 15/37 (LS 180, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.014 | 17/37 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.030 | 14/37 (LS 180, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.077 | 8/37 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.077 | 18/37 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.090 | 8/37 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.18× | +3.1 | 0.096 | 5/37 (LS 180, NCI-H2347, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.433×** | -22.9 | 0e+00 | 33/37 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -14.0 | 6e-42 | 26/37 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.461×** | -13.9 | 2e-41 | 27/35 (C32, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -13.5 | 1e-39 | 25/32 (C32, SW 900, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -13.5 | 2e-39 | 30/38 (C32, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -13.1 | 4e-37 | 23/37 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.500×** | -12.6 | 1e-34 | 31/36 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.541×** | -11.2 | 4e-27 | 26/36 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.593×** | -10.1 | 3e-22 | 28/37 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.692×** | -10.1 | 5e-22 | 23/37 (RKO, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -9.7 | 1e-20 | 30/37 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -9.4 | 4e-19 | 26/37 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.620×** | -9.2 | 1e-18 | 29/38 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.684×** | -9.1 | 4e-18 | 26/37 (C32, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.633×** | -8.8 | 8e-17 | 29/39 (NCI-H596, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.655×** | -8.3 | 3e-15 | 27/38 (C32, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.662×** | -8.0 | 6e-14 | 31/37 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.648×** | -7.8 | 3e-13 | 29/37 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.718×** | -7.6 | 8e-13 | 26/37 (C32, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.756×** | -7.5 | 1e-12 | 25/37 (C32, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.694×** | -7.0 | 5e-11 | 23/37 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 367 | 0 | 37 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0666× (z -31.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.344× (z -18.3) |
| [[BT-474 (line)]] | alt | 322 | 0 | 23 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.1) |
| [[LS 180 (line)]] | wt | 267 | 0 | 23 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -27.9) |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 19 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 203 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -33.5) |
| [[SW 900 (line)]] | alt | 219 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -25.9) |
| [[CFPAC-1 (line)]] | alt | 191 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.396× (z -11.0) |
| [[A549 (line)]] | wt | 154 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -24.1) |
| [[KATO III (line)]] | alt | 93.0 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.8) |
| [[RKO (line)]] | wt | 122 | 1 | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.93× (z +9.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -18.5) |
| [[HS-578T (line)]] | alt | 522 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -10.9) |
| [[A498 (line)]] | wt | 192 | 1 (1 ⚠) | 4 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.96× (z +9.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.5) |
| [[COLO 205 (line)]] | alt | 53.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 107 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.4) |
| [[PANC-1 (line)]] | alt | 41.6 | 1 | 4 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.83× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 173 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.4) |
| [[H4 (line)]] | wt | 114 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.1) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.440× (z -11.0) |
| [[LoVo (line)]] | wt | 49.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 103 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.39× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.7) |
| [[HT-29 (line)]] | alt | 584 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 85.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 68.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.7) |
| [[NCI-H596 (line)]] | alt | 99.2 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.151× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -18.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 94.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.4) |
| [[SNU-423 (line)]] | alt | 72.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.8) |
| [[AN3 CA (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0817× (z -13.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 87.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 138 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0844× (z -9.1) |
| [[A-172 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 20.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN2]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[PITPNC1]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PHC2]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[S100A16]] | +0.68 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DOCK5]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DUSP5]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[NPC1]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.64 | +0.68 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM33]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[FMR1]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[SH3BGRL]] | -0.54 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[PATL1]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PAIP1]] | -0.54 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[HACD2]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 23, C 3. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | ABHD17C activity raises ST3GAL1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 3.62× lower at baseline in the lines without ABHD17C | 0.007 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[C11orf91]] | B | C11orf91 activity raises ST3GAL1's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 4.69× lower at baseline in the lines without C11orf91 | 0.010 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[TRIB1]] | B | TRIB1 activity raises ST3GAL1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 5.56× lower at baseline in the lines without TRIB1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[MAML3]] | B | MAML3 activity raises ST3GAL1's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 2.57× lower at baseline in the lines without MAML3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[DUSP4]] | B | DUSP4 activity raises ST3GAL1's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.06× lower at baseline in the lines without DUSP4 | 0.015 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[RGS2]] | B | RGS2 activity raises ST3GAL1's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 2.73× lower at baseline in the lines without RGS2 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[FAM83A]] | B | FAM83A activity raises ST3GAL1's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.99× lower at baseline in the lines without FAM83A | 0.021 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[EFNB2]] | B | EFNB2 activity raises ST3GAL1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without EFNB2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[CLDN10-AS1]] | B | CLDN10-AS1 activity raises ST3GAL1's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without CLDN10-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[BACE2]] | B | BACE2 activity raises ST3GAL1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 3.07× lower at baseline in the lines without BACE2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[MARCHF3]] | B | MARCHF3 activity raises ST3GAL1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 4.46× lower at baseline in the lines without MARCHF3 | 0.036 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[TREM1]] | B | TREM1 activity raises ST3GAL1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.26× lower at baseline in the lines without TREM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 31, C 2. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOT7]] | B | ST3GAL1 activity lowers ACOT7's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.29× higher at baseline in the lines without ST3GAL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[LHFPL2]] | B | ST3GAL1 activity raises LHFPL2's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without ST3GAL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[LUZP1]] | B | ST3GAL1 activity raises LUZP1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without ST3GAL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[SHB]] | B | ST3GAL1 activity raises SHB's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without ST3GAL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[PLEKHM1]] | B | ST3GAL1 activity raises PLEKHM1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without ST3GAL1 | 0.026 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[TRIB1]] | B | ST3GAL1 activity raises TRIB1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.96× lower at baseline in the lines without ST3GAL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[S100P]] | B | ST3GAL1 activity raises S100P's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without ST3GAL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[DUSP5]] | B | ST3GAL1 activity raises DUSP5's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without ST3GAL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[SEMA4B]] | B | ST3GAL1 activity raises SEMA4B's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without ST3GAL1 | 0.036 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[C11orf91]] | B | ST3GAL1 activity raises C11orf91's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without ST3GAL1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[LIPG]] | B | ST3GAL1 activity raises LIPG's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without ST3GAL1 | 0.039 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[ITGA2]] | B | ST3GAL1 activity raises ITGA2's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.92× lower at baseline in the lines without ST3GAL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.0, 5.2); signed map (7.4, 48.2). **Vector** length 129, 39.6% of its response variance represented; |z| ≥ 3 in 1,608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.6 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.1 | +0.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.6 | -8.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.6 | -9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.4 | -9.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -7.2 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.0 | -6.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -6.9 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | ST3 beta-galactoside alpha-2,3-sialyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:133,454,848-133,571,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST3O, SIATFL, ST3GalA.1; previously SIAT4A |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 21 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Keratan sulfate biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q11201](https://www.uniprot.org/uniprotkb/Q11201) (CMP-N-acetylneuraminate-beta-galactosamide-alpha-2,3-sialyltransferase 1):

> A beta-galactoside alpha2->3 sialyltransferase involved in terminal sialylation of glycoproteins and glycolipids. Catalyzes the transfer of sialic acid (N-acetyl-neuraminic acid; Neu5Ac) from the nucleotide sugar donor CMP-Neu5Ac onto acceptor Galbeta-(1->3)-GalNAc-terminated glycoconjugates through an alpha2-3 linkage. Adds sialic acid to the core 1 O-glycan, Galbeta-(1->3)-GalNAc-O-Ser/Thr, which is a major structure of mucin-type O-glycans. As part of a homeostatic mechanism that regulates …

**Summary**, from NCBI Gene [6482](https://www.ncbi.nlm.nih.gov/gene/6482):

> The protein encoded by this gene is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to galactose-containing substrates. The encoded protein is normally found in the Golgi but can be proteolytically processed to a soluble form. Correct glycosylation of the encoded protein may be critical to its sialyltransferase activity. This protein, which is a member of glycosyltransferase family 29, can use the same acceptor substrates as does sialyltransferase 4B. …

**Accessions** — [HGNC:10862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10862) · Entrez [6482](https://www.ncbi.nlm.nih.gov/gene/6482) · UniProt [Q11201](https://www.uniprot.org/uniprotkb/Q11201) · Ensembl [ENSG00000008513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008513)

## Data

Gene col 175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 175); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 175]; `tensor/DDL_lfc|DDL_z.npy` [175]; `embed/gene_vectors.npy` [175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 175 or target_col == 175). Every well: [[ST3GAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST3GAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
