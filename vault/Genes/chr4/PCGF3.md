---
symbol: "PCGF3"
type: "gene"
col: 11702
ensembl_id: "ENSG00000185619"
name: "polycomb group ring finger 3"
location: "4p16.3"
module: 89
arm: "+"
pooled_cpm: 49.19
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# PCGF3

*polycomb group ring finger 3* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.29× (z +5.6, q 1e-05, up in 25 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.41× (z +4.1, q 0.007, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.459× (z -17.2, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF358]] (+0.68, fdr 1e-05), [[ZNF117]] (+0.57, fdr 3e-04), [[FBXL19]] (+0.56, fdr 1e-05); moves opposite to [[BHLHE41]] (-0.48, fdr 2e-05), [[FH]] (-0.46, fdr 3e-05), [[CDK6]] (-0.45, fdr 3e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.6 | 1e-05 | 25/47 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.17× | +5.0 | 1e-04 | 21/48 (LoVo, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.007 | 20/48 (MIA PaCa-2, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.16× | +3.3 | 0.13 | 12/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.16× | +3.3 | 0.13 | 17/47 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.24 | 6/48 (Panc 03.27, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.459×** | -17.2 | 0e+00 | 44/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.605×** | -16.3 | 0e+00 | 41/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -16.1 | 0e+00 | 40/48 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.563×** | -12.7 | 6e-35 | 45/48 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.605×** | -11.5 | 9e-29 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.616×** | -11.1 | 9e-27 | 41/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -8.5 | 2e-15 | 40/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.697×** | -8.3 | 8e-15 | 40/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.718×** | -7.6 | 2e-12 | 39/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **0.752×** | -6.6 | 3e-09 | 29/49 (H4, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.754×** | -6.0 | 1e-07 | 24/45 (NCI-H2030, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.803×** | -4.8 | 6e-05 | 19/41 (HCT15, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.813×** | -4.8 | 8e-05 | 18/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.691×** | -4.4 | 4e-04 | 18/49 (AN3 CA, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.833×** | -4.2 | 1e-03 | 21/48 (SW48, A-172, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.861× | -3.2 | 0.051 | 16/47 (C-33 A, AN3 CA, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.913× | -3.0 | 0.090 | 8/48 (SNU-1, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 61.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -15.7) |
| [[HCT15 (line)]] | alt | 66.1 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 56.9 | 0 | 5 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.197× (z -14.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 47.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 55.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 68.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -13.3) |
| [[KATO III (line)]] | alt | 53.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.8) |
| [[LS 180 (line)]] | wt | 55.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 69.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -18.7) |
| [[SNU-423 (line)]] | alt | 63.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -15.3) |
| [[A-427 (line)]] | wt | 51.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.4) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.1) |
| [[C-33 A (line)]] | alt | 80.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.1) |
| [[COLO 205 (line)]] | alt | 57.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.6) |
| [[H4 (line)]] | wt | 74.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -11.0) |
| [[HOP62 (line)]] | alt | 62.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.489× (z -8.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -14.8) |
| [[SW480 (line)]] | alt | 47.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -15.5) |
| [[BT-474 (line)]] | alt | 54.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.1) |
| [[C32 (line)]] | wt | 55.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -12.2) |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -9.2) |
| [[J82 (line)]] | alt | 58.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -10.4) |
| [[LoVo (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[NCI-H1573 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 45.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 51.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -9.1) |
| [[PANC-1 (line)]] | alt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~69% of this change |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -8.7) |
| [[SNU-1 (line)]] | wt | 52.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.332× (z -11.6) |
| [[SW 1271 (line)]] | alt | 59.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0840× (z -8.9) |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -8.5) |
| [[SW48 (line)]] | wt | 58.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[A498 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF358]] | +0.68 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZNF117]] | +0.57 | +0.26 / +0.64 | both halves | 3e-04 |  |
| [[FBXL19]] | +0.56 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ARMH3]] | +0.56 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TM2D1]] | +0.56 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ADAT3]] | +0.55 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MED9]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.53 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TRIP4]] | +0.52 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[METTL22]] | +0.52 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[MARK4]] | +0.52 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[MAFIP]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BHLHE41]] | -0.48 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[FH]] | -0.46 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CDK6]] | -0.45 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.45 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CFAP97]] | -0.45 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[SGMS2]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[LINC01473]] | -0.45 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[PLCB4]] | -0.44 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[HIVEP3]] | -0.43 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[GTF3A]] ⚠ | -0.43 | -0.45 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC15]] | -0.43 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[EXTL2]] | -0.43 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PER2]] | -0.43 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PCGF3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.486). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.5, -7.1); signed map (-4.1, -1.5). **Vector** length 88.3, 19.3% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +7.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +5.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.7 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | -1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -17.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -16.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | polycomb group ring finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:705,748-770,089 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36550, DONG1, RNF3A, MGC40413; previously RNF3 |
| Gene groups (HGNC) | Ring finger proteins; Polycomb group ring fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3KNV8](https://www.uniprot.org/uniprotkb/Q3KNV8) (Polycomb group RING finger protein 3):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Within the PRC1-like complex, regulates RNF2 ubiquitin ligase activity. Plays a redundant role with …

**Summary**, from NCBI Gene [10336](https://www.ncbi.nlm.nih.gov/gene/10336):

> The protein encoded by this gene contains a C3HC4 type RING finger, which is a motif known to be involved in protein-protein interactions. The specific function of this protein has not yet been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10066) · Entrez [10336](https://www.ncbi.nlm.nih.gov/gene/10336) · UniProt [Q3KNV8](https://www.uniprot.org/uniprotkb/Q3KNV8) · Ensembl [ENSG00000185619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185619)

## Data

Gene col 11702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11702); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11702]; `tensor/DDL_lfc|DDL_z.npy` [11702]; `embed/gene_vectors.npy` [11702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11702 or target_col == 11702). Every well: [[PCGF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCGF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
