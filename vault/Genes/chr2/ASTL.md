---
symbol: "ASTL"
type: "gene"
col: 12060
ensembl_id: "ENSG00000188886"
name: "astacin like metalloendopeptidase"
location: "2q11.2"
module: 109
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 24
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# ASTL

*astacin like metalloendopeptidase* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.6× (z +23.1, q 0e+00, up in 10 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.329× (z -6.9, q 3e-09, down in 11 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR3]] (+0.79, fdr 7e-06), [[EGR2]] (+0.77, fdr 7e-06), [[DUSP2]] (+0.76, fdr 7e-06, ⚠ same locus), [[EGR1]] (+0.73, fdr 7e-06); moves opposite to [[RNPC3]] (-0.49, fdr 2e-04).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 8 go from it, the strongest it → [[ETV5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.6×** | +23.1 | 0e+00 | 10/13 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.11×** | +12.1 | 4e-31 | 17/19 (NCI-H460, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.89×** | +10.6 | 7e-24 | 17/21 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.94×** | +9.1 | 9e-18 | 5/11 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.85×** | +9.0 | 3e-17 | 15/20 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +7.8 | 4e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +7.3 | 2e-11 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.89×** | +6.5 | 4e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.9 | 2e-07 | 4/15 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +5.6 | 2e-06 | 11/21 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +5.3 | 5e-06 | 4/15 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +5.3 | 5e-06 | 11/21 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.97×** | +4.5 | 3e-04 | 18/21 (SW480, NCI-H23, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.02×** | +3.3 | 0.034 | 1/7 (HT-29) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +3.3 | 0.036 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.051 | 1/20 (SW480) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.63×** | +3.1 | 0.066 | 4/18 (RKO, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.329×** | -6.9 | 3e-09 | 11/21 (SW480, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.484×** | -5.2 | 7e-05 | 11/21 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.502×** | -4.6 | 7e-04 | 13/21 (HCT15, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.513×** | -4.5 | 0.001 | 13/21 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.641×** | -4.2 | 0.003 | 12/21 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.624×** | -3.9 | 0.010 | 8/21 (SW480, CHP-212, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.630×** | -3.8 | 0.010 | 15/20 (SW48, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.584×** | -3.5 | 0.038 | 11/15 (SW480, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -3.2 | 0.078 | 10/18 (SW48, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 0.05 µM |  | 0.611× | -3.1 | 0.10 | 6/20 (CHP-212, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.622× | -3.1 | 0.11 | 11/17 (SW480, CHP-212, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.634× | -3.1 | 0.11 | 4/18 (HCT15, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | 0.723× | -3.0 | 0.11 | 12/21 (NCI-H23, SW480, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 50.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0440× (z -12.3) |
| [[HT-29 (line)]] | alt | 7.84 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0129× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 26.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0226× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 1.16 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 135× (z +15.0) | — |
| [[SW480 (line)]] | alt | 9.05 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +9.6) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0444× (z -9.9) |
| [[HCT15 (line)]] | alt | 8.39 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0212× (z -9.1) |
| [[HOP62 (line)]] | alt | 5.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.9× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 4.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +13.1) | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.0555× (z -10.3) |
| [[A-172 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.695 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.978 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.792 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.888 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR3]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[EGR2]] | +0.77 | +0.80 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[DUSP2]] | +0.76 | +0.74 / +0.78 | both halves | 7e-06 | ⚠ same locus (4.7 kb, same strand: neighbours can correlate without regulation) |
| [[EGR1]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.72 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ERCC1]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[IER2]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SPATA32]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BTBD19]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[FBXO41]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NCKAP5L]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FOSL1]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[FOS]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPC3]] | -0.49 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ASTL's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises ASTL's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[DUSP2]] | C | DUSP2 activity raises ASTL's level | lines that do not express DUSP2 (23) vs lines expressing it (27) | 2.60× lower at baseline in the lines without DUSP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ASTL, HOXA11, KCNE3; maybe low, not absent; co-absent with the target |
| [[NKD2]] | C | NKD2 activity raises ASTL's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without NKD2 | 0.035 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETV5]] | B | ASTL activity raises ETV5's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without ASTL | 0.013 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[NCKAP5L]] | B | ASTL activity raises NCKAP5L's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.12× lower at baseline in the lines without ASTL | 0.053 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[ERCC1]] | B | ASTL activity raises ERCC1's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.21× lower at baseline in the lines without ASTL | 0.078 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[SPRED2]] | B | ASTL activity raises SPRED2's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.28× lower at baseline in the lines without ASTL | 0.080 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[ETV4]] | B | ASTL activity raises ETV4's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without ASTL | 0.091 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[EGR3]] | B | ASTL activity raises EGR3's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without ASTL | 0.099 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[DUSP2]] | C | ASTL activity raises DUSP2's level | lines that do not express ASTL (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without ASTL | 3e-04 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent; co-absent with the target |
| [[NKD2]] | C | ASTL activity raises NKD2's level | lines that do not express ASTL (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without ASTL | 0.087 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, -1.0); signed map (5.9, 29.7). **Vector** length 53.7, 12.8% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.61 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.61 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.57 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +23.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.3 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | astacin like metalloendopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,122,818-96,138,502 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ovastacin, SAS1B |
| Gene groups (HGNC) | Astacins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6HA08](https://www.uniprot.org/uniprotkb/Q6HA08) (Astacin-like metalloendopeptidase):

> Oocyte-specific oolemmal receptor involved in sperm and egg adhesion and fertilization. Plays a role in the polyspermy inhibition. Probably acts as a protease for the post-fertilization cleavage of ZP2. Cleaves the sperm-binding ZP2 at the surface of the zona pellucida after fertilization and cortical granule exocytosis, rendering the zona pellucida unable to support further sperm binding.

**Summary**, from NCBI Gene [431705](https://www.ncbi.nlm.nih.gov/gene/431705):

> Predicted to enable aspartic-type peptidase activity; glutamic-type peptidase activity; and metalloendopeptidase activity. Predicted to be involved in several processes, including negative regulation of binding activity of sperm to zona pellucida; positive regulation of protein processing; and prevention of polyspermy. Predicted to be located in cortical granule and plasma membrane. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31704) · Entrez [431705](https://www.ncbi.nlm.nih.gov/gene/431705) · UniProt [Q6HA08](https://www.uniprot.org/uniprotkb/Q6HA08) · Ensembl [ENSG00000188886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188886)

## Data

Gene col 12060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12060); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12060]; `tensor/DDL_lfc|DDL_z.npy` [12060]; `embed/gene_vectors.npy` [12060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12060 or target_col == 12060). Every well: [[ASTL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASTL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
