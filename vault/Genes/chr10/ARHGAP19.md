---
symbol: "ARHGAP19"
type: "gene"
col: 13101
ensembl_id: "ENSG00000213390"
name: "Rho GTPase activating protein 19"
location: "10q24.1"
module: 22
arm: "+"
pooled_cpm: 38.88
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ARHGAP19

*Rho GTPase activating protein 19* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +12.9, q 3e-35, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.666× (z -10.6, q 3e-23, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.664× (z -7.2, q 1e-10, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OIP5]] (+0.74, fdr 7e-06), [[SPAG5]] (+0.72, fdr 7e-06), [[FAM72D]] (+0.71, fdr 7e-06); moves opposite to [[GDAP1]] (-0.57, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +12.9 | 3e-35 | 42/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +10.7 | 4e-24 | 35/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +10.3 | 2e-22 | 37/47 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.6 | 2e-19 | 29/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +9.4 | 6e-19 | 39/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.50×** | +7.5 | 9e-12 | 30/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +6.4 | 1e-08 | 25/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.37×** | +5.8 | 4e-07 | 24/46 (HT-29, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.3 | 6e-06 | 24/48 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +4.5 | 4e-04 | 19/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.017 | 18/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.022 | 15/48 (HOP62, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.022 | 17/48 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.076 | 10/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +3.1 | 0.079 | 9/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.079 | 7/48 (SW 900, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.666×** | -10.6 | 3e-23 | 36/48 (A-427, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.664×** | -7.2 | 1e-10 | 29/48 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.680×** | -7.1 | 2e-10 | 32/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -6.9 | 7e-10 | 25/48 (AN3 CA, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.544×** | -5.8 | 6e-07 | 27/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.752×** | -4.8 | 1e-04 | 22/43 (C-33 A, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -4.5 | 5e-04 | 18/48 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.793×** | -4.3 | 0.001 | 14/48 (H4, HS-578T, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.805×** | -4.0 | 0.004 | 17/48 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.662×** | -4.0 | 0.004 | 17/45 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.807×** | -3.9 | 0.004 | 16/48 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.801×** | -3.9 | 0.004 | 18/47 (NCI-H2030, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.799×** | -3.9 | 0.004 | 20/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.7 | 0.009 | 20/48 (A498, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.697×** | -3.5 | 0.019 | 21/48 (SW48, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.834× | -3.3 | 0.031 | 11/48 (RKO, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.831×** | -3.3 | 0.034 | 14/48 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.837× | -3.3 | 0.035 | 11/47 (PANC-1, LS 180, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.061 | 6/48 (SW 1088, SNU-423, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.727×** | -3.1 | 0.061 | 10/48 (A-427, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.848× | -3.0 | 0.066 | 10/48 (C32, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 81.8 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +13.8) | [[Selinexor (drug)]] 5 µM 0.594× (z -10.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 40.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.41× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 80.2 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.449× (z -11.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 31.0 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 40.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0942× (z -13.1) |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.361× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 13.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 60.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.92× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -11.4) |
| [[C-33 A (line)]] | alt | 88.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 50.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -8.8) |
| [[KATO III (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 56.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +17.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 53.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -11.4) |
| [[SW1417 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.487× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 38.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.2) | — |
| [[A-172 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OIP5]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.72 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[FAM72D]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[PTTG1]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[FAM72A]] | +0.68 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[PRR11]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[MIS18BP1]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[FAM72B]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[TACC3]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[PIF1]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDAP1]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.4, -56.7); signed map (-49.9, -39.8). **Vector** length 118, 31.2% of its response variance represented; |z| ≥ 3 in 1,178 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.55 to 28); *Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal* (reactome, mean cos +0.51 to 28); *Amplification of signal from the kinetochores* (reactome, mean cos +0.51 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +9.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.4 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.3 | +12.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.3 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.2 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -7.2 | -10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:97,222,173-97,292,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00194, MGC14258 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CB8](https://www.uniprot.org/uniprotkb/Q14CB8) (Rho GTPase-activating protein 19):

> Has GTPase activator activity toward RHOA; RHOA activation results in GTP hydrolysis and conversion from an active GTP-bound to an inactive GDP-bound state. Lacks GTPase activator activity toward RAC1 or CDC42.

**Summary**, from NCBI Gene [84986](https://www.ncbi.nlm.nih.gov/gene/84986):

> Members of the ARHGAP family, such as ARHGAP19, encode negative regulators of Rho GTPases (see RHOA; MIM 165390), which are involved in cell migration, proliferation, and differentiation, actin remodeling, and G1 cell cycle progression (Lv et al., 2007 [PubMed 17454002]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23724) · Entrez [84986](https://www.ncbi.nlm.nih.gov/gene/84986) · UniProt [Q14CB8](https://www.uniprot.org/uniprotkb/Q14CB8) · Ensembl [ENSG00000213390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213390)

## Data

Gene col 13101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13101); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13101]; `tensor/DDL_lfc|DDL_z.npy` [13101]; `embed/gene_vectors.npy` [13101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13101 or target_col == 13101). Every well: [[ARHGAP19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
