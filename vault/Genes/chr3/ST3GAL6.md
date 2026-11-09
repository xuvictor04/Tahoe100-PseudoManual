---
symbol: "ST3GAL6"
type: "gene"
col: 740
ensembl_id: "ENSG00000064225"
name: "ST3 beta-galactoside alpha-2,3-sialyltransferase 6"
location: "3q12.1"
module: 92
arm: "+"
pooled_cpm: 74.25
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ST3GAL6

*ST3 beta-galactoside alpha-2,3-sialyltransferase 6* — 3q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.86× (z +11.8, q 2e-29, up in 16 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +10.2, q 7e-22, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.509× (z -13.4, q 6e-38, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK14]] (+0.53, fdr 4e-05), [[CNIH3]] (+0.53, fdr 2e-05), [[SATB2]] (+0.53, fdr 4e-05); moves opposite to [[ALDH3B1]] (-0.50, fdr 1e-05), [[PLRG1]] (-0.47, fdr 7e-05), [[HAX1]] (-0.46, fdr 7e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MAMLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +11.8 | 2e-29 | 16/33 (Panc 03.27, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +10.2 | 7e-22 | 24/41 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.1 | 3e-10 | 19/39 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 1e-07 | 20/40 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.0 | 2e-07 | 16/42 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.0 | 2e-07 | 18/39 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.9 | 4e-07 | 21/39 (AN3 CA, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.004 | 18/40 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 7/40 (NCI-H2030, AN3 CA, …) | top dose only | position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.006 | 4/40 (SNU-423, hTERT-HPNE, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.010 | 6/41 (SNU-423, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.22×** | +3.6 | 0.013 | 14/35 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimatoprost (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.042 | 7/41 (SW480, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.050 | 5/41 (SW480, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.078 | 4/40 (SNU-423, SW480, …) | all doses, flat | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.099 | 9/40 (A-172, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.509×** | -13.4 | 6e-38 | 32/40 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.518×** | -13.0 | 2e-36 | 31/40 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -10.7 | 2e-24 | 30/40 (Hs 766T, C32, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -10.3 | 9e-23 | 26/40 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.738×** | -6.1 | 1e-07 | 21/42 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.754×** | -5.2 | 2e-05 | 13/40 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.772×** | -5.1 | 2e-05 | 16/40 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.785×** | -5.0 | 4e-05 | 19/41 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.851× | -4.4 | 8e-04 | 11/40 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.804×** | -4.2 | 0.002 | 14/40 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.816×** | -4.0 | 0.003 | 15/40 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.856× | -3.8 | 0.007 | 15/40 (Hs 766T, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.827×** | -3.8 | 0.007 | 13/41 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -3.6 | 0.011 | 2/42 (HOP62, SW48) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.833× | -3.6 | 0.012 | 17/40 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.823×** | -3.6 | 0.013 | 11/39 (CFPAC-1, CHP-212, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.834× | -3.4 | 0.019 | 13/39 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.862× | -3.4 | 0.019 | 12/40 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 398 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0887× (z -19.5) |
| [[Hs 766T (line)]] | wt | 586 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0338× (z -20.1) |
| [[LOX-IMVI (line)]] | wt | 184 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.2) |
| [[SK-MEL-2 (line)]] | alt | 350 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0841× (z -18.1) |
| [[J82 (line)]] | alt | 109 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -13.7) |
| [[A498 (line)]] | wt | 43.0 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.435× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 47.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.375× (z -9.4) |
| [[SW 900 (line)]] | alt | 93.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 80.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -9.6) |
| [[HOP62 (line)]] | alt | 116 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -11.7) |
| [[HS-578T (line)]] | alt | 94.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 41.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 94.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.1) |
| [[SHP-77 (line)]] | alt | 68.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -11.7) |
| [[SW 1271 (line)]] | alt | 69.5 | 0 | 2 | — | [[Rifaximin (drug)]] 0.05 µM 0.0711× (z -8.9) |
| [[A-427 (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.9) |
| [[A549 (line)]] | wt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +10.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 88.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.9) |
| [[LS 180 (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.80× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 44.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -9.8) |
| [[A-172 (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK14]] | +0.53 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[CNIH3]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[SATB2]] | +0.53 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[RPSAP52]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[TRBC2]] | +0.51 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[B4GALT6]] | +0.49 | +0.45 / +0.40 | both halves | 5e-05 | pathway: Asparagine N-linked glycosylation |
| [[RHOJ]] | +0.49 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SCHIP1]] | +0.49 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[LINC02934]] | +0.49 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[ANKH]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ING2-DT]] | +0.48 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[RASGRF2]] | +0.48 | +0.43 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3B1]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PLRG1]] | -0.47 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[HAX1]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[MUC1]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[KBTBD7]] | -0.45 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[METTL14]] | -0.44 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[NUDT12]] | -0.43 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[CCDC6]] | -0.42 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[RASSF4]] | -0.42 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[RNF20]] | -0.42 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[RAD17]] | -0.42 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[MAP3K13]] | -0.42 | -0.39 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ST3GAL6's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOX5]] | B | SOX5 activity raises ST3GAL6's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without SOX5 | 0.065 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5 |
| [[TOP2A]] | B | TOP2A activity lowers ST3GAL6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAMLD1]] | B | ST3GAL6 activity raises MAMLD1's level | lines that do not express ST3GAL6 (8) vs lines expressing it (42) | 4.30× lower at baseline in the lines without ST3GAL6 | 0.024 | ⚠ within organs, on part of the lines; also absent: DCBLD2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.8, 9.3); signed map (12.8, 50.8). **Vector** length 105, 25.0% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.7 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.6 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -5.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | ST3 beta-galactoside alpha-2,3-sialyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.1 — chr3:98,732,236-98,821,201 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ST3GALVI; previously SIAT10 |
| Gene groups (HGNC) | Sialyltransferases |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 13 pathways, smallest: Lewis blood group biosynthesis; Blood group systems biosynthesis; Pre-NOTCH Processing in Golgi |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y274](https://www.uniprot.org/uniprotkb/Q9Y274) (Type 2 lactosamine alpha-2,3-sialyltransferase):

> Transfers the sialyl residue from CMP-N-acetyl-beta-neuraminate to the terminal galactose residue on sugar chains of glycoproteins and glycolipids. Its alpha-2,3-sialyltransferase activity is specific toward type II glycan chains (Galbeta1-4GlcNAc) on glycoproteins and glycolipids such as neolactosides nLc4Cer and nLc6Cer, whose sialyl-products serve as precursors for the Lewis X antigen. Critically involved in the synthesis of functional selectin ligands needed for neutrophil recruitment …

**Summary**, from NCBI Gene [10402](https://www.ncbi.nlm.nih.gov/gene/10402):

> The protein encoded by this gene is a member of the sialyltransferase family. Members of this family are enzymes that transfer sialic acid from the activated cytidine 5'-monophospho-N-acetylneuraminic acid to terminal positions on sialylated glycolipids (gangliosides) or to the N- or O-linked sugar chains of glycoproteins. This protein has high specificity for neolactotetraosylceramide and neolactohexaosylceramide as glycolipid substrates and may contribute to the formation of selectin ligands …

**Accessions** — [HGNC:18080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18080) · Entrez [10402](https://www.ncbi.nlm.nih.gov/gene/10402) · UniProt [Q9Y274](https://www.uniprot.org/uniprotkb/Q9Y274) · Ensembl [ENSG00000064225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064225)

## Data

Gene col 740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 740); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 740]; `tensor/DDL_lfc|DDL_z.npy` [740]; `embed/gene_vectors.npy` [740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 740 or target_col == 740). Every well: [[ST3GAL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST3GAL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
