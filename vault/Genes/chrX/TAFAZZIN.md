---
symbol: "TAFAZZIN"
type: "gene"
col: 2218
ensembl_id: "ENSG00000102125"
name: "tafazzin, phospholipid-lysophospholipid transacylase"
location: "Xq28"
module: 65
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# TAFAZZIN

*tafazzin, phospholipid-lysophospholipid transacylase* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[LY-2584702 (tosylate salt) (drug)]] 5 µM: 1.52× (z +3.8, q 0.068, up in 3 of 28 measured lines) ⚠ toxic.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.396× (z -16.2, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAUS4]] (+0.60, fdr 4e-05), [[FCSK]] (+0.57, fdr 4e-05), [[VPS26B]] (+0.55, fdr 6e-05); moves opposite to [[BCL10-AS1]] (-0.48, fdr 1e-04), [[BACH1]] (-0.48, fdr 5e-05), [[PLSCR2]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GABRE]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.068 | 3/28 (A549, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.21× | +3.4 | 0.12 | 7/33 (SHP-77, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.31× | +3.4 | 0.12 | 3/47 (SW480, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.21× | +3.3 | 0.12 | 9/45 (A549, SW480, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.29× | +3.3 | 0.13 | 10/42 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.17 | 3/44 (SNU-1, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.396×** | -16.2 | 0e+00 | 42/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.485×** | -12.6 | 5e-34 | 29/44 (MIA PaCa-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.518×** | -11.5 | 4e-28 | 36/47 (SHP-77, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.536×** | -10.9 | 2e-25 | 31/47 (BT-474, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -10.6 | 3e-24 | 27/47 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.545×** | -10.6 | 3e-24 | 36/47 (SW 900, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -10.3 | 8e-23 | 31/45 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -9.8 | 9e-21 | 28/46 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.723×** | -7.9 | 1e-13 | 23/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.642×** | -7.7 | 7e-13 | 28/47 (A-172, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.659×** | -7.2 | 2e-11 | 27/47 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -6.3 | 1e-08 | 22/47 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.701×** | -5.9 | 1e-07 | 23/41 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.711×** | -5.9 | 1e-07 | 21/47 (NCI-H2030, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.796×** | -5.6 | 9e-07 | 18/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.726×** | -5.6 | 9e-07 | 21/48 (AN3 CA, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -5.1 | 9e-06 | 16/47 (SW 1271, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.773×** | -4.4 | 3e-04 | 16/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.684×** | -3.4 | 0.015 | 10/44 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.693×** | -3.3 | 0.022 | 11/47 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -12.8) |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -10.9) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.117× (z -10.6) |
| [[BT-474 (line)]] | alt | 5.54 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0631× (z -9.8) |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 20.0 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.195× (z -12.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.2) |
| [[A-172 (line)]] | wt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -11.6) |
| [[J82 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0458× (z -19.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 8.43 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.266× (z -12.0) |
| [[A498 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -9.7) |
| [[A549 (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 8.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.0) |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.5) |
| [[HS-578T (line)]] | alt | 8.30 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.213× (z -9.5) |
| [[RKO (line)]] | wt | 8.57 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.110× (z -9.1) |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -10.4) |
| [[SNU-1 (line)]] | wt | 9.69 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0691× (z -9.4) |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS4]] | +0.60 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[FCSK]] | +0.57 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[VPS26B]] | +0.55 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[PGAP2]] | +0.54 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[ANO8]] | +0.53 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[RHOT1]] | +0.52 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ZNF18]] | +0.52 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[PXK]] | +0.51 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[SUCLG1]] | +0.50 | +0.32 / +0.42 | both halves | 2e-04 |  |
| [[SKIC3]] | +0.50 | +0.49 / +0.26 | both halves | 4e-04 |  |
| [[REPS1]] | +0.50 | +0.47 / +0.27 | both halves | 3e-04 |  |
| [[KIF3A]] | +0.49 | +0.45 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL10-AS1]] | -0.48 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[BACH1]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PLSCR2]] | -0.47 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[TSPYL1]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[TAF7]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ETNK1]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 | pathway: Glycerophospholipid biosynthesis |
| [[CTSS]] | -0.47 | -0.49 / -0.21 | both halves | 7e-04 |  |
| [[CDKN2B-AS1]] | -0.46 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[SLC5A3]] | -0.46 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[SLIT2]] | -0.45 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[ARAP2]] | -0.45 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[LYPD1]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRE]] | B | GABRE activity lowers TAFAZZIN's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.19× higher at baseline in the lines without GABRE | 0.079 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | TAFAZZIN's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | TAFAZZIN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.406 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.414). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.0, -3.8); signed map (-24.6, -14.1). **Vector** length 57.2, 8.07% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +1.2 | -5.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.2 | +3.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -16.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | tafazzin, phospholipid-lysophospholipid transacylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,411,524-154,421,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTHS, G4.5, TAZ1; previously CMD3A, EFE2, EFE, TAZ |
| Reactome | 6 pathways, smallest: Acyl chain remodeling of CL; Mitochondrial protein import; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16635](https://www.uniprot.org/uniprotkb/Q16635) (Tafazzin):

> Acyltransferase required to remodel newly synthesized phospholipid cardiolipin (1',3'-bis-[1,2-diacyl-sn-glycero-3-phospho]-glycerol or CL), a key component of the mitochondrial inner membrane, with tissue specific acyl chains necessary for adequate mitochondrial function. Its role in cellular physiology is to improve mitochondrial performance. CL is critical for the coassembly of lipids and proteins in mitochondrial membranes, for instance, remodeling of the acyl groups of CL in the …

**Summary**, from NCBI Gene [6901](https://www.ncbi.nlm.nih.gov/gene/6901):

> This gene encodes a protein that is expressed at high levels in cardiac and skeletal muscle. Mutations in this gene have been associated with a number of clinical disorders including Barth syndrome, dilated cardiomyopathy (DCM), hypertrophic DCM, endocardial fibroelastosis, and left ventricular noncompaction (LVNC). Multiple transcript variants encoding different isoforms have been described. A long form and a short form of each of these isoforms is produced; the short form lacks a hydrophobic …

**Accessions** — [HGNC:11577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11577) · Entrez [6901](https://www.ncbi.nlm.nih.gov/gene/6901) · UniProt [Q16635](https://www.uniprot.org/uniprotkb/Q16635) · Ensembl [ENSG00000102125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102125)

## Data

Gene col 2218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2218); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2218]; `tensor/DDL_lfc|DDL_z.npy` [2218]; `embed/gene_vectors.npy` [2218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2218 or target_col == 2218). Every well: [[TAFAZZIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAFAZZIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
