---
symbol: "TFRC"
type: "gene"
col: 1014
ensembl_id: "ENSG00000072274"
name: "transferrin receptor"
location: "3q29"
module: 149
arm: "+"
pooled_cpm: 150.62
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 8
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# TFRC

*transferrin receptor* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 4.21× (z +15.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Sodium Salicylate (drug)]] 5 µM: 0.693× (z -5.8, q 5e-06, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTDSS1]] (+0.64, fdr 7e-06), [[SLC16A1]] (+0.63, fdr 7e-06), [[PRPS2]] (+0.60, fdr 1e-05); moves opposite to [[ZNF579]] (-0.69, fdr 1e-05), [[ANKRD49]] (-0.66, fdr 7e-06), [[MAU2]] (-0.66, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.21×** | +15.9 | 0e+00 | 48/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.98×** | +12.0 | 6e-31 | 47/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.94×** | +11.9 | 2e-30 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.76×** | +10.6 | 3e-24 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.63×** | +10.1 | 5e-22 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +9.8 | 1e-20 | 44/49 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.48×** | +9.5 | 2e-19 | 46/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +8.5 | 1e-15 | 33/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **4.67×** | +8.1 | 3e-14 | 48/48 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.00×** | +7.6 | 1e-12 | 45/48 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Ciclopirox (drug)]] 5 µM |  | **1.62×** | +7.5 | 3e-12 | 45/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.87×** | +6.9 | 3e-10 | 42/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.80×** | +6.2 | 2e-08 | 30/44 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.74×** | +6.1 | 5e-08 | 32/49 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.70×** | +5.6 | 7e-07 | 34/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +5.4 | 3e-06 | 34/48 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +5.3 | 4e-06 | 43/48 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 1e-05 | 33/48 (NCI-H1573, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.8 | 3e-05 | 34/48 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +4.3 | 5e-04 | 39/49 (NCI-H1573, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.002 | 37/48 (AsPC-1, A498, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.033 | 30/48 (SW 900, H4, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.044 | 26/48 (A-172, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.693×** | -5.8 | 5e-06 | 48/49 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.689×** | -4.1 | 0.010 | 38/48 (SW 1088, SW 900, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.698×** | -4.0 | 0.012 | 37/49 (NCI-H2347, NCI-H2030, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.709×** | -3.8 | 0.019 | 28/48 (COLO 205, KATO III, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.789×** | -3.7 | 0.022 | 36/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.735×** | -3.4 | 0.052 | 30/48 (SW 1271, LS 180, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **0.735×** | -3.4 | 0.052 | 38/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.765×** | -3.2 | 0.084 | 30/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.745× | -3.1 | 0.12 | 23/48 (KATO III, RKO, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.819× | -3.1 | 0.12 | 24/48 (SW480, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.752× | -3.0 | 0.12 | 21/48 (SW480, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 96.2 | 14 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 15.3× (z +21.3) | — |
| [[NCI-H460 (line)]] | wt | 106 | 12 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 27.1× (z +25.1) | — |
| [[AsPC-1 (line)]] | alt | 73.7 | 11 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 16.7× (z +23.7) | — |
| [[LoVo (line)]] | wt | 129 | 11 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.1× (z +20.8) | — |
| [[NCI-H1792 (line)]] | alt | 92.8 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +20.2) | — |
| [[SW480 (line)]] | alt | 206 | 9 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.64× (z +20.8) | — |
| [[KATO III (line)]] | alt | 213 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.52× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 101 | 8 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.15× (z +19.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 111 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.7× (z +18.4) | — |
| [[SW 900 (line)]] | alt | 132 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.23× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 181 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.5× (z +19.3) | — |
| [[Panc 03.27 (line)]] | alt | 162 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +14.1) | — |
| [[SW48 (line)]] | wt | 244 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.2× (z +18.0) | — |
| [[COLO 205 (line)]] | alt | 178 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.95× (z +18.3) | — |
| [[H4 (line)]] | wt | 133 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.30× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 208 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +12.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 49.4 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.85× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 123 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.72× (z +11.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 162 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.11× (z +20.2) | — |
| [[SNU-423 (line)]] | alt | 79.7 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 203 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.02× (z +16.5) | — |
| [[A498 (line)]] | wt | 98.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +20.4) | — |
| [[HT-29 (line)]] | alt | 215 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.4) | — |
| [[A-427 (line)]] | wt | 138 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +14.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 153 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 200 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.01× (z +11.4) | — |
| [[A-172 (line)]] | wt | 73.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 251 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 128 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.31× (z +11.2) | — |
| [[J82 (line)]] | alt | 155 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 215 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.09× (z +9.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.38× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 204 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +15.0) | — |
| [[SHP-77 (line)]] | alt | 94.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 197 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +15.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[BT-474 (line)]] | alt | 207 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +8.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[C32 (line)]] | wt | 143 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 225 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.35× (z +9.7) | — |
| [[RKO (line)]] | wt | 202 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +9.3) | — |
| [[A549 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 174 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*28 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTDSS1]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLC16A1]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PRPS2]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[AHCY]] | +0.56 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CYCS]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 | STRING 400 |
| [[PAICS]] | +0.55 | +0.45 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[BPNT2]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MDH2]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 | STRING 436 |
| [[GLB1L2]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PKM]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[BTAF1]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ARHGAP4]] | +0.53 | +0.40 / +0.52 | both halves | 5e-05 | pathway: CDC42 GTPase cycle |

## Genes that move opposite

*72 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF579]] | -0.69 | -0.57 / -0.72 | both halves | 1e-05 |  |
| [[ANKRD49]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[MAU2]] | -0.66 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[NKAPD1]] | -0.64 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.63 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[TRAPPC2B]] | -0.61 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[TTF1]] | -0.61 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[FRG1]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[TRIM4]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[EAPP]] | -0.59 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[GPATCH8]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TEFM]] | -0.58 | -0.56 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TFRC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction -0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.0, 2.2); signed map (-46.7, 25.4). **Vector** length 103, 40.2% of its response variance represented; |z| ≥ 3 in 1,567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +9.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | +9.0 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +9.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -7.4 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.0 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.9 | +0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | +8.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | transferrin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,012,511-196,082,153 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD71, TFR1, p90 |
| Gene groups (HGNC) | CD molecules; M28 metallopeptidases |
| Hallmark sets | UV_RESPONSE_UP, HEME_METABOLISM, MTORC1_SIGNALING, E2F_TARGETS |
| Reactome | 27 pathways, smallest: Transferrin endocytosis and recycling; RHOH GTPase cycle; RND1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P02786](https://www.uniprot.org/uniprotkb/P02786) (Transferrin receptor protein 1):

> Cellular uptake of iron occurs via receptor-mediated endocytosis of ligand-occupied transferrin receptor into specialized endosomes. Endosomal acidification leads to iron release. The apotransferrin-receptor complex is then recycled to the cell surface with a return to neutral pH and the concomitant loss of affinity of apotransferrin for its receptor. Transferrin receptor is necessary for development of erythrocytes and the nervous system (By similarity). A second ligand, the hereditary …

**Summary**, from NCBI Gene [7037](https://www.ncbi.nlm.nih.gov/gene/7037):

> This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:11763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11763) · Entrez [7037](https://www.ncbi.nlm.nih.gov/gene/7037) · UniProt [P02786](https://www.uniprot.org/uniprotkb/P02786) · Ensembl [ENSG00000072274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072274)

## Data

Gene col 1014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1014); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1014]; `tensor/DDL_lfc|DDL_z.npy` [1014]; `embed/gene_vectors.npy` [1014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1014 or target_col == 1014). Every well: [[TFRC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFRC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
