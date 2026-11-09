---
symbol: "ACSF2"
type: "gene"
col: 9417
ensembl_id: "ENSG00000167107"
name: "acyl-CoA synthetase family member 2"
location: "17q21.33"
module: 30
arm: "+"
pooled_cpm: 18.21
n_lines_expressing: 48
n_dd_up: 30
n_dd_down: 32
n_dd_up_clean: 27
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ACSF2

*acyl-CoA synthetase family member 2* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.64× (z +8.2, q 1e-13, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.456× (z -13.0, q 1e-35, down in 39 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.674× (z -9.2, q 6e-18, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185A]] (+0.64, fdr 1e-05), [[ZFP14]] (+0.61, fdr 1e-05), [[THRA]] (+0.61, fdr 2e-05); moves opposite to [[PIGW]] (-0.62, fdr 1e-05), [[ADAT1]] (-0.59, fdr 4e-05), [[HOMER1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +8.2 | 1e-13 | 27/45 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +8.1 | 1e-13 | 33/46 (BT-474, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +7.5 | 1e-11 | 28/46 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +6.3 | 3e-08 | 26/46 (A498, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.3 | 3e-08 | 23/46 (A498, COLO 205, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.30×** | +6.1 | 1e-07 | 24/46 (NCI-H2347, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.8 | 6e-07 | 20/45 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 5e-05 | 19/43 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 1e-04 | 20/46 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 9e-04 | 13/46 (HEC-1-A, HS-578T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 9e-04 | 16/46 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.001 | 14/45 (HEC-1-A, MIA PaCa-2, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.001 | 11/41 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.1 | 0.001 | 12/45 (KATO III, BT-474, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 13/46 (LS 180, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 16/46 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.9 | 0.003 | 11/46 (RKO, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.456×** | -13.0 | 1e-35 | 39/45 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.657×** | -9.8 | 3e-20 | 29/45 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -9.2 | 6e-18 | 29/45 (BT-474, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -9.0 | 2e-17 | 31/44 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -8.7 | 4e-16 | 28/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.587×** | -8.5 | 3e-15 | 28/45 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.600×** | -8.4 | 3e-15 | 23/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -7.4 | 1e-11 | 28/46 (Panc 03.27, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -7.1 | 8e-11 | 24/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.656×** | -6.7 | 1e-09 | 25/39 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -6.2 | 3e-08 | 25/45 (HT-29, BT-474, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -6.2 | 3e-08 | 19/46 (BT-474, SNU-423, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.496×** | -6.1 | 6e-08 | 28/44 (SW 900, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.519×** | -5.7 | 6e-07 | 22/44 (A498, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -5.5 | 2e-06 | 18/41 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.543×** | -5.3 | 5e-06 | 21/43 (CFPAC-1, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.595×** | -4.5 | 2e-04 | 17/43 (NCI-H1792, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -4.5 | 2e-04 | 17/46 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.775×** | -4.1 | 0.001 | 6/46 (MIA PaCa-2, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -4.0 | 0.002 | 16/45 (HT-29, Panc 03.27, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.0 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.230× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.142× (z -13.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -11.6) |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.256× (z -10.7) |
| [[LoVo (line)]] | wt | 10.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.232× (z -8.8) |
| [[A-427 (line)]] | wt | 17.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0799× (z -15.6) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.3) |
| [[A498 (line)]] | wt | 15.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +9.1) | — |
| [[A549 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[C-33 A (line)]] | alt | 7.02 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0536× (z -8.9) |
| [[C32 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HEC-1-A (line)]] | alt | 42.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.9) |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -13.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 7.08 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -9.9) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185A]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ZFP14]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[THRA]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PLEKHM3]] | +0.57 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[NISCH]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PRUNE1]] | +0.57 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[HMGN3]] | +0.56 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ZNF552]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SUFU]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CDC14B]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CNNM2]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGW]] | -0.62 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ADAT1]] | -0.59 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[HOMER1]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CYREN]] | -0.57 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SECISBP2]] | -0.56 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ALG13]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MYH3]] | -0.54 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[PITX1-AS1]] | -0.54 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ZNF800]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[METTL1]] | -0.53 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[HCG18]] | -0.53 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[ZNF34]] | -0.52 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ACSF2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.2, -10.2); signed map (-29.8, -6.7). **Vector** length 74.1, 13.7% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +8.1 |
|  | [[NG25 (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.5 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -13.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,426,158-50,474,845 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20920, ACSMW |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CM8](https://www.uniprot.org/uniprotkb/Q96CM8) (Medium-chain acyl-CoA ligase ACSF2, mitochondrial):

> Acyl-CoA synthases catalyze the initial reaction in fatty acid metabolism, by forming a thioester with CoA. Has some preference toward medium-chain substrates. Plays a role in adipocyte differentiation.

**Summary**, from NCBI Gene [80221](https://www.ncbi.nlm.nih.gov/gene/80221):

> Enables medium-chain fatty acid-CoA ligase activity. Predicted to be involved in fatty acid metabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26101) · Entrez [80221](https://www.ncbi.nlm.nih.gov/gene/80221) · UniProt [Q96CM8](https://www.uniprot.org/uniprotkb/Q96CM8) · Ensembl [ENSG00000167107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167107)

## Data

Gene col 9417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9417); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9417]; `tensor/DDL_lfc|DDL_z.npy` [9417]; `embed/gene_vectors.npy` [9417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9417 or target_col == 9417). Every well: [[ACSF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
