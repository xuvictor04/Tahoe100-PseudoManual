---
symbol: "EVA1C"
type: "gene"
col: 9399
ensembl_id: "ENSG00000166979"
name: "eva-1 homolog C"
location: "21q22.11"
module: 97
arm: "+"
pooled_cpm: 50.94
n_lines_expressing: 35
n_dd_up: 10
n_dd_down: 43
n_dd_up_clean: 10
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# EVA1C

*eva-1 homolog C* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Citalopram (hydrobromide) (drug)]] 0.05 µM: 1.63× (z +6.3, q 1e-07, up in 20 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.196× (z -29.8, q 0e+00, down in 31 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNED1]] (+0.54, fdr 5e-05), [[PHACTR3]] (+0.54, fdr 2e-05), [[TBC1D8]] (+0.52, fdr 1e-05); moves opposite to [[RNF11]] (-0.50, fdr 3e-05), [[MXD1]] (-0.50, fdr 4e-05), [[EPB41]] (-0.48, fdr 5e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HMGA2]] → it (grade B ⚠); 6 go from it, the strongest it → [[LAMB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.63×** | +6.3 | 1e-07 | 20/35 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.56×** | +5.8 | 2e-06 | 20/33 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.56×** | +5.7 | 2e-06 | 19/33 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.010 | 11/33 (LS 180, RKO, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.033 | 10/33 (KATO III, J82, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.033 | 14/33 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.043 | 12/33 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.057 | 15/33 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.20× | +3.3 | 0.057 | 13/33 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.077 | 13/33 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.094 | 10/33 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 12/33 (NCI-H1573, RPMI-7951, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.11 | 15/33 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.196×** | -29.8 | 0e+00 | 31/33 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.230×** | -19.0 | 0e+00 | 30/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.243×** | -17.6 | 0e+00 | 30/33 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.315×** | -14.9 | 0e+00 | 30/33 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.366×** | -13.0 | 1e-36 | 28/33 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.395×** | -12.0 | 3e-31 | 28/33 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.396×** | -12.0 | 4e-31 | 28/33 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -10.2 | 1e-22 | 26/32 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.506×** | -8.8 | 9e-17 | 23/33 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.513×** | -8.6 | 4e-16 | 27/33 (LS 180, LoVo, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -7.5 | 3e-12 | 22/33 (SW48, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.563×** | -7.1 | 5e-11 | 21/28 (SW48, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.590×** | -6.8 | 4e-10 | 20/33 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.645×** | -5.7 | 6e-07 | 20/31 (SW480, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.444×** | -5.5 | 2e-06 | 19/30 (SW48, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.654×** | -5.2 | 8e-06 | 18/33 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -5.0 | 2e-05 | 20/34 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -4.8 | 6e-05 | 18/32 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -4.4 | 3e-04 | 18/32 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 197 | 0 | 25 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0406× (z -34.7) |
| [[HOP62 (line)]] | alt | 86.4 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -26.0) |
| [[LS 180 (line)]] | wt | 88.7 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -22.8) |
| [[NCI-H1573 (line)]] | alt | 42.1 | 12 | 3 | [[Clobetasol propionate (drug)]] 0.05 µM 4.93× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -16.6) |
| [[SW48 (line)]] | wt | 235 | 0 | 14 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0427× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.102× (z -16.2) |
| [[LoVo (line)]] | wt | 88.7 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -20.2) |
| [[A549 (line)]] | wt | 93.7 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -25.5) |
| [[C32 (line)]] | wt | 111 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.0592× (z -28.5) |
| [[SW1417 (line)]] | alt | 110 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -27.2) |
| [[SW480 (line)]] | alt | 76.1 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -27.0) |
| [[A-172 (line)]] | wt | 34.1 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0841× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.257× (z -13.3) |
| [[RKO (line)]] | wt | 38.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0481× (z -31.8) |
| [[hTERT-HPNE (line)]] | wt | 84.8 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.00455× (z -27.0) |
| [[H4 (line)]] | wt | 35.9 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0678× (z -12.2) |
| [[HS-578T (line)]] | alt | 33.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.2) |
| [[HT-29 (line)]] | alt | 46.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -18.5) |
| [[J82 (line)]] | alt | 38.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.4) |
| [[KATO III (line)]] | alt | 32.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -16.4) |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0760× (z -25.9) |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -20.1) |
| [[NCI-H1792 (line)]] | alt | 73.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0418× (z -24.1) |
| [[Panc 03.27 (line)]] | alt | 39.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.5) |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 58.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.6) |
| [[HCT15 (line)]] | alt | 65.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.7) |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.2) |
| [[SW 1088 (line)]] | alt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -10.6) |
| [[A-427 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.19 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.73 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.79 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNED1]] | +0.54 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[PHACTR3]] | +0.54 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[TBC1D8]] | +0.52 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[LDLRAD3]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[TNS4]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TPK1]] | +0.50 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[ITPK1]] | +0.50 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RHOBTB2]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[URB2]] | +0.50 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ZHX3]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TRMT6]] | +0.50 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[TGFBR2]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF11]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MXD1]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[EPB41]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[OPTN]] | -0.47 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SQSTM1]] | -0.45 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[EMD]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[MTMR11]] | -0.45 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[ARMCX3]] | -0.44 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[ARID5A]] | -0.44 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SLC41A2]] | -0.44 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[RND1]] | -0.43 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PIK3IP1]] | -0.43 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2]] | B | HMGA2 activity raises EVA1C's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.44× lower at baseline in the lines without HMGA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[PIWIL4]] | B | PIWIL4 activity raises EVA1C's level | lines that do not express PIWIL4 (11) vs lines expressing it (39) | 3.32× lower at baseline in the lines without PIWIL4 | 0.010 | ⚠ within organs, on part of the lines; also absent: FUT4, CTSZ, ARHGAP23 |
| [[SH3RF3]] | B | SH3RF3 activity strengthens EVA1C's drug response | lines that do not express SH3RF3 (7) vs lines expressing it (26) | the lines without SH3RF3 respond 0.74× as strongly (z diff +2.09); strongest at Homoharringtonine 0.5 µM: 0.42x vs 0.19x (z diff +4.3) | 0.029 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1; target measured in part of the lines; artifact flags |
| [[NPAS2]] | B | NPAS2 activity raises EVA1C's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without NPAS2 | 0.036 | ⚠ within organs, on part of the lines |
| [[TGFBR2]] | B | TGFBR2 activity raises EVA1C's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 3.81× lower at baseline in the lines without TGFBR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[FUT4]] | B | FUT4 activity raises EVA1C's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 3.20× lower at baseline in the lines without FUT4 | 0.054 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB1]] | B | EVA1C activity raises LAMB1's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without EVA1C | 0.018 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[PIWIL4]] | B | EVA1C activity raises PIWIL4's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without EVA1C | 0.023 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[TBC1D8]] | B | EVA1C activity raises TBC1D8's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without EVA1C | 0.030 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[DOCK5]] | B | EVA1C activity raises DOCK5's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without EVA1C | 0.055 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| cells under [[Vemurafenib (drug)]] 5 µM | B | EVA1C activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express EVA1C (15) vs lines expressing it (33) | the lines without EVA1C: 0.86× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[TGFBR2]] | B | EVA1C activity raises TGFBR2's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without EVA1C | 0.087 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.3, 43.8); signed map (11.1, 35.1). **Vector** length 99.9, 27.7% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.7 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.7 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +3.5 | -4.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | -0.3 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -8.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.7 | -1.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | eva-1 homolog C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:32,412,006-32,515,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B18, PRED34, B19; previously C21orf64, C21orf63, FAM176C |
| Gene groups (HGNC) | EVA1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [P58658](https://www.uniprot.org/uniprotkb/P58658) (Protein eva-1 homolog C):

> Binds heparin.

**Summary**, from NCBI Gene [59271](https://www.ncbi.nlm.nih.gov/gene/59271):

> Enables heparin binding activity. Located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13239) · Entrez [59271](https://www.ncbi.nlm.nih.gov/gene/59271) · UniProt [P58658](https://www.uniprot.org/uniprotkb/P58658) · Ensembl [ENSG00000166979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166979)

## Data

Gene col 9399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9399); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9399]; `tensor/DDL_lfc|DDL_z.npy` [9399]; `embed/gene_vectors.npy` [9399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9399 or target_col == 9399). Every well: [[EVA1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVA1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
