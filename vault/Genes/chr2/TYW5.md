---
symbol: "TYW5"
type: "gene"
col: 8607
ensembl_id: "ENSG00000162971"
name: "tRNA-yW synthesizing protein 5"
location: "2q33.1"
module: 28
arm: "+"
pooled_cpm: 29.61
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TYW5

*tRNA-yW synthesizing protein 5* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.58× (z +35.9, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.658× (z -8.4, q 4e-14, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM128]] (+0.72, fdr 7e-06), [[FAM114A2]] (+0.69, fdr 7e-06), [[TRMT10B]] (+0.67, fdr 1e-05); moves opposite to [[PRDX1]] (-0.59, fdr 1e-05), [[HSPA8]] (-0.57, fdr 1e-05), [[TPI1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF571]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.58×** | +35.9 | 0e+00 | 47/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.69×** | +19.7 | 0e+00 | 45/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.71×** | +19.1 | 0e+00 | 42/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +17.5 | 0e+00 | 27/36 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +12.2 | 2e-32 | 29/43 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +11.2 | 4e-27 | 43/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +10.5 | 8e-24 | 43/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +9.9 | 2e-21 | 40/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +9.0 | 1e-17 | 30/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +7.4 | 6e-12 | 28/48 (CFPAC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.0 | 2e-10 | 30/45 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.7 | 6e-07 | 23/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +4.9 | 4e-05 | 22/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.7 | 9e-05 | 2/48 (MIA PaCa-2, HS-578T) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.24×** | +4.3 | 6e-04 | 20/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +4.2 | 9e-04 | 13/46 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.001 | 20/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.009 | 7/48 (LoVo, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.4 | 0.022 | 8/48 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.0 | 0.071 | 9/48 (LS 180, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -8.4 | 4e-14 | 32/48 (SW480, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.7 | 6e-04 | 21/47 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -4.6 | 6e-04 | 16/48 (SW480, J82, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -4.6 | 6e-04 | 17/48 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.816×** | -4.1 | 0.006 | 14/47 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.849× | -3.3 | 0.091 | 10/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.850× | -3.3 | 0.091 | 6/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.744× | -3.1 | 0.13 | 12/42 (Hs 766T, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.857× | -3.1 | 0.13 | 15/48 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.860× | -3.0 | 0.15 | 14/48 (SW480, PANC-1, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 37.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +21.6) | — |
| [[LoVo (line)]] | wt | 25.8 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +16.7) | — |
| [[NCI-H460 (line)]] | wt | 33.1 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +20.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.415× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 36.0 | 4 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +17.8) | [[Digitoxin (drug)]] 5 µM 0.396× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -9.4) |
| [[A-172 (line)]] | wt | 25.4 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +21.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0879× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 27.6 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +24.0) | [[Digitoxin (drug)]] 0.5 µM 0.455× (z -9.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HOP62 (line)]] | alt | 29.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +17.8) | — |
| [[A498 (line)]] | wt | 33.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +19.3) | — |
| [[NCI-H1573 (line)]] | alt | 43.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +17.7) | — |
| [[SW 900 (line)]] | alt | 28.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.18× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 21.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +14.8) | — |
| [[J82 (line)]] | alt | 30.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.1) | — |
| [[A549 (line)]] | wt | 35.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 25.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +18.0) | — |
| [[KATO III (line)]] | alt | 21.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 30.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +17.6) | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.0) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.114× (z -8.7) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 20.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 38.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 34.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.2) | — |
| [[RKO (line)]] | wt | 27.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +14.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 32.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 35.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.94× (z +14.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.306× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SNU-423 (line)]] | alt | 21.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.281× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 35.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.98× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.0) | — |
| [[A-427 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -12.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 1 | — | [[BAY1125976 (drug)]] 0.05 µM 0.0622× (z -9.0) |
| [[BT-474 (line)]] | alt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +15.1) | — |
| [[CHP-212 (line)]] | wt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.9) | — |
| [[SW48 (line)]] | wt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM128]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[FAM114A2]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.67 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[CHMP4A]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ZSCAN21]] | +0.66 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CHURC1]] | +0.66 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[MDM4]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ETFRF1]] | +0.64 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[POLI]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.63 | +0.79 / +0.43 | both halves | 3e-05 |  |
| [[GORAB]] | +0.62 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC4]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[HSPA8]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TPI1]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SFXN5]] | -0.53 | -0.37 / -0.60 | both halves | 7e-05 |  |
| [[CKS2]] | -0.53 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[TXN]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.51 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[AHSA1]] | -0.51 | -0.62 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF571]] | B | ZNF571 activity raises TYW5's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 1.23× lower at baseline in the lines without ZNF571 | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[CCDC113]] | C | CCDC113 activity raises TYW5's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.36× lower at baseline in the lines without CCDC113 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.4, 5.1); signed map (5.7, -23.9). **Vector** length 107, 26.9% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +35.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +19.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +17.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | +0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -4.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | tRNA-yW synthesizing protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:199,928,913-199,955,736 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37953; previously C2orf60 |
| Gene groups (HGNC) | JmjC hydroxylases |
| Reactome | 4 pathways, smallest: Synthesis of wybutosine at G37 of tRNA(Phe); tRNA modification in the nucleus and cytosol; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RUC4](https://www.uniprot.org/uniprotkb/A2RUC4) (tRNA wybutosine-synthesizing protein 5):

> tRNA hydroxylase that acts as a component of the wybutosine biosynthesis pathway. Wybutosine is a hyper modified guanosine with a tricyclic base found at the 3'-position adjacent to the anticodon of eukaryotic phenylalanine tRNA. Catalyzes the hydroxylation of 7-(a-amino-a-carboxypropyl)wyosine (yW-72) into undermodified hydroxywybutosine (OHyW*). OHyW* being further transformed into hydroxywybutosine (OHyW) by LCMT2/TYW4. OHyW is a derivative of wybutosine found in higher eukaryotes.

**Summary**, from NCBI Gene [129450](https://www.ncbi.nlm.nih.gov/gene/129450):

> Enables several functions, including iron ion binding activity; protein homodimerization activity; and tRNA(Phe) (7-(3-amino-3-carboxypropyl)wyosine37-C2)-hydroxylase activity. Involved in wybutosine biosynthetic process. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26754) · Entrez [129450](https://www.ncbi.nlm.nih.gov/gene/129450) · UniProt [A2RUC4](https://www.uniprot.org/uniprotkb/A2RUC4) · Ensembl [ENSG00000162971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162971)

## Data

Gene col 8607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8607); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8607]; `tensor/DDL_lfc|DDL_z.npy` [8607]; `embed/gene_vectors.npy` [8607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8607 or target_col == 8607). Every well: [[TYW5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYW5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
