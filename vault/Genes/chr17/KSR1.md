---
symbol: "KSR1"
type: "gene"
col: 6486
ensembl_id: "ENSG00000141068"
name: "kinase suppressor of ras 1"
location: "17q11.2"
module: 115
arm: "+"
pooled_cpm: 38.82
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# KSR1

*kinase suppressor of ras 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.85× (z +13.6, q 4e-39, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.514× (z -10.3, q 2e-22, down in 30 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.723× (z -5.0, q 6e-05, down in 25 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0641×, SW1417 0.134×, A-427 0.191×, CFPAC-1 0.132×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.0722×, A549 0.199×, NCI-H460 0.262×, C32 0.143×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.248×, A498 0.260×, A-172 0.253×, NCI-H1792 0.186×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SNU-1 0.139×, SW 900 0.193×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.362×); [[Thymol (drug)]] 0.5 µM in 1 line (SW48 0.201×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC69]] (+0.51, fdr 7e-05), [[HES2]] (+0.51, fdr 9e-05), [[CASZ1]] (+0.50, fdr 4e-05); moves opposite to [[XPNPEP3]] (-0.51, fdr 3e-05), [[MKRN3]] (-0.45, fdr 2e-04), [[MAP3K7]] (-0.44, fdr 3e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF423]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +13.6 | 4e-39 | 39/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +12.7 | 3e-34 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +10.8 | 6e-25 | 37/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +10.5 | 1e-23 | 38/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +9.3 | 2e-18 | 34/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +8.2 | 3e-14 | 32/46 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.7 | 1e-12 | 27/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +7.2 | 6e-11 | 25/47 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.38×** | +6.9 | 2e-10 | 37/47 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.42×** | +5.4 | 3e-06 | 25/47 (RKO, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 9e-06 | 21/46 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.36×** | +4.8 | 9e-05 | 21/46 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +4.7 | 1e-04 | 23/47 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.68×** | +4.2 | 0.001 | 13/41 (A498, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 17/46 (NCI-H460, SW48, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.038 | 12/47 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6486.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0641×, SW1417 0.134×, A-427 0.191×, CFPAC-1 0.132×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.0722×, A549 0.199×, NCI-H460 0.262×, C32 0.143×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.248×, A498 0.260×, A-172 0.253×, NCI-H1792 0.186×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SNU-1 0.139×, SW 900 0.193×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.362×); [[Thymol (drug)]] 0.5 µM in 1 line (SW48 0.201×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.514×** | -10.3 | 2e-22 | 30/43 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -10.3 | 2e-22 | 25/38 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.536×** | -8.7 | 8e-16 | 23/42 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -5.0 | 6e-05 | 25/46 (SNU-1, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.777×** | -3.9 | 0.010 | 23/46 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.783×** | -3.8 | 0.014 | 19/46 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.796×** | -3.5 | 0.032 | 18/46 (COLO 205, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~91% of this change | **0.814×** | -3.2 | 0.099 | 16/45 (NCI-H661, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 22.4 | 5 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.19× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 27.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 33.3 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 19.4 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 51.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +17.6) | — |
| [[NCI-H1792 (line)]] | alt | 227 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -8.9) |
| [[SW1417 (line)]] | alt | 34.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 32.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 48.6 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.269× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 18.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 38.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0641× (z -20.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 34.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 65.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 40.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.30× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 46.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.0722× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.8) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 5 µM 0.262× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 65.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.27× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 91.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 150 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.193× (z -8.7) |
| [[A-427 (line)]] | wt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -12.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Raltitrexed (drug)]] 5 µM 2.17× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 61.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0768× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~91% of this change |
| [[RKO (line)]] | wt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 35.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.63× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.139× (z -10.0) |
| [[SW48 (line)]] | wt | 33.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.201× (z -8.6) |
| [[AN3 CA (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC69]] | +0.51 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[HES2]] | +0.51 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[CASZ1]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PTPRU]] | +0.50 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[RHOV]] | +0.49 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[PTGES]] | +0.49 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[RNF19B]] | +0.48 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[ARL4D]] | +0.48 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[ARHGAP44]] | +0.48 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[C3]] | +0.47 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[SIPA1L2]] | +0.46 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[GLIPR2]] | +0.46 | +0.23 / +0.61 | both halves | 5e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPNPEP3]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MKRN3]] | -0.45 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[MAP3K7]] | -0.44 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[MIPEP]] | -0.43 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[SLC35F5]] | -0.42 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[LINC00159]] | -0.41 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[DNAAF10]] | -0.41 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[ZNG1E]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[SLC30A9]] | -0.41 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[VPS45]] | -0.40 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[RAD18]] | -0.40 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[POLR1HASP]] | -0.39 | -0.26 / -0.43 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF423]] | B | ZNF423 activity lowers KSR1's level | lines that do not express ZNF423 (5) vs lines expressing it (45) | 1.76× higher at baseline in the lines without ZNF423 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLIT1; maybe low, not absent; its own permutation p |
| [[GLIPR2]] | B | GLIPR2 activity raises KSR1's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 1.61× lower at baseline in the lines without GLIPR2 | 0.065 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[PPP1R14C]] | B | PPP1R14C activity lowers KSR1's level | lines that do not express PPP1R14C (14) vs lines expressing it (36) | 1.15× higher at baseline in the lines without PPP1R14C | 0.089 | ⚠ within organs, on part of the lines; also absent: APLP1, CACNA1B, ENTREP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.5, 41.1); signed map (22.3, 22.4). **Vector** length 91.4, 22.3% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.5 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.4 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +0.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.2 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.7 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.7 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | +7.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | +0.2 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | kinase suppressor of ras 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:27,456,448-27,626,438 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RSU2; previously KSR |
| Gene groups (HGNC) | RAF family; Pseudokinases |
| Reactome | 15 pathways, smallest: RAF activation; Signaling by high-kinase activity BRAF mutants; MAP2K and MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVT5](https://www.uniprot.org/uniprotkb/Q8IVT5) (Kinase suppressor of Ras 1):

> Part of a multiprotein signaling complex which promotes phosphorylation of Raf family members and activation of downstream MAP kinases (By similarity). Independently of its kinase activity, acts as MAP2K1/MEK1 and MAP2K2/MEK2-dependent allosteric activator of BRAF; upon binding to MAP2K1/MEK1 or MAP2K2/MEK2, dimerizes with BRAF and promotes BRAF-mediated phosphorylation of MAP2K1/MEK1 and/or MAP2K2/MEK2. Promotes activation of MAPK1 and/or MAPK3, both in response to EGF and to cAMP (By …

**Summary**, from NCBI Gene [8844](https://www.ncbi.nlm.nih.gov/gene/8844):

> Enables 14-3-3 protein binding activity and ATP binding activity. Involved in positive regulation of MAPK cascade. Located in cytosol; endoplasmic reticulum; and membrane. Part of protein-containing complex. Implicated in breast adenocarcinoma. Biomarker of breast cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6465) · Entrez [8844](https://www.ncbi.nlm.nih.gov/gene/8844) · UniProt [Q8IVT5](https://www.uniprot.org/uniprotkb/Q8IVT5) · Ensembl [ENSG00000141068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141068)

## Data

Gene col 6486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6486); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6486]; `tensor/DDL_lfc|DDL_z.npy` [6486]; `embed/gene_vectors.npy` [6486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6486 or target_col == 6486). Every well: [[KSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
