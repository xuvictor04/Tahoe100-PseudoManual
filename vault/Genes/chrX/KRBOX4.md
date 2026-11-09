---
symbol: "KRBOX4"
type: "gene"
col: 7149
ensembl_id: "ENSG00000147121"
name: "KRAB domain containing 4"
location: "Xp11.3"
module: 197
arm: "+"
pooled_cpm: 32.58
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# KRBOX4

*KRAB domain containing 4* — Xp11.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.510× (z -14.7, q 0e+00, down in 36 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.611× (z -5.9, q 3e-07, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOX3]] (+0.64, fdr 1e-05), [[TBP]] (+0.61, fdr 1e-05), [[SLC30A6]] (+0.60, fdr 9e-06); moves opposite to [[NFIB]] (-0.61, fdr 1e-05), [[CARMIL1]] (-0.60, fdr 1e-05), [[NEO1]] (-0.59, fdr 1e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF160]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.19× | +3.6 | 0.15 | 13/46 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.11× | +3.4 | 0.22 | 4/46 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.510×** | -14.7 | 0e+00 | 36/45 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -12.6 | 7e-34 | 26/36 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.736×** | -9.9 | 1e-20 | 28/45 (C32, H4, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.705×** | -7.6 | 3e-12 | 20/33 (SW480, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.717×** | -7.6 | 3e-12 | 23/43 (C32, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.707×** | -7.6 | 3e-12 | 28/46 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.730×** | -7.2 | 6e-11 | 25/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.745×** | -6.7 | 2e-09 | 23/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.611×** | -5.9 | 3e-07 | 24/46 (SW480, C32, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.835× | -5.8 | 3e-07 | 22/46 (SNU-423, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.786×** | -5.5 | 2e-06 | 24/46 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.781×** | -5.4 | 3e-06 | 17/43 (J82, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -5.4 | 3e-06 | 21/46 (RPMI-7951, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.808×** | -4.9 | 5e-05 | 19/46 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.826×** | -4.3 | 5e-04 | 16/46 (RPMI-7951, Hs 766T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.043 | 4/46 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.769×** | -3.1 | 0.052 | 15/43 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.872× | -3.0 | 0.070 | 15/46 (C32, MIA PaCa-2, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.778×** | -3.0 | 0.070 | 11/44 (SW 900, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.826×** | -2.9 | 0.077 | 6/46 (NCI-H661, J82, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.783×** | -2.9 | 0.077 | 9/44 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.783×** | -2.9 | 0.077 | 8/46 (HOP62, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.874× | -2.8 | 0.091 | 9/44 (J82, CHP-212, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.883× | -2.8 | 0.091 | 4/45 (MIA PaCa-2, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 71.8 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 48.3 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0384× (z -29.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.119× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 40.5 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[J82 (line)]] | alt | 45.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -16.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 51.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 39.2 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -15.4) ⚠ toxic |
| [[H4 (line)]] | wt | 51.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 2 (1 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.0707× (z -9.8) |
| [[Hs 766T (line)]] | wt | 57.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 75.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.381× (z -10.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 40.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.358× (z -9.3) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 23.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.342× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.400× (z -8.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HCT15 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.361× (z -9.2) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -9.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -12.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.461× (z -8.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -13.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -11.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOX3]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[TBP]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SLC30A6]] | +0.60 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[VDAC1P8]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[VIPAS39]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GLE1]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ZNF568]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 | same gene group |
| [[KIAA0319L]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[NOXRED1]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[VRK3]] | +0.54 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[CHURC1-FNTB]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CCDC32]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFIB]] | -0.61 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[CARMIL1]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NEO1]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[CDH2]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PPM1L]] | -0.55 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[CHN1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SMAD2]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CDYL]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[CACHD1]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PLCE1]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TLE1]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF160]] | C | ZNF160 activity raises KRBOX4's level | lines that do not express ZNF160 (4) vs lines expressing it (46) | 4.39× lower at baseline in the lines without ZNF160 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF845, TBL1X, ZNF551; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction -0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.4, 36.8); signed map (-19.6, -1.5). **Vector** length 74.5, 13.6% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.1 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | -0.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -14.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.0 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.4 | -7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | KRAB domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:46,447,292-46,497,422 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20344; previously ZNF673, KRBOX4 |
| Gene groups (HGNC) | KRAB domain containing |
| Matched by | ensembl_id |

UniProt [Q5JUW0](https://www.uniprot.org/uniprotkb/Q5JUW0) carries no function annotation.

**Summary**, from NCBI Gene [55634](https://www.ncbi.nlm.nih.gov/gene/55634):

> This encodes a zinc finger protein with an N-terminal KRAB (Kruppel-associated) domain found in transcriptional repressors. This gene is located in a region of the X chromosome thought to be involved in nonsyndromic X-linked cognitive disability. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:26007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26007) · Entrez [55634](https://www.ncbi.nlm.nih.gov/gene/55634) · UniProt [Q5JUW0](https://www.uniprot.org/uniprotkb/Q5JUW0) · Ensembl [ENSG00000147121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147121)

## Data

Gene col 7149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7149); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7149]; `tensor/DDL_lfc|DDL_z.npy` [7149]; `embed/gene_vectors.npy` [7149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7149 or target_col == 7149). Every well: [[KRBOX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRBOX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
