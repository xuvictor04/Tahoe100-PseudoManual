---
symbol: "BMI1"
type: "gene"
col: 9626
ensembl_id: "ENSG00000168283"
name: "BMI1 proto-oncogene, polycomb ring finger"
location: "10p12.2"
module: 28
arm: "+"
pooled_cpm: 42.13
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# BMI1

*BMI1 proto-oncogene, polycomb ring finger* — 10p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +17.1, q 0e+00, up in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.84× (z +11.6, q 9e-29, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.660× (z -7.4, q 5e-11, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.742× (z -5.7, q 3e-06, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEZF1]] (+0.70, fdr 7e-06), [[CGGBP1]] (+0.70, fdr 7e-06), [[LIG4]] (+0.68, fdr 1e-05); moves opposite to [[UQCRH]] (-0.69, fdr 7e-06), [[TOMM5]] (-0.69, fdr 7e-06), [[MED31]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SCRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +17.1 | 0e+00 | 40/43 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +15.4 | 0e+00 | 33/39 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.70×** | +14.2 | 1e-43 | 40/47 (NCI-H23, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +11.6 | 9e-29 | 36/47 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +9.9 | 8e-21 | 33/43 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +9.7 | 4e-20 | 31/46 (BT-474, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.61×** | +8.7 | 3e-16 | 36/47 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +8.1 | 3e-14 | 40/47 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +5.8 | 4e-07 | 30/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.7 | 6e-07 | 27/44 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.6 | 1e-06 | 22/47 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.32×** | +5.3 | 6e-06 | 27/44 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.27×** | +4.6 | 2e-04 | 25/47 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.4 | 5e-04 | 21/48 (A-427, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.002 | 17/47 (A-427, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.007 | 15/46 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.013 | 17/47 (KATO III, NCI-H23, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.014 | 20/47 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.015 | 14/46 (LS 180, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.023 | 10/46 (SK-MEL-2, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.660×** | -7.4 | 5e-11 | 34/47 (LS 180, NCI-H1792, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.723×** | -6.2 | 2e-07 | 29/46 (SW48, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.742×** | -5.7 | 3e-06 | 27/47 (SW48, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.772×** | -4.9 | 1e-04 | 22/47 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.781×** | -4.7 | 3e-04 | 24/47 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.655×** | -4.2 | 0.003 | 20/42 (NCI-H1792, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.783× | -3.2 | 0.10 | 15/47 (LOX-IMVI, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.0 | 0.18 | 16/46 (HEC-1-A, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 34.6 | 5 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -12.9) |
| [[LS 180 (line)]] | wt | 60.6 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.3) | [[Bortezomib (drug)]] 0.05 µM 0.391× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 64.3 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -8.6) |
| [[A498 (line)]] | wt | 18.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 68.6 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.23× (z +12.3) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.185× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 56.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.72× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 50.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +14.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.0) | — |
| [[A-172 (line)]] | wt | 45.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.1) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[KATO III (line)]] | alt | 38.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +14.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 38.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 38.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 63.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.397× (z -10.2) |
| [[RKO (line)]] | wt | 62.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.6) ⚠ cell-cycle shift, explains ~41% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -19.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 62.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +11.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 87.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -12.6) |
| [[BT-474 (line)]] | alt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 63.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[HepG2_C3A (line)]] | wt | 73.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[Hs 766T (line)]] | wt | 39.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 57.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +18.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[PANC-1 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 77.4 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.285× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[CGGBP1]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[LIG4]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[DDX6]] | +0.66 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.66 | +0.50 / +0.60 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 630 |
| [[ZFP91]] | +0.66 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CFL2]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CILK1]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SCRN1]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TRAM2-AS1]] | +0.65 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[AASDHPPT]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.69 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TOMM5]] | -0.69 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[MED31]] | -0.66 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[EIF3K]] | -0.64 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[GPR89B]] | -0.64 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[SNRPD2]] | -0.63 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ZCCHC17]] | -0.63 | -0.64 / -0.49 | both halves | 2e-05 |  |
| [[MYO9B]] | -0.63 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[DHDDS]] | -0.62 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RNF121]] | -0.61 | -0.59 / -0.49 | both halves | 1e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCRN1]] | B | SCRN1 activity raises BMI1's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without SCRN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |
| [[PSMB5]] | B | PSMB5 activity raises BMI1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PPP1R9A]] | B | PPP1R9A activity raises BMI1's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without PPP1R9A | 0.087 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[TAF9]] | C | TAF9's natural level weakens BMI1's drug response | TAF9's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.01; direction clear | 0.030 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.9, 2.0); signed map (16.7, -31.3). **Vector** length 109, 28.3% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +7.2 | +14.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +11.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.6 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +15.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.4 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.3 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -1.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | BMI1 proto-oncogene, polycomb ring finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.2 — chr10:22,321,099-22,331,484 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF51; previously PCGF4 |
| Gene groups (HGNC) | Ring finger proteins; Polycomb group ring fingers |
| Reactome | 20 pathways, smallest: SUMOylation of DNA methylation proteins; Transcriptional Regulation by E2F6; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known |
| Matched by | ensembl_id |

**Function**, from UniProt [P35226](https://www.uniprot.org/uniprotkb/P35226) (Polycomb complex protein BMI-1):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. The complex composed of RNF2, UB2D3 and BMI1 binds nucleosomes, and has activity only with …

**Summary**, from NCBI Gene [648](https://www.ncbi.nlm.nih.gov/gene/648):

> This gene encodes a ring finger protein that is major component of the polycomb group complex 1 (PRC1). This complex functions through chromatin remodeling as an essential epigenetic repressor of multiple regulatory genes involved in embryonic development and self-renewal in somatic stem cells. This protein also plays a central role in DNA damage repair. This gene is an oncogene and aberrant expression is associated with numerous cancers and is associated with resistance to certain …

**Accessions** — [HGNC:1066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1066) · Entrez [648](https://www.ncbi.nlm.nih.gov/gene/648) · UniProt [P35226](https://www.uniprot.org/uniprotkb/P35226) · Ensembl [ENSG00000168283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168283)

## Data

Gene col 9626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9626); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9626]; `tensor/DDL_lfc|DDL_z.npy` [9626]; `embed/gene_vectors.npy` [9626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9626 or target_col == 9626). Every well: [[BMI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
