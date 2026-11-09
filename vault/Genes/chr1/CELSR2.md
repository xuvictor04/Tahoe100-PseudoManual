---
symbol: "CELSR2"
type: "gene"
col: 6679
ensembl_id: "ENSG00000143126"
name: "cadherin EGF LAG seven-pass G-type receptor 2"
location: "1p13.3"
module: 50
arm: "+"
pooled_cpm: 6.97
n_lines_expressing: 41
n_dd_up: 22
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CELSR2

*cadherin EGF LAG seven-pass G-type receptor 2* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +11.3, q 6e-27, up in 16 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +7.2, q 8e-11, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.355× (z -11.3, q 4e-27, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAG1]] (+0.67, fdr 1e-05), [[PODXL2]] (+0.65, fdr 7e-06), [[GPC4]] (+0.64, fdr 1e-05); moves opposite to [[NSRP1]] (-0.56, fdr 8e-05), [[HSCB]] (-0.55, fdr 3e-05), [[AK6]] (-0.55, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AIF1L]] → it (grade B ⚠); 13 go from it, the strongest it → [[SAMD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +11.3 | 6e-27 | 16/20 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +10.5 | 3e-23 | 6/10 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.30×** | +9.5 | 4e-19 | 25/39 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +9.4 | 1e-18 | 10/14 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.90×** | +7.3 | 3e-11 | 24/38 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.2 | 8e-11 | 22/33 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +6.8 | 9e-10 | 20/37 (HT-29, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +5.5 | 3e-06 | 15/39 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.9 | 7e-05 | 15/36 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +4.6 | 2e-04 | 12/37 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.48×** | +4.4 | 4e-04 | 13/38 (SNU-423, A498, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 9/37 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.002 | 9/37 (Hs 766T, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.44×** | +4.0 | 0.002 | 8/27 (C32, J82, …) | two highest doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +3.9 | 0.004 | 5/37 (NCI-H2347, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 7/37 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.008 | 7/38 (A498, A549, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.011 | 7/39 (NCI-H1573, A-172, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.049 | 11/37 (Hs 766T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.051 | 7/37 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.080 | 2/38 (C32, Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.355×** | -11.3 | 4e-27 | 30/36 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.579×** | -8.8 | 4e-16 | 23/32 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.476×** | -8.4 | 6e-15 | 21/31 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.484×** | -8.3 | 2e-14 | 29/37 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.484×** | -8.3 | 2e-14 | 19/37 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.501×** | -7.9 | 4e-13 | 25/39 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -7.5 | 6e-12 | 24/35 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.539×** | -7.0 | 2e-10 | 24/38 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.551×** | -6.8 | 8e-10 | 22/37 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.593×** | -5.7 | 6e-07 | 20/35 (A-427, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -4.7 | 2e-04 | 20/37 (LS 180, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -4.2 | 0.001 | 21/36 (BT-474, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -3.8 | 0.006 | 7/39 (HepG2/C3A, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -3.7 | 0.009 | 12/36 (LoVo, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.539×** | -3.7 | 0.009 | 14/33 (RKO, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -3.5 | 0.015 | 16/38 (A498, SHP-77, …) | top dose only |  |
| [[Oxaprozin (drug)]] 0.05 µM |  | **0.737×** | -3.5 | 0.018 | 6/37 (LS 180, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.9 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 6.13 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0741× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 4.93 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -10.1) |
| [[A-427 (line)]] | wt | 7.69 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -9.3) |
| [[A498 (line)]] | wt | 11.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +9.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.135× (z -12.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 7.20 | 0 | 2 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0733× (z -9.5) |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0780× (z -10.7) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0908× (z -10.0) |
| [[C32 (line)]] | wt | 8.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0955× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.7) |
| [[LoVo (line)]] | wt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.8) |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.1) |
| [[SW48 (line)]] | wt | 16.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0879× (z -9.5) |
| [[A549 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAG1]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GPC4]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PTGFRN]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SELENON]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NAGA]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[TP53I11]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PARP1]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.59 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[FAM234A]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZMYM3]] | +0.59 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[FKBP9]] | +0.58 | +0.52 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.56 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[HSCB]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[AK6]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ZNF791]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ATF4]] | -0.55 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[MRPS18C]] | -0.55 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[FCF1]] | -0.54 | -0.29 / -0.63 | both halves | 3e-04 |  |
| [[TATDN1]] | -0.53 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[N4BP2L2]] | -0.53 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[NOXRED1]] | -0.52 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ZBTB8OS]] | -0.52 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SNHG8]] | -0.52 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AIF1L]] | B | AIF1L activity raises CELSR2's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without AIF1L | 0.046 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[PODXL2]] | B | PODXL2 activity raises CELSR2's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 2.18× lower at baseline in the lines without PODXL2 | 0.051 | ⚠ within organs, on part of the lines |
| [[PLBD1]] | B | PLBD1 activity raises CELSR2's level | lines that do not express PLBD1 (24) vs lines expressing it (26) | 1.60× lower at baseline in the lines without PLBD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD1]] | B | CELSR2 activity raises SAMD1's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without CELSR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[PODXL2]] | B | CELSR2 activity raises PODXL2's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.86× lower at baseline in the lines without CELSR2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[AIF1L]] | B | CELSR2 activity raises AIF1L's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.63× lower at baseline in the lines without CELSR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[CBX2]] | B | CELSR2 activity raises CBX2's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.21× lower at baseline in the lines without CELSR2 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[PARP1]] | B | CELSR2 activity raises PARP1's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without CELSR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[ADAM15]] | B | CELSR2 activity raises ADAM15's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without CELSR2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[MMP15]] | B | CELSR2 activity raises MMP15's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.10× lower at baseline in the lines without CELSR2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[SEPTIN3]] | B | CELSR2 activity raises SEPTIN3's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without CELSR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[NUP210]] | B | CELSR2 activity raises NUP210's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 3.24× lower at baseline in the lines without CELSR2 | 0.058 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[CDK16]] | B | CELSR2 activity raises CDK16's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without CELSR2 | 0.062 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[CNN3]] | B | CELSR2 activity weakens CNN3's drug response | lines that do not express CELSR2 (7) vs lines expressing it (37) | the lines without CELSR2 respond 1.58× as strongly (z diff -1.75); strongest at Panobinostat 5 µM: 2.20x vs 1.46x (z diff -3.3) | 0.091 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HYAL2]] | B | CELSR2 activity raises HYAL2's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without CELSR2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.2, -25.4); signed map (-29.7, -40.7). **Vector** length 59.8, 9.61% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -8.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cadherin EGF LAG seven-pass G-type receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,249,539-109,275,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0279, MEGF3, Flamingo1, CDHF10, ADGRC2; previously EGFL2 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily C; CELSR cadherins |
| Hallmark sets | KRAS_SIGNALING_DN, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCU4](https://www.uniprot.org/uniprotkb/Q9HCU4) (Cadherin EGF LAG seven-pass G-type receptor 2):

> Receptor that may have an important role in cell/cell signaling during nervous system formation.

**Summary**, from NCBI Gene [1952](https://www.ncbi.nlm.nih.gov/gene/1952):

> The protein encoded by this gene is a member of the flamingo subfamily, part of the cadherin superfamily. The flamingo subfamily consists of nonclassic-type cadherins; a subpopulation that does not interact with catenins. The flamingo cadherins are located at the plasma membrane and have nine cadherin domains, seven epidermal growth factor-like repeats and two laminin A G-type repeats in their ectodomain. They also have seven transmembrane domains, a characteristic unique to this subfamily. It …

**Accessions** — [HGNC:3231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3231) · Entrez [1952](https://www.ncbi.nlm.nih.gov/gene/1952) · UniProt [Q9HCU4](https://www.uniprot.org/uniprotkb/Q9HCU4) · Ensembl [ENSG00000143126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143126)

## Data

Gene col 6679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6679); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6679]; `tensor/DDL_lfc|DDL_z.npy` [6679]; `embed/gene_vectors.npy` [6679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6679 or target_col == 6679). Every well: [[CELSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
