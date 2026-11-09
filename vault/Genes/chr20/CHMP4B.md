---
symbol: "CHMP4B"
type: "gene"
col: 2135
ensembl_id: "ENSG00000101421"
name: "charged multivesicular body protein 4B"
location: "20q11.22"
module: 40
arm: "-"
pooled_cpm: 126.89
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CHMP4B

*charged multivesicular body protein 4B* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.28× (z +20.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.763× (z -5.7, q 8e-06, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.816× (z -4.7, q 3e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM8]] (+0.62, fdr 1e-05), [[CREBL2]] (+0.61, fdr 1e-05), [[TAB3]] (+0.58, fdr 1e-05); moves opposite to [[GLMN]] (-0.64, fdr 7e-06), [[INTS10]] (-0.58, fdr 2e-05), [[FANCC]] (-0.58, fdr 9e-06).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[VNN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +20.9 | 0e+00 | 44/48 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **5.87×** | +19.4 | 0e+00 | 49/49 (NCI-H1573, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +16.4 | 0e+00 | 41/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +15.1 | 0e+00 | 42/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +11.2 | 6e-27 | 37/44 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +11.2 | 6e-27 | 42/49 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +10.9 | 6e-26 | 40/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +10.5 | 6e-24 | 41/45 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.37×** | +9.5 | 2e-19 | 38/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +9.2 | 1e-18 | 37/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.2 | 3e-11 | 39/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.0 | 1e-10 | 35/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.9 | 3e-10 | 40/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.7 | 1e-09 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.3 | 1e-08 | 30/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 2e-06 | 30/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 3e-04 | 28/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 4e-04 | 24/48 (NCI-H1573, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 8e-04 | 24/47 (HT-29, PANC-1, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 21/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.004 | 24/48 (RPMI-7951, SW480, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.763×** | -5.7 | 8e-06 | 28/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.771×** | -5.5 | 1e-05 | 38/49 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.775×** | -5.4 | 1e-05 | 40/49 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.777×** | -5.3 | 2e-05 | 28/48 (A-172, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -4.7 | 3e-04 | 25/48 (SNU-423, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.806×** | -4.5 | 5e-04 | 25/48 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.4 | 0.048 | 20/49 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.846× | -3.3 | 0.066 | 19/48 (NCI-H1792, A549, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.746×** | -3.2 | 0.079 | 23/49 (COLO 205, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.861× | -3.2 | 0.092 | 14/48 (A549, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 89.7 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.24× (z +18.8) | — |
| [[KATO III (line)]] | alt | 146 | 9 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 55.1 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.0) | — |
| [[A-172 (line)]] | wt | 134 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +21.4) | [[Belinostat (drug)]] 5 µM 0.460× (z -10.1) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A549 (line)]] | wt | 112 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +22.7) | — |
| [[NCI-H1573 (line)]] | alt | 112 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 22.2× (z +19.4) | — |
| [[SW48 (line)]] | wt | 70.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 56.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 118 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.2) | — |
| [[SNU-423 (line)]] | alt | 176 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +21.6) | — |
| [[SW480 (line)]] | alt | 104 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +14.6) | — |
| [[A498 (line)]] | wt | 189 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 121 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +16.5) | — |
| [[LoVo (line)]] | wt | 94.8 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +17.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.2) | — |
| [[NCI-H1792 (line)]] | alt | 170 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.1) | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.39× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 280 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.61× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.461× (z -10.7) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HEC-1-A (line)]] | alt | 77.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 99.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +17.2) | — |
| [[J82 (line)]] | alt | 181 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 140 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 4.74× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 202 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +18.0) | — |
| [[RPMI-7951 (line)]] | alt | 144 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 89.4 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 14.3× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 131 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 319 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.08× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 211 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +20.9) | — |
| [[HepG2_C3A (line)]] | wt | 276 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.4) | — |
| [[RKO (line)]] | wt | 155 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.45× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 215 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.07× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.501× (z -8.9) ⚠ cell-cycle shift, explains ~17% of this change |
| [[Hs 766T (line)]] | wt | 219 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.05× (z +14.3) | — |
| [[HT-29 (line)]] | alt | 210 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 72.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.91× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +12.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 59.5 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.56× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 98.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.69× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 113 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.93× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0857× (z -9.8) |
| [[AN3 CA (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 190 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM8]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[CREBL2]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[TAB3]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[RIPK2-DT]] | +0.56 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ZBED9]] | +0.55 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[CCDC50]] | +0.55 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[STAT6]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF19]] | +0.55 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[MMRN2]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[COQ5]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[ZNF646]] | +0.53 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[OPTN]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 | pathway: Autophagy |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLMN]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[INTS10]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[FANCC]] | -0.58 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[EEF1AKMT4]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[PDE7A]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SDF2L1]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[NDC1]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 | pathway: HCMV Infection |
| [[ISOC2]] | -0.54 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ORC2]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[CLPP]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[BCKDHB]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NUP85]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 | pathway: HCMV Infection |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VNN1]] | B | VNN1 activity raises CHMP4B's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 1.53× lower at baseline in the lines without VNN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CHMP4B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CHMP4B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ITGB8]] | B | ITGB8 activity raises CHMP4B's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.23× lower at baseline in the lines without ITGB8 | 0.086 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.423). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.7, -22.0); signed map (9.4, -27.4). **Vector** length 102, 31.3% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.6 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.5 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +20.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +9.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | +0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | +6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | +0.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:33,811,348-33,854,366 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ553F4.4, Shax1, SNF7-2, VPS32B; previously C20orf178 |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III |
| Reactome | 29 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H444](https://www.uniprot.org/uniprotkb/Q9H444) (Charged multivesicular body protein 4b):

> Probable core component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. The …

**Summary**, from NCBI Gene [128866](https://www.ncbi.nlm.nih.gov/gene/128866):

> This gene encodes a member of the chromatin-modifying protein/charged multivesicular body protein (CHMP) protein family. The protein is part of the endosomal sorting complex required for transport (ESCRT) complex III (ESCRT-III), which functions in the sorting of endocytosed cell-surface receptors into multivesicular endosomes. The ESCRT machinery also functions in the final abscisson stage of cytokinesis and in the budding of enveloped viruses such as HIV-1. The three proteins of the CHMP4 …

**Accessions** — [HGNC:16171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16171) · Entrez [128866](https://www.ncbi.nlm.nih.gov/gene/128866) · UniProt [Q9H444](https://www.uniprot.org/uniprotkb/Q9H444) · Ensembl [ENSG00000101421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101421)

## Data

Gene col 2135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2135); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2135]; `tensor/DDL_lfc|DDL_z.npy` [2135]; `embed/gene_vectors.npy` [2135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2135 or target_col == 2135). Every well: [[CHMP4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
