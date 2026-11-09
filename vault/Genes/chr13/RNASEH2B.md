---
symbol: "RNASEH2B"
type: "gene"
col: 5812
ensembl_id: "ENSG00000136104"
name: "ribonuclease H2 subunit B"
location: "13q14.3"
module: 18
arm: "+"
pooled_cpm: 22.51
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RNASEH2B

*ribonuclease H2 subunit B* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.09× (z +14.1, q 3e-42, up in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.30× (z +4.8, q 2e-04, up in 15 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.568× (z -15.2, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXCT1]] (+0.68, fdr 1e-05), [[CSE1L]] (+0.67, fdr 7e-06), [[TADA2A]] (+0.67, fdr 7e-06); moves opposite to [[NOSIP]] (-0.66, fdr 1e-05), [[FAM89B]] (-0.60, fdr 2e-05), [[NDRG1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EHD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +14.1 | 3e-42 | 34/43 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +11.0 | 2e-25 | 21/31 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +9.5 | 3e-19 | 26/37 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +5.7 | 2e-06 | 25/47 (SW480, PANC-1, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 15/47 (SW480, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.7 | 3e-04 | 14/48 (SNU-423, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.17× | +4.3 | 0.002 | 16/48 (NCI-H2347, J82, …) | top dose only | low cells (technical?) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.026 | 5/47 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.5 | 0.031 | 12/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.079 | 10/47 (H4, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 1.19× | +3.2 | 0.079 | 20/47 (SW480, HCT15, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.081 | 12/45 (SW480, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5812.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.568×** | -15.2 | 0e+00 | 36/47 (A498, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.510×** | -12.8 | 3e-35 | 35/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.568×** | -10.7 | 1e-24 | 32/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.604×** | -9.6 | 1e-19 | 30/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -8.0 | 2e-13 | 28/48 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.695×** | -6.9 | 5e-10 | 24/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -6.6 | 4e-09 | 28/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -5.7 | 1e-06 | 21/48 (PANC-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -5.3 | 8e-06 | 24/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.758×** | -5.3 | 8e-06 | 18/47 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.775×** | -4.8 | 8e-05 | 20/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.790×** | -4.5 | 4e-04 | 17/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.649×** | -4.3 | 8e-04 | 16/47 (Panc 03.27, J82, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.1 | 0.002 | 2/48 (RPMI-7951, hTERT-HPNE) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.812×** | -3.8 | 0.006 | 14/47 (SK-MEL-2, HEC-1-A, …) | top dose only | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.023 | 14/47 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.713×** | -3.4 | 0.024 | 11/47 (HCT15, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.797×** | -3.1 | 0.058 | 9/48 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.9 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 45.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.4) |
| [[A-427 (line)]] | wt | 34.5 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0768× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.148× (z -8.6) |
| [[PANC-1 (line)]] | alt | 22.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.7) |
| [[SW48 (line)]] | wt | 41.3 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.248× (z -8.8) |
| [[J82 (line)]] | alt | 36.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.0) |
| [[KATO III (line)]] | alt | 29.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -12.4) |
| [[LS 180 (line)]] | wt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 23.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.4) |
| [[A498 (line)]] | wt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.9) |
| [[BT-474 (line)]] | alt | 9.90 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0936× (z -9.7) |
| [[COLO 205 (line)]] | alt | 49.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -9.5) |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 9.08 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0654× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.216× (z -10.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0721× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 1 | — | [[Adenosine (drug)]] 0.05 µM 0.0676× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.8) |
| [[RKO (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.143× (z -8.7) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.9) |
| [[SW 1271 (line)]] | alt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.1) |
| [[A-172 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXCT1]] | +0.68 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CSE1L]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TADA2A]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SEPHS1]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TMEM209]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[NAE1]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[RAD51D]] | +0.64 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[USP46]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TIMELESS]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PRTFDC1]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SLC12A2-DT]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[TMPO]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOSIP]] | -0.66 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NDRG1]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[LGALS1]] | -0.58 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[KCNQ1OT1]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.57 | -0.53 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RRAS]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TRPT1]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[NBEAL1]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PLIN3]] | -0.55 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[GIPR]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RASA4B]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ATOSB]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHD2]] | B | EHD2 activity lowers RNASEH2B's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 1.69× higher at baseline in the lines without EHD2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[PDE3B]] | B | PDE3B activity raises RNASEH2B's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.39× lower at baseline in the lines without PDE3B | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[ZNF239]] | B | ZNF239 activity lowers RNASEH2B's level | lines that do not express ZNF239 (8) vs lines expressing it (42) | 1.51× higher at baseline in the lines without ZNF239 | 0.087 | ⚠ within organs, on part of the lines |
| [[MVB12B]] | B | MVB12B activity raises RNASEH2B's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without MVB12B | 0.088 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[MCM3]] | C | MCM3 activity raises RNASEH2B's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without MCM3 | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-22.7, -38.2); signed map (-3.9, -39.6). **Vector** length 95.3, 21.1% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.5 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | +4.0 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.9 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -10.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease H2 subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:50,909,747-51,024,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11712; previously DLEU8, AGS2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TBB1](https://www.uniprot.org/uniprotkb/Q5TBB1) (Ribonuclease H2 subunit B):

> Non catalytic subunit of RNase H2, an endonuclease that specifically degrades the RNA of RNA:DNA hybrids. Participates in DNA replication, possibly by mediating the removal of lagging-strand Okazaki fragment RNA primers during DNA replication. Mediates the excision of single ribonucleotides from DNA:RNA duplexes.

**Summary**, from NCBI Gene [79621](https://www.ncbi.nlm.nih.gov/gene/79621):

> RNase H2 is composed of a single catalytic subunit (A) and two non-catalytic subunits (B and C) and specifically degrades the RNA of RNA:DNA hybrids. The protein encoded by this gene is the non-catalytic B subunit of RNase H2, which is thought to play a role in DNA replication. Multiple transcript variants encoding different isoforms have been found for this gene. Defects in this gene are a cause of Aicardi-Goutieres syndrome type 2 (AGS2). [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:25671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25671) · Entrez [79621](https://www.ncbi.nlm.nih.gov/gene/79621) · UniProt [Q5TBB1](https://www.uniprot.org/uniprotkb/Q5TBB1) · Ensembl [ENSG00000136104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136104)

## Data

Gene col 5812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5812); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5812]; `tensor/DDL_lfc|DDL_z.npy` [5812]; `embed/gene_vectors.npy` [5812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5812 or target_col == 5812). Every well: [[RNASEH2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASEH2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
