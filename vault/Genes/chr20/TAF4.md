---
symbol: "TAF4"
type: "gene"
col: 5098
ensembl_id: "ENSG00000130699"
name: "TATA-box binding protein associated factor 4"
location: "20q13.33"
module: 3
arm: "+"
pooled_cpm: 57.35
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TAF4

*TATA-box binding protein associated factor 4* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.13× (z +13.6, q 2e-39, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.462× (z -13.9, q 5e-41, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 0.5 µM: 0.823× (z -3.5, q 0.040, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-427 0.123×, NCI-H460 0.146×, HEC-1-A 0.194×, HCT15 0.128×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.0809×, RKO 0.192×, C-33 A 0.200×, LOX-IMVI 0.231×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 0.138×, RKO 0.164×, SW480 0.362×, C-33 A 0.236×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR2C2]] (+0.69, fdr 7e-06), [[FOXK2]] (+0.65, fdr 7e-06), [[DCUN1D2]] (+0.63, fdr 7e-06); moves opposite to [[NDUFA5]] (-0.62, fdr 1e-05), [[GORAB]] (-0.60, fdr 3e-05), [[DDX1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.13×** | +13.6 | 2e-39 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +10.4 | 5e-23 | 46/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +9.1 | 1e-17 | 35/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +8.9 | 7e-17 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +7.2 | 9e-11 | 34/48 (Hs 766T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.6 | 3e-09 | 29/49 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.5 | 5e-09 | 31/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-06 | 31/48 (Hs 766T, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +5.2 | 1e-05 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +4.8 | 1e-04 | 26/48 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.7 | 2e-04 | 25/47 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.5 | 3e-04 | 25/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 8e-04 | 20/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.005 | 19/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.005 | 22/48 (COLO 205, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.010 | 22/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.010 | 15/48 (SW480, SK-MEL-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.064 | 10/49 (CFPAC-1, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5098.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-427 0.123×, NCI-H460 0.146×, HEC-1-A 0.194×, HCT15 0.128×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.0809×, RKO 0.192×, C-33 A 0.200×, LOX-IMVI 0.231×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 0.138×, RKO 0.164×, SW480 0.362×, C-33 A 0.236×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.462×** | -13.9 | 5e-41 | 41/49 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -12.2 | 7e-32 | 36/43 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.742×** | -5.0 | 1e-04 | 27/45 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.3 | 0.003 | 16/48 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.804×** | -3.9 | 0.010 | 23/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.823×** | -3.5 | 0.040 | 16/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.844× | -3.1 | 0.18 | 15/48 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.846× | -3.0 | 0.18 | 10/47 (LS 180, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.3 | 7 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.94× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -21.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 69.5 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 102 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -14.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 48.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 42.5 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.54× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 143 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 61.2 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.56× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 72.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -21.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 91.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 54.3 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 82.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -14.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 63.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -17.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0809× (z -21.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 79.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -12.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 83.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.53× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 34.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 61.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -9.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.102× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 54.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -16.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 49.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -19.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.422× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2C2]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.65 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[DCUN1D2]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CASTOR3P]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ANKS1A]] | +0.62 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[UBE2G1]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GIT1]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[AGAP3]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.60 | +0.69 / +0.47 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[TSPAN17]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[NRF1]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PRDM15]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.62 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[GORAB]] | -0.60 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[DDX1]] | -0.59 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[DZIP3]] | -0.57 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[SLC25A46]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[CLCN3]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[FCF1]] | -0.55 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[DBT]] | -0.55 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CHURC1]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[AIMP1]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[LYRM2]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity lowers TAF4's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.298). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.7, -4.2); signed map (-42.5, 0.7). **Vector** length 95.7, 25.2% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +3.7 | +10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.6 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +13.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -8.3 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.1 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -0.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.9 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -4.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:61,953,469-62,065,881 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII130, TAFII135; previously TAF4A, TAF2C1, TAF2C |
| Gene groups (HGNC) | General transcription factor IID complex subunits |
| Reactome | 19 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [O00268](https://www.uniprot.org/uniprotkb/O00268) (Transcription initiation factor TFIID subunit 4):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF4 may maintain an …

**Summary**, from NCBI Gene [6874](https://www.ncbi.nlm.nih.gov/gene/6874):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11537) · Entrez [6874](https://www.ncbi.nlm.nih.gov/gene/6874) · UniProt [O00268](https://www.uniprot.org/uniprotkb/O00268) · Ensembl [ENSG00000130699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130699)

## Data

Gene col 5098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5098); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5098]; `tensor/DDL_lfc|DDL_z.npy` [5098]; `embed/gene_vectors.npy` [5098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5098 or target_col == 5098). Every well: [[TAF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
