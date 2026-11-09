---
symbol: "DYNC1I2"
type: "gene"
col: 1185
ensembl_id: "ENSG00000077380"
name: "dynein cytoplasmic 1 intermediate chain 2"
location: "2q31.1"
module: 17
arm: "+"
pooled_cpm: 135.41
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DYNC1I2

*dynein cytoplasmic 1 intermediate chain 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.60× (z +12.7, q 3e-34, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 1.97×, NCI-H2030 2.03×, A-427 2.39×, SNU-423 2.35×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (RPMI-7951 2.93×, SNU-423 2.36×, KATO III 2.17×, A-427 2.09×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.36×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.687× (z -10.2, q 1e-21, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIFAP3]] (+0.61, fdr 1e-05), [[ACTR10]] (+0.58, fdr 3e-05), [[ZC2HC1A]] (+0.58, fdr 5e-05); moves opposite to [[RAI1]] (-0.57, fdr 4e-05), [[SMAD6]] (-0.51, fdr 3e-05), [[HNRNPF]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1185.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 1.97×, NCI-H2030 2.03×, A-427 2.39×, SNU-423 2.35×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (RPMI-7951 2.93×, SNU-423 2.36×, KATO III 2.17×, A-427 2.09×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.36×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +12.7 | 3e-34 | 42/49 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +8.3 | 4e-14 | 32/44 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +6.1 | 2e-07 | 25/45 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.20×** | +4.8 | 2e-04 | 23/47 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.4 | 0.001 | 14/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.11 | 15/47 (SNU-1, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.13 | 2/48 (SW48, C-33 A) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.13 | 12/48 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.14 | 13/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -10.2 | 1e-21 | 37/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -9.8 | 4e-20 | 40/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.699×** | -9.7 | 4e-20 | 34/48 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.708×** | -9.4 | 8e-19 | 33/48 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.819×** | -7.7 | 2e-12 | 25/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.824×** | -7.4 | 1e-11 | 25/49 (A549, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.777×** | -6.9 | 6e-10 | 32/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.790×** | -6.4 | 1e-08 | 28/48 (A-172, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.793×** | -6.3 | 2e-08 | 28/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.828×** | -5.1 | 2e-05 | 24/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.832×** | -5.0 | 3e-05 | 23/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.709×** | -4.9 | 5e-05 | 24/49 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.847× | -4.5 | 3e-04 | 22/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | 0.857× | -4.1 | 0.002 | 19/47 (HepG2/C3A, AN3 CA, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.772×** | -3.7 | 0.009 | 19/45 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.910× | -3.6 | 0.010 | 10/48 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.05 µM |  | 0.887× | -3.3 | 0.035 | 4/48 (Hs 766T, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 192 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.497× (z -12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.571× (z -10.2) |
| [[HS-578T (line)]] | alt | 147 | 1 (1 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +10.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -11.1) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.479× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -13.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.537× (z -9.5) |
| [[HOP62 (line)]] | alt | 129 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.502× (z -11.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.620× (z -11.2) |
| [[LS 180 (line)]] | wt | 104 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -11.6) |
| [[A-427 (line)]] | wt | 96.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 186 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -16.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[H4 (line)]] | wt | 162 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.442× (z -9.8) |
| [[J82 (line)]] | alt | 136 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.643× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 181 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.528× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.541× (z -10.3) |
| [[A498 (line)]] | wt | 195 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.68× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.615× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[KATO III (line)]] | alt | 99.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 102 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +8.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.532× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 104 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.480× (z -8.8) |
| [[COLO 205 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.495× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 160 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[PANC-1 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +12.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.60× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIFAP3]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[ACTR10]] | +0.58 | +0.64 / +0.45 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins; STRING 970 |
| [[ZC2HC1A]] | +0.58 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[MYO5A]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZMYM6]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ABI1]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[DYNC1LI2]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 999 |
| [[DCTN2]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 | pathway: AURKA Activation by TPX2; STRING 996 |
| [[SUCLG1]] | +0.53 | +0.50 / +0.29 | both halves | 2e-04 |  |
| [[VPS29]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[VPS35]] | +0.51 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SUGT1]] | +0.51 | +0.57 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAI1]] | -0.57 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SMAD6]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPF]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PRDM15]] | -0.47 | -0.58 / -0.23 | both halves | 5e-04 |  |
| [[LRP5]] | -0.46 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[PKP4]] | -0.45 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[ZNF718]] | -0.43 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[CDC25A]] | -0.43 | -0.41 / -0.40 | both halves | 5e-05 | pathway: Cell Cycle Checkpoints |
| [[ADGRA3]] | -0.43 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[SUZ12P1]] | -0.43 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[RAVER1]] | -0.43 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[NUP210]] | -0.43 | -0.49 / -0.34 | both halves | 1e-04 | pathway: HCMV Early Events |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.332). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-20.8, -14.2); signed map (-15.9, 1.9). **Vector** length 110, 30.9% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.9 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +12.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +3.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.8 | -10.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | -9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | -4.3 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Artesunate (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[Erlotinib (drug)]] 5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein cytoplasmic 1 intermediate chain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:171,687,409-171,750,158 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIC74; previously DNCI2 |
| Gene groups (HGNC) | WD repeat domain containing; Dynein 1 complex subunits; Dynein intermediate chains |
| Reactome | 54 pathways, smallest: Aggrephagy; COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13409](https://www.uniprot.org/uniprotkb/Q13409) (Cytoplasmic dynein 1 intermediate chain 2):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function. Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles along microtubules. The intermediate chains mediate the binding of dynein to dynactin via its 150 kDa component (p150-glued) DCTN1 (By similarity). Involved in membrane-transport, such …

**Summary**, from NCBI Gene [1781](https://www.ncbi.nlm.nih.gov/gene/1781):

> This gene encodes a member of the dynein intermediate chain family. The encoded protein is a non-catalytic component of the cytoplasmic dynein 1 complex, which acts as a retrograde microtubule motor to transport organelles and vesicles. A pseudogene of this gene is located on chromosome 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:2964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2964) · Entrez [1781](https://www.ncbi.nlm.nih.gov/gene/1781) · UniProt [Q13409](https://www.uniprot.org/uniprotkb/Q13409) · Ensembl [ENSG00000077380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077380)

## Data

Gene col 1185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1185); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1185]; `tensor/DDL_lfc|DDL_z.npy` [1185]; `embed/gene_vectors.npy` [1185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1185 or target_col == 1185). Every well: [[DYNC1I2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC1I2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
