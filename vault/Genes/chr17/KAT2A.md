---
symbol: "KAT2A"
type: "gene"
col: 2991
ensembl_id: "ENSG00000108773"
name: "lysine acetyltransferase 2A"
location: "17q21.2"
module: 4
arm: "+"
pooled_cpm: 9.65
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KAT2A

*lysine acetyltransferase 2A* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.94× (z +15.1, q 0e+00, up in 15 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.57× (z +7.2, q 7e-11, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.609× (z -8.1, q 2e-13, down in 27 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.635× (z -4.3, q 0.006, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTBN2]] (+0.70, fdr 7e-06), [[MAPK12]] (+0.67, fdr 7e-06), [[PFAS]] (+0.66, fdr 7e-06); moves opposite to [[ING2]] (-0.59, fdr 1e-05), [[LGALS1]] (-0.58, fdr 1e-05), [[SELENOK]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LAMC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +15.1 | 0e+00 | 15/16 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.59×** | +14.6 | 0e+00 | 34/37 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +9.6 | 2e-19 | 22/23 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +7.2 | 7e-11 | 29/47 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +6.9 | 5e-10 | 29/47 (Panc 03.27, A498, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.7 | 1e-06 | 24/37 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.0 | 4e-05 | 8/48 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.8 | 1e-04 | 15/40 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 0.001 | 18/43 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.66×** | +4.1 | 0.002 | 12/46 (KATO III, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.9 | 0.004 | 13/27 (SK-MEL-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.8 | 0.008 | 17/39 (SW1417, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.008 | 17/46 (PANC-1, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.39×** | +3.7 | 0.009 | 11/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.042 | 7/38 (A-427, HCT15, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.054 | 4/43 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.609×** | -8.1 | 2e-13 | 27/44 (NCI-H23, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.635×** | -4.3 | 0.006 | 20/44 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.707×** | -3.9 | 0.020 | 16/46 (RKO, BT-474, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.731×** | -3.6 | 0.034 | 17/47 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -3.6 | 0.034 | 16/46 (HCT15, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.693×** | -3.4 | 0.054 | 10/47 (A-427, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.747×** | -3.4 | 0.057 | 18/46 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.765× | -3.1 | 0.12 | 12/47 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.46 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 15.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0572× (z -11.9) |
| [[A-172 (line)]] | wt | 9.02 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +8.9) ⚠ toxic; transcription drop | [[Tadalafil (drug)]] 5 µM 0.145× (z -8.9) |
| [[A-427 (line)]] | wt | 19.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -8.9) |
| [[A498 (line)]] | wt | 8.90 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.96× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 9.94 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0576× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.04× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.17× (z +11.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 6.95 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0691× (z -9.1) |
| [[A549 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN2]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MAPK12]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PFAS]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[SLC19A1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[WDR77]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | pathway: Chromatin modifying enzymes; STRING 422 |
| [[RPSA]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[IPO4]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[EME2]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[PFKM]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SLC5A6]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PLCG1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING2]] | -0.59 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[LGALS1]] | -0.58 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.57 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[KRTCAP2]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RSPH3]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MED19]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[BTG1]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RNF19A]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[PURA]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[GPX4]] | -0.53 | -0.37 / -0.56 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises KAT2A's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without LAMC3 | 0.007 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[NCS1]] | B | NCS1 activity raises KAT2A's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without NCS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[LRP3]] | B | LRP3 activity raises KAT2A's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without LRP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[DUXAP8]] | B | DUXAP8 activity raises KAT2A's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without DUXAP8 | 0.092 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.8, -28.6); signed map (-6.0, -44.8). **Vector** length 78.9, 15.3% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +6.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,113,111-42,121,367 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCN5, PCAF-b; previously GCN5L2 |
| Gene groups (HGNC) | Lysine acetyltransferases; ATAC complex; SAGA complex; GCN5 related N-acetyltransferases; Bromodomain containing |
| Hallmark sets | NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING |
| Reactome | 39 pathways, smallest: RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells; NOTCH4 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92830](https://www.uniprot.org/uniprotkb/Q92830) (Histone acetyltransferase KAT2A):

> Protein lysine acyltransferase that catalyzes acetylation of histone and non-histone proteins using acetyl-CoA. Also catalyzes acyl-CoA-dependent acylation of lysine residues in proteins using alternative acyl-CoA donors, including propionyl-CoA, butyryl-CoA, succinyl-CoA, glutaryl-CoA, crotonyl-CoA and lactoyl-CoA. Acts as a histone lysine succinyltransferase: catalyzes succinylation of histone H3 on 'Lys-79' (H3K79succ), with a maximum frequency around the transcription start sites of genes. …

**Summary**, from NCBI Gene [2648](https://www.ncbi.nlm.nih.gov/gene/2648):

> KAT2A, or GCN5, is a histone acetyltransferase (HAT) that functions primarily as a transcriptional activator. It also functions as a repressor of NF-kappa-B (see MIM 164011) by promoting ubiquitination of the NF-kappa-B subunit RELA (MIM 164014) in a HAT-independent manner (Mao et al., 2009 [PubMed 19339690]).[supplied by OMIM, Sep 2009]

**Accessions** — [HGNC:4201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4201) · Entrez [2648](https://www.ncbi.nlm.nih.gov/gene/2648) · UniProt [Q92830](https://www.uniprot.org/uniprotkb/Q92830) · Ensembl [ENSG00000108773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108773)

## Data

Gene col 2991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2991); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2991]; `tensor/DDL_lfc|DDL_z.npy` [2991]; `embed/gene_vectors.npy` [2991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2991 or target_col == 2991). Every well: [[KAT2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
