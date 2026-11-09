---
symbol: "RTN4R"
type: "gene"
col: 470
ensembl_id: "ENSG00000040608"
name: "reticulon 4 receptor"
location: "22q11.21"
module: 2
arm: "+"
pooled_cpm: 2.56
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RTN4R

*reticulon 4 receptor* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.46× (z +7.3, q 2e-10, up in 20 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.469× (z -6.1, q 6e-07, down in 21 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HT-29 0.0931×, HEC-1-A 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0572×); [[Megestrol (drug)]] 0.05 µM in 1 line (AsPC-1 0.0434×); [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 0.0917×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMS3]] (+0.65, fdr 1e-05), [[STK32C]] (+0.64, fdr 1e-05), [[CORO7]] (+0.64, fdr 1e-05); moves opposite to [[USP40]] (-0.62, fdr 1e-05), [[DECR1]] (-0.62, fdr 7e-05), [[MCTS1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[JAG2]] → it (grade B ⚠); 10 go from it, the strongest it → [[LDLRAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +7.3 | 2e-10 | 20/36 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +6.6 | 1e-08 | 19/38 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.4 | 1e-05 | 9/16 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +5.2 | 2e-05 | 16/37 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +5.1 | 3e-05 | 11/42 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.003 | 9/37 (HT-29, A549, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.1 | 0.003 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.020 | 5/35 (HEC-1-A, HS-578T, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.023 | 8/26 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.3 | 0.056 | 4/19 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.069 | 4/22 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.069 | 3/39 (PANC-1, LoVo, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.070 | 8/35 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.070 | 7/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.47×** | +3.1 | 0.073 | 5/38 (LoVo, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.073 | 6/25 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.094 | 8/30 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 470.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HT-29 0.0931×, HEC-1-A 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0572×); [[Megestrol (drug)]] 0.05 µM in 1 line (AsPC-1 0.0434×); [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 0.0917×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.469×** | -6.1 | 6e-07 | 21/38 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.566×** | -4.4 | 0.003 | 12/34 (LoVo, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~6% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.39 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0917× (z -8.9) |
| [[A-172 (line)]] | wt | 4.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0572× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 3.03 | 0 | 1 | — | [[Megestrol (drug)]] 0.05 µM 0.0434× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 6.32 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 9.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0931× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.699 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[STK32C]] | +0.64 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CORO7]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CROCCP3]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TNK2]] | +0.63 | +0.58 / +0.54 | both halves | 1e-05 | same gene group |
| [[JAG2]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[IGSF8]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CABLES2]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[OGG1]] | +0.62 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SH2B2]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 | same gene group |
| [[ANKRD9]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[MPND]] | +0.60 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP40]] | -0.62 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[DECR1]] | -0.62 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[MCTS1]] | -0.61 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TBCK]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[MTREX]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[AFG1L]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RGS5]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CLHC1]] | -0.55 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ZSCAN30]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MRPS7]] | -0.55 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[C11orf58]] | -0.55 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | JAG2 activity raises RTN4R's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without JAG2 | 0.032 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[IGSF3]] | B | IGSF3 activity raises RTN4R's level | lines that do not express IGSF3 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without IGSF3 | 0.046 | ⚠ within organs, on part of the lines; also absent: FARP1, KCNIP3 |
| [[BMP8B]] | B | BMP8B activity raises RTN4R's level | lines that do not express BMP8B (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without BMP8B | 0.067 | ⚠ within organs, on part of the lines; also absent: PBX4, SPECC1, CTSV; maybe low, not absent; its own permutation p |
| [[PRKCZ]] | B | PRKCZ activity raises RTN4R's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without PRKCZ | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAP1]] | C | RTN4R activity raises LDLRAP1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without RTN4R | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[KNDC1]] | C | RTN4R activity raises KNDC1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.82× lower at baseline in the lines without RTN4R | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[PLCG2]] | C | RTN4R activity raises PLCG2's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 3.97× lower at baseline in the lines without RTN4R | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[MCPH1]] | C | RTN4R activity lowers MCPH1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 1.47× higher at baseline in the lines without RTN4R | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[MCTS1]] | C | RTN4R activity raises MCTS1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without RTN4R | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[TNK2]] | C | RTN4R activity raises TNK2's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without RTN4R | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[PBX4]] | C | RTN4R activity raises PBX4's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without RTN4R | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[MLXIPL]] | C | RTN4R activity raises MLXIPL's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.62× lower at baseline in the lines without RTN4R | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[PRKCZ]] | C | RTN4R activity raises PRKCZ's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without RTN4R | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[IGSF3]] | C | RTN4R activity raises IGSF3's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 3.26× lower at baseline in the lines without RTN4R | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.1, -0.9); signed map (-43.8, -4.8). **Vector** length 55.4, 9.08% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +6.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 4 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,241,415-20,283,246 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NgR1, NgR, NOGOR |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Reticulon 4 receptor family |
| Reactome | 4 pathways, smallest: Axonal growth inhibition (RHOA activation); p75NTR regulates axonogenesis; p75 NTR receptor-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZR6](https://www.uniprot.org/uniprotkb/Q9BZR6) (Reticulon-4 receptor):

> Receptor for RTN4, OMG and MAG. Functions as a receptor for the sialylated gangliosides GT1b and GM1. Besides, functions as a receptor for chondroitin sulfate proteoglycans (By similarity). Can also bind heparin (By similarity). Intracellular signaling cascades are triggered via the coreceptor NGFR. Signaling mediates activation of Rho and downstream reorganization of the actin cytoskeleton. Mediates axonal growth inhibition. Plays a role in regulating axon regeneration and neuronal plasticity …

**Summary**, from NCBI Gene [65078](https://www.ncbi.nlm.nih.gov/gene/65078):

> This gene encodes the receptor for reticulon 4, oligodendrocyte myelin glycoprotein and myelin-associated glycoprotein. This receptor mediates axonal growth inhibition and may play a role in regulating axonal regeneration and plasticity in the adult central nervous system. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18601) · Entrez [65078](https://www.ncbi.nlm.nih.gov/gene/65078) · UniProt [Q9BZR6](https://www.uniprot.org/uniprotkb/Q9BZR6) · Ensembl [ENSG00000040608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040608)

## Data

Gene col 470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 470); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 470]; `tensor/DDL_lfc|DDL_z.npy` [470]; `embed/gene_vectors.npy` [470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 470 or target_col == 470). Every well: [[RTN4R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN4R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
