---
symbol: "PRRC2B"
type: "gene"
col: 16375
ensembl_id: "ENSG00000288701"
name: "proline rich coiled-coil 2B"
location: "9q34.13"
module: 5
arm: "+"
pooled_cpm: 289.48
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PRRC2B

*proline rich coiled-coil 2B* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +10.7, q 4e-24, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.482× (z -20.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF124]] (+0.72, fdr 3e-05), [[UTP20]] (+0.71, fdr 7e-06), [[ANKRD40]] (+0.71, fdr 1e-05); moves opposite to [[YIF1B]] (-0.70, fdr 1e-05), [[ACBD3]] (-0.70, fdr 7e-06), [[GBF1]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CREG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +10.7 | 4e-24 | 39/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +7.4 | 3e-11 | 32/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +7.0 | 5e-10 | 37/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +6.0 | 3e-07 | 30/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.9 | 4e-07 | 29/48 (SW480, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.8 | 4e-07 | 20/49 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +5.8 | 4e-07 | 38/48 (RKO, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.9 | 6e-05 | 22/48 (A498, COLO 205, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 5e-04 | 20/48 (A498, NCI-H460, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.4 | 5e-04 | 18/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +4.4 | 7e-04 | 21/48 (A498, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.11× | +4.0 | 0.002 | 13/48 (HOP62, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.004 | 22/48 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.004 | 21/44 (NCI-H1573, HCT15, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.012 | 21/45 (AsPC-1, A-172, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.014 | 16/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.022 | 24/49 (J82, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.026 | 21/49 (BT-474, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.12× | +3.0 | 0.068 | 8/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.084 | 21/48 (A498, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.482×** | -20.0 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.505×** | -18.7 | 0e+00 | 48/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.514×** | -18.2 | 0e+00 | 47/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -8.1 | 1e-13 | 35/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.804×** | -6.0 | 3e-07 | 32/48 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.735×** | -4.4 | 0.001 | 35/49 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.892× | -3.1 | 0.14 | 6/48 (A-172, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 321 | 6 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -14.7) |
| [[A498 (line)]] | wt | 297 | 5 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.76× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.589× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 151 | 5 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.505× (z -10.0) |
| [[C32 (line)]] | wt | 304 | 1 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.11× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.337× (z -18.1) |
| [[HOP62 (line)]] | alt | 234 | 5 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.523× (z -12.7) |
| [[C-33 A (line)]] | alt | 430 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 269 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -16.4) |
| [[SW480 (line)]] | alt | 332 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.415× (z -20.7) |
| [[SK-MEL-2 (line)]] | alt | 386 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -20.7) |
| [[A549 (line)]] | wt | 276 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.455× (z -14.5) |
| [[BT-474 (line)]] | alt | 656 | 2 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.552× (z -11.0) |
| [[LoVo (line)]] | wt | 271 | 2 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.301× (z -22.8) |
| [[LS 180 (line)]] | wt | 231 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 197 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.508× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 374 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -25.9) |
| [[RKO (line)]] | wt | 785 | 1 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.23× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.455× (z -13.1) |
| [[A-172 (line)]] | wt | 152 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.446× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 464 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -16.8) |
| [[HepG2_C3A (line)]] | wt | 253 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.8) |
| [[KATO III (line)]] | alt | 337 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.515× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 481 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -23.5) |
| [[SW1417 (line)]] | alt | 315 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -15.7) |
| [[SW48 (line)]] | wt | 363 | 1 | 3 | [[TAK-901 (drug)]] 0.05 µM 2.94× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.249× (z -19.0) |
| [[A-427 (line)]] | wt | 207 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -17.6) |
| [[COLO 205 (line)]] | alt | 227 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.1) | — |
| [[J82 (line)]] | alt | 454 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 368 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.414× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 119 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.569× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 168 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.463× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 214 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.567× (z -10.8) |
| [[PANC-1 (line)]] | alt | 269 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.450× (z -16.4) |
| [[SHP-77 (line)]] | alt | 327 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.574× (z -10.0) |
| [[SNU-1 (line)]] | wt | 276 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.494× (z -10.5) |
| [[SNU-423 (line)]] | alt | 274 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 126 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.88× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.555× (z -8.9) |
| [[H4 (line)]] | wt | 237 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 247 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.544× (z -10.1) |
| [[SW 900 (line)]] | alt | 177 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.512× (z -9.4) |
| [[CHP-212 (line)]] | wt | 398 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -9.5) |
| [[AN3 CA (line)]] | alt | 350 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 376 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 178 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 182 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 348 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF124]] | +0.72 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[UTP20]] | +0.71 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ANKRD40]] | +0.71 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[DHX37]] | +0.70 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[SLC39A10]] | +0.67 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ZNF300]] | +0.67 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PRDM11]] | +0.67 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[SLC5A6]] | +0.66 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.66 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RCC2]] | +0.66 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CRPPA]] | +0.66 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[SNX5]] | +0.66 | +0.50 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | -0.70 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ACBD3]] | -0.70 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[GBF1]] | -0.68 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ERLEC1]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[SNAPC3]] | -0.67 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PJA2]] | -0.67 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[COG6]] | -0.66 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[GOLPH3L]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[PIGH]] | -0.65 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ARL3]] | -0.65 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[SRP54]] | -0.65 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[SLC17A5]] | -0.65 | -0.53 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREG2]] | B | CREG2 activity lowers PRRC2B's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.36× higher at baseline in the lines without CREG2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[HDAC6]] | B | HDAC6 activity raises PRRC2B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAXC]] | B | FAXC activity raises PRRC2B's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without FAXC | 0.046 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[CREG2]] | C | CREG2 activity weakens PRRC2B's drug response | lines that do not express CREG2 (19) vs lines expressing it (29) | the lines without CREG2 respond 0.91× as strongly (z diff +0.06); strongest at Panobinostat 0.05 µM: 0.71x vs 0.78x (z diff -1.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A; target measured in part of the lines; both ways; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.4, -27.8); signed map (22.8, -31.1). **Vector** length 136, 45.7% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +11.1 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +10.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.7 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.6 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.1 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.2 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.7 | -18.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -20.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -18.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.1 | -6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | proline rich coiled-coil 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:131,373,636-131,500,197 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10526, LQFBS-1; previously KIAA0515, BAT2L, BAT2L1 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JSZ5](https://www.uniprot.org/uniprotkb/Q5JSZ5) (Translational regulator PRRC2B):

> Promotes leaky scanning, allowing ribosomes to bypass the translation start codons of upstream open reading frames (ORFs) in mRNAs and facilitating efficient translation of the downstream main ORF. Binds to GA- or CU-rich elements near the translation initiation codon of the main open reading frame on a subset of mRNAs, promoting their translation via interaction with translation initiation factors. Promotes translation of cyclin CCND2, ensuring G1/S transition and cell proliferation. …

**Summary**, from NCBI Gene [84726](https://www.ncbi.nlm.nih.gov/gene/84726):

> Enables RNA binding activity. Predicted to be involved in cell differentiation. Predicted to act upstream of or within in utero embryonic development. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28121) · Entrez [84726](https://www.ncbi.nlm.nih.gov/gene/84726) · UniProt [Q5JSZ5](https://www.uniprot.org/uniprotkb/Q5JSZ5) · Ensembl [ENSG00000288701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000288701)

## Data

Gene col 16375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16375); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16375]; `tensor/DDL_lfc|DDL_z.npy` [16375]; `embed/gene_vectors.npy` [16375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16375 or target_col == 16375). Every well: [[PRRC2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRC2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
