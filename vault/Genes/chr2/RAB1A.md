---
symbol: "RAB1A"
type: "gene"
col: 6116
ensembl_id: "ENSG00000138069"
name: "RAB1A, member RAS oncogene family"
location: "2p14"
module: 56
arm: "+"
pooled_cpm: 422.03
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# RAB1A

*RAB1A, member RAS oncogene family* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.54× (z +8.0, q 9e-13, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.516× (z -10.4, q 2e-22, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.724× (z -4.9, q 5e-05, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54]] (+0.77, fdr 7e-06), [[ACBD3]] (+0.76, fdr 7e-06), [[EIF2AK3]] (+0.75, fdr 7e-06); moves opposite to [[RANGAP1]] (-0.64, fdr 7e-06), [[ANAPC7]] (-0.63, fdr 1e-05), [[ATE1]] (-0.62, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +8.0 | 9e-13 | 47/49 (A498, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +6.0 | 4e-07 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +6.0 | 4e-07 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +5.9 | 5e-07 | 42/48 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.6 | 5e-04 | 32/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.22× | +3.2 | 0.11 | 26/48 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.22× | +3.1 | 0.18 | 24/47 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.18 | 24/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.516×** | -10.4 | 2e-22 | 41/44 (CHP-212, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -10.0 | 5e-21 | 46/49 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.610×** | -8.1 | 1e-13 | 37/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.637×** | -6.8 | 1e-09 | 35/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.659×** | -6.8 | 1e-09 | 36/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.668×** | -6.6 | 4e-09 | 35/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.762×** | -5.9 | 4e-07 | 29/49 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.730×** | -4.9 | 5e-05 | 39/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.724×** | -4.9 | 5e-05 | 35/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.9 | 5e-05 | 29/48 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.770×** | -4.2 | 0.001 | 36/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.776×** | -4.0 | 0.003 | 31/48 (NCI-H2347, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.786×** | -3.9 | 0.004 | 32/48 (H4, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.029 | 28/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.807×** | -3.4 | 0.029 | 28/50 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.047 | 28/49 (SW1417, SW48, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.049 | 26/49 (COLO 205, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 519 | 0 | 12 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.553× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 491 | 2 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 4.38× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CFPAC-1 (line)]] | alt | 608 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 438 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.1) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HT-29 (line)]] | alt | 477 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.507× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 479 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 442 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 855 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 432 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.77× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.479× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 703 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -14.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 593 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 492 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 493 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H1573 (line)]] | alt | 553 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -15.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 501 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -16.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 615 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.88× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.467× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 553 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[COLO 205 (line)]] | alt | 389 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.42× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 388 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 351 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 367 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 316 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 508 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -13.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 304 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.535× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 455 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.43× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -11.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 380 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.12× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 282 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.34× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 347 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -17.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 454 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.432× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 268 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 331 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.77× (z +8.8) | — |
| [[J82 (line)]] | alt | 235 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.517× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 422 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 302 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.24× (z +9.0) | — |
| [[A-427 (line)]] | wt | 388 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 278 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 209 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 478 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 458 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 444 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 307 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 700 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 344 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54]] | +0.77 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.76 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[GBF1]] | +0.74 | +0.80 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 875 |
| [[TFG]] | +0.73 | +0.79 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 574 |
| [[TBC1D23]] | +0.73 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[COPB1]] | +0.71 | +0.78 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 811 |
| [[DPM1]] | +0.70 | +0.79 / +0.56 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[SEC31A]] | +0.69 | +0.76 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC61B]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.68 | +0.76 / +0.59 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 687 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANGAP1]] | -0.64 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.63 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[ATE1]] | -0.62 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[NUP188]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 | pathway: Mitotic Prophase |
| [[CTPS1]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.58 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[BTBD1]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[GNL3L]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[RBM12]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[GRWD1]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.57 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ELK4]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RAB1A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CA12]] | B | CA12 activity strengthens RAB1A's drug response | lines that do not express CA12 (29) vs lines expressing it (21) | the lines without CA12 respond 0.88× as strongly (z diff +1.01); strongest at Panobinostat 0.5 µM: 0.75x vs 0.54x (z diff +3.4) | 0.069 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; artifact flags |
| [[CA12]] | B | CA12 activity raises RAB1A's level | lines that do not express CA12 (29) vs lines expressing it (21) | 1.25× lower at baseline in the lines without CA12 | 0.096 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, -34.6); signed map (-49.7, 12.3). **Vector** length 114, 52.1% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.61 to 10); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.55 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.1 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | -10.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | -0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | -0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.6 | +2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.3 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.9 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RAB1A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:65,070,696-65,130,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YPT1; previously RAB1 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 18 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; RAB geranylgeranylation; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P62820](https://www.uniprot.org/uniprotkb/P62820) (Ras-related protein Rab-1A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB1A regulates vesicular protein transport from the endoplasmic reticulum (ER) to the Golgi compartment and on to the …

**Summary**, from NCBI Gene [5861](https://www.ncbi.nlm.nih.gov/gene/5861):

> This gene encodes a member of the Ras superfamily of GTPases. Members of the gene family cycle between inactive GDP-bound and active GTP-bound forms. This small GTPase controls vesicle traffic from the endoplasmic reticulum to the Golgi apparatus. Multiple alternatively spliced transcript variants have been identified for this gene which encode different protein isoforms. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:9758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9758) · Entrez [5861](https://www.ncbi.nlm.nih.gov/gene/5861) · UniProt [P62820](https://www.uniprot.org/uniprotkb/P62820) · Ensembl [ENSG00000138069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138069)

## Data

Gene col 6116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6116); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6116]; `tensor/DDL_lfc|DDL_z.npy` [6116]; `embed/gene_vectors.npy` [6116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6116 or target_col == 6116). Every well: [[RAB1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
