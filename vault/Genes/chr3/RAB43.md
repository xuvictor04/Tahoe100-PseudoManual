---
symbol: "RAB43"
type: "gene"
col: 10295
ensembl_id: "ENSG00000172780"
name: "RAB43, member RAS oncogene family"
location: "3q21.3"
module: 142
arm: "+"
pooled_cpm: 21.55
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# RAB43

*RAB43, member RAS oncogene family* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +6.9, q 3e-09, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.224× (z -14.4, q 2e-44, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTLL3]] (+0.67, fdr 7e-06), [[MARK4]] (+0.67, fdr 7e-06), [[SENP5]] (+0.67, fdr 1e-05); moves opposite to [[STX17]] (-0.65, fdr 9e-06), [[YTHDC2]] (-0.59, fdr 1e-05), [[TIGD2]] (-0.59, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.9 | 3e-09 | 29/46 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.8 | 5e-04 | 2/48 (NCI-H23, AsPC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.224×** | -14.4 | 2e-44 | 43/47 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.333×** | -13.2 | 2e-37 | 37/41 (Panc 03.27, A498, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.338×** | -13.0 | 1e-36 | 45/47 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.349×** | -12.7 | 2e-34 | 30/46 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.532×** | -10.7 | 8e-25 | 29/47 (A-172, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.428×** | -9.4 | 4e-19 | 30/35 (LOX-IMVI, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.423×** | -8.3 | 8e-15 | 24/30 (SNU-423, NCI-H2030, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.542×** | -7.4 | 1e-11 | 40/48 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.637×** | -5.4 | 3e-06 | 26/48 (KATO III, CFPAC-1, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -5.3 | 7e-06 | 29/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.666×** | -4.9 | 5e-05 | 24/46 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.645×** | -4.2 | 0.001 | 22/44 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.524×** | -4.1 | 0.002 | 23/44 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | **0.728×** | -3.8 | 0.005 | 22/44 (HS-578T, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.549×** | -3.8 | 0.006 | 21/44 (RPMI-7951, J82, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.695×** | -3.5 | 0.015 | 18/46 (NCI-H2030, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.032 | 16/47 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.032 | 15/48 (SK-MEL-2, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 38.3 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -14.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.108× (z -11.3) |
| [[A-172 (line)]] | wt | 33.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -20.7) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0615× (z -17.0) |
| [[A498 (line)]] | wt | 30.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0626× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 32.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 46.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0453× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.111× (z -12.5) |
| [[HT-29 (line)]] | alt | 22.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.7) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -10.0) |
| [[SW480 (line)]] | alt | 25.3 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -12.8) |
| [[A549 (line)]] | wt | 9.56 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0492× (z -15.0) |
| [[C32 (line)]] | wt | 25.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0740× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 38.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0762× (z -12.7) |
| [[HOP62 (line)]] | alt | 25.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 19.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0715× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0867× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 25.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.199× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.172× (z -8.6) |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.152× (z -9.6) |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0524× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.131× (z -9.2) |
| [[H4 (line)]] | wt | 33.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0446× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0955× (z -16.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0927× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0567× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0791× (z -10.2) |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0718× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -11.2) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0570× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -16.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.2) ⚠ cell-cycle shift, explains ~59% of this change |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0531× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0536× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.251× (z -8.6) |
| [[SHP-77 (line)]] | alt | 7.11 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0785× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -10.4) |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL3]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MARK4]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SENP5]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.64 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ARPC5L]] | +0.64 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[MBOAT7]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[CSNK1G2]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZNF251]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZNF668]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[SYCE1L]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX17]] | -0.65 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[YTHDC2]] | -0.59 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.59 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[VPS13C]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CRADD]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[DZIP3]] | -0.56 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.56 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[RFK]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[COMMD8]] | -0.55 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[CASC9]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[NT5DC1]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[AGL]] | -0.55 | -0.48 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.6, -0.7); signed map (-46.4, 0.8). **Vector** length 95.6, 23.5% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.8 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.2 | -14.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.0 | -13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB43, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:129,087,569-129,122,801 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAB41, RAB11B, ISY1 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 5 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; RAB geranylgeranylation; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YS6](https://www.uniprot.org/uniprotkb/Q86YS6) (Ras-related protein Rab-43):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. Involved in retrograde transport from the endocytic pathway to the Golgi apparatus. Required for the structural …

**Summary**, from NCBI Gene [339122](https://www.ncbi.nlm.nih.gov/gene/339122):

> Enables G protein activity. Involved in several processes, including endoplasmic reticulum to Golgi vesicle-mediated transport; regulation of Golgi organization; and retrograde transport, plasma membrane to Golgi. Located in Golgi membrane; endoplasmic reticulum-Golgi intermediate compartment membrane; and phagocytic vesicle. Is active in cis-Golgi network membrane and endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19983) · Entrez [339122](https://www.ncbi.nlm.nih.gov/gene/339122) · UniProt [Q86YS6](https://www.uniprot.org/uniprotkb/Q86YS6) · Ensembl [ENSG00000172780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172780)

## Data

Gene col 10295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10295); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10295]; `tensor/DDL_lfc|DDL_z.npy` [10295]; `embed/gene_vectors.npy` [10295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10295 or target_col == 10295). Every well: [[RAB43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
