---
symbol: "PHOSPHO2"
type: "gene"
col: 6870
ensembl_id: "ENSG00000144362"
name: "phosphatase, orphan 2"
location: "2q31.1"
module: 25
arm: "+"
pooled_cpm: 6.09
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PHOSPHO2

*phosphatase, orphan 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +10.5, q 4e-23, up in 5 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.39× (z +4.1, q 0.004, up in 4 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 15.4×, BT-474 9.58×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 17.4×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 17.0×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.562× (z -6.7, q 8e-09, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUNDC2]] (+0.59, fdr 3e-05), [[CTC1]] (+0.58, fdr 8e-05), [[RWDD4]] (+0.56, fdr 1e-04); moves opposite to [[ZSWIM6]] (-0.54, fdr 3e-05), [[LUZP1]] (-0.53, fdr 3e-05), [[CLEC16A]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MSX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6870.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 15.4×, BT-474 9.58×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 17.4×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 17.0×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +10.5 | 4e-23 | 5/9 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.50×** | +7.1 | 3e-10 | 22/46 (SW480, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.9 | 1e-09 | 16/29 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.9 | 5e-07 | 18/32 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +5.6 | 2e-06 | 5/17 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.004 | 4/46 (NCI-H23, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.37×** | +3.9 | 0.007 | 10/44 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.009 | 8/47 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.11 | 8/38 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 1.31× | +3.0 | 0.13 | 4/47 (NCI-H23, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.562×** | -6.7 | 8e-09 | 23/43 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.582×** | -6.7 | 8e-09 | 22/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.605×** | -6.0 | 5e-07 | 21/45 (NCI-H1792, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -5.9 | 7e-07 | 20/46 (CFPAC-1, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -5.6 | 3e-06 | 17/44 (NCI-H1792, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.663×** | -5.1 | 4e-05 | 17/40 (SW480, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.672×** | -4.9 | 8e-05 | 15/47 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.623×** | -4.2 | 0.002 | 12/36 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.707×** | -4.1 | 0.003 | 10/43 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.740×** | -3.7 | 0.012 | 14/44 (C32, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -3.4 | 0.030 | 8/38 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.031 | 10/48 (A-427, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.752×** | -3.4 | 0.032 | 16/36 (PANC-1, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.601×** | -3.3 | 0.042 | 13/24 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fulvestrant (drug)]] 0.5 µM |  | **0.768×** | -3.2 | 0.044 | 9/44 (HepG2/C3A, LS 180, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.780×** | -3.1 | 0.069 | 9/46 (H4, RKO, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.776×** | -3.0 | 0.081 | 9/47 (HT-29, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 14.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.4× (z +11.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 7.17 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.58× (z +8.6) ⚠ toxic; transcription drop | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0871× (z -9.3) |
| [[PANC-1 (line)]] | alt | 6.27 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0747× (z -15.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 6.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0627× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 5.72 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.121× (z -9.6) |
| [[KATO III (line)]] | alt | 4.24 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0937× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 6.71 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0771× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 3.91 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0653× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 3.28 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0704× (z -9.6) |
| [[SHP-77 (line)]] | alt | 8.20 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.110× (z -8.7) |
| [[SW480 (line)]] | alt | 7.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUNDC2]] | +0.59 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CTC1]] | +0.58 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[RWDD4]] | +0.56 | +0.33 / +0.66 | both halves | 1e-04 |  |
| [[TMEM237]] | +0.55 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[MANEA]] | +0.55 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[ZNF852]] | +0.53 | +0.37 / +0.58 | both halves | 7e-05 |  |
| [[CA5BP1-1]] | +0.52 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[DPY19L4]] | +0.52 | +0.19 / +0.59 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CISD2]] | +0.51 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[LYRM7]] | +0.51 | +0.32 / +0.57 | both halves | 1e-04 |  |
| [[TIGD1]] | +0.51 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[KLHL23]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 | STRING 635; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RCAN3]] | +0.50 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[EIF2D]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[LUZP1]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CLEC16A]] | -0.51 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[UCKL1-AS1]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SETX]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[MSX1]] | -0.50 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[C11orf91]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TUT7]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[POMP]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ADRM1]] | -0.48 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[FAM32A]] | -0.48 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[RAB35]] | -0.48 | -0.48 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX1]] | B | MSX1 activity raises PHOSPHO2's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without MSX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises PHOSPHO2's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without ZNF594-DT | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.2, -19.2); signed map (-25.9, -34.1). **Vector** length 54.3, 6.79% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | -0.6 |
|  | [[Afatinib (drug)]] 5 µM |  | +0.9 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +0.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.3 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphatase, orphan 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,694,454-169,701,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22679 |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCD6](https://www.uniprot.org/uniprotkb/Q8TCD6) (Pyridoxal phosphate phosphatase PHOSPHO2):

> Phosphatase that has high activity toward pyridoxal 5'-phosphate (PLP). Also active at much lower level toward pyrophosphate, phosphoethanolamine (PEA), phosphocholine (PCho), phospho-l-tyrosine, fructose-6-phosphate, p-nitrophenyl phosphate, and h-glycerophosphate.

**Summary**, from NCBI Gene [493911](https://www.ncbi.nlm.nih.gov/gene/493911):

> Predicted to enable phosphatase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28316) · Entrez [493911](https://www.ncbi.nlm.nih.gov/gene/493911) · UniProt [Q8TCD6](https://www.uniprot.org/uniprotkb/Q8TCD6) · Ensembl [ENSG00000144362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144362)

## Data

Gene col 6870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6870); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6870]; `tensor/DDL_lfc|DDL_z.npy` [6870]; `embed/gene_vectors.npy` [6870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6870 or target_col == 6870). Every well: [[PHOSPHO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHOSPHO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
