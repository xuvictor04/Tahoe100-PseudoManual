---
symbol: "CUTC"
type: "gene"
col: 4138
ensembl_id: "ENSG00000119929"
name: "cutC copper transporter"
location: "10q24.2"
module: 49
arm: "+"
pooled_cpm: 46.08
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# CUTC

*cutC copper transporter* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.61× (z +10.2, q 1e-21, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.692× (z -11.0, q 3e-25, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTPD7]] (+0.85, fdr 7e-06, ⚠ same locus), [[TMED3]] (+0.76, fdr 7e-06), [[LINC02693]] (+0.70, fdr 7e-06), [[NBPF20]] (+0.64, fdr 1e-05); moves opposite to [[UBR5]] (-0.58, fdr 4e-05), [[FMR1]] (-0.57, fdr 1e-05), [[HMGN2]] (-0.57, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +10.2 | 1e-21 | 29/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.3 | 4e-05 | 18/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +5.2 | 5e-05 | 20/48 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.1 | 6e-05 | 19/48 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +5.0 | 6e-05 | 22/47 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.3 | 0.002 | 22/49 (NCI-H1573, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.006 | 13/48 (SW 900, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +3.9 | 0.006 | 15/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.014 | 10/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.015 | 19/48 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.5 | 0.023 | 15/48 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.089 | 5/48 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.089 | 14/48 (C32, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -11.0 | 3e-25 | 32/48 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -10.7 | 2e-24 | 34/48 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.826×** | -5.7 | 2e-06 | 26/48 (A-172, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -5.6 | 3e-06 | 22/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.764×** | -5.6 | 3e-06 | 22/48 (RKO, A498, …) | rises with dose | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.817×** | -4.9 | 7e-05 | 20/48 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.781×** | -4.9 | 7e-05 | 20/42 (Panc 03.27, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -4.4 | 8e-04 | 21/49 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 5 µM |  | 0.867× | -4.3 | 0.001 | 12/48 (RKO, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.823×** | -4.2 | 0.002 | 18/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.9 | 0.005 | 17/48 (RKO, J82, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.6 | 0.012 | 14/49 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.887× | -3.6 | 0.017 | 16/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.5 | 0.017 | 10/47 (RKO, NCI-H2030, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.716×** | -3.5 | 0.021 | 14/46 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.870× | -3.4 | 0.026 | 12/48 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.894× | -3.3 | 0.028 | 9/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.035 | 13/48 (SW48, RKO, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.857× | -3.2 | 0.045 | 17/47 (RKO, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.056 | 13/49 (AsPC-1, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 152 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.9) |
| [[AsPC-1 (line)]] | alt | 65.6 | 1 | 8 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.18× (z +8.8) | [[Trametinib (drug)]] 5 µM 0.277× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.329× (z -9.9) |
| [[A498 (line)]] | wt | 80.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -16.0) |
| [[J82 (line)]] | alt | 41.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 69.9 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.13× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.1) |
| [[A549 (line)]] | wt | 61.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.5) |
| [[HS-578T (line)]] | alt | 49.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.4) |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H2030 (line)]] | alt | 58.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 40.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -8.8) |
| [[A-172 (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.25× (z +10.0) | — |
| [[H4 (line)]] | wt | 58.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.2) |
| [[LoVo (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LOX-IMVI (line)]] | wt | 37.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 79.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -13.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0845× (z -9.9) |
| [[SW48 (line)]] | wt | 28.8 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0825× (z -11.8) |
| [[A-427 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTPD7]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 | STRING 448; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TMED3]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[LINC02693]] | +0.70 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NBPF20]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[YKT6]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SEC22B]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CNST]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[HM13]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TRIM27]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[NBPF9]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[EFL1]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[EP400P1]] | +0.58 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBR5]] | -0.58 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[FMR1]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.57 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PLXNB2]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[CHASERR]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[DYRK1A]] | -0.55 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[DDR1]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CFAP418]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZHX1]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CILK1]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[SIAH1]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[YAP1]] | -0.53 | -0.33 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CUTC's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers CUTC's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ENTPD7]] | C | ENTPD7's natural level strengthens CUTC's drug response | ENTPD7's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.57; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, -32.8); signed map (-50.9, 7.1). **Vector** length 112, 28.2% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +10.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.2 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cutC copper transporter |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:99,702,558-99,756,134 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-32 |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTM9](https://www.uniprot.org/uniprotkb/Q9NTM9) (Copper homeostasis protein cutC homolog):

> May play a role in copper homeostasis. Can bind one Cu(1+) per subunit.

**Summary**, from NCBI Gene [51076](https://www.ncbi.nlm.nih.gov/gene/51076):

> Members of the CUT family of copper transporters are associated with copper homeostasis and are involved in the uptake, storage, delivery, and efflux of copper (Gupta et al., 1995 [PubMed 7635807]; Li et al., 2005 [PubMed 16182249]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24271) · Entrez [51076](https://www.ncbi.nlm.nih.gov/gene/51076) · UniProt [Q9NTM9](https://www.uniprot.org/uniprotkb/Q9NTM9) · Ensembl [ENSG00000119929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119929)

## Data

Gene col 4138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4138); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4138]; `tensor/DDL_lfc|DDL_z.npy` [4138]; `embed/gene_vectors.npy` [4138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4138 or target_col == 4138). Every well: [[CUTC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUTC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
