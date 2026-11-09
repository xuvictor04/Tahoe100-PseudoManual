---
symbol: "MTOR"
type: "gene"
col: 12679
ensembl_id: "ENSG00000198793"
name: "mechanistic target of rapamycin kinase"
location: "1p36.22"
module: 36
arm: "+"
pooled_cpm: 49.71
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 93
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# MTOR

*mechanistic target of rapamycin kinase* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.78× (z +11.4, q 1e-27, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.29× (z +7.1, q 2e-10, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.730× (z -8.9, q 4e-16, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARN]] (+0.72, fdr 7e-06), [[HERC2]] (+0.65, fdr 7e-06), [[EXOC2]] (+0.65, fdr 7e-06); moves opposite to [[KDM5B]] (-0.59, fdr 9e-06), [[HOOK2]] (-0.59, fdr 1e-05), [[VASN]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 93 go from it, the strongest it → [[INSR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.78×** | +11.4 | 1e-27 | 34/48 (SW480, LS 180, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.67×** | +10.2 | 4e-22 | 34/48 (SW480, LS 180, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.57×** | +9.0 | 4e-17 | 29/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +7.1 | 2e-10 | 27/48 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 7e-09 | 29/48 (SNU-423, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.3 | 3e-08 | 28/48 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.36×** | +6.2 | 5e-08 | 28/47 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +5.8 | 5e-07 | 28/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.7 | 6e-07 | 24/48 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +5.6 | 1e-06 | 25/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.4 | 3e-06 | 23/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.29×** | +5.1 | 1e-05 | 26/47 (SNU-423, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 2e-05 | 22/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +4.9 | 4e-05 | 28/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +4.3 | 7e-04 | 18/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.003 | 20/48 (SNU-423, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.003 | 22/48 (HOP62, SW 900, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.009 | 11/48 (NCI-H460, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.730×** | -8.9 | 4e-16 | 39/48 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.645×** | -8.7 | 7e-16 | 38/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -5.9 | 8e-07 | 24/47 (AsPC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -4.9 | 2e-04 | 22/48 (A-427, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.785×** | -4.8 | 2e-04 | 24/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.806×** | -4.3 | 0.002 | 24/48 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.810×** | -4.2 | 0.002 | 25/48 (H4, HEC-1-A, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.018 | 17/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.028 | 17/48 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.849× | -3.2 | 0.065 | 12/48 (KATO III, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 32.1 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +11.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.33× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.9 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +10.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.0) | — |
| [[SW480 (line)]] | alt | 49.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 34.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +11.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 68.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -10.2) |
| [[C32 (line)]] | wt | 50.6 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.130× (z -9.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 41.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 31.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.6) | — |
| [[LoVo (line)]] | wt | 38.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +10.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 85.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -11.0) |
| [[SNU-1 (line)]] | wt | 50.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -9.4) |
| [[A498 (line)]] | wt | 55.4 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.561× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 39.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.5) |
| [[HOP62 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 85.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 43.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.327× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 52.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 69.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +9.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW48 (line)]] | wt | 47.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -8.5) |
| [[A-172 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARN]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[HERC2]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.62 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[EHMT1]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 | pathway: Regulation of TP53 Activity |
| [[AAGAB]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ATR]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 | same gene group; pathway: Cellular response to heat stress; STRING 436 |
| [[DNAJC16]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GFM1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[LETM1]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[HERC2P9]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[E2F4]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5B]] | -0.59 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[HOOK2]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[VASN]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[RYBP]] | -0.57 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.57 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[PPM1N]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[TEC]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[NDUFV2-AS1]] | -0.54 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[SPTBN4]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[VAV1]] | -0.53 | -0.40 / -0.50 | both halves | 4e-05 | pathway: Co-stimulation by CD28 |
| [[SERPINI1]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*93 arrows, 93 of them with an alert ⚠; grade A 0, B 93, C 0. Shown: the 12 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INSR]] | B | MTOR activity lowers INSR's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[FKBP14]] | B | MTOR activity raises FKBP14's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[WASHC2C]] | B | MTOR activity lowers WASHC2C's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[TSPAN13]] | B | MTOR activity raises TSPAN13's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MCM8]] | B | MTOR activity raises MCM8's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[WDR19]] | B | MTOR activity lowers WDR19's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[CENPN]] | B | MTOR activity raises CENPN's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[DTL]] | B | MTOR activity raises DTL's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[WDR62]] | B | MTOR activity raises WDR62's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MARS1]] | B | MTOR activity raises MARS1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds |
| [[SMAP2]] | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ERICH1]] | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.2, -30.5); signed map (-18.1, -53.4). **Vector** length 114, 31.2% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM |  | +4.3 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.4 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.1 | +6.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.9 | -8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.1 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.5 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.6 | -4.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | mechanistic target of rapamycin kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,106,535-11,262,556 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mTOR, RAFT1, RAPT1, FLJ44809; previously FRAP, FRAP2, FRAP1 |
| Gene groups (HGNC) | MTOR complex 1; MTOR complex 2; Armadillo like helical domain containing; Phosphatidylinositol 3-kinase-related kinase family |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 38 pathways, smallest: Dengue virus modulates apoptosis; CD28 dependent PI3K/Akt signaling; mTORC1-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P42345](https://www.uniprot.org/uniprotkb/P42345) (Serine/threonine-protein kinase mTOR):

> Serine/threonine protein kinase which is a central regulator of cellular metabolism, growth and survival in response to hormones, growth factors, nutrients, energy and stress signals. MTOR directly or indirectly regulates the phosphorylation of at least 800 proteins. Functions as part of 2 structurally and functionally distinct signaling complexes mTORC1 and mTORC2 (mTOR complex 1 and 2). In response to nutrients, growth factors or amino acids, mTORC1 is recruited to the lysosome membrane and …

**Summary**, from NCBI Gene [2475](https://www.ncbi.nlm.nih.gov/gene/2475):

> The protein encoded by this gene belongs to a family of phosphatidylinositol kinase-related kinases. These kinases mediate cellular responses to stresses such as DNA damage and nutrient deprivation. This kinase is a component of two distinct complexes, mTORC1, which controls protein synthesis, cell growth and proliferation, and mTORC2, which is a regulator of the actin cytoskeleton, and promotes cell survival and cell cycle progression. This protein acts as the target for the cell-cycle arrest …

**Accessions** — [HGNC:3942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3942) · Entrez [2475](https://www.ncbi.nlm.nih.gov/gene/2475) · UniProt [P42345](https://www.uniprot.org/uniprotkb/P42345) · Ensembl [ENSG00000198793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198793)

## Data

Gene col 12679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12679); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12679]; `tensor/DDL_lfc|DDL_z.npy` [12679]; `embed/gene_vectors.npy` [12679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12679 or target_col == 12679). Every well: [[MTOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
