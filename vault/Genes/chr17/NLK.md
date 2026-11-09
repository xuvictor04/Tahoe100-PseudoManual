---
symbol: "NLK"
type: "gene"
col: 1484
ensembl_id: "ENSG00000087095"
name: "nemo like kinase"
location: "17q11.2"
module: 36
arm: "+"
pooled_cpm: 133.28
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NLK

*nemo like kinase* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.57× (z +9.7, q 2e-19, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.429× (z -17.8, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.724× (z -6.8, q 8e-10, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW11]] (+0.64, fdr 7e-06), [[HIRA]] (+0.63, fdr 1e-05), [[DAP3]] (+0.61, fdr 1e-05); moves opposite to [[FMR1]] (-0.59, fdr 1e-05), [[STAG2]] (-0.57, fdr 3e-05), [[RAB21]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +9.7 | 2e-19 | 41/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +8.7 | 1e-15 | 39/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +8.6 | 1e-15 | 40/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +7.5 | 7e-12 | 38/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.5 | 4e-06 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.3 | 1e-05 | 27/48 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 7e-05 | 31/48 (SNU-423, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +4.8 | 1e-04 | 28/48 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 5e-04 | 27/47 (HEC-1-A, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +4.2 | 0.001 | 21/48 (HS-578T, SW1417, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.013 | 19/49 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.6 | 0.016 | 21/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.18× | +3.5 | 0.023 | 22/48 (A549, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.429×** | -17.8 | 0e+00 | 44/49 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -16.4 | 0e+00 | 36/44 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.469×** | -15.1 | 0e+00 | 38/45 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.579×** | -11.8 | 5e-30 | 44/48 (SW 1271, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.665×** | -8.5 | 3e-15 | 36/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.787×** | -7.3 | 2e-11 | 26/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -6.8 | 8e-10 | 31/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -6.8 | 1e-09 | 28/49 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.842× | -5.2 | 1e-05 | 22/48 (RKO, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.795×** | -5.0 | 4e-05 | 24/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.813×** | -4.5 | 4e-04 | 26/48 (RPMI-7951, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -4.4 | 5e-04 | 25/48 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -4.4 | 5e-04 | 22/48 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.681×** | -4.3 | 6e-04 | 20/38 (Panc 03.27, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.833×** | -4.0 | 0.003 | 22/48 (NCI-H460, SW1417, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.841× | -3.7 | 0.006 | 20/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.889× | -3.6 | 0.010 | 9/48 (A-172, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.842× | -3.4 | 0.016 | 19/47 (H4, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.869× | -2.9 | 0.081 | 19/49 (HOP62, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 107 | 3 | 10 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 2.08× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.308× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.484× (z -10.1) |
| [[A549 (line)]] | wt | 170 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.5) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -10.8) |
| [[C32 (line)]] | wt | 230 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -13.1) |
| [[KATO III (line)]] | alt | 117 | 3 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.46× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -20.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 166 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.372× (z -12.6) |
| [[HS-578T (line)]] | alt | 111 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -12.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 170 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -20.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 239 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -15.8) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 211 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -18.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 107 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.42× (z +10.1) | [[Docetaxel (drug)]] 0.05 µM 0.395× (z -10.6) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 153 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.94× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -18.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 140 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.74× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -16.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 156 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0661× (z -33.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 90.7 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +12.6) | — |
| [[J82 (line)]] | alt | 155 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.8) |
| [[LS 180 (line)]] | wt | 86.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +9.1) | — |
| [[SW480 (line)]] | alt | 141 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.54× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -11.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.354× (z -9.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 232 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.7) |
| [[RKO (line)]] | wt | 160 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0861× (z -24.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0845× (z -29.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 98.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -22.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -16.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 97.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 70.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 254 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.142× (z -13.1) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -11.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 95.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -12.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.466× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 97.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -14.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 85.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -18.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.375× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[SW48 (line)]] | wt | 75.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW11]] | +0.64 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[HIRA]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[DAP3]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[KLHL18]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TYW1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[UBE3C]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[MED27]] | +0.60 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ZDHHC5]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.58 | +0.65 / +0.49 | both halves | 2e-05 |  |
| [[EXOC2]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GBA2]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[EIF3K]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMR1]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[STAG2]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[RAB21]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ZNF442]] | -0.54 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[HMGN2]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CYB5D2]] | -0.53 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[DPH6-DT]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CPEB2]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[NOTCH2NLC]] | -0.53 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MBIP]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CLN5]] | -0.52 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[FAM117A]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NLK's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-12.0, -17.1); signed map (-47.3, -21.5). **Vector** length 118, 37.0% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | -0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.8 | +0.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.7 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -10.9 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.7 | -15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.2 | -16.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.4 | -17.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.5 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -5.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.2 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -4.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -4.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | nemo like kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,041,737-28,196,381 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Atypical mitogen-activated protein kinases |
| Reactome | 3 pathways, smallest: Ca2+ pathway; Beta-catenin independent WNT signaling; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBE8](https://www.uniprot.org/uniprotkb/Q9UBE8) (Serine/threonine-protein kinase NLK):

> Serine/threonine-protein kinase that regulates a number of transcription factors with key roles in cell fate determination. Positive effector of the non-canonical Wnt signaling pathway, acting downstream of WNT5A, MAP3K7/TAK1 and HIPK2. Negative regulator of the canonical Wnt/beta-catenin signaling pathway. Binds to and phosphorylates TCF7L2/TCF4 and LEF1, promoting the dissociation of the TCF7L2/LEF1/beta-catenin complex from DNA, as well as the ubiquitination and subsequent proteolysis of …

**Summary**, from NCBI Gene [51701](https://www.ncbi.nlm.nih.gov/gene/51701):

> Enables DNA-binding transcription factor binding activity; protein serine/threonine kinase activity; and ubiquitin protein ligase binding activity. Involved in several processes, including negative regulation of TORC1 signaling; protein stabilization; and transforming growth factor beta receptor signaling pathway. Predicted to be located in cytosol and nucleoplasm. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29858) · Entrez [51701](https://www.ncbi.nlm.nih.gov/gene/51701) · UniProt [Q9UBE8](https://www.uniprot.org/uniprotkb/Q9UBE8) · Ensembl [ENSG00000087095](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087095)

## Data

Gene col 1484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1484); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1484]; `tensor/DDL_lfc|DDL_z.npy` [1484]; `embed/gene_vectors.npy` [1484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1484 or target_col == 1484). Every well: [[NLK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
