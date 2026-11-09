---
symbol: "GIT2"
type: "gene"
col: 6306
ensembl_id: "ENSG00000139436"
name: "GIT ArfGAP 2"
location: "12q24.11"
module: 30
arm: "+"
pooled_cpm: 51.98
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GIT2

*GIT ArfGAP 2* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.74× (z +11.0, q 1e-25, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -19.7, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A6]] (+0.69, fdr 1e-05), [[CDK5RAP1]] (+0.66, fdr 7e-06), [[KIAA2013]] (+0.63, fdr 1e-05); moves opposite to [[NANOS3]] (-0.61, fdr 1e-05), [[ABCA10]] (-0.59, fdr 6e-05), [[MTNR1A]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +11.0 | 1e-25 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +10.5 | 3e-23 | 43/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +8.6 | 2e-15 | 38/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +5.8 | 1e-06 | 33/48 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.9 | 1e-04 | 21/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 0.001 | 23/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.007 | 20/49 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.028 | 9/48 (A-427, hTERT-HPNE, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.030 | 14/48 (KATO III, PANC-1, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.4 | 0.045 | 13/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.075 | 10/48 (HCT15, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -19.7 | 0e+00 | 36/48 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -11.4 | 1e-27 | 33/45 (RKO, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.625×** | -9.4 | 1e-18 | 37/49 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.614×** | -9.4 | 1e-18 | 31/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -9.2 | 4e-18 | 32/42 (SHP-77, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -8.6 | 1e-15 | 33/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -7.1 | 9e-11 | 37/47 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -5.1 | 2e-05 | 25/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.797×** | -4.5 | 3e-04 | 21/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.804× | -3.1 | 0.11 | 9/48 (RKO, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 0.807× | -3.1 | 0.11 | 11/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 131 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -27.6) |
| [[NCI-H460 (line)]] | wt | 61.4 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -22.0) |
| [[AsPC-1 (line)]] | alt | 65.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -26.4) |
| [[HEC-1-A (line)]] | alt | 53.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.574× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 65.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 58.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -20.6) |
| [[PANC-1 (line)]] | alt | 42.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.29× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 62.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.4) |
| [[A-172 (line)]] | wt | 60.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -14.6) |
| [[A-427 (line)]] | wt | 42.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 48.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -19.0) |
| [[A549 (line)]] | wt | 56.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.3) |
| [[H4 (line)]] | wt | 47.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.213× (z -9.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.0) |
| [[HOP62 (line)]] | alt | 53.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -16.0) |
| [[Hs 766T (line)]] | wt | 54.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.5) |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 47.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 47.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 64.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 36.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -13.2) |
| [[SHP-77 (line)]] | alt | 58.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -17.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 53.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.3) |
| [[AN3 CA (line)]] | alt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -10.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 40.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -11.1) |
| [[CHP-212 (line)]] | wt | 49.8 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.152× (z -8.5) |
| [[COLO 205 (line)]] | alt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.8) |
| [[HCT15 (line)]] | alt | 52.7 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.258× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -11.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.8) |
| [[J82 (line)]] | alt | 54.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -11.0) |
| [[KATO III (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 52.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -13.4) |
| [[RKO (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.274× (z -9.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 62.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -17.8) |
| [[SW1417 (line)]] | alt | 39.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.4) |
| [[C-33 A (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | +0.69 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[KIAA2013]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RHOT1]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CDAN1]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ATPAF2]] | +0.61 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[MMS19]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ATRN]] | +0.59 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[UNC45A]] | +0.58 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[CCZ1B]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SNTA1]] | +0.58 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NANOS3]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.59 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[MTNR1A]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SLC2A9]] | -0.55 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[NFATC1]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[FKRP]] | -0.54 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[UBE2D3-AS1]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[SYNGAP1]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SRSF6]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SLC22A1]] | -0.54 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[HIVEP2-DT]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MMP25]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GIT2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SNTA1]] | B | SNTA1 activity raises GIT2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.24× lower at baseline in the lines without SNTA1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-5.2, -16.4); signed map (-36.2, -2.0). **Vector** length 97.4, 24.4% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.7 | +10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +11.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.3 | -19.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.5 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.7 | -11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.9 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | GIT ArfGAP 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,929,804-109,996,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0148, PKL |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing |
| Reactome | 11 pathways, smallest: RHOV GTPase cycle; RHOU GTPase cycle; RHOJ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14161](https://www.uniprot.org/uniprotkb/Q14161) (ARF GTPase-activating protein GIT2):

> GTPase-activating protein for ADP ribosylation factor family members, including ARF1.

**Summary**, from NCBI Gene [9815](https://www.ncbi.nlm.nih.gov/gene/9815):

> This gene encodes a member of the GIT protein family, which interact with G protein-coupled receptor kinases and possess ADP-ribosylation factor (ARF) GTPase-activating protein (GAP) activity. GIT proteins traffic between cytoplasmic complexes, focal adhesions, and the cell periphery, and interact with Pak interacting exchange factor beta (PIX) to form large oligomeric complexes that transiently recruit other proteins. GIT proteins regulate cytoskeletal dynamics and participate in receptor …

**Accessions** — [HGNC:4273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4273) · Entrez [9815](https://www.ncbi.nlm.nih.gov/gene/9815) · UniProt [Q14161](https://www.uniprot.org/uniprotkb/Q14161) · Ensembl [ENSG00000139436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139436)

## Data

Gene col 6306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6306); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6306]; `tensor/DDL_lfc|DDL_z.npy` [6306]; `embed/gene_vectors.npy` [6306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6306 or target_col == 6306). Every well: [[GIT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
