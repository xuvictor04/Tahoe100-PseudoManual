---
symbol: "RDH13"
type: "gene"
col: 8349
ensembl_id: "ENSG00000160439"
name: "retinol dehydrogenase 13"
location: "19q13.42"
module: 31
arm: "+"
pooled_cpm: 37.49
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 67
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# RDH13

*retinol dehydrogenase 13* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.24× (z +17.8, q 0e+00, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.646× (z -9.1, q 3e-17, down in 20 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.777× (z -7.9, q 9e-13, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMC6]] (+0.74, fdr 7e-06), [[PPARD]] (+0.71, fdr 1e-05), [[FA2H]] (+0.71, fdr 7e-06); moves opposite to [[NNT]] (-0.57, fdr 6e-05), [[SH3BGRL]] (-0.56, fdr 3e-05), [[RAB11FIP2]] (-0.55, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +17.8 | 0e+00 | 35/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +15.9 | 0e+00 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +13.1 | 5e-37 | 31/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +9.3 | 3e-18 | 27/47 (HS-578T, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.4 | 9e-06 | 19/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +5.3 | 9e-06 | 18/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 5e-05 | 17/48 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.9 | 6e-05 | 19/46 (C32, NCI-H1792, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 8e-04 | 17/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.004 | 10/44 (SHP-77, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 13/46 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.004 | 11/46 (A-172, SNU-1, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 16/44 (LS 180, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.086 | 8/44 (SW 900, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -9.1 | 3e-17 | 20/35 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.777×** | -7.9 | 9e-13 | 23/47 (NCI-H1573, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.762×** | -6.0 | 4e-07 | 21/41 (HCT15, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.752×** | -5.8 | 1e-06 | 20/47 (MIA PaCa-2, SW48, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.763×** | -5.7 | 2e-06 | 22/46 (LS 180, SW 1271, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.781×** | -5.5 | 5e-06 | 18/47 (SW48, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -5.3 | 9e-06 | 18/45 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.807×** | -4.7 | 2e-04 | 17/46 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.665×** | -4.7 | 2e-04 | 18/44 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.800×** | -4.7 | 2e-04 | 17/46 (PANC-1, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.813×** | -4.6 | 2e-04 | 18/48 (SW48, MIA PaCa-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.814×** | -4.5 | 3e-04 | 20/47 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.848× | -4.2 | 9e-04 | 13/47 (MIA PaCa-2, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.872× | -4.2 | 9e-04 | 12/47 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.868× | -4.0 | 0.002 | 16/47 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.884× | -3.9 | 0.004 | 15/47 (SW1417, SW48, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.889× | -3.7 | 0.008 | 12/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.852× | -3.3 | 0.025 | 11/46 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 213 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -16.8) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.203× (z -12.6) |
| [[SW48 (line)]] | wt | 142 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -14.6) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.380× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 60.1 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LoVo (line)]] | wt | 68.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.368× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 0 | 3 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -13.2) ⚠ position not correctable |
| [[SW480 (line)]] | alt | 37.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.9) | — |
| [[A498 (line)]] | wt | 15.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.5) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.15× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 2 | — | [[Tolmetin (drug)]] 5 µM 0.0640× (z -8.8) |
| [[COLO 205 (line)]] | alt | 83.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 14.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.03× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 36.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 91.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -13.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[A-172 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -9.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -14.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 51.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[J82 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.421× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 23.1 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.14× (z +9.5) | — |
| [[A-427 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMC6]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[PPARD]] | +0.71 | +0.67 / +0.57 | both halves | 1e-05 | pathway: Signaling by Nuclear Receptors |
| [[FA2H]] | +0.71 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[SEMA3B]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.71 | +0.78 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.7 kb: neighbours can correlate without regulation) |
| [[CRYBG2]] | +0.70 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[FAM83E]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PLEKHM1P1]] | +0.69 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CLDN4]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SERPINB1]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.68 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PTK6]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | -0.57 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[SH3BGRL]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | -0.55 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[VBP1]] | -0.55 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[CASD1]] | -0.54 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[C5orf15]] | -0.54 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 67, C 0. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity raises RDH13's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[LIPH]] | B | LIPH activity raises RDH13's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without LIPH | 7e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[CDH1]] | B | CDH1 activity raises RDH13's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.46× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[CLDN4]] | B | CLDN4 activity raises RDH13's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without CLDN4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[ATP2C2]] | B | ATP2C2 activity raises RDH13's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.61× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[CLDN7]] | B | CLDN7 activity raises RDH13's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without CLDN7 | 0.002 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[HS3ST1]] | B | HS3ST1 activity raises RDH13's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[CBLC]] | B | CBLC activity raises RDH13's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without CBLC | 0.002 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[FAM83B]] | B | FAM83B activity raises RDH13's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without FAM83B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[C1orf116]] | B | C1orf116 activity raises RDH13's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without C1orf116 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[RNF39]] | B | RNF39 activity raises RDH13's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without RNF39 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[TRIM15]] | B | TRIM15 activity raises RDH13's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.42× lower at baseline in the lines without TRIM15 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 55.7); signed map (-0.4, 37.7). **Vector** length 114, 28.2% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +15.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +17.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.3 | +13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.8 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.5 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.0 | -5.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.9 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.9 | -4.5 |
|  | [[NG25 (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -4.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.3 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | retinol dehydrogenase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,039,108-55,071,291 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR7C3 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 3 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBN7](https://www.uniprot.org/uniprotkb/Q8NBN7) (Retinol dehydrogenase 13):

> Retinol dehydrogenase with a clear preference for NADP. Oxidizes all-trans-retinol, but seems to reduce all-trans-retinal with much higher efficiency. Has no activity toward steroids.

**Summary**, from NCBI Gene [112724](https://www.ncbi.nlm.nih.gov/gene/112724):

> This gene encodes a mitochondrial short-chain dehydrogenase/reductase, which catalyzes the reduction and oxidation of retinoids. The encoded enzyme may function in retinoic acid production and may also protect the mitochondria against oxidative stress. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:19978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19978) · Entrez [112724](https://www.ncbi.nlm.nih.gov/gene/112724) · UniProt [Q8NBN7](https://www.uniprot.org/uniprotkb/Q8NBN7) · Ensembl [ENSG00000160439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160439)

## Data

Gene col 8349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8349); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8349]; `tensor/DDL_lfc|DDL_z.npy` [8349]; `embed/gene_vectors.npy` [8349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8349 or target_col == 8349). Every well: [[RDH13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDH13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
