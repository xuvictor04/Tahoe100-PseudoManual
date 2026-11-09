---
symbol: "GNL3L"
type: "gene"
col: 5022
ensembl_id: "ENSG00000130119"
name: "G protein nucleolar 3 like"
location: "Xp11.22"
module: 5
arm: "+"
pooled_cpm: 90.19
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GNL3L

*G protein nucleolar 3 like* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.35× (z +17.8, q 0e+00, up in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.40× (z +7.0, q 3e-10, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.769× (z -5.7, q 6e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.82, fdr 7e-06), [[PUM3]] (+0.80, fdr 7e-06), [[PUS1]] (+0.79, fdr 7e-06); moves opposite to [[ANG]] (-0.75, fdr 7e-06), [[RNASE4]] (-0.74, fdr 7e-06), [[MXI1]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +17.8 | 0e+00 | 39/44 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +17.0 | 0e+00 | 45/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +12.7 | 2e-34 | 38/45 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +9.9 | 5e-21 | 40/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +7.0 | 3e-10 | 36/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +6.7 | 2e-09 | 35/48 (SHP-77, NCI-H1573, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.61×** | +5.4 | 6e-06 | 33/48 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +4.6 | 3e-04 | 27/48 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 4e-04 | 24/48 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.4 | 5e-04 | 16/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 5e-04 | 23/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 22/48 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.002 | 21/48 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.9 | 0.004 | 21/48 (A-172, A549, …) | rises with dose | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +3.8 | 0.005 | 18/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.19× | +3.7 | 0.007 | 18/48 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.010 | 19/48 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.017 | 14/48 (SW480, Hs 766T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.4 | 0.020 | 19/48 (A549, RPMI-7951, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.3 | 0.024 | 16/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.045 | 8/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.769×** | -5.7 | 6e-06 | 26/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.824×** | -4.2 | 0.007 | 21/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.829×** | -4.1 | 0.008 | 21/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.714×** | -3.8 | 0.018 | 16/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.839× | -3.7 | 0.023 | 20/49 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.7 | 0.023 | 25/49 (PANC-1, RKO, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.892× | -3.6 | 0.030 | 14/48 (RKO, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.4 | 0.044 | 18/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.859× | -3.3 | 0.056 | 17/49 (hTERT-HPNE, NCI-H460, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.855× | -3.3 | 0.056 | 13/47 (LoVo, RPMI-7951, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.872× | -3.1 | 0.093 | 13/48 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.861× | -3.0 | 0.11 | 12/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 85.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[A498 (line)]] | wt | 46.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.37× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[CFPAC-1 (line)]] | alt | 33.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 155 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -16.1) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.533× (z -9.7) |
| [[SW480 (line)]] | alt | 197 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.96× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.574× (z -8.5) |
| [[A-427 (line)]] | wt | 118 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 90.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +16.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 71.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +13.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 79.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 41.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 42.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 72.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 44.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +12.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 85.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 61.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.08× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -9.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HT-29 (line)]] | alt | 92.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +8.5) | — |
| [[LoVo (line)]] | wt | 78.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +13.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 51.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 44.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 96.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +14.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[C32 (line)]] | wt | 45.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 89.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.589× (z -8.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[KATO III (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 63.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 64.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +10.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.82× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.173× (z -9.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 | STRING 451 |
| [[PUM3]] | +0.80 | +0.76 / +0.87 | both halves | 7e-06 | STRING 876 |
| [[PUS1]] | +0.79 | +0.85 / +0.76 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.77 | +0.76 / +0.82 | both halves | 7e-06 | STRING 831 |
| [[UTP20]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | STRING 522 |
| [[ARMC6]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[ZNF121]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[ALG8]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 | STRING 444 |
| [[LETM1]] | +0.73 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 | STRING 439 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANG]] | -0.75 | -0.72 / -0.71 | both halves | 7e-06 |  |
| [[RNASE4]] | -0.74 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[MXI1]] | -0.71 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[ARL3]] | -0.66 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[VPS37D]] | -0.66 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[KBTBD3]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.65 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[RAB8B]] | -0.64 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[APAF1]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[MPC2]] | -0.63 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[HCFC1R1]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GNL3L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ADM]] | B | ADM activity lowers GNL3L's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.87× higher at baseline in the lines without ADM | 0.060 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[LRP1]] | C | LRP1 activity lowers GNL3L's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.36× higher at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |
| [[TXNRD3]] | C | TXNRD3 activity lowers GNL3L's level | lines that do not express TXNRD3 (3) vs lines expressing it (47) | 2.11× higher at baseline in the lines without TXNRD3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FSCN1, ELK3, XG; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.9, -33.9); signed map (-0.7, -47.7). **Vector** length 138, 42.9% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.61 to 13); *rRNA processing* (reactome, mean cos +0.54 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.1 | +9.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +12.7 |
|  | [[EX229 (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +4.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | G protein nucleolar 3 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:54,530,183-54,621,521 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10613, GNL3B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVN8](https://www.uniprot.org/uniprotkb/Q9NVN8) (Guanine nucleotide-binding protein-like 3-like protein):

> Stabilizes TERF1 telomeric association by preventing TERF1 recruitment by PML. Stabilizes TERF1 protein by preventing its ubiquitination and hence proteasomal degradation. Does so by interfering with TERF1-binding to FBXO4 E3 ubiquitin-protein ligase. Required for cell proliferation. By stabilizing TRF1 protein during mitosis, promotes metaphase-to-anaphase transition. Stabilizes MDM2 protein by preventing its ubiquitination, and hence proteasomal degradation. By acting on MDM2, may affect TP53 …

**Summary**, from NCBI Gene [54552](https://www.ncbi.nlm.nih.gov/gene/54552):

> The protein encoded by this gene appears to be a nucleolar GTPase that is essential for ribosomal pre-rRNA processing and cell proliferation. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:25553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25553) · Entrez [54552](https://www.ncbi.nlm.nih.gov/gene/54552) · UniProt [Q9NVN8](https://www.uniprot.org/uniprotkb/Q9NVN8) · Ensembl [ENSG00000130119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130119)

## Data

Gene col 5022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5022); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5022]; `tensor/DDL_lfc|DDL_z.npy` [5022]; `embed/gene_vectors.npy` [5022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5022 or target_col == 5022). Every well: [[GNL3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNL3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
