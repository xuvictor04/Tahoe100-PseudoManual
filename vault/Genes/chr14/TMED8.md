---
symbol: "TMED8"
type: "gene"
col: 1991
ensembl_id: "ENSG00000100580"
name: "transmembrane p24 trafficking protein family member 8"
location: "14q24.3"
module: 15
arm: "+"
pooled_cpm: 41.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TMED8

*transmembrane p24 trafficking protein family member 8* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +21.9, q 0e+00, up in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2030 2.14×, NCI-H23 2.69×, HS-578T 3.08×, LoVo 2.18×, …).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.395× (z -13.6, q 1e-39, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZUP1]] (+0.70, fdr 7e-06), [[SDHAF4]] (+0.63, fdr 7e-06), [[TMEM68]] (+0.62, fdr 1e-05); moves opposite to [[C11orf96]] (-0.57, fdr 1e-05), [[NR4A1]] (-0.56, fdr 3e-05), [[ALCAM]] (-0.51, fdr 6e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1991.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2030 2.14×, NCI-H23 2.69×, HS-578T 3.08×, LoVo 2.18×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +21.9 | 0e+00 | 43/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +10.6 | 1e-23 | 32/48 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.40×** | +9.2 | 5e-18 | 31/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.39×** | +8.9 | 1e-16 | 27/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +7.7 | 2e-12 | 27/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.27×** | +6.8 | 9e-10 | 24/48 (BT-474, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.22×** | +5.6 | 2e-06 | 18/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.20×** | +5.3 | 1e-05 | 17/48 (BT-474, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.18× | +4.6 | 2e-04 | 17/48 (PANC-1, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.004 | 11/48 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.4 | 0.039 | 13/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.12× | +3.2 | 0.060 | 7/48 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.12× | +3.2 | 0.061 | 12/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.089 | 13/48 (KATO III, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.090 | 11/47 (NCI-H2030, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 1.08× | +3.0 | 0.090 | 3/48 (A498, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -13.6 | 1e-39 | 41/49 (A549, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.519×** | -9.6 | 2e-19 | 29/48 (RKO, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.750×** | -8.1 | 1e-13 | 27/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -8.0 | 2e-13 | 26/44 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.766×** | -7.2 | 8e-11 | 24/47 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.837× | -7.0 | 2e-10 | 23/48 (J82, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.784×** | -6.8 | 8e-10 | 24/48 (A-427, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.794×** | -6.4 | 9e-09 | 22/48 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.804×** | -6.1 | 7e-08 | 22/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.811×** | -5.9 | 3e-07 | 21/48 (NCI-H460, J82, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -5.1 | 1e-05 | 15/48 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.724×** | -4.7 | 1e-04 | 19/48 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.854× | -4.4 | 5e-04 | 20/48 (SW480, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.875× | -3.7 | 0.008 | 16/48 (NCI-H2030, SW 1271, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.884× | -3.3 | 0.039 | 9/47 (SW1417, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.0 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 51.2 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.461× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 43.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.229× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0873× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 31.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -13.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 37.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 33.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[KATO III (line)]] | alt | 32.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 43.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 62.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 53.6 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.183× (z -8.7) |
| [[SNU-1 (line)]] | wt | 38.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Hydroxyfasudil (drug)]] 5 µM 0.0583× (z -9.2) |
| [[A498 (line)]] | wt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -12.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 46.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.5) | — |
| [[H4 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[HS-578T (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 92.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +14.9) | — |
| [[NCI-H23 (line)]] | alt | 50.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.5) | — |
| [[RKO (line)]] | wt | 48.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0202× (z -18.9) |
| [[SHP-77 (line)]] | alt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.2) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SW 900 (line)]] | alt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 38.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.3) | — |
| [[SW48 (line)]] | wt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZUP1]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[SDHAF4]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TMEM68]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CIAO2A]] | +0.62 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[GLE1]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PPP1R8]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CMC1]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[BIVM]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[C8orf76]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[MTX2]] | +0.59 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[INTS8]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.58 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf96]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[NR4A1]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ALCAM]] | -0.51 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[KLF2]] | -0.51 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[CSRNP1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[IER2]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[IL3RA]] | -0.48 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[JUNB]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SOCS3]] | -0.48 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[LINC00641]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MFSD12]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[LIMA1]] | -0.48 | -0.37 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMED8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FZD3]] | B | FZD3 activity raises TMED8's level | lines that do not express FZD3 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without FZD3 | 0.060 | ⚠ within organs, on part of the lines; also absent: FBXO16, SLC16A10, LINC02456; maybe low, not absent; its own permutation p |
| [[CCDC144CP]] | B | CCDC144CP activity raises TMED8's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without CCDC144CP | 0.079 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[FGD1]] | B | FGD1 activity raises TMED8's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without FGD1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.2, 19.6); signed map (-30.6, -19.6). **Vector** length 91.6, 19.0% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.1 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +21.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +5.0 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.9 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.6 | +5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.5 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -0.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,335,029-77,377,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM15B |
| Gene groups (HGNC) | GOLD domain containing |
| Matched by | ensembl_id |

UniProt [Q6PL24](https://www.uniprot.org/uniprotkb/Q6PL24) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:18633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18633) · Entrez [283578](https://www.ncbi.nlm.nih.gov/gene/283578) · UniProt [Q6PL24](https://www.uniprot.org/uniprotkb/Q6PL24) · Ensembl [ENSG00000100580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100580)

## Data

Gene col 1991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1991); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1991]; `tensor/DDL_lfc|DDL_z.npy` [1991]; `embed/gene_vectors.npy` [1991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1991 or target_col == 1991). Every well: [[TMED8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
