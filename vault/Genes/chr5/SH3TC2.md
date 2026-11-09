---
symbol: "SH3TC2"
type: "gene"
col: 9784
ensembl_id: "ENSG00000169247"
name: "SH3 domain and tetratricopeptide repeats 2"
location: "5q32"
module: 195
arm: "+"
pooled_cpm: 13.22
n_lines_expressing: 30
n_dd_up: 15
n_dd_down: 46
n_dd_up_clean: 13
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# SH3TC2

*SH3 domain and tetratricopeptide repeats 2* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.31× (z +8.1, q 5e-13, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.260× (z -18.2, q 0e+00, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3TC2-DT]] (+0.93, fdr 7e-06, ⚠ same locus), [[MYEOV]] (+0.66, fdr 7e-06), [[LINC02320]] (+0.66, fdr 7e-06), [[ETV4]] (+0.66, fdr 7e-06); moves opposite to [[GABARAP]] (-0.53, fdr 2e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[MAP3K2]] (-0.53, fdr 1e-04), [[YY1AP1]] (-0.51, fdr 4e-05), [[RAB9A]] (-0.51, fdr 2e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PTPRZ1]] → it (grade B ⚠); 7 go from it, the strongest it → [[ARHGAP27P1-BPTFP1-KPNA2P3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +8.1 | 5e-13 | 14/27 (SW1417, Hs 766T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.76×** | +5.5 | 1e-05 | 18/28 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.39×** | +4.5 | 0.002 | 16/28 (SNU-1, SW480, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.014 | 9/28 (NCI-H2347, BT-474, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.8 | 0.018 | 10/24 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.026 | 9/28 (HEC-1-A, Hs 766T, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.030 | 7/27 (SW1417, SW480, …) | all doses, flat | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.5 | 0.030 | 9/27 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.037 | 4/27 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.4 | 0.041 | 7/24 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.050 | 6/27 (HEC-1-A, SNU-423, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.050 | 7/27 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.050 | 4/28 (SW1417, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.050 | 5/28 (SW1417, LS 180, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.066 | 10/27 (SW480, SNU-1, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.260×** | -18.2 | 0e+00 | 25/27 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.303×** | -11.4 | 1e-27 | 26/27 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.349×** | -9.6 | 1e-19 | 22/27 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.372×** | -9.4 | 8e-19 | 23/27 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -9.2 | 4e-18 | 21/26 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.382×** | -9.2 | 5e-18 | 24/27 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.394×** | -8.9 | 6e-17 | 20/27 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.472×** | -7.8 | 3e-13 | 21/28 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.446×** | -7.7 | 9e-13 | 21/27 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.486×** | -6.9 | 4e-10 | 17/27 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.491×** | -6.8 | 7e-10 | 18/27 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.501×** | -6.6 | 3e-09 | 18/27 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.589×** | -6.3 | 2e-08 | 19/28 (NCI-H460, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.518×** | -6.3 | 2e-08 | 18/27 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -5.8 | 3e-07 | 21/28 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -5.5 | 1e-06 | 17/27 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 45.2 | 0 | 17 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0155× (z -20.7) |
| [[MIA PaCa-2 (line)]] | alt | 75.8 | 0 | 15 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0378× (z -29.2) |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 12 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 60.1 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -16.6) |
| [[SW480 (line)]] | alt | 17.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0787× (z -23.2) |
| [[AsPC-1 (line)]] | alt | 20.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -15.0) |
| [[SNU-1 (line)]] | wt | 81.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.2) |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0518× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 40.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0715× (z -15.2) |
| [[LoVo (line)]] | wt | 8.45 | 0 | 4 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0570× (z -11.4) |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.7) |
| [[COLO 205 (line)]] | alt | 6.98 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -9.4) |
| [[Hs 766T (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.2) |
| [[HOP62 (line)]] | alt | 5.79 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.485× (z -8.5) ⚠ position not correctable |
| [[HT-29 (line)]] | alt | 7.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 9.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0867× (z -10.4) |
| [[A-172 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3TC2-DT]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[MYEOV]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[LINC02320]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ETV4]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ACOT7]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ANO1]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[C13orf46]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[BLACAT1]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 | same gene group |
| [[SLC48A1]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[EIPR1]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.59 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[MIR4280HG]] | +0.58 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | -0.53 | -0.48 / -0.53 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MAP3K2]] | -0.53 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[YY1AP1]] | -0.51 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[RAB9A]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ETFRF1]] | -0.50 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SIRT1]] | -0.50 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SPACA9]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[DNAJC27]] | -0.49 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[DNAJC12]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRZ1]] | B | PTPRZ1 activity raises SH3TC2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.96× lower at baseline in the lines without PTPRZ1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[COL13A1]] | B | COL13A1 activity raises SH3TC2's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without COL13A1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[LAPTM5]] | B | LAPTM5 activity raises SH3TC2's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without LAPTM5 | 0.068 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[SH3TC2-DT]] | C | SH3TC2-DT activity raises SH3TC2's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 4.99× lower at baseline in the lines without SH3TC2-DT | 1e-04 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G; co-absent with the target |
| [[PIWIL1]] | C | PIWIL1 activity raises SH3TC2's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.67× lower at baseline in the lines without PIWIL1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | SH3TC2 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 1.45× lower at baseline in the lines without SH3TC2 | 0.022 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent |
| [[NIBAN2]] | B | SH3TC2 activity raises NIBAN2's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without SH3TC2 | 0.043 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent |
| [[ITGA6]] | B | SH3TC2 activity raises ITGA6's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 2.41× lower at baseline in the lines without SH3TC2 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent |
| [[KPNA2P3]] | B | SH3TC2 activity raises KPNA2P3's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without SH3TC2 | 0.051 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent |
| [[SH3TC2-DT]] | C | SH3TC2 activity raises SH3TC2-DT's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 4.07× lower at baseline in the lines without SH3TC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent; co-absent with the target |
| [[ANO1]] | C | SH3TC2 activity raises ANO1's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 4.15× lower at baseline in the lines without SH3TC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent; co-absent with the target |
| [[PIWIL1]] | C | SH3TC2 activity raises PIWIL1's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 2.21× lower at baseline in the lines without SH3TC2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.0, 4.9); signed map (4.6, 39.9). **Vector** length 99.7, 28.8% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.3 | -7.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.1 | -6.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.0 | -4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.0 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain and tetratricopeptide repeats 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:148,923,639-149,063,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1985, CMT4C |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; MicroRNA protein coding host genes; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF17](https://www.uniprot.org/uniprotkb/Q8TF17) (SH3 domain and tetratricopeptide repeat-containing protein 2):

> Is involved in nerve myelination and is required for the integrity of nodes of Ranvier (By similarity). It probably functions as a Rab effector in the regulation of endocytic recycling.

**Summary**, from NCBI Gene [79628](https://www.ncbi.nlm.nih.gov/gene/79628):

> This gene encodes a protein with two N-terminal Src homology 3 (SH3) domains and 10 tetratricopeptide repeat (TPR) motifs, and is a member of a small gene family. The gene product has been proposed to be an adapter or docking molecule. Mutations in this gene result in autosomal recessive Charcot-Marie-Tooth disease type 4C, a childhood-onset neurodegenerative disease characterized by demyelination of motor and sensory neurons. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29427) · Entrez [79628](https://www.ncbi.nlm.nih.gov/gene/79628) · UniProt [Q8TF17](https://www.uniprot.org/uniprotkb/Q8TF17) · Ensembl [ENSG00000169247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169247)

## Data

Gene col 9784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9784); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9784]; `tensor/DDL_lfc|DDL_z.npy` [9784]; `embed/gene_vectors.npy` [9784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9784 or target_col == 9784). Every well: [[SH3TC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3TC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
