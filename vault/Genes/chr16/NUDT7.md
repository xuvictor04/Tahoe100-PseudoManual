---
symbol: "NUDT7"
type: "gene"
col: 6460
ensembl_id: "ENSG00000140876"
name: "nudix hydrolase 7"
location: "16q23.1"
module: 45
arm: "+"
pooled_cpm: 2.1
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# NUDT7

*nudix hydrolase 7* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.93× (z +8.3, q 6e-14, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.59× (z +5.3, q 2e-05, up in 10 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.341× (z -8.6, q 3e-15, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53TG1]] (+0.60, fdr 1e-05), [[C1orf115]] (+0.60, fdr 1e-05), [[PRSS16]] (+0.59, fdr 3e-05); moves opposite to [[ACAD9]] (-0.51, fdr 2e-04), [[GLYR1]] (-0.45, fdr 4e-04), [[MCM3AP]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[C2orf68]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +8.3 | 6e-14 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +6.1 | 4e-07 | 1/1 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +5.4 | 1e-05 | 2/9 (NCI-H2030, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +5.3 | 2e-05 | 10/40 (LS 180, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +5.2 | 2e-05 | 16/41 (SW480, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +5.2 | 2e-05 | 13/36 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.7 | 0.015 | 2/6 (NCI-H1573, NCI-H2030) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +3.7 | 0.018 | 3/41 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.035 | 4/38 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.051 | 11/42 (KATO III, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.2 | 0.064 | 3/13 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.073 | 8/29 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.079 | 4/34 (KATO III, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.082 | 4/38 (NCI-H2030, A549, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.082 | 11/40 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.341×** | -8.6 | 3e-15 | 28/43 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.388×** | -7.6 | 8e-12 | 23/36 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.438×** | -6.6 | 6e-09 | 16/32 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.548×** | -4.8 | 2e-04 | 17/40 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -4.7 | 3e-04 | 9/16 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.629×** | -3.7 | 0.017 | 11/28 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.721×** | -3.7 | 0.017 | 19/32 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -3.6 | 0.020 | 13/31 (LS 180, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -3.5 | 0.031 | 10/30 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.652×** | -3.4 | 0.031 | 18/38 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.740×** | -3.4 | 0.031 | 9/38 (NCI-H1573, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -3.3 | 0.045 | 12/36 (KATO III, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.633×** | -3.2 | 0.067 | 12/32 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -3.1 | 0.092 | 7/22 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 4.45 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0946× (z -11.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0517× (z -10.4) |
| [[A-427 (line)]] | wt | 8.75 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.175× (z -8.5) |
| [[PANC-1 (line)]] | alt | 2.16 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -11.9) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0840× (z -8.5) |
| [[KATO III (line)]] | alt | 4.53 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0460× (z -11.8) |
| [[LS 180 (line)]] | wt | 3.01 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0636× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 4.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0973× (z -8.8) |
| [[SNU-423 (line)]] | alt | 3.69 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0533× (z -8.9) |
| [[A-172 (line)]] | wt | 0.840 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.550 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.927 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53TG1]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[C1orf115]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PRSS16]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[DOC2A]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ID2-AS1]] | +0.56 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[DUSP19]] | +0.54 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LYRM9]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RYBP]] | +0.54 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[ACBD4]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 | pathway: Fatty acid metabolism |
| [[CLN8-AS1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[FLVCR1-DT]] | +0.54 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[SYT9-AS1]] | +0.53 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAD9]] | -0.51 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[GLYR1]] | -0.45 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[MCM3AP]] | -0.44 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[FAM120B]] | -0.44 | -0.39 / -0.24 | both halves | 5e-04 |  |
| [[LIN52]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[MFN2]] | -0.43 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[BRD9]] | -0.43 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[ANKMY1]] | -0.43 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[ING5]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises NUDT7's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without RASGEF1A | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises NUDT7's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without SYT9-AS1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HENMT1]] | B | HENMT1 activity raises NUDT7's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without HENMT1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[HES2]] | B | HES2 activity raises NUDT7's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.32× lower at baseline in the lines without HES2 | 0.098 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf68]] | C | NUDT7 activity raises C2orf68's level | lines that do not express NUDT7 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without NUDT7 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: PKN3, EZR, CORO2A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-0.8, 32.9); signed map (41.1, -9.6). **Vector** length 35.4, 3.89% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -1.4 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.8 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.7 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:77,722,492-77,742,260 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 5 pathways, smallest: Peroxisomal lipid metabolism; Peroxisomal protein import; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C024](https://www.uniprot.org/uniprotkb/P0C024) (Peroxisomal coenzyme A diphosphatase NUDT7):

> Fatty acyl-coenzyme A (CoA) diphosphatase that hydrolyzes fatty acyl-CoA to yield acyl-4'-phosphopantetheine and adenosine 3',5'-bisphosphate (By similarity). Cleaves CoA, CoA esters and oxidized CoA with similar efficiencies (By similarity). Preferentially hydrolyzes medium-chain acyl-CoAs and bile acid-CoAs (By similarity). Has no activity toward NDP-sugars, CDP-alcohols, (deoxy)nucleoside 5'-triphosphates, nucleoside 5'-di or monophosphates, diadenosine polyphosphates, NAD, NADH, NADP, NADPH …

**Summary**, from NCBI Gene [283927](https://www.ncbi.nlm.nih.gov/gene/283927):

> The protein encoded by this gene is a member of the Nudix hydrolase family. Nudix hydrolases eliminate potentially toxic nucleotide metabolites from the cell and regulate the concentrations and availability of many different nucleotide substrates, cofactors, and signaling molecules. Alternatively spliced transcript variants encoding multiple isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:8054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8054) · Entrez [283927](https://www.ncbi.nlm.nih.gov/gene/283927) · UniProt [P0C024](https://www.uniprot.org/uniprotkb/P0C024) · Ensembl [ENSG00000140876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140876)

## Data

Gene col 6460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6460); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6460]; `tensor/DDL_lfc|DDL_z.npy` [6460]; `embed/gene_vectors.npy` [6460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6460 or target_col == 6460). Every well: [[NUDT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
