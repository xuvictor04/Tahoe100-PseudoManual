---
symbol: "DNAAF4"
type: "gene"
col: 14973
ensembl_id: "ENSG00000256061"
name: "dynein axonemal assembly factor 4"
location: "15q21.3"
module: 17
arm: "+"
pooled_cpm: 8.85
n_lines_expressing: 47
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DNAAF4

*dynein axonemal assembly factor 4* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.97× (z +19.0, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.449× (z -9.5, q 2e-18, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRAK1BP1]] (+0.70, fdr 7e-06), [[NPHP1]] (+0.70, fdr 7e-06), [[IFT22]] (+0.68, fdr 7e-06); moves opposite to [[KLHL29]] (-0.50, fdr 7e-05), [[AOC2]] (-0.49, fdr 5e-04), [[CCDC168]] (-0.47, fdr 8e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[THRB]] → it (grade B ⚠); 2 go from it, the strongest it → [[PKIG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.97×** | +19.0 | 0e+00 | 44/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.56×** | +16.5 | 0e+00 | 41/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.48×** | +14.8 | 0e+00 | 43/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +6.9 | 1e-09 | 29/44 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +6.4 | 1e-08 | 22/44 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.1 | 8e-08 | 18/32 (A549, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +6.0 | 1e-07 | 13/22 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +5.9 | 3e-07 | 23/40 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +5.8 | 6e-07 | 22/44 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.7 | 7e-07 | 20/30 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.43×** | +5.5 | 2e-06 | 18/45 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.0 | 3e-05 | 9/17 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 5e-05 | 17/44 (NCI-H1792, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 11/44 (NCI-H2030, SW480, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 9/44 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.011 | 12/42 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.011 | 12/44 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.027 | 9/44 (SW480, BT-474, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.032 | 8/44 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.063 | 4/44 (PANC-1, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.449×** | -9.5 | 2e-18 | 32/44 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.487×** | -7.8 | 2e-12 | 29/44 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -6.8 | 3e-09 | 24/42 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -6.1 | 2e-07 | 23/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.712×** | -4.0 | 0.007 | 16/44 (H4, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -3.8 | 0.013 | 18/34 (HS-578T, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.751×** | -3.4 | 0.059 | 10/44 (SHP-77, Panc 03.27, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.599× | -3.2 | 0.11 | 10/35 (A-172, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -3.0 | 0.14 | 14/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.767× | -3.0 | 0.14 | 7/44 (AN3 CA, NCI-H1573, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.19 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.59× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.208× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 9.63 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0565× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -8.6) |
| [[SW480 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -12.5) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.160× (z -9.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 10.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 8.18 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.38× (z +8.8) | — |
| [[LoVo (line)]] | wt | 10.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.86× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.138× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 12.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 7.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK1BP1]] | +0.70 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NPHP1]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[IFT22]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CSTPP1]] | +0.67 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[TBC1D19]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[BBS5]] | +0.62 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[TTC26]] | +0.61 | +0.44 / +0.64 | both halves | 3e-05 | same gene group |
| [[STX8]] | +0.61 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CEP162]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[VPS50]] | +0.60 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[WDR7]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TTC5]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL29]] | -0.50 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[AOC2]] | -0.49 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[CCDC168]] | -0.47 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[DGKH]] | -0.47 | -0.19 / -0.42 | ⚠ not reproduced | 9e-04 |  |
| [[RAB27A]] | -0.47 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | B | THRB activity lowers DNAAF4's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.52× higher at baseline in the lines without THRB | 0.048 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers DNAAF4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises DNAAF4's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.87× lower at baseline in the lines without ZNF594-DT | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[PKIG]] | C | PKIG activity raises DNAAF4's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.62× lower at baseline in the lines without PKIG | 0.018 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIG]] | C | DNAAF4 activity raises PKIG's level | lines that do not express DNAAF4 (3) vs lines expressing it (47) | 7.55× lower at baseline in the lines without DNAAF4 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; co-absent with the target; its own permutation p |
| [[CSTPP1]] | C | DNAAF4 activity raises CSTPP1's level | lines that do not express DNAAF4 (3) vs lines expressing it (47) | 2.12× lower at baseline in the lines without DNAAF4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.7, -0.1); signed map (-20.5, -18.9). **Vector** length 67.2, 11.6% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Assembly of the 9+0 primary cilium* (reactome, mean cos +0.51 to 11); *Intraflagellar transport* (reactome, mean cos +0.51 to 6); *Cilium Assembly* (reactome, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +19.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +14.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal assembly factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,410,525-55,508,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EKN1, FLJ37882, CILD25, pf23; previously DYX1C1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXU2](https://www.uniprot.org/uniprotkb/Q8WXU2) (Dynein axonemal assembly factor 4):

> Axonemal dynein assembly factor required for ciliary motility. Involved in neuronal migration during development of the cerebral neocortex. May regulate the stability and proteasomal degradation of the estrogen receptors that play an important role in neuronal differentiation, survival and plasticity.

**Summary**, from NCBI Gene [161582](https://www.ncbi.nlm.nih.gov/gene/161582):

> This gene encodes a tetratricopeptide repeat domain-containing protein. The encoded protein interacts with estrogen receptors and the heat shock proteins, Hsp70 and Hsp90. An homologous protein in rat has been shown to function in neuronal migration in the developing neocortex. A chromosomal translocation involving this gene is associated with a susceptibility to developmental dyslexia. Mutations in this gene are associated with deficits in reading and spelling. Alternative splicing results in …

**Accessions** — [HGNC:21493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21493) · Entrez [161582](https://www.ncbi.nlm.nih.gov/gene/161582) · UniProt [Q8WXU2](https://www.uniprot.org/uniprotkb/Q8WXU2) · Ensembl [ENSG00000256061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256061)

## Data

Gene col 14973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14973); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14973]; `tensor/DDL_lfc|DDL_z.npy` [14973]; `embed/gene_vectors.npy` [14973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14973 or target_col == 14973). Every well: [[DNAAF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAAF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
