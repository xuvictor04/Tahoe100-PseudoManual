---
symbol: "PPA1"
type: "gene"
col: 11134
ensembl_id: "ENSG00000180817"
name: "inorganic pyrophosphatase 1"
location: "10q22.1"
module: 106
arm: "+"
pooled_cpm: 64.57
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PPA1

*inorganic pyrophosphatase 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +17.5, q 0e+00, up in 38 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.47× (z +6.9, q 2e-10, up in 31 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM29]] (+0.54, fdr 1e-05), [[PDLIM1]] (+0.53, fdr 3e-05), [[MTHFD1]] (+0.52, fdr 5e-05); moves opposite to [[BBIP1]] (-0.51, fdr 3e-05), [[FAM32A]] (-0.49, fdr 4e-04), [[CREM]] (-0.49, fdr 7e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 25 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.73×** | +17.5 | 0e+00 | 38/41 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.89×** | +16.6 | 0e+00 | 42/47 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.20×** | +13.2 | 2e-37 | 37/43 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.90×** | +11.6 | 4e-29 | 43/48 (HOP62, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.89×** | +11.5 | 1e-28 | 43/48 (A-427, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.84×** | +11.1 | 2e-26 | 42/48 (A-427, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.46×** | +9.7 | 2e-20 | 31/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.74×** | +9.6 | 4e-20 | 40/48 (NCI-H460, A498, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.71×** | +9.3 | 1e-18 | 38/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +8.2 | 2e-14 | 33/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +7.0 | 1e-10 | 34/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +6.9 | 2e-10 | 31/48 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.4 | 8e-09 | 30/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.42×** | +6.3 | 1e-08 | 27/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +6.2 | 2e-08 | 30/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.70×** | +5.0 | 2e-05 | 25/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +4.8 | 4e-05 | 21/49 (A-427, HT-29, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +4.7 | 7e-05 | 22/48 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.1 | 9e-04 | 17/48 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.002 | 18/48 (HT-29, C32, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.005 | 12/48 (HepG2/C3A, J82, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.005 | 19/48 (AsPC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.005 | 15/48 (NCI-H2030, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.007 | 15/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.011 | 16/48 (HT-29, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.013 | 16/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.018 | 15/47 (AsPC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.864× | -9.0 | 1e-16 | 14/49 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.836× | -3.2 | 0.40 | 10/48 (CFPAC-1, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.850× | -3.0 | 0.47 | 14/47 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 81.6 | 8 (6 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.65× (z +16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.43× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 33.2 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.2) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 30.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 30.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 3.88× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 54.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 71.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.73× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 67.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 54.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 45.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +8.6) | — |
| [[A549 (line)]] | wt | 60.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 72.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 78.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 51.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[AsPC-1 (line)]] | alt | 70.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 56.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.54× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 64.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 68.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.1) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 89.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.2) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H1792 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SHP-77 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 152 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +8.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM29]] | +0.54 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[MTHFD1]] | +0.52 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[IFNGR1]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[STOM]] | +0.51 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PON2]] | +0.51 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[EIF1AX]] | +0.51 | +0.39 / +0.58 | both halves | 6e-05 | STRING 410 |
| [[CD24]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[DNAJC15]] | +0.50 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[PDZD8]] | +0.50 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[LAD1]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[B4GALT5]] | +0.49 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBIP1]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[FAM32A]] | -0.49 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[CREM]] | -0.49 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ADGRL1-AS1]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[PAIP2]] | -0.48 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[WDR26]] | -0.46 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[DEDD2]] | -0.46 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[ZMAT5]] | -0.46 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[TMEM101]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ZNF446]] | -0.45 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[TRIM39]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[OTUD5]] | -0.45 | -0.44 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA3]] | B | ANXA3 activity raises PPA1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.71× lower at baseline in the lines without ANXA3 | 0.024 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[LRRC8B]] | B | LRRC8B activity raises PPA1's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without LRRC8B | 0.059 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |
| [[PLEKHA7]] | B | PLEKHA7 activity raises PPA1's level | lines that do not express PLEKHA7 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without PLEKHA7 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CD24]] | B | CD24 activity raises PPA1's level | lines that do not express CD24 (24) vs lines expressing it (26) | 1.59× lower at baseline in the lines without CD24 | 0.063 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2 |
| [[TRIM29]] | B | TRIM29 activity raises PPA1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 1.67× lower at baseline in the lines without TRIM29 | 0.092 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, 41.4); signed map (49.7, -1.1). **Vector** length 92.9, 25.8% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.0 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.0 | +17.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +4.5 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +7.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | +0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.3 | +5.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | inorganic pyrophosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,202,835-70,233,911 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SID6-8061, Ppase, IOPPP, PP1; previously PP |
| Gene groups (HGNC) | Inorganic pyrophosphatase family |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Pyrophosphate hydrolysis; Cytosolic tRNA aminoacylation; tRNA Aminoacylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15181](https://www.uniprot.org/uniprotkb/Q15181) (Inorganic pyrophosphatase):

> Catalyzes the hydrolysis of inorganic diphosphate into two phosphate molecules. Has MAP kinase serine/threonine phosphatase activity toward c-Jun N-terminal kinase (JNK) and, in neuronal cells, is involved in the negative regulation of neurite growth via JNK dephosphorylation (By similarity).

**Summary**, from NCBI Gene [5464](https://www.ncbi.nlm.nih.gov/gene/5464):

> The protein encoded by this gene is a member of the inorganic pyrophosphatase (PPase) family. PPases catalyze the hydrolysis of pyrophosphate to inorganic phosphate, which is important for the phosphate metabolism of cells. Studies of a similar protein in bovine suggested a cytoplasmic localization of this enzyme. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9226) · Entrez [5464](https://www.ncbi.nlm.nih.gov/gene/5464) · UniProt [Q15181](https://www.uniprot.org/uniprotkb/Q15181) · Ensembl [ENSG00000180817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180817)

## Data

Gene col 11134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11134); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11134]; `tensor/DDL_lfc|DDL_z.npy` [11134]; `embed/gene_vectors.npy` [11134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11134 or target_col == 11134). Every well: [[PPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
