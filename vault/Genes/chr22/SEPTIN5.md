---
symbol: "SEPTIN5"
type: "gene"
col: 11568
ensembl_id: "ENSG00000184702"
name: "septin 5"
location: "22q11.21"
module: 132
arm: "+"
pooled_cpm: 3.33
n_lines_expressing: 38
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 15
direction_downstream: 26
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SEPTIN5

*septin 5* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.34× (z +8.1, q 2e-13, up in 10 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clofarabine (drug)]] 0.5 µM: 1.47× (z +3.7, q 0.028, up in 4 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -12.3, q 8e-32, down in 23 of 26 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.363× (z -9.6, q 2e-19, down in 23 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZD4]] (+0.73, fdr 7e-06), [[BRSK2]] (+0.70, fdr 1e-05), [[SHANK3]] (+0.69, fdr 7e-06); moves opposite to [[PTPRB]] (-0.47, fdr 3e-04), [[PCED1B]] (-0.47, fdr 6e-05), [[PDCD7]] (-0.45, fdr 5e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[PTPRB]] → it (grade B ⚠); 26 go from it, the strongest it → [[SMARCD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.1 | 2e-13 | 10/13 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +6.9 | 1e-09 | 3/6 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +6.8 | 2e-09 | 4/8 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clofarabine (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.028 | 4/34 (A498, HOP62, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.6 | 0.031 | 0/6 | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.6 | 0.031 | 4/19 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.046 | 5/35 (SW480, NCI-H2347, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.062 | 5/33 (SW480, CHP-212, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.063 | 5/32 (NCI-H23, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 0.05 µM |  | 1.40× | +3.1 | 0.11 | 3/33 (HS-578T, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.401×** | -12.3 | 8e-32 | 23/26 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -9.6 | 2e-19 | 23/34 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.392×** | -8.9 | 1e-16 | 16/22 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.369×** | -8.4 | 4e-15 | 24/31 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.443×** | -7.7 | 1e-12 | 19/31 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -7.7 | 1e-12 | 16/24 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -7.5 | 6e-12 | 20/34 (HOP62, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.491×** | -6.7 | 1e-09 | 20/34 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.536×** | -5.9 | 2e-07 | 15/24 (A-172, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.579×** | -5.2 | 1e-05 | 14/35 (NCI-H23, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.599×** | -4.8 | 7e-05 | 16/33 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.618×** | -4.5 | 3e-04 | 16/33 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -3.9 | 0.004 | 6/34 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -3.6 | 0.012 | 9/36 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.687×** | -3.5 | 0.015 | 8/36 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.690×** | -3.5 | 0.016 | 12/34 (C32, LOX-IMVI, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.691×** | -3.5 | 0.016 | 7/34 (RKO, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -3.3 | 0.035 | 6/31 (NCI-H460, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.709×** | -3.2 | 0.036 | 5/27 (SK-MEL-2, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 7.96 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -12.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.0876× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 4.76 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0347× (z -15.2) |
| [[PANC-1 (line)]] | alt | 3.69 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0424× (z -13.2) |
| [[A-172 (line)]] | wt | 8.94 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0753× (z -10.1) |
| [[C32 (line)]] | wt | 6.41 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0453× (z -10.3) |
| [[HOP62 (line)]] | alt | 4.23 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0431× (z -16.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0253× (z -13.9) |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0953× (z -11.2) |
| [[A-427 (line)]] | wt | 6.26 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0994× (z -8.7) |
| [[A549 (line)]] | wt | 2.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0412× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 5.73 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 4.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0812× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 6.24 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0800× (z -8.6) |
| [[A498 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZD4]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[BRSK2]] | +0.70 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[GNAZ]] | +0.69 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SLC4A3]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[VASH1]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ARHGEF25]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[B4GALNT4]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SEPTIN3]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | same gene group; STRING 989 |
| [[SULT4A1]] | +0.57 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[RAB6B]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[PLCG1]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRB]] | -0.47 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[PCED1B]] | -0.47 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[PDCD7]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 10, C 5. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRB]] | B | PTPRB activity lowers SEPTIN5's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.28× higher at baseline in the lines without PTPRB | 0.003 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[GNAZ]] | B | GNAZ activity raises SEPTIN5's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.25× lower at baseline in the lines without GNAZ | 0.012 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[LAMC3]] | B | LAMC3 activity raises SEPTIN5's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 2.69× lower at baseline in the lines without LAMC3 | 0.015 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[PDZD4]] | B | PDZD4 activity raises SEPTIN5's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.30× lower at baseline in the lines without PDZD4 | 0.038 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SPEG]] | B | SPEG activity raises SEPTIN5's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without SPEG | 0.042 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[VASH1]] | B | VASH1 activity raises SEPTIN5's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without VASH1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[BOLA3-DT]] | B | BOLA3-DT activity raises SEPTIN5's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.52× lower at baseline in the lines without BOLA3-DT | 0.054 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[PCED1B]] | B | PCED1B activity lowers SEPTIN5's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.04× higher at baseline in the lines without PCED1B | 0.064 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[GAS6]] | B | GAS6 activity raises SEPTIN5's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without GAS6 | 0.075 | ⚠ within organs, on part of the lines |
| [[BRSK2]] | B | BRSK2 activity raises SEPTIN5's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.97× lower at baseline in the lines without BRSK2 | 0.085 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[CERCAM]] | C | CERCAM activity raises SEPTIN5's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 2.35× lower at baseline in the lines without CERCAM | 0.004 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9; co-absent with the target |
| [[KIF26A]] | C | KIF26A activity raises SEPTIN5's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.50× lower at baseline in the lines without KIF26A | 0.016 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 19, C 7. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCD3]] | B | SEPTIN5 activity raises SMARCD3's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.33× lower at baseline in the lines without SEPTIN5 | 0.009 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[BRSK2]] | B | SEPTIN5 activity raises BRSK2's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without SEPTIN5 | 0.014 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[LLGL1]] | B | SEPTIN5 activity raises LLGL1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.52× lower at baseline in the lines without SEPTIN5 | 0.021 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[MAPK12]] | B | SEPTIN5 activity raises MAPK12's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without SEPTIN5 | 0.024 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[CHST14]] | B | SEPTIN5 activity raises CHST14's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.45× lower at baseline in the lines without SEPTIN5 | 0.029 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[SHANK3]] | B | SEPTIN5 activity raises SHANK3's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.80× lower at baseline in the lines without SEPTIN5 | 0.033 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[CAPN1]] | B | SEPTIN5 activity lowers CAPN1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.79× higher at baseline in the lines without SEPTIN5 | 0.036 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[PLBD2]] | B | SEPTIN5 activity raises PLBD2's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without SEPTIN5 | 0.050 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[TUBGCP6]] | B | SEPTIN5 activity raises TUBGCP6's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.19× lower at baseline in the lines without SEPTIN5 | 0.051 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[PCED1B]] | B | SEPTIN5 activity lowers PCED1B's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.92× higher at baseline in the lines without SEPTIN5 | 0.057 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[PLOD1]] | B | SEPTIN5 activity raises PLOD1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without SEPTIN5 | 0.058 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[ZNF483]] | B | SEPTIN5 activity raises ZNF483's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without SEPTIN5 | 0.058 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.0, 40.9); signed map (23.6, 27.0). **Vector** length 52.7, 8.55% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +0.9 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -7.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | septin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,714,503-19,724,224 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCDCREL-1, H5, Septin-5, CDCREL-1; previously PNUTL1, SEPT5 |
| Gene groups (HGNC) | Septins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99719](https://www.uniprot.org/uniprotkb/Q99719) (Septin-5):

> Filament-forming cytoskeletal GTPase (By similarity). May play a role in cytokinesis (Potential). May play a role in platelet secretion (By similarity).

**Summary**, from NCBI Gene [5413](https://www.ncbi.nlm.nih.gov/gene/5413):

> This gene is a member of the septin gene family of nucleotide binding proteins, originally described in yeast as cell division cycle regulatory proteins. Septins are highly conserved in yeast, Drosophila, and mouse and appear to regulate cytoskeletal organization. Disruption of septin function disturbs cytokinesis and results in large multinucleate or polyploid cells. This gene is mapped to 22q11, the region frequently deleted in DiGeorge and velocardiofacial syndromes. A translocation …

**Accessions** — [HGNC:9164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9164) · Entrez [5413](https://www.ncbi.nlm.nih.gov/gene/5413) · UniProt [Q99719](https://www.uniprot.org/uniprotkb/Q99719) · Ensembl [ENSG00000184702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184702)

## Data

Gene col 11568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11568); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11568]; `tensor/DDL_lfc|DDL_z.npy` [11568]; `embed/gene_vectors.npy` [11568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11568 or target_col == 11568). Every well: [[SEPTIN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
