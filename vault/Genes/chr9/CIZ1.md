---
symbol: "CIZ1"
type: "gene"
col: 7267
ensembl_id: "ENSG00000148337"
name: "CDKN1A interacting zinc finger protein 1"
location: "9q34.11"
module: 171
arm: "+"
pooled_cpm: 48.54
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# CIZ1

*CDKN1A interacting zinc finger protein 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +19.7, q 0e+00, up in 36 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.25× (z +4.5, q 0.001, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW480 4.96×, SHP-77 10.2×, HOP62 4.70×, J82 5.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SHP-77 8.08×, SW480 3.61×, J82 5.15×, LoVo 4.89×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 4.27×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.685× (z -10.1, q 5e-21, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VTI1B]] (+0.69, fdr 7e-06), [[DCTN1]] (+0.66, fdr 7e-06), [[ADD1]] (+0.64, fdr 7e-06); moves opposite to [[METTL23]] (-0.62, fdr 7e-06), [[TUBB4B]] (-0.61, fdr 2e-05), [[PFN1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TRIM15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7267.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW480 4.96×, SHP-77 10.2×, HOP62 4.70×, J82 5.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SHP-77 8.08×, SW480 3.61×, J82 5.15×, LoVo 4.89×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 4.27×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +19.7 | 0e+00 | 36/38 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +18.6 | 0e+00 | 45/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +12.7 | 1e-34 | 42/45 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.5 | 0.001 | 22/48 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.031 | 15/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.035 | 9/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.15 | 20/47 (SHP-77, NCI-H2030, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.17× | +3.1 | 0.15 | 15/48 (SW480, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.685×** | -10.1 | 5e-21 | 35/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -5.8 | 2e-06 | 32/48 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -5.2 | 4e-05 | 25/48 (HS-578T, A-172, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.762×** | -5.1 | 4e-05 | 25/48 (A498, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.804×** | -4.3 | 0.002 | 23/48 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.809×** | -4.1 | 0.003 | 23/48 (NCI-H460, SNU-423, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.804×** | -3.8 | 0.010 | 19/48 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.823×** | -3.8 | 0.011 | 20/47 (HEC-1-A, SW 900, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.828×** | -3.7 | 0.015 | 20/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.839× | -3.4 | 0.037 | 19/48 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.884× | -3.3 | 0.043 | 13/48 (A-427, HS-578T, …) | top dose only |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.840× | -3.3 | 0.048 | 13/47 (NCI-H1792, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.846× | -3.3 | 0.048 | 21/48 (NCI-H1573, C32, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.841× | -3.0 | 0.098 | 8/48 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 68.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.6) |
| [[A549 (line)]] | wt | 49.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +11.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 47.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.70× (z +17.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 72.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +17.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 42.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.11× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 45.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 46.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.2× (z +19.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 32.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.02× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 47.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +21.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 33.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.40× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.9) |
| [[A498 (line)]] | wt | 66.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +12.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +12.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 37.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.45× (z +15.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 54.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 48.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -13.8) |
| [[PANC-1 (line)]] | alt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 51.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +10.2) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 0.5 µM 0.101× (z -11.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 66.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +9.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 78.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +10.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -8.5) |
| [[HCT15 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 73.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 58.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 43.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.8) |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VTI1B]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ADD1]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CTC1]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[NAPB]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[RPL10]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[EIF3C]] | +0.62 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[RWDD4]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[TMEM183A]] | +0.61 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[EIF2D]] | +0.60 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[THOC5]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ATPAF1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL23]] | -0.62 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[TUBB4B]] | -0.61 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[PFN1]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[KCTD11]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[HES1]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[GASAL1]] | -0.56 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[FOXA2]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[C14orf119]] | -0.56 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[MIDN]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ISG20L2]] | -0.55 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.55 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[POLR2L]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM15]] | B | TRIM15 activity lowers CIZ1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.20× higher at baseline in the lines without TRIM15 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[PRKCA]] | B | PRKCA activity lowers CIZ1's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 1.26× higher at baseline in the lines without PRKCA | 0.074 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CIZ1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CIZ1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-10.2, -13.7); signed map (-35.3, -22.1). **Vector** length 107, 26.2% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +19.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +12.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.6 | +0.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.1 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Thymol (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | CDKN1A interacting zinc finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,161,251-128,204,383 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LSFR1, ZNF356 |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULV3](https://www.uniprot.org/uniprotkb/Q9ULV3) (Cip1-interacting zinc finger protein):

> May regulate the subcellular localization of CIP/WAF1.

**Summary**, from NCBI Gene [25792](https://www.ncbi.nlm.nih.gov/gene/25792):

> The protein encoded by this gene is a zinc finger DNA binding protein that interacts with CIP1, part of a complex with cyclin E. The encoded protein may regulate the cellular localization of CIP1. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:16744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16744) · Entrez [25792](https://www.ncbi.nlm.nih.gov/gene/25792) · UniProt [Q9ULV3](https://www.uniprot.org/uniprotkb/Q9ULV3) · Ensembl [ENSG00000148337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148337)

## Data

Gene col 7267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7267); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7267]; `tensor/DDL_lfc|DDL_z.npy` [7267]; `embed/gene_vectors.npy` [7267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7267 or target_col == 7267). Every well: [[CIZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
