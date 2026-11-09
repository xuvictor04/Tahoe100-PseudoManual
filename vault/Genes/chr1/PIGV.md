---
symbol: "PIGV"
type: "gene"
col: 689
ensembl_id: "ENSG00000060642"
name: "phosphatidylinositol glycan anchor biosynthesis class V"
location: "1p36.11"
module: 80
arm: "+"
pooled_cpm: 5.33
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# PIGV

*phosphatidylinositol glycan anchor biosynthesis class V* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +14.1, q 4e-42, up in 28 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.475× (z -9.5, q 8e-19, down in 29 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.519× (z -8.4, q 1e-14, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WAKMAR2]] (+0.75, fdr 4e-05), [[ENO3]] (+0.74, fdr 2e-05), [[C19orf54]] (+0.74, fdr 7e-05); moves opposite to [[PIP4K2A]] (-0.65, fdr 4e-05), [[GNA12]] (-0.61, fdr 2e-04), [[TMEM120B]] (-0.61, fdr 3e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CYP1B1-AS1]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Menadione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +14.1 | 4e-42 | 28/39 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +11.4 | 2e-27 | 34/40 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +7.4 | 2e-11 | 19/46 (SW480, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +6.2 | 9e-08 | 21/44 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.8 | 8e-07 | 14/38 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.3 | 1e-05 | 6/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +5.2 | 1e-05 | 6/47 (J82, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 14/37 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 7e-04 | 1/10 (HS-578T) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 12/46 (hTERT-HPNE, SNU-423, …) | rises with dose | position effect removed |
| [[Neratinib (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.033 | 7/43 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.037 | 5/46 (NCI-H2347, C32, …) | all doses, flat | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -9.5 | 8e-19 | 29/39 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -8.4 | 1e-14 | 25/44 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -7.7 | 2e-12 | 27/44 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -6.8 | 1e-09 | 21/45 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.626×** | -6.0 | 2e-07 | 16/47 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -5.9 | 3e-07 | 20/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.642×** | -5.7 | 1e-06 | 18/44 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -5.5 | 3e-06 | 18/44 (H4, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -5.1 | 2e-05 | 12/43 (SK-MEL-2, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.662×** | -5.1 | 2e-05 | 15/35 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -5.1 | 2e-05 | 17/40 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.704×** | -4.5 | 3e-04 | 15/47 (PANC-1, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.731×** | -3.8 | 0.006 | 14/44 (SHP-77, SW 900, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.014 | 6/47 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.766×** | -3.4 | 0.023 | 14/46 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -3.4 | 0.026 | 11/42 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.606×** | -3.4 | 0.026 | 6/42 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.049 | 15/42 (SNU-423, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.84 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.210× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.265× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 8.15 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0589× (z -12.2) |
| [[C-33 A (line)]] | alt | 8.44 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0696× (z -9.1) |
| [[HS-578T (line)]] | alt | 4.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 3.16 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0463× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 4.91 | 0 | 2 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0501× (z -11.7) |
| [[SNU-423 (line)]] | alt | 5.43 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +9.1) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.114× (z -8.5) |
| [[A498 (line)]] | wt | 4.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +9.7) | — |
| [[A549 (line)]] | wt | 3.70 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0706× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 3.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 5.95 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0698× (z -8.5) |
| [[HOP62 (line)]] | alt | 5.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 5.13 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0741× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +9.2) | — |
| [[J82 (line)]] | alt | 7.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +8.7) | — |
| [[KATO III (line)]] | alt | 3.60 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0738× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 7.03 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -8.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 7.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0780× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 3.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 6.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +9.4) | — |
| [[A-172 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAKMAR2]] | +0.75 | +0.80 / +0.41 | both halves | 4e-05 |  |
| [[ENO3]] | +0.74 | +0.80 / +0.47 | both halves | 2e-05 |  |
| [[C19orf54]] | +0.74 | +0.78 / +0.38 | both halves | 7e-05 |  |
| [[MEPCE]] | +0.73 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[SIX5]] | +0.72 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.72 | +0.78 / +0.35 | both halves | 1e-04 |  |
| [[ZC3H4]] | +0.72 | +0.76 / +0.42 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | +0.71 | +0.79 / +0.28 | both halves | 3e-04 |  |
| [[NEPRO-AS1]] | +0.70 | +0.78 / +0.37 | both halves | 7e-05 |  |
| [[ACTR3-AS1]] | +0.70 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[NEK8]] | +0.70 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[C7orf31]] | +0.70 | +0.73 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP4K2A]] | -0.65 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[GNA12]] | -0.61 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[TMEM120B]] | -0.61 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[PCMT1]] | -0.60 | -0.62 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[FAM118A]] | -0.60 | -0.60 / -0.25 | both halves | 4e-04 |  |
| [[PACC1]] | -0.60 | -0.56 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises PIGV's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without CYP1B1-AS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[TRIP6]] | B | TRIP6 activity weakens PIGV's drug response | lines that do not express TRIP6 (12) vs lines expressing it (36) | the lines without TRIP6 respond 1.39× as strongly (z diff -1.06); strongest at Ouabain (Octahydrate) 0.5 µM: 0.29x vs 0.52x (z diff -3.3) | 0.065 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4; target measured in part of the lines; artifact flags |
| [[TRIP6]] | B | TRIP6 activity lowers PIGV's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.40× higher at baseline in the lines without TRIP6 | 0.066 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[TOP2A]] | B | TOP2A activity lowers PIGV's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Menadione (drug)]] 0.5 µM | C | PIGV's natural level lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | PIGV's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.261 over the table, 0.009 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | PIGV's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | PIGV's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.043 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 10.6); signed map (18.6, -12.1). **Vector** length 71.2, 11.4% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.8 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class V |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,787,054-26,800,659 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20477, PIG-V, GPI-MT-II |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases; Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUD9](https://www.uniprot.org/uniprotkb/Q9NUD9) (GPI alpha-1,6-mannosyltransferase 2):

> Alpha-1,6-mannosyltransferase that catalyzes the transfer of the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates in the seventh …

**Summary**, from NCBI Gene [55650](https://www.ncbi.nlm.nih.gov/gene/55650):

> This gene encodes a mannosyltransferase enzyme involved in the biosynthesis of glycosylphosphatidylinositol (GPI). GPI is a complex glycolipid that functions as a membrane anchor for many proteins and plays a role in multiple cellular processes including protein sorting and signal transduction. The encoded protein is localized to the endoplasmic reticulum and transfers the second mannose to the GPI backbone. Mutations in this gene are associated with hyperphosphatasia cognitive disability …

**Accessions** — [HGNC:26031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26031) · Entrez [55650](https://www.ncbi.nlm.nih.gov/gene/55650) · UniProt [Q9NUD9](https://www.uniprot.org/uniprotkb/Q9NUD9) · Ensembl [ENSG00000060642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060642)

## Data

Gene col 689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 689); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 689]; `tensor/DDL_lfc|DDL_z.npy` [689]; `embed/gene_vectors.npy` [689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 689 or target_col == 689). Every well: [[PIGV — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGV.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
