---
symbol: "AHI1-DT"
type: "gene"
col: 13775
ensembl_id: "ENSG00000231028"
name: "AHI1 divergent transcript"
location: "6q23.3"
module: 23
arm: "+"
pooled_cpm: 7.29
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 22
n_dd_up_clean: 25
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# AHI1-DT

*AHI1 divergent transcript* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.27× (z +15.4, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.444× (z -7.4, q 6e-11, down in 29 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.468× (z -7.0, q 1e-09, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.82, fdr 1e-05), [[OXA1L-DT]] (+0.81, fdr 7e-06), [[GAS2]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LRRC17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.27×** | +15.4 | 0e+00 | 38/41 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.38×** | +8.0 | 4e-13 | 34/46 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +7.3 | 4e-11 | 26/38 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.69×** | +6.8 | 2e-09 | 24/47 (HT-29, KATO III, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.08×** | +6.7 | 2e-09 | 28/47 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.78×** | +5.3 | 1e-05 | 20/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.80×** | +5.2 | 2e-05 | 23/44 (NCI-H23, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.1 | 3e-05 | 9/20 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.68×** | +4.8 | 1e-04 | 18/44 (KATO III, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.7 | 1e-04 | 4/13 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.5 | 3e-04 | 17/38 (HT-29, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +4.5 | 3e-04 | 15/46 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 5e-04 | 17/47 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.41×** | +4.3 | 8e-04 | 17/48 (HEC-1-A, NCI-H23, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.63×** | +4.2 | 9e-04 | 14/46 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.002 | 19/47 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.002 | 14/48 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.002 | 13/46 (NCI-H23, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.444×** | -7.4 | 6e-11 | 29/47 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.468×** | -7.0 | 1e-09 | 27/47 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.483×** | -6.7 | 5e-09 | 27/47 (COLO 205, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.498×** | -6.4 | 2e-08 | 24/40 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.540×** | -5.7 | 2e-06 | 23/46 (H4, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.544×** | -5.6 | 2e-06 | 21/47 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.545×** | -5.6 | 2e-06 | 25/47 (COLO 205, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.667×** | -5.3 | 1e-05 | 25/47 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.576×** | -5.0 | 3e-05 | 22/47 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.585×** | -4.9 | 5e-05 | 23/46 (SW480, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.596×** | -4.7 | 1e-04 | 20/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.600×** | -4.7 | 1e-04 | 20/40 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.630×** | -4.2 | 0.001 | 16/42 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -4.1 | 0.002 | 18/44 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.647×** | -4.0 | 0.002 | 15/47 (NCI-H661, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.455×** | -3.6 | 0.009 | 13/44 (H4, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.484×** | -3.4 | 0.025 | 15/40 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.611×** | -3.2 | 0.037 | 9/48 (C32, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 46.5 | 0 | 7 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LOX-IMVI (line)]] | wt | 5.93 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0761× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 19.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +9.4) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SW480 (line)]] | alt | 6.90 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.165× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 8.91 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 9.89 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0430× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 4.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +8.7) | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0923× (z -11.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 2.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.28× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 5.78 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 6.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.82 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.81 | +0.75 / +0.59 | both halves | 7e-06 | same gene group |
| [[GAS2]] | +0.79 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[EFCAB6]] | +0.79 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[HEXIM2-AS1]] | +0.79 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.79 | +0.74 / +0.54 | both halves | 1e-05 | same gene group |
| [[UFL1-AS1]] | +0.78 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[USP38-DT]] | +0.78 | +0.79 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZBED5-AS1]] | +0.78 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.78 | +0.76 / +0.38 | both halves | 7e-05 |  |
| [[PNISR-AS1]] | +0.77 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[BDNF-AS]] | +0.77 | +0.81 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC17]] | B | LRRC17 activity raises AHI1-DT's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without LRRC17 | 0.024 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers AHI1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLTCL1]] | C | CLTCL1 activity weakens AHI1-DT's drug response | lines that do not express CLTCL1 (3) vs lines expressing it (45) | the lines without CLTCL1 respond 1.84× as strongly (z diff -2.02); rises at some drug-doses, falls at others (48% from rises): Ouabain (Octahydrate) 5 µM: 0.17x vs 0.47x (z diff -4.5); Selinexor 5 µM: 2.37x vs 1.57x (z diff -3.2); Doxorubicin (hydrochloride) 5 µM: 3.28x vs 2.44x (z diff -2.5) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[RFX3-DT]] | C | RFX3-DT activity raises AHI1-DT's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[CD72]] | C | CD72 activity raises AHI1-DT's level | lines that do not express CD72 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without CD72 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TCF7, DUSP19, MIR4435-2HG; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.828). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.5, 18.5); signed map (28.9, -9.2). **Vector** length 86.9, 18.7% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.4 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.1 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.6 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.1 | -5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | AHI1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q23.3 — chr6:135,497,422-135,828,703 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C6orf217, NCRNA00271, LINC00271 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

UniProt [P0C7V0](https://www.uniprot.org/uniprotkb/P0C7V0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32526) · Entrez [100131814](https://www.ncbi.nlm.nih.gov/gene/100131814) · UniProt [P0C7V0](https://www.uniprot.org/uniprotkb/P0C7V0) · Ensembl [ENSG00000231028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231028)

## Data

Gene col 13775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13775); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13775]; `tensor/DDL_lfc|DDL_z.npy` [13775]; `embed/gene_vectors.npy` [13775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13775 or target_col == 13775). Every well: [[AHI1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHI1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
