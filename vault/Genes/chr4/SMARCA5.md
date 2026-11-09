---
symbol: "SMARCA5"
type: "gene"
col: 7695
ensembl_id: "ENSG00000153147"
name: "SNF2 related chromatin remodeling ATPase 5"
location: "4q31.21"
module: 51
arm: "+"
pooled_cpm: 157.9
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SMARCA5

*SNF2 related chromatin remodeling ATPase 5* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +15.5, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.91× (z +7.1, q 1e-10, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.726× (z -8.9, q 3e-16, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM4]] (+0.63, fdr 7e-06), [[SF3B1]] (+0.62, fdr 1e-05), [[ATRX]] (+0.62, fdr 8e-06); moves opposite to [[CAPN10]] (-0.60, fdr 1e-05), [[WDR20]] (-0.58, fdr 1e-05), [[PIGF]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.74×** | +15.5 | 0e+00 | 44/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +15.1 | 0e+00 | 46/49 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +13.2 | 3e-37 | 42/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +9.1 | 1e-17 | 38/48 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.52×** | +8.6 | 1e-15 | 38/48 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +7.6 | 3e-12 | 32/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +7.1 | 1e-10 | 42/49 (COLO 205, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 2e-06 | 31/48 (CFPAC-1, HT-29, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.30×** | +5.5 | 3e-06 | 27/48 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +5.2 | 1e-05 | 29/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.7 | 1e-04 | 28/48 (CFPAC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.002 | 25/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.37×** | +3.5 | 0.022 | 23/47 (HepG2/C3A, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.024 | 23/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.17× | +3.2 | 0.044 | 17/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.2 | 0.044 | 10/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Goserelin (acetate) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.058 | 5/49 (SHP-77, HT-29, …) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.058 | 17/48 (HCT15, HS-578T, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -8.9 | 3e-16 | 39/49 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.701×** | -5.3 | 3e-05 | 38/48 (SNU-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.9 | 2e-04 | 27/48 (A498, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.0 | 0.009 | 0/50 | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.839× | -3.7 | 0.026 | 21/48 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.060 | 20/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.855× | -3.2 | 0.13 | 15/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | 0.857× | -3.1 | 0.14 | 17/47 (AsPC-1, COLO 205, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.817× | -3.0 | 0.15 | 19/49 (CHP-212, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 157 | 12 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +17.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.90× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 219 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1573 (line)]] | alt | 167 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 158 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +16.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 116 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +19.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.44× (z +8.5) | — |
| [[LoVo (line)]] | wt | 173 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +18.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1792 (line)]] | alt | 166 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +19.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SNU-1 (line)]] | wt | 166 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.6) ⚠ cell-cycle shift, explains ~42% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.1) |
| [[A498 (line)]] | wt | 194 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +13.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +10.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 171 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +18.2) ⚠ cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -9.5) |
| [[C32 (line)]] | wt | 135 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +16.0) ⚠ cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.1) |
| [[HS-578T (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HT-29 (line)]] | alt | 207 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +11.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 141 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +14.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 105 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[LS 180 (line)]] | wt | 217 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 156 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 115 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2347 (line)]] | alt | 169 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.2) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[PANC-1 (line)]] | alt | 126 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 227 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HCT15 (line)]] | alt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 148 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +16.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Hs 766T (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +12.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 152 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[RKO (line)]] | wt | 187 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 87.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 181 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.8) ⚠ cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -8.5) |
| [[A-172 (line)]] | wt | 170 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 232 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 169 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW1417 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A-427 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 237 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 202 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SF3B1]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | same gene group; pathway: B-WICH complex positively regulates rRNA expression; STRING 905 |
| [[ATRX]] | +0.62 | +0.57 / +0.64 | both halves | 8e-06 | same gene group; pathway: Chromosome Maintenance; STRING 442 |
| [[DNAJC8]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CDC5L]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 | same gene group; STRING 572 |
| [[SAMD9]] | +0.57 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.57 | +0.46 / +0.61 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression; STRING 770 |
| [[FYTTD1]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[HTATSF1]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ACIN1]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[IFT81]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[RIF1]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN10]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[WDR20]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[PIGF]] | -0.55 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[FAM86DP]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[DHRS1]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[DPY19L3]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[POM121]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ZFYVE27]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZMYND19]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.5, 9.1); signed map (11.4, -27.8). **Vector** length 127, 40.8% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.8 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +6.5 | +15.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +1.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.3 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.3 | -8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | -6.8 | -3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -6.5 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -0.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.0 | -3.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.8 | -3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | SNF2 related chromatin remodeling ATPase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:143,513,702-143,557,486 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hSNF2H, hISWI, ISWI |
| Gene groups (HGNC) | Myb/SANT domain containing; SNF2 related family; Chromatin accessibility complex; B-WICH chromatin-remodelling complex subunits; ACF complex; WICH complex |
| Reactome | 13 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; B-WICH complex positively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O60264](https://www.uniprot.org/uniprotkb/O60264) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 5):

> ATPase that possesses intrinsic ATP-dependent nucleosome-remodeling activity. Catalytic subunit of ISWI chromatin-remodeling complexes, which form ordered nucleosome arrays on chromatin and facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair; this may require intact histone H4 tails. Within the ISWI chromatin-remodeling complexes, slides edge- and center-positioned histone octamers away from their original location on the DNA template. …

**Summary**, from NCBI Gene [8467](https://www.ncbi.nlm.nih.gov/gene/8467):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The protein encoded by this gene is a component of the chromatin remodeling and spacing factor RSF, a facilitator of the transcription of class II genes by RNA polymerase II. The encoded protein is similar in sequence to the Drosophila ISWI …

**Accessions** — [HGNC:11101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11101) · Entrez [8467](https://www.ncbi.nlm.nih.gov/gene/8467) · UniProt [O60264](https://www.uniprot.org/uniprotkb/O60264) · Ensembl [ENSG00000153147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153147)

## Data

Gene col 7695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7695); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7695]; `tensor/DDL_lfc|DDL_z.npy` [7695]; `embed/gene_vectors.npy` [7695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7695 or target_col == 7695). Every well: [[SMARCA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
