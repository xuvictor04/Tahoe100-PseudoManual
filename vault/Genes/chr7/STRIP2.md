---
symbol: "STRIP2"
type: "gene"
col: 4895
ensembl_id: "ENSG00000128578"
name: "striatin interacting protein 2"
location: "7q32.1"
module: 34
arm: "+"
pooled_cpm: 33.79
n_lines_expressing: 44
n_dd_up: 30
n_dd_down: 17
n_dd_up_clean: 23
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# STRIP2

*striatin interacting protein 2* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.07× (z +14.8, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.558× (z -10.9, q 7e-25, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPC1]] (+0.61, fdr 1e-05), [[TIAM1]] (+0.56, fdr 1e-05), [[OSMR]] (+0.54, fdr 3e-05); moves opposite to [[DNAJC27]] (-0.54, fdr 2e-05), [[ZNF451]] (-0.53, fdr 4e-05), [[ACP6]] (-0.52, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARHGAP20]] → it (grade B ⚠); 5 go from it, the strongest it → [[ATP6V0D1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.07×** | +14.8 | 0e+00 | 38/42 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.05×** | +14.7 | 0e+00 | 36/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.90×** | +14.0 | 2e-42 | 36/42 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.41×** | +11.6 | 8e-29 | 37/41 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.23×** | +10.5 | 7e-24 | 32/42 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.77×** | +7.1 | 1e-10 | 28/41 (SW480, KATO III, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +6.6 | 4e-09 | 23/40 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +5.7 | 1e-06 | 23/41 (SK-MEL-2, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.53×** | +5.6 | 1e-06 | 22/41 (HT-29, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.0 | 4e-05 | 20/42 (LS 180, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 21/41 (SK-MEL-2, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 4e-04 | 17/42 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 6e-04 | 18/41 (HT-29, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.86×** | +4.3 | 8e-04 | 12/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +4.3 | 8e-04 | 21/41 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 18/40 (SW48, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +4.0 | 0.002 | 15/42 (SW1417, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.003 | 18/41 (SW48, LS 180, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.558×** | -10.9 | 7e-25 | 31/42 (C32, COLO 205, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.622×** | -8.8 | 3e-16 | 29/42 (COLO 205, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.629×** | -8.6 | 1e-15 | 29/43 (C32, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.559×** | -7.7 | 3e-12 | 28/42 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.583×** | -7.1 | 1e-10 | 29/41 (C32, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.362×** | -7.0 | 2e-10 | 30/43 (RKO, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.611×** | -6.5 | 7e-09 | 25/42 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.392×** | -6.5 | 8e-09 | 26/37 (COLO 205, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.711×** | -6.4 | 1e-08 | 27/42 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.450×** | -5.5 | 2e-06 | 23/38 (NCI-H1792, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -5.1 | 2e-05 | 21/40 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.745×** | -3.9 | 0.004 | 17/40 (SW48, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.813×** | -3.9 | 0.004 | 17/41 (C32, LoVo, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.746×** | -3.9 | 0.004 | 17/41 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.762×** | -3.4 | 0.026 | 16/41 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.781×** | -3.3 | 0.039 | 14/42 (hTERT-HPNE, RPMI-7951, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.075 | 14/42 (KATO III, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 303 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.266× (z -14.2) |
| [[RKO (line)]] | wt | 141 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0996× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.323× (z -11.9) |
| [[COLO 205 (line)]] | alt | 92.3 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.133× (z -17.1) |
| [[LoVo (line)]] | wt | 86.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.238× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 12.5 | 4 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 7.01× (z +11.4) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.82× (z +9.2) | — |
| [[SW480 (line)]] | alt | 17.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.93× (z +10.5) | — |
| [[KATO III (line)]] | alt | 42.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.324× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 68.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.306× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.97× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 39.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +10.1) | — |
| [[SW48 (line)]] | wt | 39.2 | 2 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 8.12× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 10.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 5.62× (z +8.7) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.108× (z -11.2) |
| [[HT-29 (line)]] | alt | 8.65 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 11.2× (z +9.9) ⚠ unreliable plate only | — |
| [[NCI-H2347 (line)]] | alt | 45.2 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.457× (z -9.0) |
| [[A498 (line)]] | wt | 25.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 32.5 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0707× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.281× (z -9.0) |
| [[HOP62 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.04× (z +9.5) ⚠ unreliable plate only | — |
| [[J82 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0857× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 55.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.178× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 48.5 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.342× (z -8.6) |
| [[SW 900 (line)]] | alt | 46.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.315× (z -9.6) |
| [[A-427 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPC1]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TIAM1]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[OSMR]] | +0.54 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[GFOD1]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[EHD4]] | +0.51 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[ST3GAL1]] | +0.51 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[LIPG]] | +0.49 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[DIAPH1]] | +0.49 | +0.51 / +0.38 | both halves | 7e-05 |  |
| [[TEAD4]] | +0.49 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[PIP4K2A]] | +0.48 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[USB1]] | +0.48 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[TBC1D2]] | +0.48 | +0.38 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC27]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZNF451]] | -0.53 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[ACP6]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TP53]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[KLHDC2]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MBIP]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[PPIL4]] | -0.49 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[FBXO8]] | -0.48 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[LINC00663]] | -0.48 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[VIRMA]] | -0.48 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SLC35E2B]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ATF2]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP20]] | B | ARHGAP20 activity raises STRIP2's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 1.68× lower at baseline in the lines without ARHGAP20 | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC |
| [[JAK2]] | B | JAK2 activity raises STRIP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[PRSS3]] | B | PRSS3 activity raises STRIP2's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without PRSS3 | 0.096 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[SESTD1]] | C | SESTD1 activity raises STRIP2's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without SESTD1 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0D1-DT]] | B | STRIP2 activity weakens ATP6V0D1-DT's drug response | lines that do not express STRIP2 (6) vs lines expressing it (41) | the lines without STRIP2 respond 1.55× as strongly (z diff -2.00); strongest at Harringtonine 5 µM: 0.15x vs 0.34x (z diff -3.5) | 0.052 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[USB1]] | B | STRIP2 activity lowers USB1's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.16× higher at baseline in the lines without STRIP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |
| [[LUZP1]] | B | STRIP2 activity raises LUZP1's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.83× lower at baseline in the lines without STRIP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |
| [[NDUFA5]] | B | STRIP2 activity raises NDUFA5's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.29× lower at baseline in the lines without STRIP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |
| [[CCDC7]] | B | STRIP2 activity lowers CCDC7's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.32× higher at baseline in the lines without STRIP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.404). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 19.4); signed map (-9.7, 44.4). **Vector** length 122, 33.5% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.1 | +11.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.2 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.0 | +7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.9 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.8 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.8 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.8 | -8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.5 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.1 | -3.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.0 | -10.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.7 | -7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.6 | -6.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.5 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | striatin interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:129,434,432-129,488,399 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1170, FAR11B; previously FAM40B |
| Gene groups (HGNC) | STRIPAK complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULQ0](https://www.uniprot.org/uniprotkb/Q9ULQ0) (Striatin-interacting protein 2):

> Calmodulin-binding scaffolding protein which is the center of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes such as cell growth, differentiation, apoptosis, metabolism and immune regulation. Required …

**Summary**, from NCBI Gene [57464](https://www.ncbi.nlm.nih.gov/gene/57464):

> Predicted to enable protein-macromolecule adaptor activity. Predicted to be involved in cytoskeleton organization and negative regulation of hippo signaling. Located in cytoplasm. Part of FAR/SIN/STRIPAK complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22209) · Entrez [57464](https://www.ncbi.nlm.nih.gov/gene/57464) · UniProt [Q9ULQ0](https://www.uniprot.org/uniprotkb/Q9ULQ0) · Ensembl [ENSG00000128578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128578)

## Data

Gene col 4895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4895); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4895]; `tensor/DDL_lfc|DDL_z.npy` [4895]; `embed/gene_vectors.npy` [4895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4895 or target_col == 4895). Every well: [[STRIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
