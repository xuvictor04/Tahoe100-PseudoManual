---
symbol: "TJAP1"
type: "gene"
col: 5989
ensembl_id: "ENSG00000137221"
name: "tight junction associated protein 1"
location: "6p21.1"
module: 170
arm: "+"
pooled_cpm: 30.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# TJAP1

*tight junction associated protein 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +32.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.663× (z -8.6, q 5e-15, down in 20 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.254×, PANC-1 0.349×, HCT15 0.193×, NCI-H460 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Panc 03.27 0.145×, NCI-H23 0.187×, hTERT-HPNE 0.131×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CFPAC-1 0.242×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.241×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.75, fdr 7e-06), [[MED18]] (+0.73, fdr 7e-06), [[NFKBIL1]] (+0.72, fdr 7e-06); moves opposite to [[HACD3]] (-0.69, fdr 7e-06), [[TMEM97]] (-0.63, fdr 1e-05), [[GMPS]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOMER3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +32.2 | 0e+00 | 48/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.34×** | +17.7 | 0e+00 | 47/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.12×** | +12.9 | 8e-36 | 41/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.7 | 1e-29 | 41/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +9.9 | 8e-21 | 39/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +8.2 | 3e-14 | 35/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +7.3 | 3e-11 | 32/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.8 | 9e-10 | 25/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +5.7 | 7e-07 | 21/48 (HS-578T, A498, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +5.5 | 2e-06 | 22/48 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.19× | +5.4 | 3e-06 | 22/48 (Panc 03.27, SW1417, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.2 | 1e-05 | 22/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.0 | 2e-05 | 23/48 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +4.8 | 6e-05 | 17/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.23×** | +4.4 | 4e-04 | 15/48 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.004 | 10/48 (NCI-H2347, LOX-IMVI, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.007 | 10/48 (NCI-H23, NCI-H460, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.7 | 0.007 | 9/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.017 | 17/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.017 | 8/48 (A-427, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5989.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.254×, PANC-1 0.349×, HCT15 0.193×, NCI-H460 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Panc 03.27 0.145×, NCI-H23 0.187×, hTERT-HPNE 0.131×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CFPAC-1 0.242×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.241×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -8.6 | 5e-15 | 20/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.769×** | -5.7 | 3e-06 | 26/44 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.780×** | -5.0 | 1e-04 | 20/42 (CFPAC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.797×** | -4.9 | 1e-04 | 15/48 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | 0.849× | -3.4 | 0.070 | 20/47 (NCI-H1792, H4, …) | top dose only |  |
| [[Lucanthone (drug)]] 5 µM |  | 0.853× | -3.3 | 0.080 | 8/48 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **0.812×** | -3.2 | 0.096 | 14/47 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.907× | -3.0 | 0.19 | 6/48 (SW48, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 30.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +19.0) | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +22.3) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -12.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 30.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +16.8) | — |
| [[BT-474 (line)]] | alt | 25.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +13.3) | [[Canagliflozin (drug)]] 0.05 µM 0.241× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 30.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +18.7) | — |
| [[HS-578T (line)]] | alt | 32.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +18.7) | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +14.9) | — |
| [[AsPC-1 (line)]] | alt | 24.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 30.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -11.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 38.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[NCI-H23 (line)]] | alt | 48.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -17.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 45.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -17.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 48.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +19.9) | — |
| [[A-427 (line)]] | wt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.6) | — |
| [[H4 (line)]] | wt | 40.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.6) | — |
| [[J82 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +15.3) | — |
| [[KATO III (line)]] | alt | 34.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +17.2) | — |
| [[LS 180 (line)]] | wt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +15.4) | — |
| [[NCI-H2347 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.1) | — |
| [[RKO (line)]] | wt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 33.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[SW48 (line)]] | wt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.75 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[MED18]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[YJU2B]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GORAB]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[HELQ]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.66 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[ZNF140]] | +0.66 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ZNF264]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PI4KB]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD3]] | -0.69 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[TMEM97]] | -0.63 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[GMPS]] | -0.61 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[LDHB]] | -0.60 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ELOVL5]] | -0.60 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[STT3B]] | -0.60 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.59 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[LBR]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[DPY19L1]] | -0.59 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[METAP1]] | -0.58 | -0.72 / -0.37 | both halves | 9e-05 |  |
| [[ADAM15]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOMER3]] | C | HOMER3 activity raises TJAP1's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.35× lower at baseline in the lines without HOMER3 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.860). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-38.1, 3.9); signed map (0.2, -15.1). **Vector** length 87.2, 18.4% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +32.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +17.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +11.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | -4.7 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +0.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | tight junction associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,477,523-43,506,556 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PILT; previously TJP4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTD0](https://www.uniprot.org/uniprotkb/Q5JTD0) (Tight junction-associated protein 1):

> Plays a role in regulating the structure of the Golgi apparatus.

**Summary**, from NCBI Gene [93643](https://www.ncbi.nlm.nih.gov/gene/93643):

> This gene encodes a tight junction-associated protein. Incorporation of the encoded protein into tight junctions occurs at a late stage of formation of the junctions. The encoded protein localizes to the Golgi and may function in vesicle trafficking. Alternatively spliced transcript variants have been described. A related pseudogene exists on the X chromosome. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:17949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17949) · Entrez [93643](https://www.ncbi.nlm.nih.gov/gene/93643) · UniProt [Q5JTD0](https://www.uniprot.org/uniprotkb/Q5JTD0) · Ensembl [ENSG00000137221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137221)

## Data

Gene col 5989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5989); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5989]; `tensor/DDL_lfc|DDL_z.npy` [5989]; `embed/gene_vectors.npy` [5989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5989 or target_col == 5989). Every well: [[TJAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TJAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
