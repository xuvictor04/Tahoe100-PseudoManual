---
symbol: "SNHG14"
type: "gene"
col: 13378
ensembl_id: "ENSG00000224078"
name: "small nucleolar RNA host gene 14"
location: "15q11.2"
module: 26
arm: "+"
pooled_cpm: 95.46
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SNHG14

*small nucleolar RNA host gene 14* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Filgotinib (drug)]] 5 µM: 1.49× (z +4.8, q 9e-04, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.394× (z -11.1, q 1e-25, down in 30 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.455× (z -9.3, q 9e-19, down in 29 of 34 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDC-AS1]] (+0.60, fdr 3e-05), [[SUCLG2-DT]] (+0.59, fdr 4e-05), [[PXDNL]] (+0.59, fdr 4e-05); moves opposite to [[DGAT2]] (-0.49, fdr 2e-04), [[VPS37C]] (-0.47, fdr 2e-04), [[LIPE]] (-0.46, fdr 4e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KIAA0825]] → it (grade B ⚠); 13 go from it, the strongest it → cells under [[Bortezomib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +4.8 | 9e-04 | 28/34 (A549, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +4.7 | 9e-04 | 25/34 (C-33 A, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.020 | 21/34 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.8 | 0.021 | 18/34 (A-427, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.4 | 0.061 | 17/32 (RPMI-7951, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.061 | 19/34 (HS-578T, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.0 | 0.20 | 2/36 (NCI-H23, MIA PaCa-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.394×** | -11.1 | 1e-25 | 30/34 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.521×** | -10.9 | 2e-25 | 28/34 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.430×** | -10.0 | 3e-21 | 30/34 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.439×** | -9.8 | 2e-20 | 31/34 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.440×** | -9.7 | 2e-20 | 31/34 (HepG2/C3A, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.455×** | -9.3 | 9e-19 | 29/34 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.478×** | -8.7 | 2e-16 | 29/34 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.447×** | -8.0 | 7e-14 | 29/34 (NCI-H460, A-427, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.541×** | -7.3 | 2e-11 | 30/34 (HEC-1-A, C32, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.567×** | -6.7 | 1e-09 | 26/34 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.602×** | -6.0 | 1e-07 | 26/34 (LOX-IMVI, C32, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.622×** | -5.6 | 9e-07 | 26/34 (SW 900, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.576×** | -4.9 | 4e-05 | 21/33 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -4.8 | 7e-05 | 24/34 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.621×** | -4.7 | 8e-05 | 24/33 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.678×** | -4.6 | 1e-04 | 23/34 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.688×** | -4.4 | 3e-04 | 20/34 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.820×** | -3.3 | 0.026 | 19/35 (CFPAC-1, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.770×** | -3.1 | 0.052 | 18/34 (HepG2/C3A, A-427, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 235 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -18.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 161 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -10.3) |
| [[A-427 (line)]] | wt | 179 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -12.4) |
| [[C32 (line)]] | wt | 155 | 0 | 9 (9 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.219× (z -11.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 125 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -14.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 148 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -14.2) |
| [[H4 (line)]] | wt | 129 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HepG2_C3A (line)]] | wt | 235 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.262× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 78.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.1) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -13.2) |
| [[SNU-423 (line)]] | alt | 135 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.0) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 131 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 405 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.9) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HEC-1-A (line)]] | alt | 331 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 53.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -8.6) |
| [[J82 (line)]] | alt | 66.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -11.1) |
| [[AN3 CA (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[C-33 A (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 211 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 90.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.03× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[RPMI-7951 (line)]] | alt | 83.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -8.5) |
| [[A-172 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 376 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDC-AS1]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SUCLG2-DT]] | +0.59 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[PXDNL]] | +0.59 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[PIPOX]] | +0.57 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[MKLN1]] | +0.57 | +0.39 / +0.42 | both halves | 6e-05 |  |
| [[NQO1-DT]] | +0.57 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[FRZB]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[NEK11]] | +0.57 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[LINC02615]] | +0.57 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[SPAG16]] | +0.56 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ANKRD7]] | +0.55 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[DPH6-DT]] | +0.54 | +0.43 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGAT2]] | -0.49 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[VPS37C]] | -0.47 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[LIPE]] | -0.46 | -0.24 / -0.28 | both halves | 4e-04 |  |
| [[SLC27A2]] | -0.46 | -0.45 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0825]] | B | KIAA0825 activity raises SNHG14's level | lines that do not express KIAA0825 (9) vs lines expressing it (41) | 3.69× lower at baseline in the lines without KIAA0825 | 0.064 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, SPART, CCDC102B; maybe low, not absent |
| [[FRG1-DT]] | B | FRG1-DT activity raises SNHG14's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 3.31× lower at baseline in the lines without FRG1-DT | 0.074 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[FRZB]] | C | FRZB activity raises SNHG14's level | lines that do not express FRZB (4) vs lines expressing it (46) | 3.25× lower at baseline in the lines without FRZB | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bortezomib (drug)]] 5 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.69× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Erlotinib (drug)]] 0.05 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.24× the cells of the other lines | 0.029 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Pimozide (drug)]] 0.05 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.16× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Folic acid (drug)]] 5 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.10× the cells of the other lines | 0.049 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.27× the cells of the other lines | 0.051 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Ixazomib citrate (drug)]] 5 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.40× the cells of the other lines | 0.054 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Benproperine (phosphate) (drug)]] 0.05 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.15× the cells of the other lines | 0.066 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Mifepristone (drug)]] 0.5 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 0.87× the cells of the other lines | 0.075 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Fenofibrate (drug)]] 0.05 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.21× the cells of the other lines | 0.079 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Furosemide (drug)]] 0.5 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.14× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.19× the cells of the other lines | 0.084 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Apalutamide (drug)]] 0.5 µM | C | [[ENSG00000214265]], SNHG14, [[SNRPN]] activity raises the cells' numbers under Apalutamide 0.5 µM (protects the cells) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 0.86× the cells of the other lines | 0.089 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.6, 17.5); signed map (20.7, -0.5). **Vector** length 96.7, 30.7% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.8 | +1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.7 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.5 | -8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.7 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.5 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 14 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q11.2 — chr15:24,978,583-25,420,336 (+) |
| Ensembl biotype | lncRNA |
| Also known as | 116HG, NCRNA00214, UBE3A-AS, UBE3A-ATS; previously UBE3A-AS1, IPW |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [104472715](https://www.ncbi.nlm.nih.gov/gene/104472715):

> This gene is located within the Prader-Willi critical region and produces a long, spliced paternally-imprinted RNA that initiates within a common upstream promoter region shared by the SNRPN (small nuclear ribonucleoprotein polypeptide N) and SNURF genes. This transcript serves as a host RNA for the small nucleolar RNA, C/D box 115 and 116 clusters. This RNA extends in antisense into the region of the ubiquitin protein ligase E3A gene (UBE3A), and is thought to regulate imprinted expression of …

**Accessions** — [HGNC:37462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37462) · Entrez [104472715](https://www.ncbi.nlm.nih.gov/gene/104472715) · Ensembl [ENSG00000224078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224078)

## Data

Gene col 13378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13378); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13378]; `tensor/DDL_lfc|DDL_z.npy` [13378]; `embed/gene_vectors.npy` [13378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13378 or target_col == 13378). Every well: [[SNHG14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
