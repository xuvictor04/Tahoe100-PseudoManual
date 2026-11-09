---
symbol: "SIRT3"
type: "gene"
col: 6594
ensembl_id: "ENSG00000142082"
name: "sirtuin 3"
location: "11p15.5"
module: 11
arm: "+"
pooled_cpm: 10.17
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SIRT3

*sirtuin 3* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +7.8, q 5e-12, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.389× (z -13.9, q 5e-41, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXLD1]] (+0.62, fdr 1e-05), [[ZNF446]] (+0.60, fdr 2e-05), [[CDPF1]] (+0.57, fdr 1e-05); moves opposite to [[DIO2]] (-0.50, fdr 3e-04), [[CCSER1]] (-0.49, fdr 4e-05), [[EGFEM1P]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCSER1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.8 | 5e-12 | 26/45 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +5.9 | 9e-07 | 23/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 0.001 | 14/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.011 | 11/46 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.023 | 7/40 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.028 | 5/44 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.14 | 3/39 (AsPC-1, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.22× | +3.0 | 0.18 | 7/47 (SW480, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.389×** | -13.9 | 5e-41 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -12.2 | 9e-32 | 31/43 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -10.4 | 3e-23 | 34/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.484×** | -9.8 | 2e-20 | 32/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.511×** | -9.5 | 2e-19 | 23/38 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.683×** | -7.9 | 3e-13 | 25/46 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -7.6 | 2e-12 | 26/47 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.635×** | -6.4 | 1e-08 | 21/46 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.660×** | -6.1 | 7e-08 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -5.7 | 7e-07 | 21/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -5.7 | 7e-07 | 19/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.681×** | -5.6 | 9e-07 | 20/46 (C32, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -4.8 | 8e-05 | 15/46 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.711×** | -4.7 | 1e-04 | 17/44 (J82, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.808×** | -4.4 | 4e-04 | 13/47 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.662×** | -4.3 | 6e-04 | 10/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.601×** | -3.9 | 0.003 | 7/44 (PANC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.648×** | -3.3 | 0.024 | 10/43 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.743×** | -3.1 | 0.045 | 6/46 (Panc 03.27, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.668×** | -3.1 | 0.045 | 13/42 (HS-578T, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.6 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.203× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 8.28 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.155× (z -11.3) |
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -11.5) |
| [[C32 (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.129× (z -10.4) |
| [[A-172 (line)]] | wt | 19.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 17.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -10.9) |
| [[HT-29 (line)]] | alt | 6.25 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0665× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0863× (z -9.0) |
| [[J82 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.244× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 8.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 7.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 9.09 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.22 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0828× (z -11.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 9.43 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0602× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 4.51 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.117× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 8.99 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -9.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXLD1]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ZNF446]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CDPF1]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZER1]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[LYRM9]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[CRAMP1]] | +0.55 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[FBXL9P]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ZNF48]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TMEM134]] | +0.53 | +0.29 / +0.63 | both halves | 3e-04 |  |
| [[ZNF333]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[RPUSD2]] | +0.53 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[TMEM129]] | +0.52 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIO2]] | -0.50 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[CCSER1]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[EGFEM1P]] | -0.49 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[FAM171B]] | -0.48 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[HBG2]] | -0.48 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[ACSL4]] | -0.47 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[VOPP1]] | -0.46 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[SLIT2]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[FSTL5]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MECOM]] | -0.46 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[MMP16]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ABLIM1]] | -0.46 | -0.27 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCSER1]] | B | CCSER1 activity lowers SIRT3's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 1.31× higher at baseline in the lines without CCSER1 | 0.026 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.315). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-45.9, -2.8); signed map (-7.7, -4.9). **Vector** length 50.8, 6.49% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.6 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | -1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.0 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -3.9 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.5 | -0.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | sirtuin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:215,030-236,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SIR2L3 |
| Gene groups (HGNC) | Sirtuins |
| Reactome | 12 pathways, smallest: Regulation of FOXO transcriptional activity by acetylation; Mitochondrial unfolded protein response (UPRmt); Maturation of TCA enzymes and regulation of TCA cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTG7](https://www.uniprot.org/uniprotkb/Q9NTG7) (NAD-dependent protein deacetylase sirtuin-3, mitochondrial):

> NAD-dependent protein deacetylase. Activates or deactivates mitochondrial target proteins by deacetylating key lysine residues. Known targets include ACSS1, IDH, GDH, SOD2, PDHA1, LCAD, SDHA, MRPL12 and the ATP synthase subunit ATP5PO. Contributes to the regulation of the cellular energy metabolism. Important for regulating tissue-specific ATP levels. In response to metabolic stress, deacetylates transcription factor FOXO3 and recruits FOXO3 and mitochondrial RNA polymerase POLRMT to mtDNA to …

**Summary**, from NCBI Gene [23410](https://www.ncbi.nlm.nih.gov/gene/23410):

> SIRT3 encodes a member of the sirtuin family of class III histone deacetylases, homologs to the yeast Sir2 protein. The encoded protein is found exclusively in mitochondria, where it can eliminate reactive oxygen species, inhibit apoptosis, and prevent the formation of cancer cells. SIRT3 has far-reaching effects on nuclear gene expression, cancer, cardiovascular disease, neuroprotection, aging, and metabolic control. [provided by RefSeq, May 2019]

**Accessions** — [HGNC:14931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14931) · Entrez [23410](https://www.ncbi.nlm.nih.gov/gene/23410) · UniProt [Q9NTG7](https://www.uniprot.org/uniprotkb/Q9NTG7) · Ensembl [ENSG00000142082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142082)

## Data

Gene col 6594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6594); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6594]; `tensor/DDL_lfc|DDL_z.npy` [6594]; `embed/gene_vectors.npy` [6594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6594 or target_col == 6594). Every well: [[SIRT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
