---
symbol: "MIR99AHG"
type: "gene"
col: 13261
ensembl_id: "ENSG00000215386"
name: "mir-99a-let-7c cluster host gene"
location: "21q21.1"
module: 9
arm: "+"
pooled_cpm: 74.16
n_lines_expressing: 13
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 26
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MIR99AHG

*mir-99a-let-7c cluster host gene* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.84× (z +22.7, q 0e+00, up in 6 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.660× (z -4.9, q 5e-04, down in 9 of 11 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.694× (z -4.2, q 0.007, down in 5 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.0386×, A-427 0.151×, SNU-1 0.106×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-1 0.0460×, C-33 A 0.0877×, A-427 0.188×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.156×, SNU-1 0.144×, C-33 A 0.270×); [[Auranofin (drug)]] 5 µM in 3 lines (C-33 A 0.198×, A-427 0.276×, SNU-1 0.281×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.210×, SNU-1 0.268×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMRN1]] (+0.69, fdr 7e-06), [[UNC5C]] (+0.67, fdr 7e-06), [[EPHA5]] (+0.67, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ROBO2]] → it (grade C ⚠); 26 go from it, the strongest it → [[TENM3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.84×** | +22.7 | 0e+00 | 6/11 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +13.2 | 3e-37 | 1/11 (A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +11.0 | 5e-26 | 1/12 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +9.7 | 7e-20 | 7/11 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +8.5 | 2e-15 | 1/11 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +5.9 | 3e-07 | 9/11 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.64×** | +5.7 | 1e-06 | 8/11 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 2e-06 | 8/11 (NCI-H460, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.3 | 7e-06 | 2/11 (A-172, SNU-1) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +4.4 | 5e-04 | 7/10 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +4.4 | 5e-04 | 6/11 (A-172, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 6e-04 | 8/12 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.3 | 6e-04 | 2/11 (A-172, A498) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +4.3 | 6e-04 | 9/12 (NCI-H460, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 6e-04 | 4/11 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.002 | 10/11 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.002 | 7/11 (LOX-IMVI, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.003 | 3/11 (SNU-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13261.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.0386×, A-427 0.151×, SNU-1 0.106×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-1 0.0460×, C-33 A 0.0877×, A-427 0.188×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.156×, SNU-1 0.144×, C-33 A 0.270×); [[Auranofin (drug)]] 5 µM in 3 lines (C-33 A 0.198×, A-427 0.276×, SNU-1 0.281×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.210×, SNU-1 0.268×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.660×** | -4.9 | 5e-04 | 9/11 (A-427, C-33 A, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.694×** | -4.2 | 0.007 | 5/11 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.766× | -3.1 | 0.32 | 8/11 (A-427, C-33 A, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 729 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -18.7) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -14.6) |
| [[SNU-1 (line)]] | wt | 1,099 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0460× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -12.7) |
| [[C-33 A (line)]] | alt | 2,249 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0386× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -16.9) |
| [[A-172 (line)]] | wt | 19.8 | 4 (1 ⚠) | 0 | [[Ponatinib (drug)]] 5 µM 5.65× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.271× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 1,021 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 156 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0964× (z -18.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 72.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +13.5) | — |
| [[A498 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.38 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.64 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.34 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.03 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.78 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMRN1]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[UNC5C]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[EPHA5]] | +0.67 | +0.55 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[LINC01203]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[KCNH5]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[THSD7A]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ZFHX4]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TENM3]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[EPHA5-AS1]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GASK1B-AS1]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CADM2]] | +0.62 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ZFHX4-AS1]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO2]] | C | ROBO2 activity raises MIR99AHG's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.42× lower at baseline in the lines without ROBO2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises MIR99AHG's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 3.47× lower at baseline in the lines without TTTY10 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[UTY]] | C | UTY activity raises MIR99AHG's level | lines that do not express UTY (31) vs lines expressing it (19) | 3.52× lower at baseline in the lines without UTY | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises MIR99AHG's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 7.14× lower at baseline in the lines without KCNH5 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[TTTY14]] | C | TTTY14 activity raises MIR99AHG's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without TTTY14 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[SEMA3D]] | C | SEMA3D activity raises MIR99AHG's level | lines that do not express SEMA3D (31) vs lines expressing it (19) | 2.58× lower at baseline in the lines without SEMA3D | 0.0995 | ⚠ within organs, on part of the lines; also absent: COL3A1, HS3ST3A1, THY1; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 5, C 21. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3-AS1]] | B | MIR99AHG activity raises TENM3-AS1's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.32× lower at baseline in the lines without MIR99AHG | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[LMNTD1]] | B | MIR99AHG activity raises LMNTD1's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 1.34× lower at baseline in the lines without MIR99AHG | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[PCDH15]] | B | MIR99AHG activity raises PCDH15's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 2.73× lower at baseline in the lines without MIR99AHG | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[SAMD11]] | B | MIR99AHG activity raises SAMD11's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.27× lower at baseline in the lines without MIR99AHG | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[PCDH9]] | B | MIR99AHG activity raises PCDH9's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.44× lower at baseline in the lines without MIR99AHG | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[TTTY14]] | C | MIR99AHG activity raises TTTY14's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 4.47× lower at baseline in the lines without MIR99AHG | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[SEMA3D]] | C | MIR99AHG activity raises SEMA3D's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 4.96× lower at baseline in the lines without MIR99AHG | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[TENM3]] | C | MIR99AHG activity raises TENM3's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 5.18× lower at baseline in the lines without MIR99AHG | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[GASK1B-AS1]] | C | MIR99AHG activity raises GASK1B-AS1's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.70× lower at baseline in the lines without MIR99AHG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[UTY]] | C | MIR99AHG activity raises UTY's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 5.97× lower at baseline in the lines without MIR99AHG | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[GASK1B]] | C | MIR99AHG activity raises GASK1B's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 5.17× lower at baseline in the lines without MIR99AHG | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[NCAM2]] | C | MIR99AHG activity raises NCAM2's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 4.20× lower at baseline in the lines without MIR99AHG | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, 32.5); signed map (39.4, 35.1). **Vector** length 61.9, 25.1% of its response variance represented; |z| ≥ 3 in 389 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +22.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +5.9 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -1.2 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mir-99a-let-7c cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q21.1 — chr21:15,928,296-16,646,364 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MONC, DILA1; previously C21orf35, FLJ38295, C21orf34, LINC00478 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [388815](https://www.ncbi.nlm.nih.gov/gene/388815):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1274) · Entrez [388815](https://www.ncbi.nlm.nih.gov/gene/388815) · Ensembl [ENSG00000215386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215386)

## Data

Gene col 13261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13261); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13261]; `tensor/DDL_lfc|DDL_z.npy` [13261]; `embed/gene_vectors.npy` [13261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13261 or target_col == 13261). Every well: [[MIR99AHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR99AHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
