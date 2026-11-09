---
symbol: "CASC2"
type: "gene"
col: 10844
ensembl_id: "ENSG00000177640"
name: "cancer susceptibility 2"
location: "10q26.11"
module: 10
arm: "+"
pooled_cpm: 15.24
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 36
n_dd_up_clean: 10
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CASC2

*cancer susceptibility 2* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.60× (z +3.9, q 0.049, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.181× (z -14.5, q 3e-45, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC191]] (+0.71, fdr 7e-06), [[SPATA17]] (+0.70, fdr 7e-06), [[FAM174A-DT]] (+0.68, fdr 7e-06); moves opposite to [[SPSB1]] (-0.54, fdr 2e-05), [[EXTL3]] (-0.53, fdr 1e-05), [[TMEM184B]] (-0.52, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[FBXO15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.049 | 20/44 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.049 | 21/45 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.049 | 22/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.049 | 19/46 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.051 | 19/46 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.060 | 18/44 (KATO III, LS 180, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.070 | 6/46 (HOP62, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +3.3 | 0.070 | 19/46 (NCI-H1573, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.070 | 16/46 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.077 | 15/45 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.077 | 19/46 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.181×** | -14.5 | 3e-45 | 44/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.202×** | -13.6 | 1e-39 | 41/44 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.235×** | -12.3 | 2e-32 | 42/45 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.261×** | -11.4 | 5e-28 | 42/45 (HCT15, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.396×** | -7.9 | 4e-13 | 40/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.385×** | -7.8 | 6e-13 | 32/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.552×** | -7.1 | 9e-11 | 27/45 (COLO 205, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.208×** | -7.0 | 2e-10 | 35/41 (A549, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.449×** | -6.5 | 4e-09 | 28/45 (Panc 03.27, MIA PaCa-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.233×** | -6.5 | 5e-09 | 34/46 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.484×** | -6.2 | 4e-08 | 31/45 (HCT15, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.406×** | -6.1 | 6e-08 | 29/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.502×** | -5.6 | 8e-07 | 26/38 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.517×** | -5.6 | 8e-07 | 29/45 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.546×** | -5.1 | 1e-05 | 27/44 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.661×** | -5.0 | 2e-05 | 31/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.592×** | -4.4 | 3e-04 | 26/43 (SNU-1, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.694×** | -4.4 | 4e-04 | 24/46 (CHP-212, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.582×** | -4.3 | 4e-04 | 23/45 (Hs 766T, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.611×** | -4.0 | 0.002 | 22/44 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.632×** | -3.9 | 0.002 | 20/46 (PANC-1, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.2 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0647× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0874× (z -10.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.177× (z -9.7) |
| [[SW480 (line)]] | alt | 20.0 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0638× (z -17.6) |
| [[COLO 205 (line)]] | alt | 25.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0249× (z -17.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0441× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 36.6 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -14.0) |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0309× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -12.1) |
| [[A-427 (line)]] | wt | 23.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -8.6) |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0438× (z -13.8) |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0431× (z -13.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0909× (z -10.6) |
| [[A549 (line)]] | wt | 19.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.8) ⚠ cell-cycle shift, explains ~82% of this change |
| [[C-33 A (line)]] | alt | 32.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0261× (z -17.4) |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -10.7) |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0342× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0373× (z -12.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 17.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0310× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.118× (z -9.4) |
| [[H4 (line)]] | wt | 13.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0597× (z -10.2) |
| [[J82 (line)]] | alt | 6.53 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -12.5) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.110× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0262× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0909× (z -9.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -9.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.188× (z -8.6) |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0464× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0858× (z -10.8) |
| [[KATO III (line)]] | alt | 16.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.169× (z -8.6) |
| [[A498 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC191]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SPATA17]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FAM174A-DT]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[C11orf65]] | +0.61 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[LRRC51]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ZRANB2-DT]] | +0.59 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[TCTN1]] | +0.58 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[SUMF1]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ZFHX3-AS1]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SLX4IP]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SPEF2]] | +0.54 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[SLC24A1]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPSB1]] | -0.54 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[EXTL3]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.52 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[THSD1]] | -0.48 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[RUNDC3A-AS1]] | -0.46 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[LYG1]] | -0.46 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[POR]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[CCDC168]] | -0.46 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ST6GALNAC6-1]] | -0.45 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ESRRA]] | -0.45 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[HMOX2]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[LINC00862]] | -0.44 | -0.29 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO15]] | B | FBXO15 activity raises CASC2's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without FBXO15 | 0.003 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[KATNAL2]] | B | KATNAL2 activity raises CASC2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without KATNAL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CASC2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[RDM1P5]] | B | RDM1P5 activity raises CASC2's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 2.11× lower at baseline in the lines without RDM1P5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[PRKN]] | B | PRKN activity raises CASC2's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.12× lower at baseline in the lines without PRKN | 0.044 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[WWOX]] | B | WWOX activity raises CASC2's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without WWOX | 0.056 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[EFCAB6]] | B | EFCAB6 activity raises CASC2's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without EFCAB6 | 0.065 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[TTC30A]] | B | TTC30A activity raises CASC2's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without TTC30A | 0.079 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[KLHL29]] | B | KLHL29 activity raises CASC2's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 2.04× lower at baseline in the lines without KLHL29 | 0.087 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers CASC2's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[CCDC171]] | C | CCDC171 activity raises CASC2's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 3.37× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SPATA17]] | C | SPATA17 activity raises CASC2's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.388). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.5, 27.8); signed map (3.2, 5.1). **Vector** length 64.9, 14.4% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.4 | -6.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.4 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.6 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | cancer susceptibility 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q26.11 — chr10:118,046,279-118,210,158 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C10orf5 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6XLA1](https://www.uniprot.org/uniprotkb/Q6XLA1) (Protein CASC2, isoform 3):

> May act as a potential tumor suppressor.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22933) · Entrez [255082](https://www.ncbi.nlm.nih.gov/gene/255082) · UniProt [Q6XLA1](https://www.uniprot.org/uniprotkb/Q6XLA1) · Ensembl [ENSG00000177640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177640)

## Data

Gene col 10844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10844); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10844]; `tensor/DDL_lfc|DDL_z.npy` [10844]; `embed/gene_vectors.npy` [10844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10844 or target_col == 10844). Every well: [[CASC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
