---
symbol: "TBC1D8B"
type: "gene"
col: 5426
ensembl_id: "ENSG00000133138"
name: "TBC1 domain family member 8B"
location: "Xq22.3"
module: 56
arm: "+"
pooled_cpm: 38.91
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 36
n_dd_up_clean: 3
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TBC1D8B

*TBC1 domain family member 8B* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.39× (z +5.7, q 8e-06, up in 31 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.341× (z -26.1, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMF1]] (+0.72, fdr 7e-06), [[TMEM263]] (+0.70, fdr 7e-06), [[LYSMD3]] (+0.69, fdr 7e-06); moves opposite to [[BCAR3]] (-0.53, fdr 2e-05), [[NUDT3]] (-0.52, fdr 3e-05), [[CROCCP3-1]] (-0.50, fdr 4e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[YIPF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +5.7 | 8e-06 | 31/42 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +5.4 | 2e-05 | 22/41 (HOP62, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.9 | 1e-04 | 23/42 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.052 | 13/42 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.22× | +3.3 | 0.11 | 15/42 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.11 | 11/42 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.11 | 11/42 (HT-29, LOX-IMVI, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.11 | 10/42 (LS 180, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.11 | 13/42 (SK-MEL-2, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.14× | +3.1 | 0.11 | 9/42 (AsPC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.341×** | -26.1 | 0e+00 | 40/41 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.304×** | -20.4 | 0e+00 | 40/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.416×** | -15.0 | 0e+00 | 39/42 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.433×** | -14.3 | 2e-44 | 36/42 (HCT15, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.434×** | -14.3 | 2e-44 | 40/42 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -14.3 | 3e-44 | 36/41 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.435×** | -13.7 | 6e-41 | 35/40 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -13.1 | 2e-37 | 34/42 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -13.1 | 2e-37 | 40/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.473×** | -12.8 | 7e-36 | 39/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.566×** | -9.8 | 9e-21 | 38/42 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.567×** | -9.7 | 1e-20 | 32/42 (Hs 766T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.569×** | -9.7 | 2e-20 | 32/42 (HCT15, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -9.6 | 4e-20 | 31/41 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -9.5 | 8e-20 | 34/40 (HCT15, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -9.4 | 2e-19 | 34/42 (KATO III, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.579×** | -8.8 | 3e-17 | 33/42 (HT-29, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.697×** | -5.9 | 7e-08 | 23/42 (LoVo, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.0) |
| [[H4 (line)]] | wt | 55.1 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.2) |
| [[HCT15 (line)]] | alt | 81.0 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -22.0) |
| [[Hs 766T (line)]] | wt | 82.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -17.7) |
| [[SNU-423 (line)]] | alt | 71.8 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -26.1) |
| [[KATO III (line)]] | alt | 124 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 34.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -18.0) |
| [[PANC-1 (line)]] | alt | 43.5 | 0 | 9 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 54.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -24.7) |
| [[hTERT-HPNE (line)]] | wt | 66.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.2) |
| [[SW480 (line)]] | alt | 42.7 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.167× (z -19.7) |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -17.5) |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -21.5) |
| [[HT-29 (line)]] | alt | 77.0 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.354× (z -9.6) |
| [[LS 180 (line)]] | wt | 51.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.6) |
| [[SW 900 (line)]] | alt | 31.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -12.6) |
| [[C32 (line)]] | wt | 32.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -21.0) |
| [[LoVo (line)]] | wt | 34.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 46.5 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.5) |
| [[A498 (line)]] | wt | 56.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.2) |
| [[A549 (line)]] | wt | 17.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.4) |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 57.0 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.352× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 40.8 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.100× (z -9.8) |
| [[COLO 205 (line)]] | alt | 73.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.6) |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.127× (z -10.2) |
| [[J82 (line)]] | alt | 21.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.7) |
| [[RKO (line)]] | wt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.3) |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.251× (z -10.5) |
| [[SW 1088 (line)]] | alt | 64.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -9.4) |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 32.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.359× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMF1]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[LYSMD3]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[SLC15A2]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[EAF2]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MORF4L2]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SUCO]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[COPB1]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis |
| [[GMPPA]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SRP54]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAR3]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[NUDT3]] | -0.52 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[CROCCP3-1]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MACROD1]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NADK]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DMAC2L]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SETD6]] | -0.48 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[HSF1]] | -0.48 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[TTL]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[DPH6]] | -0.48 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YIPF5]] | B | TBC1D8B activity raises YIPF5's level | lines that do not express TBC1D8B (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without TBC1D8B | 0.063 | ⚠ within organs, on part of the lines; also absent: AHR, MYO1B, RND3 |
| [[PDXDC1]] | B | TBC1D8B activity raises PDXDC1's level | lines that do not express TBC1D8B (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without TBC1D8B | 0.089 | ⚠ within organs, on part of the lines; also absent: AHR, MYO1B, RND3; its own permutation p |
| [[CLINT1]] | B | TBC1D8B activity raises CLINT1's level | lines that do not express TBC1D8B (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without TBC1D8B | 0.089 | ⚠ within organs, on part of the lines; also absent: AHR, MYO1B, RND3; its own permutation p |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, -36.1); signed map (-51.3, 13.3). **Vector** length 95.6, 28.3% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.52 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.52 to 16); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +0.6 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -14.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.7 | -3.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.3 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.3 | -8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -9.8 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 8B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:106,802,673-106,876,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20298, RP11-321G1.1, GRAMD8B |
| Gene groups (HGNC) | EF-hand domain containing; GRAM domain containing; TBC1 domain family members |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0IIM8](https://www.uniprot.org/uniprotkb/Q0IIM8) (TBC1 domain family member 8B):

> Involved in vesicular recycling, probably as a RAB11B GTPase-activating protein.

**Summary**, from NCBI Gene [54885](https://www.ncbi.nlm.nih.gov/gene/54885):

> This gene encodes a protein with a TBC (Tre-2/Bub2/CDC16) domain. Some mammalian proteins with this domain have been shown to function as Rab-GAPs by binding to specific Rab proteins and affecting their GTPase activity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:24715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24715) · Entrez [54885](https://www.ncbi.nlm.nih.gov/gene/54885) · UniProt [Q0IIM8](https://www.uniprot.org/uniprotkb/Q0IIM8) · Ensembl [ENSG00000133138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133138)

## Data

Gene col 5426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5426); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5426]; `tensor/DDL_lfc|DDL_z.npy` [5426]; `embed/gene_vectors.npy` [5426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5426 or target_col == 5426). Every well: [[TBC1D8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
