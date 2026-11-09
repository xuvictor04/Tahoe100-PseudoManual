---
symbol: "POU5F1"
type: "gene"
col: 12885
ensembl_id: "ENSG00000204531"
name: "POU class 5 homeobox 1"
location: "6p21.33"
module: 8
arm: "+"
pooled_cpm: 23.81
n_lines_expressing: 23
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 23
direction_downstream: 31
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# POU5F1

*POU class 5 homeobox 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.17× (z +10.6, q 2e-23, up in 11 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +9.6, q 2e-19, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.420× (z -12.8, q 6e-35, down in 20 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAVCR1]] (+0.72, fdr 1e-05), [[TIMD4]] (+0.66, fdr 1e-05), [[RHEX]] (+0.66, fdr 7e-06); moves opposite to [[KIAA1549L]] (-0.48, fdr 3e-05), [[WDFY2]] (-0.48, fdr 1e-04), [[ABTB3]] (-0.46, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[ALDH3B1]] → it (grade B ⚠); 31 go from it, the strongest it → [[ZNF496]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +10.6 | 2e-23 | 11/18 (A549, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +9.6 | 2e-19 | 10/21 (HS-578T, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.9 | 1e-16 | 2/17 (KATO III, J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +8.1 | 1e-13 | 2/19 (AsPC-1, Panc 03.27) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.0 | 4e-10 | 3/21 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.7 | 3e-09 | 7/21 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +6.6 | 4e-09 | 5/21 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.1 | 3e-05 | 3/13 (SNU-423, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +4.6 | 3e-04 | 0/21 | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.002 | 6/21 (KATO III, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 12/21 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.004 | 10/21 (AsPC-1, HepG2/C3A, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.014 | 4/21 (AsPC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.022 | 9/21 (HS-578T, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.036 | 8/21 (AsPC-1, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.041 | 11/21 (A549, CFPAC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.041 | 12/21 (HepG2/C3A, CFPAC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.043 | 7/21 (AsPC-1, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.043 | 8/21 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.051 | 9/21 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.065 | 3/21 (A498, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.420×** | -12.8 | 6e-35 | 20/21 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.432×** | -12.4 | 6e-33 | 20/21 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.443×** | -12.0 | 5e-31 | 21/21 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.615×** | -7.2 | 1e-10 | 17/21 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -4.9 | 1e-04 | 15/21 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -4.9 | 1e-04 | 14/21 (A498, HT-29, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.726×** | -4.7 | 2e-04 | 1/21 (NCI-H1792) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.729×** | -4.7 | 2e-04 | 13/21 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.729×** | -4.4 | 7e-04 | 2/21 (Panc 03.27, hTERT-HPNE) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -4.0 | 0.003 | 9/21 (A549, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.749×** | -4.0 | 0.003 | 17/21 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.769×** | -3.9 | 0.005 | 12/21 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.632×** | -3.5 | 0.017 | 5/21 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.793×** | -3.2 | 0.048 | 3/21 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.807×** | -3.2 | 0.058 | 1/21 (KATO III) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 52.8 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0717× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 93.1 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -15.2) |
| [[A498 (line)]] | wt | 65.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 38.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 207 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0792× (z -18.4) |
| [[LoVo (line)]] | wt | 58.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0782× (z -17.0) |
| [[KATO III (line)]] | alt | 18.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 76.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -10.9) |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.131× (z -9.9) |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -10.0) |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -10.2) |
| [[LS 180 (line)]] | wt | 29.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -13.0) |
| [[HS-578T (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.8) | — |
| [[A-172 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAVCR1]] | +0.72 | +0.69 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[TIMD4]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[RHEX]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[FGA]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[TM4SF4]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PON3]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[FXYD2]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[TRIM31]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DSCAML1]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PLAC8]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ABCC6]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1549L]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[WDFY2]] | -0.48 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[ABTB3]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[S100A16]] | -0.45 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[ELOVL1]] | -0.45 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[SH3KBP1]] | -0.45 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[PLSCR3]] | -0.44 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[ZNF496]] | -0.44 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[PWWP3A]] | -0.44 | -0.41 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 1, C 22. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH3B1]] | B | ALDH3B1 activity raises POU5F1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 3.46× lower at baseline in the lines without ALDH3B1 | 0.084 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[TIMD4]] | C | TIMD4 activity raises POU5F1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 7.78× lower at baseline in the lines without TIMD4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[APOL1]] | C | APOL1 activity raises POU5F1's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 3.58× lower at baseline in the lines without APOL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises POU5F1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 5.92× lower at baseline in the lines without HAVCR1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises POU5F1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 4.25× lower at baseline in the lines without IGFBP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[FGA]] | C | FGA activity raises POU5F1's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.97× lower at baseline in the lines without FGA | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises POU5F1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.29× lower at baseline in the lines without TRIM31 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[SLCO1B1]] | C | SLCO1B1 activity raises POU5F1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 2.43× lower at baseline in the lines without SLCO1B1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |
| [[TM4SF4]] | C | TM4SF4 activity raises POU5F1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 5.57× lower at baseline in the lines without TM4SF4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[ARSL]] | C | ARSL activity raises POU5F1's level | lines that do not express ARSL (26) vs lines expressing it (24) | 3.09× lower at baseline in the lines without ARSL | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4; co-absent with the target |
| [[PLA2R1]] | C | PLA2R1 activity raises POU5F1's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without PLA2R1 | 0.027 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18; co-absent with the target |
| [[SLCO1B3-SLCO1B7]] | C | SLCO1B3-SLCO1B7 activity raises POU5F1's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 7, C 24. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF496]] | B | POU5F1 activity lowers ZNF496's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.65× higher at baseline in the lines without POU5F1 | 0.015 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[EPS8]] | B | POU5F1 activity raises EPS8's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.48× lower at baseline in the lines without POU5F1 | 0.034 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[ANXA4]] | B | POU5F1 activity raises ANXA4's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.70× lower at baseline in the lines without POU5F1 | 0.042 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[SLC44A3-AS1]] | B | POU5F1 activity raises SLC44A3-AS1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without POU5F1 | 0.049 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[SPATA6L]] | B | POU5F1 activity raises SPATA6L's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.64× lower at baseline in the lines without POU5F1 | 0.060 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[SLC44A3]] | B | POU5F1 activity raises SLC44A3's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without POU5F1 | 0.087 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[ALDH3B1]] | B | POU5F1 activity raises ALDH3B1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without POU5F1 | 0.089 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[APOL1]] | C | POU5F1 activity raises APOL1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 4.20× lower at baseline in the lines without POU5F1 | 0.003 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[UGT1A6]] | C | POU5F1 activity raises UGT1A6's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 4.67× lower at baseline in the lines without POU5F1 | 0.008 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[IGFBP1]] | C | POU5F1 activity raises IGFBP1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 3.19× lower at baseline in the lines without POU5F1 | 0.008 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[PLA2R1]] | C | POU5F1 activity raises PLA2R1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 3.23× lower at baseline in the lines without POU5F1 | 0.010 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[SLCO1B1]] | C | POU5F1 activity raises SLCO1B1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without POU5F1 | 0.024 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, 44.3); signed map (52.0, 26.9). **Vector** length 76.9, 23.8% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +6.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -12.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | -12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.8 | -12.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -4.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | POU class 5 homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,164,337-31,180,731 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OCT3, Oct4, MGC22487, OCT-4, Oct3/4; previously OTF3 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Reactome | 9 pathways, smallest: Formation of the anterior neural plate; POU5F1 (OCT4), SOX2, NANOG repress genes related to differentiation; POU5F1 (OCT4), SOX2, NANOG activate genes related to proliferation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01860](https://www.uniprot.org/uniprotkb/Q01860) (POU domain, class 5, transcription factor 1):

> Transcription factor that binds to the octamer motif (5'-ATTTGCAT-3'). Forms a trimeric complex with SOX2 or SOX15 on DNA and controls the expression of a number of genes involved in embryonic development such as YES1, FGF4, UTF1 and ZFP206. Critical for early embryogenesis and for embryonic stem cell pluripotency.

**Summary**, from NCBI Gene [5460](https://www.ncbi.nlm.nih.gov/gene/5460):

> This gene encodes a transcription factor containing a POU homeodomain that plays a key role in embryonic development and stem cell pluripotency. Aberrant expression of this gene in adult tissues is associated with tumorigenesis. This gene can participate in a translocation with the Ewing's sarcoma gene on chromosome 21, which also leads to tumor formation. Alternative splicing, as well as usage of alternative AUG and non-AUG translation initiation codons, results in multiple isoforms. One of …

**Accessions** — [HGNC:9221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9221) · Entrez [5460](https://www.ncbi.nlm.nih.gov/gene/5460) · UniProt [Q01860](https://www.uniprot.org/uniprotkb/Q01860) · Ensembl [ENSG00000204531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204531)

## Data

Gene col 12885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12885); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12885]; `tensor/DDL_lfc|DDL_z.npy` [12885]; `embed/gene_vectors.npy` [12885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12885 or target_col == 12885). Every well: [[POU5F1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU5F1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
