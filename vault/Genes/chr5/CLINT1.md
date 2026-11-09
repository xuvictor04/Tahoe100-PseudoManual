---
symbol: "CLINT1"
type: "gene"
col: 3444
ensembl_id: "ENSG00000113282"
name: "clathrin interactor 1"
location: "5q33.3"
module: 56
arm: "+"
pooled_cpm: 252.37
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# CLINT1

*clathrin interactor 1* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.57× (z +9.2, q 2e-17, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.595× (z -12.8, q 5e-35, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRC1]] (+0.79, fdr 7e-06), [[SEC24D]] (+0.76, fdr 7e-06), [[GFPT1]] (+0.74, fdr 7e-06); moves opposite to [[RESF1]] (-0.56, fdr 1e-05), [[ZNF700]] (-0.55, fdr 1e-04), [[PNRC2]] (-0.55, fdr 3e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +9.2 | 2e-17 | 45/49 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +8.0 | 4e-13 | 39/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +7.3 | 5e-11 | 38/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.1 | 2e-07 | 36/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.7 | 1e-06 | 33/47 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.9 | 7e-05 | 35/45 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 7e-05 | 30/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +4.5 | 4e-04 | 26/48 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.1 | 0.003 | 26/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +3.9 | 0.006 | 24/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.042 | 26/49 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.061 | 26/48 (LoVo, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -12.8 | 5e-35 | 45/49 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -8.9 | 2e-16 | 39/47 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -8.4 | 8e-15 | 35/44 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -6.0 | 2e-07 | 33/49 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.714×** | -5.8 | 7e-07 | 30/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -5.2 | 2e-05 | 29/48 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -5.0 | 4e-05 | 28/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -4.4 | 6e-04 | 31/50 (KATO III, COLO 205, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.797×** | -4.2 | 0.001 | 29/48 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.832×** | -3.4 | 0.033 | 23/48 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.12 | 19/49 (NCI-H2122, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 322 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 361 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -19.5) |
| [[NCI-H2347 (line)]] | alt | 399 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 419 | 3 (1 ⚠) | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.60× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 197 | 3 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.44× (z +12.7) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 3.35× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 244 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.73× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -10.4) |
| [[PANC-1 (line)]] | alt | 193 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +10.9) | — |
| [[A-427 (line)]] | wt | 184 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.09× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.515× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 410 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 301 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -15.5) |
| [[HS-578T (line)]] | alt | 416 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.9) |
| [[RKO (line)]] | wt | 199 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.40× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.1) |
| [[SW480 (line)]] | alt | 168 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.74× (z +8.8) | — |
| [[A-172 (line)]] | wt | 226 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -13.1) |
| [[COLO 205 (line)]] | alt | 222 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.5) |
| [[LoVo (line)]] | wt | 362 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 224 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.68× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -13.8) |
| [[SW 900 (line)]] | alt | 338 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.7) |
| [[SW1417 (line)]] | alt | 238 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -11.3) |
| [[A549 (line)]] | wt | 294 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.1) |
| [[BT-474 (line)]] | alt | 182 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -14.2) |
| [[C-33 A (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -11.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 241 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -11.6) |
| [[H4 (line)]] | wt | 329 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -9.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 193 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -10.1) |
| [[HOP62 (line)]] | alt | 231 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.12× (z +8.6) ⚠ toxic | — |
| [[HT-29 (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.509× (z -8.9) ⚠ toxic |
| [[J82 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.95× (z +9.8) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 208 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.79× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 240 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 224 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.05 µM 0.0584× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.477× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.7) |
| [[AN3 CA (line)]] | alt | 266 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 293 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 266 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 282 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 159 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 282 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC1]] | +0.79 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.76 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.74 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[NUS1]] | +0.73 | +0.79 / +0.57 | both halves | 1e-05 |  |
| [[GORASP2]] | +0.73 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[COPB1]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[COG6]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[COPA]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.71 | +0.74 / +0.52 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis |
| [[SEC63]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.70 | +0.75 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RESF1]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZNF700]] | -0.55 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[PNRC2]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CLINT1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TBC1D8B]] | B | TBC1D8B activity raises CLINT1's level | lines that do not express TBC1D8B (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without TBC1D8B | 0.089 | ⚠ within organs, on part of the lines; also absent: AHR, MYO1B, RND3; its own permutation p |
| [[TOP2B]] | B | TOP2B activity raises CLINT1's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, -32.8); signed map (-51.6, 9.8). **Vector** length 125, 47.9% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.63 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.63 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.63 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | -8.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.4 | +4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | -0.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.4 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.5 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.3 | +4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.5 | -0.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | clathrin interactor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,785,743-157,859,145 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ENTH, KIAA0171, EPNR, CLINT |
| Reactome | 7 pathways, smallest: Assembly and Release of Dengue Virus Virions; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14677](https://www.uniprot.org/uniprotkb/Q14677) (Clathrin interactor 1):

> Binds to membranes enriched in phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2). May have a role in transport via clathrin-coated vesicles from the trans-Golgi network to endosomes. Stimulates clathrin assembly.

**Summary**, from NCBI Gene [9685](https://www.ncbi.nlm.nih.gov/gene/9685):

> This gene encodes a protein with similarity to the epsin family of endocytic adapter proteins. The encoded protein interacts with clathrin, the adapter protein AP-1 and phosphoinositides. This protein may be involved in the formation of clathrin coated vesicles and trafficking between the trans-Golgi network and endosomes. Mutations in this gene are associated with a susceptibility to schizophrenia and psychotic disorders. Alternate splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:23186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23186) · Entrez [9685](https://www.ncbi.nlm.nih.gov/gene/9685) · UniProt [Q14677](https://www.uniprot.org/uniprotkb/Q14677) · Ensembl [ENSG00000113282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113282)

## Data

Gene col 3444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3444); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3444]; `tensor/DDL_lfc|DDL_z.npy` [3444]; `embed/gene_vectors.npy` [3444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3444 or target_col == 3444). Every well: [[CLINT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLINT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
