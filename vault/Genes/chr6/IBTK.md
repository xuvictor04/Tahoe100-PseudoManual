---
symbol: "IBTK"
type: "gene"
col: 86
ensembl_id: "ENSG00000005700"
name: "inhibitor of Bruton tyrosine kinase"
location: "6q14.1"
module: 49
arm: "+"
pooled_cpm: 182.14
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# IBTK

*inhibitor of Bruton tyrosine kinase* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.31× (z +6.7, q 2e-08, up in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 1.29× (z +4.8, q 5e-04, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.398× (z -24.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL1]] (+0.54, fdr 1e-05), [[PCYT1A]] (+0.53, fdr 8e-05), [[UFL1]] (+0.53, fdr 6e-05); moves opposite to [[GHDC]] (-0.50, fdr 0.001, ⚠ one half only (not replicated)), [[NUMA1]] (-0.49, fdr 6e-04), [[EMP2]] (-0.47, fdr 4e-05), [[CCND3]] (-0.44, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 86.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +6.7 | 2e-08 | 30/48 (SW480, C32, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 5e-04 | 30/48 (SW480, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.2 | 0.004 | 18/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.9 | 0.012 | 20/45 (C32, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.16× | +3.8 | 0.014 | 7/48 (COLO 205, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.018 | 18/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.021 | 12/49 (SNU-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.13× | +3.6 | 0.021 | 8/49 (RKO, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.021 | 17/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | 1.14× | +3.5 | 0.024 | 10/48 (A549, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.039 | 17/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.046 | 16/48 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.079 | 14/48 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.097 | 13/48 (NCI-H1792, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.13× | +3.0 | 0.097 | 13/47 (SNU-1, NCI-H2030, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.097 | 7/48 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 86.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -24.0 | 0e+00 | 48/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -23.1 | 0e+00 | 48/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.513×** | -17.4 | 0e+00 | 48/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -14.1 | 3e-43 | 38/48 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -13.7 | 1e-40 | 40/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -12.7 | 4e-35 | 41/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.632×** | -11.9 | 6e-31 | 45/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -10.8 | 2e-25 | 37/48 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.666×** | -10.6 | 2e-24 | 36/48 (SW480, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.732×** | -10.3 | 3e-23 | 39/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -10.1 | 2e-22 | 38/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.671×** | -9.6 | 4e-20 | 31/45 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.704×** | -9.1 | 3e-18 | 35/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -8.2 | 8e-15 | 32/49 (NCI-H2347, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.738×** | -7.6 | 1e-12 | 27/44 (SK-MEL-2, C-33 A, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.763×** | -7.0 | 7e-11 | 32/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.803×** | -5.7 | 4e-07 | 27/49 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.652×** | -5.6 | 7e-07 | 29/49 (A549, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -5.5 | 1e-06 | 19/48 (MIA PaCa-2, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 86. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 195 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 267 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -17.8) |
| [[A498 (line)]] | wt | 298 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -25.9) |
| [[NCI-H460 (line)]] | wt | 154 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -15.0) |
| [[RKO (line)]] | wt | 175 | 2 (2 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.365× (z -14.6) |
| [[SW480 (line)]] | alt | 137 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -20.5) |
| [[A549 (line)]] | wt | 276 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -25.8) |
| [[HOP62 (line)]] | alt | 208 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -16.1) |
| [[PANC-1 (line)]] | alt | 262 | 2 (2 ⚠) | 6 | [[Harringtonine (drug)]] 5 µM 1.82× (z +9.7) ⚠ cell-cycle shift, explains ~93% of this change | [[Panobinostat (drug)]] 5 µM 0.306× (z -19.8) |
| [[LS 180 (line)]] | wt | 289 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 185 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -20.0) |
| [[Hs 766T (line)]] | wt | 267 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -19.4) |
| [[J82 (line)]] | alt | 183 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -15.2) |
| [[LoVo (line)]] | wt | 228 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -20.5) |
| [[SW 900 (line)]] | alt | 230 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -17.2) |
| [[HepG2_C3A (line)]] | wt | 252 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 293 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 195 | 1 | 4 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.91× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -10.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.472× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 156 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -14.5) |
| [[A-172 (line)]] | wt | 153 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.3) |
| [[H4 (line)]] | wt | 90.1 | 0 | 4 (2 ⚠) | — | [[OTS514 (drug)]] 5 µM 0.0520× (z -12.5) |
| [[HT-29 (line)]] | alt | 195 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -14.3) |
| [[KATO III (line)]] | alt | 195 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.360× (z -12.4) |
| [[SNU-1 (line)]] | wt | 373 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.0) |
| [[A-427 (line)]] | wt | 86.7 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.3) ⚠ cell-cycle shift, explains ~32% of this change | [[Panobinostat (drug)]] 0.5 µM 0.488× (z -9.5) |
| [[BT-474 (line)]] | alt | 171 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.422× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.481× (z -9.0) |
| [[C-33 A (line)]] | alt | 124 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.409× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 142 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.405× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 100.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.397× (z -10.5) |
| [[SHP-77 (line)]] | alt | 104 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -11.8) |
| [[SW1417 (line)]] | alt | 103 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -11.8) |
| [[SW48 (line)]] | wt | 107 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -11.4) |
| [[COLO 205 (line)]] | alt | 108 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -9.3) |
| [[CHP-212 (line)]] | wt | 131 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -28.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SNU-423 (line)]] | alt | 200 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.514× (z -9.4) |
| [[AN3 CA (line)]] | alt | 155 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 86), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL1]] | +0.54 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PCYT1A]] | +0.53 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[UFL1]] | +0.53 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[PREB]] | +0.52 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[CEP290]] | +0.52 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[PSMD4]] | +0.52 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[GOLGA5]] | +0.51 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[CMAS]] | +0.51 | +0.58 / +0.30 | both halves | 2e-04 |  |
| [[SLC33A1]] | +0.51 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[USO1]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SUPT20H]] | +0.49 | +0.49 / +0.25 | both halves | 4e-04 |  |
| [[NDUFV3]] | +0.49 | +0.44 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GHDC]] | -0.50 | -0.64 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[NUMA1]] | -0.49 | -0.49 / -0.22 | both halves | 6e-04 |  |
| [[EMP2]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CCND3]] | -0.44 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MAML1]] | -0.44 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[H2AZ2]] | -0.44 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[IL11RA]] | -0.44 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[RHOBTB2]] | -0.44 | -0.40 / -0.53 | both halves | 4e-05 | same gene group |
| [[STMN1]] | -0.44 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[EIF4EBP2]] | -0.44 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[KBTBD2]] | -0.44 | -0.35 / -0.36 | both halves | 1e-04 | same gene group |
| [[ATP1A1]] | -0.43 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[H3-3A]] | -0.43 | -0.31 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.6, -30.1); signed map (-57.2, 14.4). **Vector** length 121, 41.4% of its response variance represented; |z| ≥ 3 in 1,487 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.6 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +7.4 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +6.8 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.2 | +2.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.1 | -13.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -8.0 | -14.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.7 | -10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.9 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -10.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of Bruton tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:82,169,986-82,247,754 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564B116, BTBD26; previously BTKI |
| Gene groups (HGNC) | Ankyrin repeat domain containing; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2D0](https://www.uniprot.org/uniprotkb/Q9P2D0) (Inhibitor of Bruton tyrosine kinase):

> Acts as an inhibitor of BTK tyrosine kinase activity, thereby playing a role in B-cell development. Down-regulates BTK kinase activity, leading to interference with BTK-mediated calcium mobilization and NF-kappa-B-driven transcription.

**Summary**, from NCBI Gene [25998](https://www.ncbi.nlm.nih.gov/gene/25998):

> Bruton tyrosine kinase (BTK) is a protein tyrosine kinase that is expressed in B cells, macrophages, and neutrophils. The protein encoded by this gene binds to BTK and downregulates BTK's kinase activity. In addition, the encoded protein disrupts BTK-mediated calcium mobilization and negatively regulates the activation of nuclear factor-kappa-B-driven transcription. This gene has a pseudogene on chromosome 18. Alternative splicing results in multiple transcript variants encoding distinct …

**Accessions** — [HGNC:17853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17853) · Entrez [25998](https://www.ncbi.nlm.nih.gov/gene/25998) · UniProt [Q9P2D0](https://www.uniprot.org/uniprotkb/Q9P2D0) · Ensembl [ENSG00000005700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005700)

## Data

Gene col 86: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 86); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 86, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 86]; `tensor/DDL_lfc|DDL_z.npy` [86]; `embed/gene_vectors.npy` [86]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 86 or target_col == 86). Every well: [[IBTK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IBTK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
