---
symbol: "LRRFIP2"
type: "gene"
col: 1721
ensembl_id: "ENSG00000093167"
name: "LRR binding FLII interacting protein 2"
location: "3p22.2"
module: 214
arm: "+"
pooled_cpm: 172.65
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# LRRFIP2

*LRR binding FLII interacting protein 2* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.13× (z +14.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.762× (z -5.3, q 4e-05, down in 27 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.792× (z -4.4, q 0.002, down in 29 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF5]] (+0.64, fdr 1e-05), [[ARHGAP17]] (+0.63, fdr 7e-06), [[MBD2]] (+0.60, fdr 1e-05); moves opposite to [[EGR1]] (-0.58, fdr 1e-05), [[CCNT1]] (-0.57, fdr 1e-05), [[AGPAT5]] (-0.54, fdr 2e-05).
> It is in [[Module 214]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.13×** | +14.8 | 0e+00 | 47/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +13.3 | 8e-38 | 43/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.98×** | +12.6 | 3e-34 | 48/48 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +12.2 | 4e-32 | 47/48 (LS 180, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +11.8 | 3e-30 | 40/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.5 | 2e-19 | 33/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +9.0 | 2e-17 | 40/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +8.2 | 2e-14 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.65×** | +7.0 | 1e-10 | 43/49 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +6.5 | 6e-09 | 36/49 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 1e-08 | 33/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +6.3 | 1e-08 | 30/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +5.9 | 1e-07 | 35/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.8 | 3e-07 | 32/45 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.4 | 2e-06 | 33/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.4 | 3e-06 | 30/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 1e-04 | 25/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.001 | 27/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.762×** | -5.3 | 4e-05 | 27/49 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.756×** | -5.3 | 4e-05 | 23/44 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.792×** | -4.4 | 0.002 | 29/49 (NCI-H1792, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.800×** | -4.3 | 0.002 | 28/48 (COLO 205, NCI-H1792, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.807×** | -4.2 | 0.003 | 27/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.812×** | -4.1 | 0.005 | 26/48 (HepG2/C3A, CFPAC-1, …) | top dose only |  |
| [[Ranolazine (drug)]] 0.05 µM |  | **0.825×** | -3.7 | 0.015 | 23/48 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.015 | 23/48 (A498, SW 900, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.018 | 22/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.842× | -3.3 | 0.047 | 21/48 (NCI-H1792, Panc 03.27, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.844× | -3.3 | 0.048 | 18/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | 0.846× | -3.3 | 0.052 | 18/48 (C-33 A, NCI-H1573, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.849× | -3.2 | 0.064 | 19/48 (NCI-H1792, A-172, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.854× | -3.1 | 0.077 | 17/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.854× | -3.1 | 0.077 | 17/48 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Proglumide (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.077 | 17/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.856× | -3.0 | 0.077 | 18/48 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.857× | -3.0 | 0.077 | 21/48 (C32, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 119 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +30.7) | — |
| [[NCI-H460 (line)]] | wt | 141 | 12 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.62× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.79× (z +15.8) | — |
| [[NCI-H23 (line)]] | alt | 129 | 9 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.74× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -11.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 150 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +10.5) | — |
| [[KATO III (line)]] | alt | 106 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.04× (z +14.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.2) | — |
| [[NCI-H1792 (line)]] | alt | 278 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.35× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +11.8) | — |
| [[A549 (line)]] | wt | 220 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +24.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -13.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 139 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 223 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.9) | — |
| [[A-172 (line)]] | wt | 269 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 125 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.89× (z +15.8) | — |
| [[NCI-H2347 (line)]] | alt | 318 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 122 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 128 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 86.9 | 3 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.34× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 61.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.36× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 97.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.90× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 248 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.50× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 140 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.56× (z +18.1) | — |
| [[RKO (line)]] | wt | 169 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.68× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 218 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +9.0) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.68× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 196 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.25× (z +10.6) | — |
| [[A498 (line)]] | wt | 260 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 107 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.61× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 102 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 169 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 407 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.86× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 136 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.77× (z +10.4) | — |
| [[SW48 (line)]] | wt | 165 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.28× (z +10.4) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 200 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.35× (z +9.6) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 217 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.44× (z +9.4) | — |
| [[J82 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.20× (z +9.6) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 201 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 196 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.64× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 149 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.25× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 152 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 188 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 232 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF5]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP17]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MBD2]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PPP4R1]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[KIF1B]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[HSF2]] | +0.56 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[KPNA1]] | +0.56 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MRTFA]] | +0.55 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KRAS]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[DENND1B]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[RAB18]] | +0.53 | +0.61 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR1]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[CCNT1]] | -0.57 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[AGPAT5]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[NCBP2]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MCL1]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[EGR3]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[DDX18]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SPRED1]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CYB5D1]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[DGUOK]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGR2]] | B | EGR2 activity lowers LRRFIP2's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.39× higher at baseline in the lines without EGR2 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, -11.8); signed map (-28.3, -16.1). **Vector** length 113, 41.0% of its response variance represented; |z| ≥ 3 in 1,460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.6 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +14.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +12.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.0 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +12.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.7 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.5 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.2 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | +9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | +5.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +0.3 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.3 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | LRR binding FLII interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:37,052,626-37,183,689 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HUFI-2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y608](https://www.uniprot.org/uniprotkb/Q9Y608) (Leucine-rich repeat flightless-interacting protein 2):

> May function as activator of the canonical Wnt signaling pathway, in association with DVL3, upstream of CTNNB1/beta-catenin. Positively regulates Toll-like receptor (TLR) signaling in response to agonist probably by competing with the negative FLII regulator for MYD88-binding.

**Summary**, from NCBI Gene [9209](https://www.ncbi.nlm.nih.gov/gene/9209):

> The protein encoded by this gene, along with MYD88, binds to the cytosolic tail of toll-like receptor 4 (TLR4), which results in activation of nuclear factor kappa B signaling. The ubiquitin-like protein FAT10 prevents the interaction of the encoded protein and TLR4, thereby inactivating the nuclear factor kappa B signaling pathway. In addition, this protein can downregulate the NLRP3 inflammasome by recruiting the caspase-1 inhibitor Flightless-I to the inflammasome complex. [provided by …

**Accessions** — [HGNC:6703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6703) · Entrez [9209](https://www.ncbi.nlm.nih.gov/gene/9209) · UniProt [Q9Y608](https://www.uniprot.org/uniprotkb/Q9Y608) · Ensembl [ENSG00000093167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000093167)

## Data

Gene col 1721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1721); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1721]; `tensor/DDL_lfc|DDL_z.npy` [1721]; `embed/gene_vectors.npy` [1721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1721 or target_col == 1721). Every well: [[LRRFIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRFIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
