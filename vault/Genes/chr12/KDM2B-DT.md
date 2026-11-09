---
symbol: "KDM2B-DT"
type: "gene"
col: 15006
ensembl_id: "ENSG00000256742"
name: "KDM2B divergent transcript"
location: "12q24.31"
module: 105
arm: "+"
pooled_cpm: 5.2
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 3
direction_downstream: 20
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# KDM2B-DT

*KDM2B divergent transcript* — 12q24.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.324× (z -13.8, q 2e-40, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMAD9]] (+0.64, fdr 7e-06), [[KDM2B]] (+0.60, fdr 7e-06, ⚠ same locus), [[TLE6]] (+0.55, fdr 4e-05), [[DIXDC1]] (+0.53, fdr 1e-05); moves opposite to [[KLF3]] (-0.47, fdr 5e-05), [[XYLT1]] (-0.41, fdr 7e-05), [[TMBIM1]] (-0.41, fdr 2e-04).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SMAD9]] → it (grade B ⚠); 20 go from it, the strongest it → [[KDM2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 1.49× | +3.5 | 0.14 | 11/39 (A-427, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.46× | +3.3 | 0.14 | 8/37 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.32× | +3.3 | 0.14 | 10/40 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.48× | +3.3 | 0.14 | 1/4 (PANC-1) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15006.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.324×** | -13.8 | 2e-40 | 27/32 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.260×** | -11.7 | 4e-29 | 34/39 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.299×** | -10.4 | 3e-23 | 24/31 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.345×** | -8.9 | 1e-16 | 25/36 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.380×** | -8.4 | 6e-15 | 29/39 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.403×** | -7.9 | 4e-13 | 23/33 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.405×** | -7.5 | 4e-12 | 21/26 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -7.5 | 6e-12 | 20/33 (J82, C-33 A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.426×** | -7.4 | 1e-11 | 23/38 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.425×** | -7.0 | 1e-10 | 22/36 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.483×** | -6.3 | 2e-08 | 23/38 (LOX-IMVI, C-33 A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.489×** | -6.2 | 3e-08 | 23/39 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.492×** | -6.1 | 4e-08 | 17/38 (NCI-H23, C-33 A, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.528×** | -5.5 | 1e-06 | 21/33 (C-33 A, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.529×** | -5.5 | 2e-06 | 21/38 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -5.3 | 5e-06 | 22/38 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -5.2 | 5e-06 | 19/39 (C-33 A, J82, …) | two highest doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 28.8 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0167× (z -29.6) |
| [[J82 (line)]] | alt | 16.5 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0658× (z -13.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.179× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 8.79 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0225× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0469× (z -24.8) |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.106× (z -12.0) |
| [[PANC-1 (line)]] | alt | 8.69 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 6.34 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0389× (z -11.1) |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0712× (z -10.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 6.17 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0485× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 6.78 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 8.22 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0647× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 4.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0686× (z -9.5) |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.3) |
| [[A-172 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD9]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[KDM2B]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TLE6]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[DIXDC1]] | +0.53 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[NDUFB8]] | +0.52 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[DHRS13]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[LINC03047]] | +0.51 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ZNF292]] | +0.51 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[PIAS2]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[PANTR1]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[WDR54]] | +0.50 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[POM121C]] | +0.50 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PDK3]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF3]] | -0.47 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[XYLT1]] | -0.41 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[TMBIM1]] | -0.41 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[ZBTB7C]] | -0.40 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | SMAD9 activity raises KDM2B-DT's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without SMAD9 | 0.018 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[ZSWIM5]] | B | ZSWIM5 activity raises KDM2B-DT's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without ZSWIM5 | 0.083 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent |
| [[EFR3B]] | B | EFR3B activity raises KDM2B-DT's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 2.14× lower at baseline in the lines without EFR3B | 0.089 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 19, C 1. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B]] | B | KDM2B-DT activity raises KDM2B's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without KDM2B-DT | 0.034 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[GPR155]] | B | KDM2B-DT activity raises GPR155's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without KDM2B-DT | 0.039 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[CTDSPL2]] | B | KDM2B-DT activity raises CTDSPL2's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.18× lower at baseline in the lines without KDM2B-DT | 0.041 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[EFCAB3P1]] | B | KDM2B-DT activity raises EFCAB3P1's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without KDM2B-DT | 0.048 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[INHA]] | B | KDM2B-DT activity raises INHA's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without KDM2B-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[PEX3]] | B | KDM2B-DT activity raises PEX3's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without KDM2B-DT | 0.064 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[TFB1M]] | B | KDM2B-DT activity raises TFB1M's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.00× lower at baseline in the lines without KDM2B-DT | 0.066 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[GHR]] | B | KDM2B-DT activity raises GHR's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 4.05× lower at baseline in the lines without KDM2B-DT | 0.066 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[NOG]] | B | KDM2B-DT activity raises NOG's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 3.28× lower at baseline in the lines without KDM2B-DT | 0.067 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[WDR54]] | B | KDM2B-DT activity raises WDR54's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.05× lower at baseline in the lines without KDM2B-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[DIXDC1]] | B | KDM2B-DT activity raises DIXDC1's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without KDM2B-DT | 0.073 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[GPR146]] | B | KDM2B-DT activity raises GPR146's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without KDM2B-DT | 0.076 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.9, -19.9); signed map (-32.8, 32.4). **Vector** length 69.9, 13.1% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +2.7 | -3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.2 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +3.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -7.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | KDM2B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q24.31 — chr12:121,580,792-121,593,504 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53287) · Entrez [101928346](https://www.ncbi.nlm.nih.gov/gene/101928346) · Ensembl [ENSG00000256742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256742)

## Data

Gene col 15006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15006); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15006]; `tensor/DDL_lfc|DDL_z.npy` [15006]; `embed/gene_vectors.npy` [15006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15006 or target_col == 15006). Every well: [[KDM2B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM2B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
