---
symbol: "KRT18"
type: "gene"
col: 3190
ensembl_id: "ENSG00000111057"
name: "keratin 18"
location: "12q13.13"
module: 31
arm: "+"
pooled_cpm: 251.58
n_lines_expressing: 31
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 51
direction_downstream: 36
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KRT18

*keratin 18* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.75× (z +13.2, q 5e-37, up in 29 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.89× (z +5.4, q 8e-06, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.484× (z -5.8, q 3e-06, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT8]] (+0.84, fdr 7e-06, ⚠ same locus), [[CAPN8]] (+0.69, fdr 7e-06), [[LAD1]] (+0.64, fdr 1e-05), [[SHH]] (+0.64, fdr 8e-06); moves opposite to [[NUDT2]] (-0.51, fdr 1e-04), [[MFSD8]] (-0.49, fdr 4e-05), [[PABPN1]] (-0.48, fdr 9e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[F2RL1]] → it (grade B ⚠); 36 go from it, the strongest it → [[ITGA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.75×** | +13.2 | 5e-37 | 29/30 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +9.6 | 2e-19 | 27/28 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +8.8 | 3e-16 | 26/28 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +5.4 | 8e-06 | 21/29 (NCI-H2030, A549, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.64×** | +4.0 | 0.007 | 18/29 (AsPC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.8 | 0.014 | 7/31 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.53×** | +3.5 | 0.040 | 13/29 (A549, PANC-1, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.073 | 16/29 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.080 | 22/29 (PANC-1, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.484×** | -5.8 | 3e-06 | 27/31 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.663×** | -4.8 | 3e-04 | 23/29 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.554×** | -4.8 | 3e-04 | 25/29 (NCI-H23, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.569×** | -4.8 | 3e-04 | 24/29 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.591×** | -4.4 | 0.001 | 23/29 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.604×** | -3.9 | 0.008 | 18/29 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.631×** | -3.9 | 0.009 | 23/29 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.423×** | -3.8 | 0.010 | 27/30 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.426×** | -3.8 | 0.010 | 26/31 (NCI-H23, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.012 | 23/30 (HT-29, HCT15, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.653×** | -3.6 | 0.017 | 19/29 (SW48, SW480, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.448×** | -3.5 | 0.019 | 23/29 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.710×** | -3.3 | 0.041 | 20/29 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.554×** | -3.0 | 0.093 | 21/29 (NCI-H23, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.704×** | -3.0 | 0.093 | 19/30 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.692×** | -3.0 | 0.096 | 24/29 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 391 | 1 (1 ⚠) | 9 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.8) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.133× (z -14.7) |
| [[SW480 (line)]] | alt | 670 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -13.8) |
| [[KATO III (line)]] | alt | 818 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -15.8) |
| [[LoVo (line)]] | wt | 523 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -13.0) |
| [[HT-29 (line)]] | alt | 739 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +12.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -19.3) |
| [[LS 180 (line)]] | wt | 774 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 201 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.94× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.6) |
| [[SW48 (line)]] | wt | 269 | 0 | 4 | — | [[Trametinib (drug)]] 5 µM 0.146× (z -10.6) |
| [[A498 (line)]] | wt | 84.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 225 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +14.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 310 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -14.2) |
| [[PANC-1 (line)]] | alt | 160 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.09× (z +14.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +8.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 297 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.14× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.5) |
| [[COLO 205 (line)]] | alt | 155 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -8.9) |
| [[HCT15 (line)]] | alt | 615 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -18.4) |
| [[Hs 766T (line)]] | wt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +11.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 182 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 354 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.245× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 66.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.43× (z +13.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 638 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 692 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -8.9) |
| [[A-427 (line)]] | wt | 78.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 265 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 185 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 82.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 38.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 263 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 39.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 40.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 32.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 60.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 60.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 55.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT8]] | +0.84 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CAPN8]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LAD1]] | +0.64 | +0.74 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[SHH]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[KLK10]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ABHD11]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CASC19]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LAMA3]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[KCNH8]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.60 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[PADI1]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MST1R]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT2]] | -0.51 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[MFSD8]] | -0.49 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PABPN1]] | -0.48 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[CAPN10-DT]] | -0.47 | -0.48 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 12, C 39. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2RL1]] | B | F2RL1 activity raises KRT18's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 4.02× lower at baseline in the lines without F2RL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[TMC6]] | B | TMC6 activity raises KRT18's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.86× lower at baseline in the lines without TMC6 | 0.008 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[GJB2]] | B | GJB2 activity raises KRT18's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without GJB2 | 0.031 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[KCNH8]] | B | KCNH8 activity raises KRT18's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without KCNH8 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[DMKN]] | B | DMKN activity raises KRT18's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.66× lower at baseline in the lines without DMKN | 0.055 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[MAP2K1]] | B | MAP2K1 activity raises KRT18's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KRT86]] | B | KRT86 activity raises KRT18's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without KRT86 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[SULF2]] | B | SULF2 activity raises KRT18's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without SULF2 | 0.061 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[IL1RN]] | B | IL1RN activity raises KRT18's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without IL1RN | 0.067 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[MUC5AC]] | B | MUC5AC activity raises KRT18's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.57× lower at baseline in the lines without MUC5AC | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[ITGA6]] | B | ITGA6 activity raises KRT18's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.61× lower at baseline in the lines without ITGA6 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CTSE]] | B | CTSE activity raises KRT18's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.74× lower at baseline in the lines without CTSE | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 9, C 27. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA6]] | B | KRT18 activity raises ITGA6's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.53× lower at baseline in the lines without KRT18 | 0.012 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[TMC6]] | B | KRT18 activity raises TMC6's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 3.11× lower at baseline in the lines without KRT18 | 0.012 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[ABHD11]] | B | KRT18 activity raises ABHD11's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without KRT18 | 0.023 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[DMKN]] | B | KRT18 activity raises DMKN's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.91× lower at baseline in the lines without KRT18 | 0.033 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[CISD3]] | B | KRT18 activity raises CISD3's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without KRT18 | 0.050 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[KRT86]] | B | KRT18 activity raises KRT86's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without KRT18 | 0.050 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[ADAP1]] | B | KRT18 activity raises ADAP1's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without KRT18 | 0.054 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[LINC02832]] | B | KRT18 activity raises LINC02832's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 1.66× lower at baseline in the lines without KRT18 | 0.063 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[GJB2]] | B | KRT18 activity raises GJB2's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.51× lower at baseline in the lines without KRT18 | 0.0995 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[MISP]] | C | KRT18 activity raises MISP's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 5.84× lower at baseline in the lines without KRT18 | 3e-04 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent; co-absent with the target |
| [[KRT8]] | C | KRT18 activity raises KRT8's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 5.06× lower at baseline in the lines without KRT18 | 0.001 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent; co-absent with the target |
| [[SH2D3A]] | C | KRT18 activity raises SH2D3A's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 4.88× lower at baseline in the lines without KRT18 | 0.002 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, 50.8); signed map (66.9, 10.5). **Vector** length 108, 40.9% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +8.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.5 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -3.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.6 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | keratin 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,948,871-52,952,906 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Keratins, type I |
| Hallmark sets | PROTEIN_SECRETION, APOPTOSIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P05783](https://www.uniprot.org/uniprotkb/P05783) (Keratin, type I cytoskeletal 18):

> Structural component of intermediate filaments in simple epithelial cells. Forms intermediate filaments by heterodimerizing with the type II keratin KRT8, providing mechanical stability and resilience to epithelial cells. Involved in ARHGEF40-mediated actin stress fiber formation and tensional force-induced stress fiber formation and reinforcement. Integrates into the intermediate filament network of skeletal muscle fibers alongside desmin and KRT19, contributing to force transmission (By …

**Summary**, from NCBI Gene [3875](https://www.ncbi.nlm.nih.gov/gene/3875):

> KRT18 encodes the type I intermediate filament chain keratin 18. Keratin 18, together with its filament partner keratin 8, are perhaps the most commonly found members of the intermediate filament gene family. They are expressed in single layer epithelial tissues of the body. Mutations in this gene have been linked to cryptogenic cirrhosis. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6430) · Entrez [3875](https://www.ncbi.nlm.nih.gov/gene/3875) · UniProt [P05783](https://www.uniprot.org/uniprotkb/P05783) · Ensembl [ENSG00000111057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111057)

## Data

Gene col 3190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3190); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3190]; `tensor/DDL_lfc|DDL_z.npy` [3190]; `embed/gene_vectors.npy` [3190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3190 or target_col == 3190). Every well: [[KRT18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
