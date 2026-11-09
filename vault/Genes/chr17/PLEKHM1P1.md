---
symbol: "PLEKHM1P1"
type: "gene"
col: 13180
ensembl_id: "ENSG00000214176"
name: "pleckstrin homology and RUN domain containing M1 pseudogene 1"
location: "17q24.1"
module: 34
arm: "+"
pooled_cpm: 31.07
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 31
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PLEKHM1P1

*pleckstrin homology and RUN domain containing M1 pseudogene 1* — 17q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.33× (z +4.4, q 0.008, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.487× (z -11.0, q 2e-25, down in 29 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.617× (z -7.1, q 2e-10, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHM1]] (+0.83, fdr 7e-06), [[KPNA2P3]] (+0.75, fdr 7e-06, ⚠ same locus), [[ARHGAP27P1-BPTFP1-KPNA2P3]] (+0.75, fdr 7e-06, ⚠ same locus), [[RDH13]] (+0.69, fdr 1e-05), [[PLEK2]] (+0.69, fdr 7e-06); moves opposite to [[CFAP418]] (-0.61, fdr 3e-05), [[NFIB]] (-0.58, fdr 1e-05), [[ZNF280D]] (-0.57, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.4 | 0.008 | 22/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.037 | 18/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.25× | +3.4 | 0.11 | 17/47 (SW48, H4, …) | inconsistent across doses | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.51× | +3.3 | 0.11 | 13/48 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.24× | +3.3 | 0.11 | 17/48 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.487×** | -11.0 | 2e-25 | 29/42 (COLO 205, SW480, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.556×** | -8.7 | 1e-15 | 34/44 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.605×** | -7.4 | 3e-11 | 30/47 (LoVo, CFPAC-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -7.1 | 2e-10 | 30/48 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -7.1 | 2e-10 | 33/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.610×** | -7.0 | 2e-10 | 23/37 (HEC-1-A, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.632×** | -6.8 | 1e-09 | 23/34 (A-172, SW 900, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -6.3 | 3e-08 | 27/48 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -6.1 | 9e-08 | 27/47 (LS 180, H4, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.690×** | -5.7 | 8e-07 | 23/45 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -5.3 | 7e-06 | 26/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -4.7 | 1e-04 | 24/48 (NCI-H1573, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.738×** | -4.6 | 1e-04 | 24/49 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.739×** | -4.6 | 2e-04 | 22/47 (LoVo, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.732×** | -4.6 | 2e-04 | 23/47 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.574×** | -4.4 | 3e-04 | 19/46 (AsPC-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.577×** | -4.4 | 4e-04 | 22/45 (A549, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.821×** | -3.7 | 0.006 | 21/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.635×** | -3.6 | 0.007 | 17/47 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.859× | -3.3 | 0.027 | 13/48 (COLO 205, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.799×** | -3.2 | 0.035 | 15/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.035 | 14/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.676×** | -3.1 | 0.037 | 17/46 (SHP-77, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 65.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.327× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 67.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 33.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 57.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 27.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -9.0) |
| [[SNU-423 (line)]] | alt | 43.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.0) |
| [[A-172 (line)]] | wt | 28.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.439× (z -9.1) |
| [[A-427 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -8.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A549 (line)]] | wt | 31.7 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0786× (z -9.8) |
| [[BT-474 (line)]] | alt | 28.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.275× (z -8.7) |
| [[COLO 205 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 54.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0827× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0876× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW48 (line)]] | wt | 17.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.106× (z -8.8) |
| [[SW480 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHM1]] | +0.83 | +0.86 / +0.79 | both halves | 7e-06 |  |
| [[KPNA2P3]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 | ⚠ same locus (26.7 kb, same strand: neighbours can correlate without regulation) |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 | ⚠ same locus (3.6 kb, same strand: neighbours can correlate without regulation) |
| [[RDH13]] | +0.69 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.68 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[PPARD]] | +0.68 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[LRRC8A]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[ARHGEF18]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TINAGL1]] | +0.64 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TMC7]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[DENND2C]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ABTB1]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP418]] | -0.61 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[NFIB]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[USP24]] | -0.57 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[XPO1]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[TBC1D5]] | -0.54 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[GAS2]] | -0.54 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[MBNL3]] | -0.54 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[PAIP1]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[EIF1B-AS1]] | -0.53 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[CNTLN]] | -0.52 | -0.55 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 31, C 0. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises PLEKHM1P1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without TINAGL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[CEACAM1]] | B | CEACAM1 activity raises PLEKHM1P1's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.51× lower at baseline in the lines without CEACAM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[TFF2]] | B | TFF2 activity raises PLEKHM1P1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 1.93× lower at baseline in the lines without TFF2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[TFF1]] | B | TFF1 activity raises PLEKHM1P1's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 1.56× lower at baseline in the lines without TFF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[PLEK2]] | B | PLEK2 activity raises PLEKHM1P1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without PLEK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[LINC02725]] | B | LINC02725 activity raises PLEKHM1P1's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 1.35× lower at baseline in the lines without LINC02725 | 0.010 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425 |
| [[TMCC3]] | B | TMCC3 activity raises PLEKHM1P1's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without TMCC3 | 0.011 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PRSS3]] | B | PRSS3 activity raises PLEKHM1P1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.62× lower at baseline in the lines without PRSS3 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[ABHD17C]] | B | ABHD17C activity raises PLEKHM1P1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without ABHD17C | 0.013 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[LAMC2]] | B | LAMC2 activity raises PLEKHM1P1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.49× lower at baseline in the lines without LAMC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[S100A16]] | B | S100A16 activity raises PLEKHM1P1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without S100A16 | 0.017 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[TOR4A]] | B | TOR4A activity raises PLEKHM1P1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without TOR4A | 0.021 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.1, 53.9); signed map (0.7, 36.9). **Vector** length 102, 25.1% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +0.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.2 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | -0.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.9 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -8.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.3 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RUN domain containing M1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 17q24.1 — chr17:64,785,259-64,829,208 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | LOC440456; previously PLEKHM1P |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35411) · Entrez [440456](https://www.ncbi.nlm.nih.gov/gene/440456) · Ensembl [ENSG00000214176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214176)

## Data

Gene col 13180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13180); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13180]; `tensor/DDL_lfc|DDL_z.npy` [13180]; `embed/gene_vectors.npy` [13180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13180 or target_col == 13180). Every well: [[PLEKHM1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHM1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
