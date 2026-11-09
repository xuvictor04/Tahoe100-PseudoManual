---
symbol: "PNCK"
type: "gene"
col: 5136
ensembl_id: "ENSG00000130822"
name: "pregnancy up-regulated nonubiquitous CaM kinase"
location: "Xq28"
module: 21
arm: "+"
pooled_cpm: 4.75
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PNCK

*pregnancy up-regulated nonubiquitous CaM kinase* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +10.1, q 4e-21, up in 26 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.290× (z -10.8, q 3e-24, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC3A1]] (+0.60, fdr 3e-05), [[CATSPER2P1-1]] (+0.57, fdr 1e-05), [[PPM1N]] (+0.56, fdr 1e-05); moves opposite to [[IPO9]] (-0.54, fdr 3e-05), [[ANAPC7]] (-0.50, fdr 2e-04), [[TREX2]] (-0.50, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +10.1 | 4e-21 | 26/34 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.94×** | +5.8 | 2e-06 | 21/39 (KATO III, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.58×** | +5.7 | 3e-06 | 14/42 (KATO III, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.82×** | +5.2 | 2e-05 | 18/42 (KATO III, HT-29, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.0 | 5e-05 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.6 | 4e-04 | 13/28 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.4 | 9e-04 | 2/18 (A498, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.4 | 9e-04 | 15/40 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.005 | 13/41 (HT-29, SNU-423, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.006 | 11/40 (C-33 A, KATO III, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.015 | 10/41 (KATO III, HT-29, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.025 | 9/40 (AsPC-1, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.038 | 13/36 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.046 | 11/43 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.052 | 7/42 (Hs 766T, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.060 | 9/42 (Hs 766T, PANC-1, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.086 | 9/40 (KATO III, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.290×** | -10.8 | 3e-24 | 32/43 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.392×** | -8.1 | 1e-13 | 31/41 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.418×** | -7.6 | 6e-12 | 22/31 (KATO III, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.415×** | -7.4 | 3e-11 | 28/40 (Hs 766T, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -5.8 | 7e-07 | 21/33 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.518×** | -5.7 | 1e-06 | 22/42 (A549, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.637×** | -5.6 | 2e-06 | 19/35 (HT-29, Hs 766T, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.517×** | -5.5 | 2e-06 | 17/26 (KATO III, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.536×** | -5.4 | 3e-06 | 22/43 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.548×** | -5.2 | 9e-06 | 23/39 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.608×** | -4.3 | 8e-04 | 18/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -3.8 | 0.008 | 14/42 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.666×** | -3.4 | 0.030 | 10/42 (Hs 766T, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -3.4 | 0.032 | 15/40 (KATO III, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.698×** | -3.1 | 0.066 | 13/32 (SW1417, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 24.8 | 0 | 11 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0156× (z -22.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0273× (z -20.5) |
| [[Hs 766T (line)]] | wt | 19.7 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -14.7) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0918× (z -11.1) |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0414× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -12.0) |
| [[A549 (line)]] | wt | 4.16 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0352× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 3.18 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +10.9) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0718× (z -10.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 4.88 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0941× (z -10.5) |
| [[LoVo (line)]] | wt | 3.13 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.53× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0463× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 3.42 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0924× (z -8.7) |
| [[AN3 CA (line)]] | alt | 53.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0625× (z -11.4) |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0340× (z -11.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -11.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[J82 (line)]] | alt | 3.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0342× (z -11.0) |
| [[SNU-423 (line)]] | alt | 3.83 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0365× (z -10.0) |
| [[A-172 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC3A1]] | +0.60 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[CATSPER2P1-1]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PPM1N]] | +0.56 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[IST1]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ACSM3]] | +0.55 | +0.57 / +0.49 | both halves | 2e-05 |  |
| [[KDM5B]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[KMT2E]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[DNAJC3-DT]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[LINC02580]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[AKAP1-DT]] | +0.52 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[HRG-AS1]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CARD14]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.50 | -0.29 / -0.61 | both halves | 2e-04 |  |
| [[TREX2]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MTOR]] | -0.48 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[AP3M2]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[NSMCE4A]] | -0.47 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[SKA3]] | -0.46 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[GFM1]] | -0.46 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[ELAC2]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[CEP85]] | -0.46 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[PRPF19]] | -0.45 | -0.29 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PNCK's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, 31.5); signed map (37.1, 2.2). **Vector** length 64.4, 9.93% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -8.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -10.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | pregnancy up-regulated nonubiquitous CaM kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,669,733-153,689,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45419, CaMK1b |
| Gene groups (HGNC) | CAMK1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2M8](https://www.uniprot.org/uniprotkb/Q6P2M8) (Calcium/calmodulin-dependent protein kinase type 1B):

> Calcium/calmodulin-dependent protein kinase belonging to a proposed calcium-triggered signaling cascade. In vitro phosphorylates CREB1 and SYN1/synapsin I. Phosphorylates and activates CAMK1 (By similarity).

**Summary**, from NCBI Gene [139728](https://www.ncbi.nlm.nih.gov/gene/139728):

> PNCK is a member of the calcium/calmodulin-dependent protein kinase family of protein serine/threonine kinases (see CAMK1; MIM 604998) (Gardner et al., 2000 [PubMed 10673339]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13415) · Entrez [139728](https://www.ncbi.nlm.nih.gov/gene/139728) · UniProt [Q6P2M8](https://www.uniprot.org/uniprotkb/Q6P2M8) · Ensembl [ENSG00000130822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130822)

## Data

Gene col 5136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5136); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5136]; `tensor/DDL_lfc|DDL_z.npy` [5136]; `embed/gene_vectors.npy` [5136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5136 or target_col == 5136). Every well: [[PNCK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNCK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
