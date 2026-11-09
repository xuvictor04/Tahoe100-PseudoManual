---
symbol: "ANAPC4"
type: "gene"
col: 598
ensembl_id: "ENSG00000053900"
name: "anaphase promoting complex subunit 4"
location: "4p15.2"
module: 65
arm: "+"
pooled_cpm: 43.48
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ANAPC4

*anaphase promoting complex subunit 4* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.40× (z +5.8, q 3e-06, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.530× (z -11.1, q 1e-25, down in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.641× (z -7.7, q 1e-12, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTX2]] (+0.78, fdr 7e-06), [[METTL17]] (+0.77, fdr 7e-06), [[HEATR6]] (+0.75, fdr 7e-06); moves opposite to [[HIVEP2-DT]] (-0.65, fdr 7e-06), [[NLGN3]] (-0.59, fdr 1e-05), [[PPP1R10]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HACE1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 3e-06 | 26/48 (SW 900, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +4.9 | 3e-04 | 26/48 (SW 900, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +4.2 | 0.004 | 20/48 (AsPC-1, CHP-212, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.004 | 21/48 (CFPAC-1, SW48, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.6 | 0.034 | 17/48 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.043 | 16/48 (NCI-H460, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | 1.40× | +3.1 | 0.17 | 7/48 (A-427, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.13× | +3.0 | 0.18 | 6/48 (J82, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.530×** | -11.1 | 1e-25 | 38/48 (SHP-77, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -9.8 | 3e-20 | 34/40 (A549, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -9.8 | 3e-20 | 32/43 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.705×** | -8.6 | 1e-15 | 27/48 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -7.7 | 1e-12 | 39/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -7.4 | 2e-11 | 34/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.661×** | -6.9 | 4e-10 | 32/48 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.691×** | -6.4 | 1e-08 | 29/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.693×** | -6.4 | 1e-08 | 27/47 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.724×** | -5.6 | 1e-06 | 29/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -4.6 | 2e-04 | 24/48 (A549, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.768×** | -4.4 | 5e-04 | 23/47 (SNU-423, SW48, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.657×** | -3.8 | 0.006 | 17/49 (C32, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.806×** | -3.7 | 0.007 | 20/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.807×** | -3.7 | 0.007 | 22/48 (hTERT-HPNE, A-172, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.711×** | -3.1 | 0.065 | 12/48 (Panc 03.27, C32, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.716×** | -3.0 | 0.072 | 18/48 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.4 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 36.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -16.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[hTERT-HPNE (line)]] | wt | 48.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -14.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 38.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0838× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.3) |
| [[C32 (line)]] | wt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 56.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.380× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 42.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 48.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.391× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-1 (line)]] | wt | 57.8 | 0 | 2 | — | [[Allantoin (drug)]] 0.5 µM 0.220× (z -10.0) |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -14.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CFPAC-1 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 63.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HOP62 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.279× (z -9.5) |
| [[J82 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -8.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[LoVo (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -15.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0937× (z -17.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 51.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.416× (z -10.7) |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTX2]] | +0.78 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[METTL17]] | +0.77 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.75 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[LRIG2]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[PRMT7]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SLC35A1]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ALG9]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ANAPC5]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 | same gene group; pathway: APC-Cdc20 mediated degradation of Nek2A; STRING 999 |
| [[HACE1]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TUBE1]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2-DT]] | -0.65 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[NLGN3]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PCF11]] | -0.57 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[PURB]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | C | HACE1 activity raises ANAPC4's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.47× lower at baseline in the lines without HACE1 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.839). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.5, -10.1); signed map (-30.5, -12.6). **Vector** length 104, 27.0% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.7 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.4 | +1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -6.1 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.9 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.6 | -7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | -2.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:25,377,263-25,418,498 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APC4 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJX5](https://www.uniprot.org/uniprotkb/Q9UJX5) (Anaphase-promoting complex subunit 4):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [29945](https://www.ncbi.nlm.nih.gov/gene/29945):

> A large protein complex, termed the anaphase-promoting complex (APC), or the cyclosome, promotes metaphase-anaphase transition by ubiquitinating its specific substrates such as mitotic cyclins and anaphase inhibitor, which are subsequently degraded by the 26S proteasome. Biochemical studies have shown that the vertebrate APC contains eight subunits. The composition of the APC is highly conserved in organisms from yeast to humans. The exact function of this gene product is not known. Two …

**Accessions** — [HGNC:19990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19990) · Entrez [29945](https://www.ncbi.nlm.nih.gov/gene/29945) · UniProt [Q9UJX5](https://www.uniprot.org/uniprotkb/Q9UJX5) · Ensembl [ENSG00000053900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053900)

## Data

Gene col 598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 598); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 598]; `tensor/DDL_lfc|DDL_z.npy` [598]; `embed/gene_vectors.npy` [598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 598 or target_col == 598). Every well: [[ANAPC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
