---
symbol: "PIGK"
type: "gene"
col: 6663
ensembl_id: "ENSG00000142892"
name: "phosphatidylinositol glycan anchor biosynthesis class K"
location: "1p31.1"
module: 29
arm: "+"
pooled_cpm: 28.35
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PIGK

*phosphatidylinositol glycan anchor biosynthesis class K* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +20.7, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.25× (z +5.6, q 2e-06, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.649× (z -7.7, q 1e-11, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POGLUT3]] (+0.70, fdr 7e-06), [[UGGT1]] (+0.68, fdr 9e-06), [[ICMT]] (+0.65, fdr 7e-06); moves opposite to [[SNHG7]] (-0.64, fdr 1e-05), [[SIRT6]] (-0.63, fdr 2e-05), [[ADPRM]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +20.7 | 0e+00 | 42/42 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +19.5 | 0e+00 | 34/35 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +14.1 | 8e-43 | 35/38 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.56×** | +7.9 | 4e-13 | 30/47 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.42×** | +6.3 | 4e-08 | 29/47 (A-172, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.41×** | +6.1 | 1e-07 | 24/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.6 | 2e-06 | 22/47 (A-172, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +5.5 | 3e-06 | 25/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +5.0 | 4e-05 | 22/47 (LoVo, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.4 | 5e-04 | 16/47 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.3 | 0.001 | 15/32 (C32, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.26×** | +4.0 | 0.003 | 16/47 (SNU-423, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.25×** | +3.9 | 0.004 | 17/47 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.005 | 12/46 (NCI-H460, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.015 | 16/46 (SW480, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.065 | 8/47 (C32, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.065 | 7/47 (HT-29, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.649×** | -7.7 | 1e-11 | 23/46 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.753×** | -7.1 | 4e-10 | 27/46 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.484×** | -6.7 | 3e-09 | 29/46 (A498, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -6.2 | 9e-08 | 29/47 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -5.9 | 3e-07 | 26/47 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -5.9 | 4e-07 | 26/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.555×** | -5.4 | 4e-06 | 25/41 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.756×** | -4.7 | 2e-04 | 21/47 (J82, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.787×** | -4.2 | 0.001 | 19/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.649×** | -4.0 | 0.004 | 17/47 (PANC-1, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.817×** | -3.6 | 0.019 | 12/47 (SNU-1, AN3 CA, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.683×** | -3.5 | 0.020 | 15/46 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.872× | -3.4 | 0.030 | 12/47 (SW480, J82, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.723×** | -3.3 | 0.034 | 10/47 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.835× | -3.2 | 0.058 | 10/47 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.058 | 14/45 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.2) |
| [[HS-578T (line)]] | alt | 55.0 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.2) |
| [[PANC-1 (line)]] | alt | 34.8 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 25.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 36.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +12.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 38.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 21.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 35.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -16.5) |
| [[A549 (line)]] | wt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +11.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 41.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 40.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.7) |
| [[SNU-423 (line)]] | alt | 20.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 25.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0824× (z -9.9) |
| [[Hs 766T (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +11.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.1) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 51.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -9.8) |
| [[A-427 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT3]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.68 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[ICMT]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CD99L2]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[LRP11]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SELENON]] | +0.64 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TMEM19]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[FKBP9]] | +0.63 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[TMEM30A]] | +0.62 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[PPT1]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TAF6]] | +0.62 | +0.39 / +0.72 | both halves | 6e-05 |  |
| [[CRTAP]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG7]] | -0.64 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[SIRT6]] | -0.63 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ADPRM]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[EPB41L4A-AS1]] | -0.61 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ZNF593]] | -0.61 | -0.39 / -0.64 | both halves | 5e-05 |  |
| [[ZNF765]] | -0.61 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.61 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[SNHG8]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SNHG12]] | -0.60 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ATF4]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[MED10]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NPIPP1]] | -0.58 | -0.44 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIGK's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.0, -23.2); signed map (-24.2, -38.5). **Vector** length 97.9, 23.4% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +14.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +19.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.4 | -4.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -1.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,088,989-77,219,430 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hGPI8, GPI8, PIG-K |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol transamidase complex; Transaminases |
| Reactome | 2 pathways, smallest: Attachment of GPI anchor to uPAR; Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92643](https://www.uniprot.org/uniprotkb/Q92643) (GPI-anchor transamidase):

> Catalytic subunit of the glycosylphosphatidylinositol-anchor (GPI-anchor) transamidase (GPI-T) complex that catalyzes the formation of the linkage between a proprotein and a GPI-anchor and participates in GPI anchored protein biosynthesis. Recognizes diverse proproteins at a C-terminal signal peptide (CSP) region that lacks consensus sequence and replaces it with a GPI-anchor via a transamidation reaction. Transamidation catalysis reaction follows a two-phase mechanism. In the acyl-enzyme …

**Summary**, from NCBI Gene [10026](https://www.ncbi.nlm.nih.gov/gene/10026):

> This gene encodes a member of the cysteine protease family C13 that is involved in glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI-anchor is a glycolipid found on many blood cells and serves to anchor proteins to the cell surface. This protein is a member of the multisubunit enzyme, GPI transamidase and is thought to be its enzymatic component. GPI transamidase mediates GPI anchoring in the endoplasmic reticulum, by catalyzing the transfer of fully assembled GPI units to …

**Accessions** — [HGNC:8965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8965) · Entrez [10026](https://www.ncbi.nlm.nih.gov/gene/10026) · UniProt [Q92643](https://www.uniprot.org/uniprotkb/Q92643) · Ensembl [ENSG00000142892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142892)

## Data

Gene col 6663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6663); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6663]; `tensor/DDL_lfc|DDL_z.npy` [6663]; `embed/gene_vectors.npy` [6663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6663 or target_col == 6663). Every well: [[PIGK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
