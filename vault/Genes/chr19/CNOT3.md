---
symbol: "CNOT3"
type: "gene"
col: 1519
ensembl_id: "ENSG00000088038"
name: "CCR4-NOT transcription complex subunit 3"
location: "19q13.42"
module: 96
arm: "+"
pooled_cpm: 36.89
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# CNOT3

*CCR4-NOT transcription complex subunit 3* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.30× (z +18.4, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.657× (z -6.6, q 3e-08, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3A1]] (+0.82, fdr 7e-06), [[SRRM2]] (+0.80, fdr 7e-06), [[CELSR3]] (+0.71, fdr 7e-06); moves opposite to [[SRPK2]] (-0.62, fdr 2e-05), [[ATOX1]] (-0.60, fdr 3e-05), [[TRIM33]] (-0.58, fdr 3e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +18.4 | 0e+00 | 45/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +10.2 | 5e-22 | 41/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +10.1 | 2e-21 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.0 | 4e-17 | 27/38 (NCI-H1573, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.6 | 2e-06 | 28/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +5.4 | 6e-06 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 7e-06 | 28/48 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.4 | 7e-04 | 27/49 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.9 | 0.005 | 18/47 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.009 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.052 | 17/48 (LS 180, C-33 A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.22×** | +3.1 | 0.088 | 10/48 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.088 | 15/47 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.657×** | -6.6 | 3e-08 | 33/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.683×** | -6.0 | 7e-07 | 39/48 (HT-29, A-172, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.709×** | -5.4 | 1e-05 | 27/48 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.724×** | -5.0 | 6e-05 | 30/48 (NCI-H1573, HT-29, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.727×** | -5.0 | 6e-05 | 27/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.798×** | -5.0 | 6e-05 | 26/48 (NCI-H460, H4, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.753×** | -4.4 | 7e-04 | 30/48 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.822×** | -4.3 | 0.001 | 22/48 (SHP-77, NCI-H2347, …) | top dose only | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | 0.847× | -3.7 | 0.014 | 18/48 (NCI-H2347, NCI-H661, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.021 | 18/48 (HS-578T, BT-474, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.796×** | -3.5 | 0.023 | 21/47 (A549, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.805×** | -3.3 | 0.053 | 12/47 (BT-474, SW1417, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.812×** | -3.2 | 0.060 | 14/47 (HS-578T, AN3 CA, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.811×** | -3.1 | 0.067 | 21/48 (H4, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -3.1 | 0.069 | 11/48 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.821×** | -3.1 | 0.070 | 19/48 (H4, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.873× | -3.0 | 0.080 | 5/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.822×** | -3.0 | 0.080 | 13/47 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.695×** | -3.0 | 0.088 | 12/48 (H4, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 68.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 33.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.2) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H460 (line)]] | wt | 22.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[PANC-1 (line)]] | alt | 44.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +18.9) | — |
| [[LoVo (line)]] | wt | 31.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +9.0) | — |
| [[A-172 (line)]] | wt | 50.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.2) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 51.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.2) | — |
| [[A549 (line)]] | wt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.5) | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0843× (z -10.3) |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 57.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 29.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 36.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 39.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.9) | — |
| [[J82 (line)]] | alt | 45.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.8) | — |
| [[RKO (line)]] | wt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 46.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 64.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +8.6) | — |
| [[SW480 (line)]] | alt | 38.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.9) | — |
| [[A-427 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3A1]] | +0.82 | +0.72 / +0.84 | both halves | 7e-06 |  |
| [[SRRM2]] | +0.80 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[BRPF3]] | +0.71 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[MED12]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[USP19]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZBED6]] | +0.70 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[ATP13A1]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[BAG6]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[DXO]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[DCAF8]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[RAB1B]] | +0.66 | +0.40 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK2]] | -0.62 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[ATOX1]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[TRIM33]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[UBE2R2]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[RABGEF1P1]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PDCD10]] | -0.55 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[RASA2]] | -0.54 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[UQCRH]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SPTLC2]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[TMEM191A-1]] | -0.52 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.9, 4.2); signed map (15.4, -22.7). **Vector** length 101, 24.3% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.3 | +18.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | +1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | +0.5 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -0.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,137,749-54,155,681 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOT3H, KIAA0691, LENG2; previously NOT3 |
| Gene groups (HGNC) | CCR4-NOT transcription complex |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O75175](https://www.uniprot.org/uniprotkb/O75175) (CCR4-NOT transcription complex subunit 3):

> Component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional complex functions may be a consequence of its influence on mRNA expression. May be involved in metabolic regulation; may be involved in recruitment of the CCR4-NOT complex to deadenylation target mRNAs …

**Summary**, from NCBI Gene [4849](https://www.ncbi.nlm.nih.gov/gene/4849):

> Involved in regulation of stem cell population maintenance. Part of CCR4-NOT complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7879) · Entrez [4849](https://www.ncbi.nlm.nih.gov/gene/4849) · UniProt [O75175](https://www.uniprot.org/uniprotkb/O75175) · Ensembl [ENSG00000088038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088038)

## Data

Gene col 1519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1519); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1519]; `tensor/DDL_lfc|DDL_z.npy` [1519]; `embed/gene_vectors.npy` [1519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1519 or target_col == 1519). Every well: [[CNOT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
