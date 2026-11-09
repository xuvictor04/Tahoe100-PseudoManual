---
symbol: "BMF"
type: "gene"
col: 2413
ensembl_id: "ENSG00000104081"
name: "Bcl2 modifying factor"
location: "15q15.1"
module: 59
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 46
n_dd_up: 42
n_dd_down: 23
n_dd_up_clean: 36
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 8
direction_downstream: 10
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# BMF

*Bcl2 modifying factor* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.30× (z +14.1, q 9e-43, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.236× (z -12.3, q 7e-32, down in 34 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.388× (z -8.1, q 2e-13, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBP]] (+0.68, fdr 7e-06), [[GBP2]] (+0.67, fdr 7e-06), [[BDKRB2]] (+0.65, fdr 1e-05); moves opposite to [[HLCS]] (-0.62, fdr 1e-05), [[ALG8]] (-0.59, fdr 2e-05), [[EIPR1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[WFDC2]] → it (grade B ⚠); 10 go from it, the strongest it → [[YPEL3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 6 with an alert ⚠; shown: the 15 strongest. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.30×** | +14.1 | 9e-43 | 37/43 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.29×** | +14.1 | 9e-43 | 32/40 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.31×** | +12.4 | 6e-33 | 34/41 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.62×** | +10.9 | 2e-25 | 29/42 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +10.6 | 3e-24 | 18/31 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +10.0 | 9e-22 | 19/31 (KATO III, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.30×** | +10.0 | 1e-21 | 28/41 (Panc 03.27, A498, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.20×** | +6.7 | 2e-09 | 14/33 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.11×** | +6.1 | 7e-08 | 16/35 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.79×** | +5.7 | 5e-07 | 17/40 (C32, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.62×** | +5.6 | 1e-06 | 19/40 (SW480, C32, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.93×** | +5.4 | 4e-06 | 19/38 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +5.1 | 1e-05 | 19/38 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.53×** | +4.9 | 4e-05 | 9/43 (SK-MEL-2, C32, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.62×** | +4.9 | 4e-05 | 12/40 (C32, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.236×** | -12.3 | 7e-32 | 34/41 (SW 900, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.388×** | -8.1 | 2e-13 | 25/41 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.472×** | -6.4 | 3e-08 | 22/39 (SW 900, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.389×** | -5.7 | 1e-06 | 21/43 (KATO III, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -5.2 | 2e-05 | 17/38 (SW480, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.562×** | -4.6 | 3e-04 | 16/38 (COLO 205, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.578×** | -4.5 | 6e-04 | 12/40 (LOX-IMVI, SW 900, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.268×** | -4.4 | 7e-04 | 15/34 (SW 900, NCI-H2347, …) | two highest doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -4.4 | 7e-04 | 18/37 (HT-29, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.604×** | -4.3 | 1e-03 | 14/42 (SHP-77, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.280×** | -4.3 | 0.001 | 16/29 (SW 900, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.338×** | -3.6 | 0.013 | 13/28 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.657×** | -3.6 | 0.015 | 11/39 (SHP-77, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.666×** | -3.5 | 0.021 | 10/38 (Panc 03.27, hTERT-HPNE, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.361×** | -3.4 | 0.025 | 10/32 (CFPAC-1, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.679×** | -3.2 | 0.049 | 8/35 (NCI-H1792, SW1417, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.049 | 12/41 (SNU-423, CHP-212, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.691×** | -3.1 | 0.049 | 9/39 (HOP62, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 31.2 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0336× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0455× (z -13.3) |
| [[COLO 205 (line)]] | alt | 14.9 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -8.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.152× (z -8.5) |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0750× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 9.97 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0441× (z -12.8) |
| [[A498 (line)]] | wt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 6.51 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0964× (z -8.6) |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0678× (z -9.1) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.2× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.58 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.88× (z +8.7) ⚠ position not correctable | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0768× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[A-172 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[GBP2]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[BDKRB2]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[PIK3IP1]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[DDR1]] | +0.62 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[EFNA1]] | +0.61 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[GABARAP]] ⚠ | +0.61 | +0.60 / +0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NEU1]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SOX4]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[VASN]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MAF]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CXXC5]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLCS]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ALG8]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[EIPR1]] | -0.57 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[METTL2B]] | -0.57 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ABCE1]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ERCC8]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[TSR1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PSMD14]] | -0.55 | -0.56 / -0.45 | both halves | 3e-05 | pathway: Apoptosis |
| [[COX10]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LARS2]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[DCTD]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TANGO6]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC2]] | B | WFDC2 activity raises BMF's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.04× lower at baseline in the lines without WFDC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[BDKRB2]] | B | BDKRB2 activity raises BMF's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without BDKRB2 | 0.010 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[HNMT]] | B | HNMT activity raises BMF's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without HNMT | 0.023 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[CGNL1]] | B | CGNL1 activity raises BMF's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without CGNL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[CXXC5]] | B | CXXC5 activity raises BMF's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without CXXC5 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[SLC7A8]] | B | SLC7A8 activity raises BMF's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without SLC7A8 | 0.065 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[LRRN1]] | B | LRRN1 activity raises BMF's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.52× lower at baseline in the lines without LRRN1 | 0.065 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[MAF]] | B | MAF activity raises BMF's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.37× lower at baseline in the lines without MAF | 0.087 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YPEL3]] | C | BMF activity raises YPEL3's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[ZRANB3]] | C | BMF activity lowers ZRANB3's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.08× higher at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[RHBDD1]] | C | BMF activity lowers RHBDD1's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.00× higher at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[DNAJC11]] | C | BMF activity lowers DNAJC11's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[RAB9A]] | C | BMF activity raises RAB9A's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.36× lower at baseline in the lines without BMF | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent |
| [[GBP2]] | C | BMF activity raises GBP2's level | lines that do not express BMF (4) vs lines expressing it (46) | 3.56× lower at baseline in the lines without BMF | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent |
| [[MTHFD1L]] | C | BMF activity lowers MTHFD1L's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.27× higher at baseline in the lines without BMF | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[YPEL2]] | C | BMF activity raises YPEL2's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without BMF | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[METTL2B]] | C | BMF activity lowers METTL2B's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.40× higher at baseline in the lines without BMF | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[SSBP3]] | C | BMF activity raises SSBP3's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without BMF | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (25.5, -1.0); signed map (47.1, 9.4). **Vector** length 81.9, 17.0% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | -0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +10.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +6.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -12.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -8.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | Bcl2 modifying factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,087,890-40,108,892 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00065 |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only |
| Hallmark sets | APOPTOSIS |
| Reactome | 6 pathways, smallest: Activation of BMF and translocation to mitochondria; BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members; Activation of BH3-only proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LC9](https://www.uniprot.org/uniprotkb/Q96LC9) (Bcl-2-modifying factor):

> May play a role in apoptosis. Isoform 1 seems to be the main initiator.

**Summary**, from NCBI Gene [90427](https://www.ncbi.nlm.nih.gov/gene/90427):

> The protein encoded by this gene belongs to the BCL2 protein family. BCL2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. This protein contains a single BCL2 homology domain 3 (BH3), and has been shown to bind BCL2 proteins and function as an apoptotic activator. This protein is found to be sequestered to myosin V motors by its association with dynein light chain 2, which may be important for …

**Accessions** — [HGNC:24132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24132) · Entrez [90427](https://www.ncbi.nlm.nih.gov/gene/90427) · UniProt [Q96LC9](https://www.uniprot.org/uniprotkb/Q96LC9) · Ensembl [ENSG00000104081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104081)

## Data

Gene col 2413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2413); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2413]; `tensor/DDL_lfc|DDL_z.npy` [2413]; `embed/gene_vectors.npy` [2413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2413 or target_col == 2413). Every well: [[BMF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
