---
symbol: "NCKAP5L"
type: "gene"
col: 9493
ensembl_id: "ENSG00000167566"
name: "NCK associated protein 5 like"
location: "12q13.12"
module: 162
arm: "+"
pooled_cpm: 19.55
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 26
n_dd_up_clean: 12
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# NCKAP5L

*NCK associated protein 5 like* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.07× (z +13.4, q 5e-38, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.533× (z -7.5, q 5e-11, down in 27 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.626× (z -5.6, q 5e-06, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASMTL]] (+0.64, fdr 7e-06), [[RALY]] (+0.63, fdr 2e-05), [[ASTL]] (+0.63, fdr 1e-05); moves opposite to [[FBXW4]] (-0.54, fdr 4e-05), [[TBC1D22B]] (-0.53, fdr 1e-04), [[VRK2]] (-0.53, fdr 2e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LAG3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.07×** | +13.4 | 5e-38 | 45/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +12.0 | 8e-31 | 45/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +9.1 | 2e-17 | 32/47 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +7.9 | 4e-13 | 36/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +6.5 | 8e-09 | 31/46 (NCI-H2347, LoVo, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 8e-05 | 27/46 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.6 | 3e-04 | 24/47 (SW 900, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 0.001 | 22/47 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.002 | 20/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.008 | 18/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.015 | 17/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.097 | 14/47 (HCT15, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.533×** | -7.5 | 5e-11 | 27/43 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -6.9 | 1e-09 | 21/30 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.626×** | -5.6 | 5e-06 | 29/47 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.629×** | -5.5 | 5e-06 | 25/46 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -5.2 | 2e-05 | 28/44 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -4.5 | 7e-04 | 23/47 (LOX-IMVI, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -4.4 | 9e-04 | 24/47 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.687×** | -4.3 | 0.001 | 22/45 (NCI-H23, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.699×** | -4.2 | 0.001 | 18/44 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -4.2 | 0.002 | 20/38 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.708×** | -4.1 | 0.002 | 22/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.718×** | -3.9 | 0.004 | 18/47 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.792×** | -3.9 | 0.004 | 23/47 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.010 | 14/46 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.776×** | -3.5 | 0.015 | 17/47 (NCI-H1573, SW1417, …) | two highest doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.586×** | -3.3 | 0.032 | 16/45 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.765×** | -3.2 | 0.045 | 19/46 (C-33 A, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.756×** | -3.1 | 0.059 | 12/46 (SW480, A-172, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.758×** | -3.0 | 0.062 | 18/46 (LS 180, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **0.797×** | -3.0 | 0.068 | 15/47 (NCI-H460, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.777×** | -3.0 | 0.068 | 18/46 (NCI-H23, SW480, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.89× (z +11.0) | [[Harringtonine (drug)]] 0.5 µM 0.243× (z -8.7) |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 3 | — | [[Bendamustine (drug)]] 5 µM 0.0960× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 18.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.3) | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +11.8) | — |
| [[A549 (line)]] | wt | 16.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.30× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -9.1) ⚠ toxic |
| [[HOP62 (line)]] | alt | 19.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.5) | [[Docetaxel (drug)]] 0.05 µM 0.155× (z -12.4) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 10.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.93× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 11.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.16× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 28.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -12.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 38.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 17.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.40× (z +9.7) | — |
| [[SW480 (line)]] | alt | 34.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.91× (z +11.4) | — |
| [[C32 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0943× (z -13.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0454× (z -15.4) |
| [[KATO III (line)]] | alt | 5.22 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.14× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0465× (z -22.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[RALY]] | +0.63 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[ASTL]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[EGR3]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[EGR2]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PLEKHO2]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TGFB1]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[BCORL1]] | +0.60 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[HCN2]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[EGR1]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ETV5]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DLG4]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW4]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TBC1D22B]] | -0.53 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[VRK2]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ENTPD3-AS1]] | -0.52 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[DERA]] | -0.51 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[PCMTD1-DT]] | -0.50 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[RNF146]] | -0.50 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[RNPC3]] | -0.50 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[LSM6]] | -0.50 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[ANXA4]] | -0.49 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[AMY2B]] | -0.49 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[AHI1-DT]] | -0.49 | -0.37 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAG3]] | B | LAG3 activity raises NCKAP5L's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 2.04× lower at baseline in the lines without LAG3 | 0.047 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[ASTL]] | B | ASTL activity raises NCKAP5L's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.12× lower at baseline in the lines without ASTL | 0.053 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NCKAP5L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers NCKAP5L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NAB2]] | C | NAB2 activity raises NCKAP5L's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without NAB2 | 0.007 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, -1.3); signed map (3.3, 28.2). **Vector** length 99.8, 24.2% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +6.5 |
|  | [[Artesunate (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +13.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +9.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Posaconazole (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -4.4 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | NCK associated protein 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,791,146-49,828,750 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1602 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCH0](https://www.uniprot.org/uniprotkb/Q9HCH0) (Nck-associated protein 5-like):

> Regulates microtubule organization and stabilization. Promotes microtubule growth and bundling formation and stabilizes microtubules by increasing intense acetylation of microtubules. Both tubulin-binding and homodimer formation are required for NCKAP5L-mediated microtubule bundle formation.

**Summary**, from NCBI Gene [57701](https://www.ncbi.nlm.nih.gov/gene/57701):

> Involved in microtubule bundle formation and microtubule depolymerization. Located in centrosome and microtubule plus-end. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29321) · Entrez [57701](https://www.ncbi.nlm.nih.gov/gene/57701) · UniProt [Q9HCH0](https://www.uniprot.org/uniprotkb/Q9HCH0) · Ensembl [ENSG00000167566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167566)

## Data

Gene col 9493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9493); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9493]; `tensor/DDL_lfc|DDL_z.npy` [9493]; `embed/gene_vectors.npy` [9493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9493 or target_col == 9493). Every well: [[NCKAP5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCKAP5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
