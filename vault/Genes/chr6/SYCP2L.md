---
symbol: "SYCP2L"
type: "gene"
col: 7696
ensembl_id: "ENSG00000153157"
name: "synaptonemal complex protein 2 like"
location: "6p24.2"
module: 105
arm: "+"
pooled_cpm: 29.55
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 14
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# SYCP2L

*synaptonemal complex protein 2 like* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.53× (z +5.6, q 1e-05, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.379× (z -17.3, q 0e+00, down in 38 of 42 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.377× (z -12.8, q 6e-35, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM14B]] (+0.67, fdr 7e-06, ⚠ same locus), [[GRK3]] (+0.66, fdr 7e-06), [[RNMT]] (+0.60, fdr 3e-05), [[CCNH]] (+0.59, fdr 2e-05); moves opposite to [[NRIP1]] (-0.47, fdr 3e-05), [[ZBTB45]] (-0.45, fdr 4e-05), [[HPS6]] (-0.44, fdr 7e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RAPGEF4]] → it (grade B ⚠); 14 go from it, the strongest it → [[CCDC146]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.6 | 1e-05 | 24/43 (A-172, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.5 | 1e-05 | 23/43 (HOP62, A-172, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.074 | 12/42 (HOP62, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.29× | +3.4 | 0.10 | 19/43 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.27× | +3.0 | 0.30 | 11/42 (A-172, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.379×** | -17.3 | 0e+00 | 38/42 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.377×** | -12.8 | 6e-35 | 35/42 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.363×** | -12.7 | 6e-35 | 36/42 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.413×** | -11.6 | 9e-29 | 34/42 (Hs 766T, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.467×** | -10.0 | 2e-21 | 24/38 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.468×** | -9.6 | 1e-19 | 24/39 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.498×** | -8.8 | 1e-16 | 21/29 (NCI-H23, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.538×** | -8.1 | 3e-14 | 27/43 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.551×** | -7.8 | 4e-13 | 29/43 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.566×** | -6.9 | 3e-10 | 22/35 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -6.0 | 1e-07 | 28/42 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -6.0 | 1e-07 | 22/43 (HEC-1-A, SNU-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.724×** | -5.6 | 9e-07 | 28/43 (SNU-1, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.654×** | -5.6 | 1e-06 | 22/42 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.655×** | -5.5 | 1e-06 | 22/42 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -5.4 | 2e-06 | 22/42 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -5.2 | 5e-06 | 22/42 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.712×** | -4.3 | 6e-04 | 21/43 (PANC-1, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -4.2 | 8e-04 | 17/42 (HCT15, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.739×** | -3.8 | 0.004 | 11/43 (COLO 205, HepG2/C3A, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.008 | 18/43 (C32, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.682×** | -3.4 | 0.017 | 15/43 (C-33 A, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -2.8 | 0.090 | 7/43 (HOP62, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 83.3 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 81.7 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.310× (z -11.0) |
| [[PANC-1 (line)]] | alt | 57.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -17.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.114× (z -16.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.5) |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.114× (z -12.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 67.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[C32 (line)]] | wt | 23.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.168× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.153× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -9.0) |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 47.0 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.166× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -10.5) |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.290× (z -8.8) |
| [[A-427 (line)]] | wt | 84.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HCT15 (line)]] | alt | 52.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -8.6) |
| [[J82 (line)]] | alt | 30.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.143× (z -11.4) |
| [[A498 (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -10.0) |
| [[KATO III (line)]] | alt | 10.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 15.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0264× (z -19.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -15.3) |
| [[SW480 (line)]] | alt | 10.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 11.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.36× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0801× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0386× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -14.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.91 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0603× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[AN3 CA (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14B]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 | ⚠ same locus (34.1 kb, same strand: neighbours can correlate without regulation) |
| [[GRK3]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[RNMT]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[CCNH]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PPP1R32]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CRYBB2P1-1]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LINC02935]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.54 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[LONP1]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[EFCAB3P1]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[DUXAP10]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SLC2A1-DT]] | +0.53 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[SCARB1]] | +0.53 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRIP1]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ZBTB45]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[HPS6]] | -0.44 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[SH3RF1]] | -0.44 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[RBM15B]] | -0.43 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[CNP]] | -0.43 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SLC27A3]] | -0.42 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[TRIM47]] | -0.42 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[GPR87]] | -0.42 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[CHAMP1]] | -0.42 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[ZNF623]] | -0.42 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[ZNF747]] | -0.42 | -0.44 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF4]] | B | RAPGEF4 activity raises SYCP2L's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 3.72× lower at baseline in the lines without RAPGEF4 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[LINC02885]] | B | LINC02885 activity raises SYCP2L's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 1.84× lower at baseline in the lines without LINC02885 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |
| [[DUXAP10]] | B | DUXAP10 activity raises SYCP2L's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without DUXAP10 | 0.051 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[LINC02112]] | B | LINC02112 activity raises SYCP2L's level | lines that do not express LINC02112 (6) vs lines expressing it (44) | 2.56× lower at baseline in the lines without LINC02112 | 0.079 | ⚠ within organs, on part of the lines; also absent: DNAH6, IQCM, LINC02932; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC146]] | B | SYCP2L activity raises CCDC146's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without SYCP2L | 0.010 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[C9orf153]] | B | SYCP2L activity raises C9orf153's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.52× lower at baseline in the lines without SYCP2L | 0.010 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[TMEM14B]] | B | SYCP2L activity raises TMEM14B's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without SYCP2L | 0.012 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[TTC28-AS1]] | B | SYCP2L activity raises TTC28-AS1's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without SYCP2L | 0.049 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[LINC02935]] | B | SYCP2L activity raises LINC02935's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.71× lower at baseline in the lines without SYCP2L | 0.053 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[C4orf47]] | B | SYCP2L activity raises C4orf47's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without SYCP2L | 0.061 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[TPT1-AS1]] | B | SYCP2L activity raises TPT1-AS1's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without SYCP2L | 0.061 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[PPP1R32]] | B | SYCP2L activity raises PPP1R32's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without SYCP2L | 0.063 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[TXNDC12]] | B | SYCP2L activity raises TXNDC12's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without SYCP2L | 0.074 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[DUXAP10]] | B | SYCP2L activity raises DUXAP10's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.82× lower at baseline in the lines without SYCP2L | 0.074 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[EFCAB3P1]] | B | SYCP2L activity raises EFCAB3P1's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without SYCP2L | 0.078 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[C20orf96]] | B | SYCP2L activity raises C20orf96's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.85× lower at baseline in the lines without SYCP2L | 0.082 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.4, 33.8); signed map (-44.6, 23.5). **Vector** length 76.9, 15.9% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.1 | +3.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.1 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.6 | -17.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -12.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -12.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | synaptonemal complex protein 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:10,886,831-10,979,320 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ62D2.1, NO145; previously C6orf177 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T4T6](https://www.uniprot.org/uniprotkb/Q5T4T6) (Synaptonemal complex protein 2-like):

> Oocyte-specific protein that localizes to centromeres at the dictyate stage and regulates the survival of primordial oocytes.

**Summary**, from NCBI Gene [221711](https://www.ncbi.nlm.nih.gov/gene/221711):

> Predicted to act upstream of or within negative regulation of programmed cell death. Located in condensed chromosome, centromeric region and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21537) · Entrez [221711](https://www.ncbi.nlm.nih.gov/gene/221711) · UniProt [Q5T4T6](https://www.uniprot.org/uniprotkb/Q5T4T6) · Ensembl [ENSG00000153157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153157)

## Data

Gene col 7696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7696); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7696]; `tensor/DDL_lfc|DDL_z.npy` [7696]; `embed/gene_vectors.npy` [7696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7696 or target_col == 7696). Every well: [[SYCP2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYCP2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
