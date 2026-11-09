---
symbol: "BEAN1"
type: "gene"
col: 9328
ensembl_id: "ENSG00000166546"
name: "brain expressed associated with NEDD4 1"
location: "16q21"
module: 34
arm: "+"
pooled_cpm: 7.14
n_lines_expressing: 43
n_dd_up: 15
n_dd_down: 38
n_dd_up_clean: 10
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# BEAN1

*brain expressed associated with NEDD4 1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.60× (z +8.4, q 4e-14, up in 20 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.354× (z -12.4, q 1e-32, down in 27 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VSIG1]] (+0.57, fdr 2e-05), [[TNFRSF6B]] (+0.54, fdr 3e-05), [[TMC6]] (+0.52, fdr 2e-05); moves opposite to [[NAALADL2]] (-0.47, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +8.4 | 4e-14 | 20/40 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.0 | 5e-13 | 2/11 (NCI-H2030, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +6.0 | 5e-07 | 14/38 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +5.0 | 8e-05 | 2/13 (NCI-H2030, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.9 | 1e-04 | 1/21 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **1.30×** | +4.7 | 2e-04 | 10/40 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.92×** | +4.3 | 0.001 | 4/24 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.001 | 13/37 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.011 | 4/33 (LoVo, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.012 | 1/35 (NCI-H1792) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.012 | 11/36 (SW48, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.050 | 9/30 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.068 | 2/38 (COLO 205, SHP-77) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.1 | 0.086 | 7/36 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +3.1 | 0.086 | 6/40 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.354×** | -12.4 | 1e-32 | 27/36 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.419×** | -10.8 | 6e-25 | 21/31 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.541×** | -10.8 | 6e-25 | 23/31 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.490×** | -8.9 | 9e-17 | 22/38 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.497×** | -8.7 | 4e-16 | 23/39 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.533×** | -7.8 | 5e-13 | 23/40 (AsPC-1, HepG2/C3A, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.545×** | -7.5 | 4e-12 | 19/39 (SNU-423, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.548×** | -7.5 | 5e-12 | 22/38 (LoVo, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.562×** | -7.2 | 5e-11 | 18/39 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.580×** | -6.8 | 7e-10 | 20/39 (HepG2/C3A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.625×** | -5.5 | 2e-06 | 19/38 (HepG2/C3A, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.647×** | -5.0 | 3e-05 | 13/39 (SW1417, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.681×** | -4.8 | 8e-05 | 13/38 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.734×** | -4.5 | 3e-04 | 17/39 (HepG2/C3A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.687×** | -4.5 | 3e-04 | 17/36 (A549, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.728×** | -4.2 | 8e-04 | 15/41 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.563×** | -3.7 | 0.006 | 8/29 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -3.7 | 0.006 | 10/38 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.009 | 7/40 (HepG2/C3A, AsPC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.578×** | -3.6 | 0.009 | 11/27 (HepG2/C3A, A549, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 74.4 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0610× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.9) |
| [[SW480 (line)]] | alt | 20.1 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.201× (z -10.3) |
| [[Hs 766T (line)]] | wt | 35.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0932× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.0) |
| [[A-172 (line)]] | wt | 16.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 4.78 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0281× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0256× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.1) |
| [[LoVo (line)]] | wt | 6.18 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -9.5) |
| [[A549 (line)]] | wt | 7.06 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0968× (z -12.9) |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -10.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.182× (z -10.0) |
| [[BT-474 (line)]] | alt | 6.92 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0586× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 4.53 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0887× (z -8.6) |
| [[HOP62 (line)]] | alt | 4.22 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0889× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0881× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0474× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 7.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.3) |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0404× (z -8.7) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 9.03 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0589× (z -9.3) |
| [[A-427 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSIG1]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TNFRSF6B]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TMC6]] | +0.52 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[IQSEC1]] | +0.52 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SYNE3]] | +0.51 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[RAPGEF3]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[LEMD1]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[FAM3C]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[KRT15]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[LAT]] | +0.50 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[CAMK2B]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAALADL2]] | -0.47 | -0.54 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises BEAN1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.4% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[MTOR]] | B | MTOR activity lowers BEAN1's level | compounds that target MTOR: 4 of 8 raise it (GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 3.1% of all compounds | 0.040 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NAALADL2]] | B | NAALADL2 activity lowers BEAN1's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 2.07× higher at baseline in the lines without NAALADL2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[PPP1R14C]] | B | PPP1R14C activity raises BEAN1's level | lines that do not express PPP1R14C (14) vs lines expressing it (36) | 1.11× lower at baseline in the lines without PPP1R14C | 0.092 | ⚠ within organs, on part of the lines; also absent: APLP1, CACNA1B, ENTREP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.7, 52.0); signed map (3.8, 40.6). **Vector** length 74.2, 13.4% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -1.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +4.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | brain expressed associated with NEDD4 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:66,427,295-66,493,529 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SCA31 |
| Matched by | ensembl_id |

UniProt [Q3B7T3](https://www.uniprot.org/uniprotkb/Q3B7T3) carries no function annotation.

**Summary**, from NCBI Gene [146227](https://www.ncbi.nlm.nih.gov/gene/146227):

> The protein encoded by this gene is one of several proteins that interact with NEDD4, a member of a family of ubiquitin-protein ligases. These proteins have PY motifs in common that bind to the WW domains of NEDD4. NEDD4 is developmentally regulated, and is highly expressed in embryonic tissues. Mutations in this gene (i.e., intronic insertions of >100 copies of pentanucleotide repeats including a (TGGAA)n sequence) are associated with spinocerebellar ataxia type 31. Alternatively spliced …

**Accessions** — [HGNC:24160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24160) · Entrez [146227](https://www.ncbi.nlm.nih.gov/gene/146227) · UniProt [Q3B7T3](https://www.uniprot.org/uniprotkb/Q3B7T3) · Ensembl [ENSG00000166546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166546)

## Data

Gene col 9328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9328); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9328]; `tensor/DDL_lfc|DDL_z.npy` [9328]; `embed/gene_vectors.npy` [9328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9328 or target_col == 9328). Every well: [[BEAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
