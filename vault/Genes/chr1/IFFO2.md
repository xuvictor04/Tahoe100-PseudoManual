---
symbol: "IFFO2"
type: "gene"
col: 9888
ensembl_id: "ENSG00000169991"
name: "intermediate filament family orphan 2"
location: "1p36.13"
module: 154
arm: "+"
pooled_cpm: 24.59
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# IFFO2

*intermediate filament family orphan 2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.25× (z +26.6, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.629× (z -8.2, q 1e-13, down in 22 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.700× (z -6.6, q 2e-08, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHPN2]] (+0.63, fdr 1e-05), [[ZMIZ1]] (+0.62, fdr 1e-05), [[GRK5]] (+0.60, fdr 1e-05); moves opposite to [[PTPDC1]] (-0.52, fdr 3e-05), [[UNC50]] (-0.47, fdr 2e-04), [[MTREX]] (-0.47, fdr 1e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.25×** | +26.6 | 0e+00 | 47/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.75×** | +24.3 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.74×** | +24.3 | 0e+00 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +17.5 | 0e+00 | 36/44 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +11.7 | 2e-29 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +11.7 | 2e-29 | 32/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +8.0 | 7e-14 | 28/46 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.0 | 2e-10 | 28/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.9 | 3e-10 | 23/44 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.43×** | +6.4 | 1e-08 | 23/47 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +5.6 | 1e-06 | 18/47 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +5.5 | 2e-06 | 16/47 (PANC-1, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 5e-05 | 20/47 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.26×** | +4.3 | 7e-04 | 13/47 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 15/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.004 | 8/45 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.16× | +3.8 | 0.004 | 17/47 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -8.2 | 1e-13 | 22/33 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.700×** | -6.6 | 2e-08 | 19/47 (HS-578T, NCI-H2347, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.729×** | -5.8 | 1e-06 | 23/40 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.735×** | -5.7 | 2e-06 | 22/47 (HS-578T, AsPC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.818×** | -5.2 | 2e-05 | 20/47 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.791×** | -4.3 | 0.001 | 16/47 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.800×** | -4.1 | 0.003 | 19/47 (HS-578T, SK-MEL-2, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.809×** | -3.9 | 0.007 | 16/47 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.811×** | -3.9 | 0.007 | 15/47 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.812×** | -3.8 | 0.007 | 10/47 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.011 | 16/47 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 0.869× | -3.7 | 0.012 | 15/47 (LOX-IMVI, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.820×** | -3.6 | 0.012 | 17/46 (HS-578T, NCI-H2347, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.6 | 0.012 | 4/47 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.825×** | -3.5 | 0.015 | 3/47 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.821×** | -3.5 | 0.016 | 16/47 (HepG2/C3A, HT-29, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.819×** | -3.4 | 0.022 | 13/45 (HS-578T, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.022 | 15/47 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.023 | 12/47 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.833× | -3.4 | 0.023 | 10/47 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 0.889× | -3.1 | 0.055 | 9/47 (C32, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.9 | 5 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.46× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 14.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 41.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.5) | — |
| [[C32 (line)]] | wt | 56.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0458× (z -20.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 38.0 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.40× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 29.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.61× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.14× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -8.9) |
| [[RKO (line)]] | wt | 27.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 22.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 20.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.76× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 16.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.74× (z +14.7) | — |
| [[A-427 (line)]] | wt | 7.90 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.07× (z +9.2) | — |
| [[A498 (line)]] | wt | 25.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +16.5) | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +12.4) | — |
| [[KATO III (line)]] | alt | 32.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.75× (z +9.9) | — |
| [[LoVo (line)]] | wt | 20.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.25× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 10.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.91× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 29.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.67× (z +9.4) | — |
| [[A-172 (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.8) | — |
| [[A549 (line)]] | wt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 35.2 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.103× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -15.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -12.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 9.08 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 60.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.268× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 7.93 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.94× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -8.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHPN2]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZMIZ1]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GRK5]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[MICAL3]] | +0.59 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[PIM1]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SSBP3]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ECE1]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ARID5A]] | +0.57 | +0.51 / +0.43 | both halves | 4e-05 |  |
| [[SYNGR2]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[GPRC5A]] | +0.56 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SLC35E4]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SOX9]] | +0.56 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPDC1]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[UNC50]] | -0.47 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[MTREX]] | -0.47 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[GPALPP1]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[TCEANC2]] | -0.46 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[UQCC1]] | -0.46 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[ARMCX5-GPRASP2]] | -0.46 | -0.28 / -0.31 | both halves | 3e-04 |  |
| [[ZFR]] | -0.46 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[ZCCHC4]] | -0.46 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[N4BP2]] | -0.46 | -0.30 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers IFFO2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[LMCD1]] | B | LMCD1 activity raises IFFO2's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without LMCD1 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CRACR2B]] | B | CRACR2B activity raises IFFO2's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without CRACR2B | 0.077 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ABTB2]] | B | ABTB2 activity raises IFFO2's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without ABTB2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[PIM1]] | C | PIM1 activity strengthens IFFO2's drug response | lines that do not express PIM1 (4) vs lines expressing it (43) | the lines without PIM1 respond 0.75× as strongly (z diff +1.25); strongest at Panobinostat 0.5 µM: 1.98x vs 3.77x (z diff +3.7) | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: CLSTN3, HFE, HACD1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FZD5]] | C | FZD5 activity raises IFFO2's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without FZD5 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.7, 32.7); signed map (-4.9, 27.6). **Vector** length 102, 24.9% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +26.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +24.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +24.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +11.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.7 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -4.8 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -3.5 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.5 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.3 | -5.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | intermediate filament family orphan 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:18,904,280-18,956,676 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Intermediate filament family orphans |
| Matched by | ensembl_id |

UniProt [Q5TF58](https://www.uniprot.org/uniprotkb/Q5TF58) carries no function annotation.

**Summary**, from NCBI Gene [126917](https://www.ncbi.nlm.nih.gov/gene/126917):

> Predicted to be located in intermediate filament. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27006) · Entrez [126917](https://www.ncbi.nlm.nih.gov/gene/126917) · UniProt [Q5TF58](https://www.uniprot.org/uniprotkb/Q5TF58) · Ensembl [ENSG00000169991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169991)

## Data

Gene col 9888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9888); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9888]; `tensor/DDL_lfc|DDL_z.npy` [9888]; `embed/gene_vectors.npy` [9888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9888 or target_col == 9888). Every well: [[IFFO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFFO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
