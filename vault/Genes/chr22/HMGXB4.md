---
symbol: "HMGXB4"
type: "gene"
col: 1910
ensembl_id: "ENSG00000100281"
name: "HMG-box containing 4"
location: "22q12.3"
module: 11
arm: "+"
pooled_cpm: 73.89
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# HMGXB4

*HMG-box containing 4* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.39× (z +11.1, q 1e-25, up in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.76× (z +7.0, q 4e-10, up in 29 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (PANC-1 2.61×, HS-578T 2.46×, BT-474 2.42×, RKO 2.43×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.81×, LoVo 1.99×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 1.74×; ⚠ cell-cycle shift, explains ~46% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.496× (z -16.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.78, fdr 7e-06), [[C1orf131]] (+0.74, fdr 7e-06), [[NAIF1]] (+0.72, fdr 7e-06); moves opposite to [[ILRUN]] (-0.68, fdr 7e-06), [[FKBP1A]] (-0.63, fdr 1e-05), [[ZDHHC16]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1910.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (PANC-1 2.61×, HS-578T 2.46×, BT-474 2.42×, RKO 2.43×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.81×, LoVo 1.99×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 1.74×; ⚠ cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.39×** | +11.1 | 1e-25 | 32/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +8.2 | 9e-14 | 34/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +7.0 | 4e-10 | 29/49 (LS 180, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.21×** | +4.6 | 7e-04 | 23/48 (PANC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.014 | 17/47 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.059 | 17/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.15× | +3.2 | 0.098 | 15/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1910.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.496×** | -16.7 | 0e+00 | 47/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.507×** | -16.1 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.554×** | -14.1 | 1e-42 | 48/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -9.9 | 4e-21 | 41/48 (SW480, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -9.4 | 9e-19 | 42/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.760×** | -9.2 | 2e-18 | 36/48 (NCI-H1573, A498, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -7.5 | 5e-12 | 27/43 (A-172, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -7.2 | 3e-11 | 34/48 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.763×** | -6.4 | 8e-09 | 31/49 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -6.4 | 8e-09 | 31/50 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -6.2 | 3e-08 | 29/47 (AN3 CA, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -5.1 | 2e-05 | 19/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.865× | -4.9 | 4e-05 | 17/49 (SHP-77, A498, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.676×** | -4.9 | 4e-05 | 27/49 (NCI-H661, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.817×** | -4.8 | 6e-05 | 26/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.852× | -3.7 | 0.007 | 14/47 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.897× | -3.7 | 0.007 | 9/48 (A-172, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 81.2 | 0 | 11 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -20.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 83.4 | 1 (1 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.365× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 80.7 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.7) |
| [[A498 (line)]] | wt | 78.2 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -10.2) |
| [[PANC-1 (line)]] | alt | 72.4 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +22.2) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.474× (z -12.1) |
| [[A-172 (line)]] | wt | 65.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -10.3) |
| [[C-33 A (line)]] | alt | 103 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -12.5) |
| [[C32 (line)]] | wt | 93.0 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 82.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.338× (z -13.3) |
| [[KATO III (line)]] | alt | 82.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -10.3) |
| [[LoVo (line)]] | wt | 72.2 | 1 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 1.99× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | [[Belinostat (drug)]] 5 µM 0.510× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 57.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.7) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.377× (z -10.8) |
| [[RKO (line)]] | wt | 80.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.6) ⚠ cell-cycle shift, explains ~45% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -14.2) |
| [[SNU-423 (line)]] | alt | 90.1 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.280× (z -15.1) |
| [[J82 (line)]] | alt | 64.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -10.1) |
| [[SHP-77 (line)]] | alt | 75.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.427× (z -9.2) |
| [[BT-474 (line)]] | alt | 75.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 53.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 56.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.425× (z -10.8) |
| [[HS-578T (line)]] | alt | 94.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.3) ⚠ cell-cycle shift, explains ~45% of this change | [[Auranofin (drug)]] 5 µM 0.404× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 67.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 81.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.404× (z -10.8) |
| [[SW1417 (line)]] | alt | 55.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -9.9) |
| [[A-427 (line)]] | wt | 61.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.3) |
| [[A549 (line)]] | wt | 59.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.3) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.148× (z -13.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 86.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 78.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[H4 (line)]] | wt | 74.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -9.9) |
| [[Hs 766T (line)]] | wt | 91.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.453× (z -9.3) |
| [[HT-29 (line)]] | alt | 50.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LS 180 (line)]] | wt | 79.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.489× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.482× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 71.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.220× (z -8.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -8.6) |
| [[SNU-1 (line)]] | wt | 97.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.545× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[COIL]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[THG1L]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.70 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[SNW1]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ESF1]] | +0.69 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.69 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.68 | +0.75 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILRUN]] | -0.68 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[FKBP1A]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ZDHHC16]] | -0.60 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[PABIR2]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[PLEKHB2]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ESYT1]] | -0.59 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SLC39A6]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[STRN]] | -0.58 | -0.70 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.760). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.7, 5.0); signed map (1.0, -18.6). **Vector** length 121, 34.8% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +11.6 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +9.1 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +7.9 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.0 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.7 | -9.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | HMG-box containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:35,257,452-35,295,807 (+) |
| Ensembl biotype | protein_coding |
| Also known as | THC211630, P53N; previously HMG2L1 |
| Gene groups (HGNC) | Non-canonical high mobility group |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGU5](https://www.uniprot.org/uniprotkb/Q9UGU5) (HMG domain-containing protein 4):

> Negatively regulates Wnt/beta-catenin signaling during development.

**Summary**, from NCBI Gene [10042](https://www.ncbi.nlm.nih.gov/gene/10042):

> High mobility group (HMG) proteins are nonhistone chromosomal proteins. See HMG2 (MIM 163906) for additional information on HMG proteins.[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:5003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5003) · Entrez [10042](https://www.ncbi.nlm.nih.gov/gene/10042) · UniProt [Q9UGU5](https://www.uniprot.org/uniprotkb/Q9UGU5) · Ensembl [ENSG00000100281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100281)

## Data

Gene col 1910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1910); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1910]; `tensor/DDL_lfc|DDL_z.npy` [1910]; `embed/gene_vectors.npy` [1910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1910 or target_col == 1910). Every well: [[HMGXB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGXB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
