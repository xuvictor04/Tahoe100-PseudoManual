---
symbol: "DOT1L"
type: "gene"
col: 2516
ensembl_id: "ENSG00000104885"
name: "DOT1 like histone lysine methyltransferase"
location: "19p13.3"
module: 206
arm: "+"
pooled_cpm: 66.75
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# DOT1L

*DOT1 like histone lysine methyltransferase* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.97× (z +8.0, q 1e-12, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.450× (z -9.4, q 3e-18, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.584× (z -8.4, q 2e-14, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIVEP3]] (+0.61, fdr 1e-05), [[N4BP3]] (+0.59, fdr 2e-05), [[NKD2]] (+0.59, fdr 2e-05); moves opposite to [[ATP6V1H]] (-0.57, fdr 1e-05), [[LURAP1L]] (-0.56, fdr 2e-05), [[CSDE1]] (-0.52, fdr 7e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +8.0 | 1e-12 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +7.6 | 9e-12 | 32/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.4 | 2e-11 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +6.3 | 3e-08 | 40/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.67×** | +5.8 | 8e-07 | 29/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 2e-05 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.1 | 3e-05 | 29/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +4.3 | 0.001 | 30/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +3.7 | 0.015 | 30/49 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.015 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.36×** | +3.5 | 0.020 | 22/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.029 | 25/48 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.450×** | -9.4 | 3e-18 | 42/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.584×** | -8.4 | 2e-14 | 44/48 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -7.8 | 1e-12 | 31/43 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.554×** | -6.4 | 2e-08 | 33/45 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -5.8 | 6e-07 | 32/49 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -4.7 | 2e-04 | 33/48 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -4.1 | 0.003 | 30/47 (HepG2/C3A, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.714×** | -4.0 | 0.005 | 33/48 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.007 | 27/50 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.804×** | -3.6 | 0.021 | 24/49 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.750×** | -3.4 | 0.036 | 24/48 (LoVo, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.036 | 26/48 (A-172, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.765×** | -3.2 | 0.069 | 26/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.658×** | -3.0 | 0.095 | 24/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 66.3 | 10 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.51× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -9.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 60.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +21.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.34× (z +14.6) | — |
| [[SW480 (line)]] | alt | 42.0 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.01× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 52.8 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.48× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +18.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.59× (z +15.1) | [[Adagrasib (drug)]] 0.05 µM 0.597× (z -14.3) ⚠ position not correctable |
| [[HOP62 (line)]] | alt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 52.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +12.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 66.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0332× (z -31.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.467× (z -9.5) |
| [[SW 900 (line)]] | alt | 64.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.84× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -14.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 56.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -11.0) |
| [[A498 (line)]] | wt | 56.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.08× (z +10.5) | — |
| [[A549 (line)]] | wt | 66.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +14.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 30.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +10.0) | — |
| [[C32 (line)]] | wt | 92.8 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.418× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 78.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -9.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 77.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 98.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 73.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +15.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.159× (z -15.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 87.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.442× (z -8.8) |
| [[SW48 (line)]] | wt | 75.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.08× (z +9.9) | — |
| [[A-172 (line)]] | wt | 94.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +17.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CHP-212 (line)]] | wt | 92.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0886× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 87.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 88.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -12.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 82.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0675× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 82.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +13.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP3]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.59 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[NKD2]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CD82]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LFNG]] | +0.56 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[PRR7]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[CYTH4]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[DRAP1]] | +0.54 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[SLCO4A1]] | +0.54 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[STMN3]] | +0.53 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ACAP3]] | +0.53 | +0.32 / +0.40 | both halves | 2e-04 |  |
| [[NUP58]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1H]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[LURAP1L]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[CSDE1]] | -0.52 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[APOOL]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ZNF148]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CUL5]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SRP14]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[FRS2]] | -0.50 | -0.48 / -0.32 | both halves | 1e-04 |  |
| [[TRMT11]] | -0.49 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[GHITM]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[PSMC2]] | -0.49 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[RBM41]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DOT1L's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD20A1]] | B | ANKRD20A1 activity raises DOT1L's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without ANKRD20A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[NRARP]] | B | NRARP activity lowers DOT1L's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.39× higher at baseline in the lines without NRARP | 0.022 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[BCL11B]] | B | BCL11B activity lowers DOT1L's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.23× higher at baseline in the lines without BCL11B | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.2, -3.3); signed map (-1.7, 42.6). **Vector** length 87.5, 25.5% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | -0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.9 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +0.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.2 | -8.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.5 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.7 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | DOT1 like histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,163,933-2,232,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1814, DOT1, KMT4 |
| Gene groups (HGNC) | Histone lysine methyltransferases; 7BS protein lysine methyltransferases |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEK3](https://www.uniprot.org/uniprotkb/Q8TEK3) (Histone-lysine N-methyltransferase, H3 lysine-79 specific):

> Histone methyltransferase that methylates 'Lys-79' of histone H3. Histones in nucleosomes are preferred as substrate compared to free histones. Binds to DNA. Together with MLLT3/AF9, is involved in SCNN1A transcriptional repression following H3K79 hypermethylation at the promoter (By similarity).

**Summary**, from NCBI Gene [84444](https://www.ncbi.nlm.nih.gov/gene/84444):

> The protein encoded by this gene is a histone methyltransferase that methylates lysine-79 of histone H3. It is inactive against free core histones, but shows significant histone methyltransferase activity against nucleosomes. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:24948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24948) · Entrez [84444](https://www.ncbi.nlm.nih.gov/gene/84444) · UniProt [Q8TEK3](https://www.uniprot.org/uniprotkb/Q8TEK3) · Ensembl [ENSG00000104885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104885)

## Data

Gene col 2516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2516); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2516]; `tensor/DDL_lfc|DDL_z.npy` [2516]; `embed/gene_vectors.npy` [2516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2516 or target_col == 2516). Every well: [[DOT1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOT1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
