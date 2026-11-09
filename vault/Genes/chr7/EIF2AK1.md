---
symbol: "EIF2AK1"
type: "gene"
col: 1457
ensembl_id: "ENSG00000086232"
name: "eukaryotic translation initiation factor 2 alpha kinase 1"
location: "7p22.1"
module: 57
arm: "+"
pooled_cpm: 138.96
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# EIF2AK1

*eukaryotic translation initiation factor 2 alpha kinase 1* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +14.7, q 1e-45, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[AZD-7648 (drug)]] 5 µM: 1.78× (z +5.4, q 8e-06, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.527× (z -11.4, q 4e-27, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPRS1]] (+0.62, fdr 1e-05), [[ACP1]] (+0.61, fdr 1e-05), [[VPS35]] (+0.61, fdr 2e-05); moves opposite to [[LRFN4]] (-0.58, fdr 1e-05), [[NDUFA13]] (-0.57, fdr 3e-05, ⚠ NDUFA13 in the vector space only through flagged drug-doses), [[ZCCHC3]] (-0.55, fdr 3e-05), [[ZNF316]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +14.7 | 1e-45 | 47/49 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +12.9 | 1e-35 | 42/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +9.6 | 1e-19 | 37/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.43×** | +6.4 | 3e-08 | 40/48 (A549, SHP-77, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +5.8 | 9e-07 | 34/48 (A549, SNU-423, …) | two highest doses |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.78×** | +5.4 | 8e-06 | 43/48 (LoVo, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 2e-04 | 32/48 (A-172, HOP62, …) | two highest doses | position effect removed |
| [[Clofarabine (drug)]] 0.05 µM |  | **1.33×** | +4.6 | 3e-04 | 34/48 (CFPAC-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Goserelin (acetate) (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 3e-04 | 39/49 (KATO III, HS-578T, …) | inconsistent across doses | position effect removed |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 0.001 | 39/48 (SW480, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.012 | 15/48 (SW1417, NCI-H2030, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.15× | +3.6 | 0.016 | 9/48 (BT-474, COLO 205, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.022 | 27/47 (J82, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.21×** | +3.4 | 0.025 | 23/48 (A549, SHP-77, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.21×** | +3.3 | 0.040 | 24/50 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -11.4 | 4e-27 | 47/48 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -11.1 | 2e-26 | 47/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.691×** | -9.3 | 3e-18 | 38/48 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -8.6 | 9e-16 | 45/48 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.631×** | -8.2 | 4e-14 | 44/48 (H4, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.781×** | -4.2 | 0.002 | 24/48 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.803×** | -3.9 | 0.008 | 24/48 (SW48, KATO III, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.758×** | -3.4 | 0.051 | 26/47 (SW48, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.817×** | -3.2 | 0.085 | 23/48 (A-427, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.837× | -3.0 | 0.13 | 21/49 (A498, HOP62, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.839× | -3.0 | 0.14 | 20/47 (HOP62, C-33 A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 139 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -26.0) |
| [[BT-474 (line)]] | alt | 156 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -11.5) |
| [[SW480 (line)]] | alt | 167 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +14.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.480× (z -10.6) |
| [[Hs 766T (line)]] | wt | 130 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 122 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +11.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -13.1) |
| [[A-427 (line)]] | wt | 180 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -18.8) |
| [[A549 (line)]] | wt | 92.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +13.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.457× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 250 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.348× (z -12.9) |
| [[HS-578T (line)]] | alt | 119 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -11.5) |
| [[HT-29 (line)]] | alt | 167 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.432× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 161 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -12.9) |
| [[SNU-423 (line)]] | alt | 97.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +14.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -10.0) |
| [[A-172 (line)]] | wt | 133 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +12.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 77.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 167 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.367× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 95.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.401× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -9.3) |
| [[KATO III (line)]] | alt | 233 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.533× (z -8.6) |
| [[LoVo (line)]] | wt | 170 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.06× (z +8.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.417× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.502× (z -8.9) |
| [[LS 180 (line)]] | wt | 130 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.372× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 124 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 102 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -8.8) |
| [[PANC-1 (line)]] | alt | 198 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +14.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 89.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.1) |
| [[HCT15 (line)]] | alt | 241 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 87.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +12.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 54.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.295× (z -10.4) |
| [[SW1417 (line)]] | alt | 194 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +11.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.521× (z -8.9) |
| [[A498 (line)]] | wt | 232 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -11.6) |
| [[C-33 A (line)]] | alt | 89.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 68.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 97.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.364× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -9.5) |
| [[SHP-77 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 145 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPRS1]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 | STRING 587 |
| [[ACP1]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[VPS35]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[MDH1]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DYNC1LI2]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[NIPSNAP1]] | +0.60 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MIGA1]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LONP2]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[BLTP1]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ECHS1]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TMED2]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[COPB1]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRFN4]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[NDUFA13]] ⚠ | -0.57 | -0.58 / -0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCCHC3]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZNF316]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[DEAF1]] | -0.52 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[COPRS]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[HNRNPA0]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[GMEB2]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[CELF1]] | -0.51 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NOP56]] | -0.51 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[SEMA4C]] | -0.50 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ADNP]] | -0.50 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[IER5]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.2, -17.2); signed map (-31.3, -24.3). **Vector** length 103, 31.0% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.1 | +6.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +1.4 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +2.0 | +0.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.1 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.2 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.2 | -0.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.1 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2 alpha kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,022,247-6,059,175 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRI, KIAA1369, hHRI, HCR |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 2 alpha kinases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: Cellular response to mitochondrial stress; Response of EIF2AK1 (HRI) to heme deficiency; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQI3](https://www.uniprot.org/uniprotkb/Q9BQI3) (Eukaryotic translation initiation factor 2-alpha kinase 1):

> Metabolic-stress sensing protein kinase that phosphorylates the alpha subunit of eukaryotic translation initiation factor 2 (EIF2S1/eIF-2-alpha) in response to various stress conditions. Key activator of the integrated stress response (ISR) required for adaptation to various stress, such as heme deficiency, oxidative stress, osmotic shock, mitochondrial dysfunction and heat shock. EIF2S1/eIF-2-alpha phosphorylation in response to stress converts EIF2S1/eIF-2-alpha into a global protein …

**Summary**, from NCBI Gene [27102](https://www.ncbi.nlm.nih.gov/gene/27102):

> The protein encoded by this gene acts at the level of translation initiation to downregulate protein synthesis in response to stress. The encoded protein is a kinase that can be inactivated by hemin. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:24921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24921) · Entrez [27102](https://www.ncbi.nlm.nih.gov/gene/27102) · UniProt [Q9BQI3](https://www.uniprot.org/uniprotkb/Q9BQI3) · Ensembl [ENSG00000086232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086232)

## Data

Gene col 1457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1457); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1457]; `tensor/DDL_lfc|DDL_z.npy` [1457]; `embed/gene_vectors.npy` [1457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1457 or target_col == 1457). Every well: [[EIF2AK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2AK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
