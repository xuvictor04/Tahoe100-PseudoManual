---
symbol: "AFAP1L1"
type: "gene"
col: 8078
ensembl_id: "ENSG00000157510"
name: "actin filament associated protein 1 like 1"
location: "5q32"
module: 104
arm: "+"
pooled_cpm: 30.19
n_lines_expressing: 36
n_dd_up: 22
n_dd_down: 37
n_dd_up_clean: 20
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# AFAP1L1

*actin filament associated protein 1 like 1* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Budesonide (drug)]] 0.5 µM: 1.62× (z +7.6, q 1e-11, up in 21 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.233× (z -32.6, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3RF3]] (+0.62, fdr 7e-06), [[LDLRAD3]] (+0.59, fdr 1e-05), [[ABLIM3]] (+0.58, fdr 1e-05, ⚠ same locus), [[PXYLP1]] (+0.58, fdr 1e-05); moves opposite to [[TFAP2A-AS1]] (-0.47, fdr 4e-05), [[DDR1]] (-0.47, fdr 4e-05), [[EPCAM-DT]] (-0.46, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[JCAD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.5 µM |  | **1.62×** | +7.6 | 1e-11 | 21/34 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.6 | 1e-08 | 17/30 (LoVo, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | **1.46×** | +6.1 | 3e-07 | 19/33 (Hs 766T, SK-MEL-2, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.51×** | +6.0 | 3e-07 | 20/33 (Hs 766T, Panc 03.27, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.44×** | +5.8 | 8e-07 | 19/33 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.7 | 1e-06 | 18/34 (Hs 766T, HOP62, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 2e-06 | 20/33 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.41×** | +5.5 | 3e-06 | 16/34 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.42×** | +5.3 | 6e-06 | 13/34 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.39×** | +5.3 | 7e-06 | 21/34 (HOP62, Hs 766T, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 7e-05 | 19/33 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 8e-05 | 15/33 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 2e-04 | 14/34 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 3e-04 | 12/34 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.4 | 3e-04 | 11/25 (LoVo, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 16/34 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.002 | 12/33 (Hs 766T, RPMI-7951, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.233×** | -32.6 | 0e+00 | 33/34 (SK-MEL-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.422×** | -19.3 | 0e+00 | 28/33 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.316×** | -18.2 | 0e+00 | 31/34 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.337×** | -17.2 | 0e+00 | 33/34 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.355×** | -16.4 | 0e+00 | 28/34 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.356×** | -16.3 | 0e+00 | 31/34 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.345×** | -16.2 | 0e+00 | 30/34 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.593×** | -11.6 | 2e-29 | 22/34 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -10.6 | 1e-24 | 23/34 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.282×** | -10.3 | 4e-23 | 30/34 (PANC-1, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -9.5 | 9e-20 | 21/33 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -9.1 | 6e-18 | 22/32 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -7.5 | 2e-12 | 24/32 (J82, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -7.4 | 5e-12 | 23/34 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -7.1 | 4e-11 | 22/33 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -7.0 | 8e-11 | 18/34 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.440×** | -6.7 | 8e-10 | 25/33 (HEC-1-A, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0748× (z -30.4) |
| [[J82 (line)]] | alt | 81.4 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0984× (z -31.5) |
| [[C32 (line)]] | wt | 123 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -26.8) |
| [[PANC-1 (line)]] | alt | 61.3 | 0 | 12 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -30.4) |
| [[HOP62 (line)]] | alt | 74.1 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -31.7) |
| [[Hs 766T (line)]] | wt | 88.1 | 3 | 8 | [[Dexamethasone (drug)]] 0.05 µM 3.09× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.0562× (z -33.5) |
| [[SK-MEL-2 (line)]] | alt | 80.5 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -37.4) |
| [[HEC-1-A (line)]] | alt | 81.3 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -25.0) |
| [[LoVo (line)]] | wt | 52.0 | 1 (1 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0856× (z -33.2) |
| [[NCI-H1792 (line)]] | alt | 40.0 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0767× (z -18.2) |
| [[SNU-423 (line)]] | alt | 43.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.0) |
| [[A549 (line)]] | wt | 19.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -19.0) |
| [[HS-578T (line)]] | alt | 32.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -15.6) |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.5) |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -22.2) |
| [[RPMI-7951 (line)]] | alt | 46.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -17.6) |
| [[A-172 (line)]] | wt | 7.63 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.101× (z -9.7) |
| [[H4 (line)]] | wt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -18.5) |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -19.8) |
| [[SW480 (line)]] | alt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.9) |
| [[A-427 (line)]] | wt | 21.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.262× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -19.3) |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 9.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.6) |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3RF3]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LDLRAD3]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ABLIM3]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 | STRING 546; ⚠ same locus (11.3 kb, same strand: neighbours can correlate without regulation) |
| [[PXYLP1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FN1]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GAB3]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[TANC2]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[RNF175]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[AKAP12]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TLR2]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[GALNT18]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SRPX]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SMYD2]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAP2A-AS1]] | -0.47 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[DDR1]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[EPCAM-DT]] | -0.46 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[FAM151B-DT]] | -0.46 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TMPRSS3]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TP63]] | -0.44 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[MVP-DT]] | -0.44 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ATP1B1]] | -0.44 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TNFSF10]] | -0.44 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[EPB41]] | -0.44 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[BMF]] | -0.43 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LIPC]] | -0.43 | -0.47 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JCAD]] | B | JCAD activity raises AFAP1L1's level | lines that do not express JCAD (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without JCAD | 0.027 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[NR3C1]] | B | NR3C1 activity raises AFAP1L1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity raises AFAP1L1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TFCP2L1]] | B | TFCP2L1 activity lowers AFAP1L1's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 1.77× higher at baseline in the lines without TFCP2L1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2 |
| [[GALNT18]] | B | GALNT18 activity raises AFAP1L1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 2.82× lower at baseline in the lines without GALNT18 | 0.076 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[ABLIM3]] | B | ABLIM3 activity raises AFAP1L1's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without ABLIM3 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[ITGB3]] | C | ITGB3 activity raises AFAP1L1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.69× lower at baseline in the lines without ITGB3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.5, 13.4); signed map (16.6, 35.5). **Vector** length 106, 30.0% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +1.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.3 | +4.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.3 | +4.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.5 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -17.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -6.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | actin filament associated protein 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,271,859-149,343,637 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36748 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TED9](https://www.uniprot.org/uniprotkb/Q8TED9) (Actin filament-associated protein 1-like 1):

> May be involved in podosome and invadosome formation.

**Summary**, from NCBI Gene [134265](https://www.ncbi.nlm.nih.gov/gene/134265):

> Predicted to be located in cytoplasm; podosome; and stress fiber. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26714) · Entrez [134265](https://www.ncbi.nlm.nih.gov/gene/134265) · UniProt [Q8TED9](https://www.uniprot.org/uniprotkb/Q8TED9) · Ensembl [ENSG00000157510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157510)

## Data

Gene col 8078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8078); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8078]; `tensor/DDL_lfc|DDL_z.npy` [8078]; `embed/gene_vectors.npy` [8078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8078 or target_col == 8078). Every well: [[AFAP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFAP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
