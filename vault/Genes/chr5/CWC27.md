---
symbol: "CWC27"
type: "gene"
col: 7679
ensembl_id: "ENSG00000153015"
name: "CWC27 spliceosome associated cyclophilin"
location: "5q12.3"
module: 213
arm: "+"
pooled_cpm: 114.71
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# CWC27

*CWC27 spliceosome associated cyclophilin* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.65× (z +16.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.591× (z -25.1, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS50]] (+0.75, fdr 7e-06), [[ALKBH8]] (+0.70, fdr 7e-06), [[APOOL]] (+0.70, fdr 7e-06); moves opposite to [[LNX2]] (-0.56, fdr 1e-05), [[CCNYL1]] (-0.55, fdr 2e-05), [[INTS6L]] (-0.51, fdr 3e-05).
> It is in [[Module 213]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +16.9 | 0e+00 | 44/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +15.8 | 0e+00 | 44/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +15.7 | 0e+00 | 42/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +14.5 | 3e-45 | 39/49 (HS-578T, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +13.0 | 1e-36 | 40/49 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +11.1 | 1e-26 | 41/45 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +9.8 | 6e-21 | 27/45 (AsPC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.34×** | +9.5 | 2e-19 | 26/44 (MIA PaCa-2, HT-29, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +9.1 | 6e-18 | 38/48 (LoVo, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +7.9 | 1e-13 | 38/49 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +7.3 | 1e-11 | 30/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +7.1 | 8e-11 | 18/48 (AsPC-1, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.23×** | +6.8 | 4e-10 | 24/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.22×** | +6.6 | 2e-09 | 24/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +5.7 | 4e-07 | 22/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.14× | +4.0 | 0.002 | 15/47 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.008 | 12/48 (NCI-H2347, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.11× | +3.3 | 0.023 | 7/48 (HEC-1-A, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -25.1 | 0e+00 | 47/49 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -12.2 | 1e-31 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -9.6 | 1e-19 | 32/48 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.793×** | -7.8 | 6e-13 | 31/49 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -6.8 | 1e-09 | 29/50 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -6.1 | 1e-07 | 21/48 (A-427, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.878× | -4.2 | 0.002 | 17/47 (SNU-1, RKO, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.889× | -4.0 | 0.005 | 11/47 (SW 900, C32, …) | two highest doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.897× | -3.5 | 0.025 | 14/47 (J82, PANC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.906× | -3.2 | 0.072 | 7/47 (RKO, H4, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 59.2 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 128 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +11.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.34× (z +11.1) | — |
| [[LoVo (line)]] | wt | 96.5 | 5 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 152 | 4 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 146 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 2.70× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -21.9) |
| [[PANC-1 (line)]] | alt | 153 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.94× (z +14.7) | [[Panobinostat (drug)]] 0.5 µM 0.612× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 186 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.03× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.537× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 65.7 | 4 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.04× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -13.1) |
| [[COLO 205 (line)]] | alt | 92.4 | 4 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -12.3) |
| [[HS-578T (line)]] | alt | 119 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +12.4) | [[Tucidinostat (drug)]] 5 µM 0.627× (z -9.6) |
| [[SW480 (line)]] | alt | 162 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.71× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 82.5 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.57× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.7) |
| [[C32 (line)]] | wt | 86.5 | 3 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.48× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.3) |
| [[HOP62 (line)]] | alt | 55.0 | 3 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.4) |
| [[HT-29 (line)]] | alt | 80.4 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.24× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -8.7) |
| [[J82 (line)]] | alt | 90.4 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.0) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.432× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -9.7) |
| [[SNU-423 (line)]] | alt | 122 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.87× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -10.0) |
| [[A-172 (line)]] | wt | 89.1 | 2 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.02× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.9) |
| [[KATO III (line)]] | alt | 74.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.34× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.1) |
| [[SNU-1 (line)]] | wt | 142 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.53× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -17.1) |
| [[A549 (line)]] | wt | 90.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 213 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 105 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.73× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 65.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 105 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -11.8) |
| [[LS 180 (line)]] | wt | 103 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 132 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 123 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 1.93× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -13.4) |
| [[RKO (line)]] | wt | 146 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -20.7) |
| [[SW 900 (line)]] | alt | 97.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 79.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.0) |
| [[C-33 A (line)]] | alt | 180 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.634× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -13.5) |
| [[CHP-212 (line)]] | wt | 166 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.8) |
| [[H4 (line)]] | wt | 133 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 97.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 180 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -18.7) |
| [[SW1417 (line)]] | alt | 71.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -8.8) |
| [[SW48 (line)]] | wt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.7) |
| [[HCT15 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS50]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[ALKBH8]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[APOOL]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GTF3C3]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[CUL5]] | +0.65 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[CSTPP1]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.64 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[RBM41]] | +0.64 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[CDKAL1]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ERCC8]] | +0.62 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[CCNYL1]] | -0.55 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[INTS6L]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CXCR4]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[RELL1]] | -0.51 | -0.43 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CWC27's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-23.5, -1.0); signed map (-21.2, -21.3). **Vector** length 126, 37.2% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +16.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.9 | +15.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +15.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +7.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.1 | +6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +9.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +7.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.5 | -25.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -12.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.8 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | CWC27 spliceosome associated cyclophilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:64,766,368-65,102,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-10, SDCCAG-10; previously SDCCAG10 |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases; NTC associated proteins; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX04](https://www.uniprot.org/uniprotkb/Q6UX04) (Spliceosome-associated protein CWC27 homolog):

> As part of the spliceosome, plays a role in pre-mRNA splicing. Probable inactive PPIase with no peptidyl-prolyl cis-trans isomerase activity. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [10283](https://www.ncbi.nlm.nih.gov/gene/10283):

> Predicted to enable peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of U2-type precatalytic spliceosome and catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10664) · Entrez [10283](https://www.ncbi.nlm.nih.gov/gene/10283) · UniProt [Q6UX04](https://www.uniprot.org/uniprotkb/Q6UX04) · Ensembl [ENSG00000153015](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153015)

## Data

Gene col 7679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7679); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7679]; `tensor/DDL_lfc|DDL_z.npy` [7679]; `embed/gene_vectors.npy` [7679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7679 or target_col == 7679). Every well: [[CWC27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CWC27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
