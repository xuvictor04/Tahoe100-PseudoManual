---
symbol: "SNX2"
type: "gene"
col: 12965
ensembl_id: "ENSG00000205302"
name: "sorting nexin 2"
location: "5q23.2"
module: 45
arm: "+"
pooled_cpm: 74.67
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SNX2

*sorting nexin 2* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +17.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.708× (z -5.6, q 1e-05, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.774× (z -4.5, q 0.002, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KBTBD3]] (+0.74, fdr 7e-06), [[RRAGD]] (+0.70, fdr 7e-06), [[WDSUB1]] (+0.70, fdr 7e-06); moves opposite to [[GATAD2A]] (-0.70, fdr 7e-06), [[HNRNPAB]] (-0.67, fdr 7e-06), [[TIMM23B-AGAP6]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DNAJC12]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PREPL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +17.0 | 0e+00 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +10.1 | 2e-21 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +9.5 | 3e-19 | 44/49 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +9.4 | 9e-19 | 41/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +9.1 | 7e-18 | 43/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +9.1 | 7e-18 | 43/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +8.0 | 9e-14 | 38/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.9 | 2e-13 | 40/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +7.8 | 5e-13 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.0 | 2e-10 | 31/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +6.7 | 1e-09 | 39/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +6.7 | 1e-09 | 40/48 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +6.1 | 4e-08 | 38/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +5.9 | 1e-07 | 34/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +5.4 | 3e-06 | 40/49 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.78×** | +5.3 | 5e-06 | 37/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.708×** | -5.6 | 1e-05 | 30/45 (SW 900, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.0 | 2e-04 | 24/43 (Panc 03.27, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -4.5 | 0.002 | 25/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.844× | -4.2 | 0.004 | 21/49 (Hs 766T, Panc 03.27, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.799×** | -3.9 | 0.011 | 23/47 (SW48, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.027 | 19/48 (SW480, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.814×** | -3.6 | 0.027 | 24/49 (H4, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -3.6 | 0.027 | 13/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.047 | 18/47 (SNU-423, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.828×** | -3.3 | 0.053 | 16/49 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.828×** | -3.3 | 0.053 | 21/48 (NCI-H1792, SW48, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.834× | -3.2 | 0.073 | 17/49 (A498, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.4 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +26.7) | — |
| [[NCI-H1573 (line)]] | alt | 54.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +18.7) | — |
| [[PANC-1 (line)]] | alt | 68.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +16.6) | — |
| [[HEC-1-A (line)]] | alt | 135 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 75.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +12.1) | — |
| [[LoVo (line)]] | wt | 77.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 98.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 69.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 48.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 84.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.3) | — |
| [[A-172 (line)]] | wt | 77.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 35.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +8.7) | — |
| [[H4 (line)]] | wt | 87.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 89.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[KATO III (line)]] | alt | 67.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 96.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.0) | — |
| [[A549 (line)]] | wt | 78.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.2) | — |
| [[C-33 A (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 95.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.274× (z -11.7) |
| [[HOP62 (line)]] | alt | 53.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 74.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.9) | — |
| [[J82 (line)]] | alt | 49.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 66.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.85× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.2) | — |
| [[RKO (line)]] | wt | 65.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 82.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 84.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 99.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.453× (z -10.0) |
| [[SW 900 (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 79.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[SW480 (line)]] | alt | 68.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.2) | — |
| [[A498 (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 145 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[RRAGD]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[WDSUB1]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ZNF14]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TP53TG1]] | +0.68 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[PREPL]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ORC4]] | +0.66 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[ZNF292]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ABCA5]] | +0.64 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[METTL14]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[DBP]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.70 | -0.71 / -0.67 | both halves | 7e-06 |  |
| [[HNRNPAB]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | -0.64 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[LRP8]] | -0.64 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | -0.64 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[TTL]] | -0.64 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.61 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[GHRLOS]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.60 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[DDX5]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ANKMY1]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[HCG18]] | -0.60 | -0.49 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC12]] | B | DNAJC12 activity lowers SNX2's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without DNAJC12 | 0.073 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[FAM229B]] | B | FAM229B activity raises SNX2's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without FAM229B | 0.090 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[LCA5]] | C | LCA5 activity raises SNX2's level | lines that do not express LCA5 (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without LCA5 | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: NXPE3, E2F7, IFT74; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PREPL]] | C | SNX2's natural level weakens PREPL's drug response | SNX2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.13; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.3, -9.7); signed map (-25.1, -8.2). **Vector** length 135, 46.3% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.1 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +9.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.9 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.8 | +4.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.2 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -6.1 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:122,775,079-122,834,543 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O60749](https://www.uniprot.org/uniprotkb/O60749) (Sorting nexin-2):

> Involved in several stages of intracellular trafficking. Interacts with membranes containing phosphatidylinositol 3-phosphate (PtdIns(3P)) or phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2). Acts in part as component of the retromer membrane-deforming SNX-BAR subcomplex. The SNX-BAR retromer mediates retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN) and is involved in endosome-to-plasma membrane transport for cargo protein recycling. The SNX-BAR …

**Summary**, from NCBI Gene [6643](https://www.ncbi.nlm.nih.gov/gene/6643):

> This gene belongs to the sorting nexin family whose members contain the phosphoinositide-binding phox (PX) domain. The encoded protein is a component of the retromer complex which plays a role in protein sorting in the endocytic pathway. This protein may form oligomeric complexes with other family members. Alternate splicing results in multiple transcript variants of this gene. Pseudogenes associated with this gene are located on chromosomes 1 and 7. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:11173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11173) · Entrez [6643](https://www.ncbi.nlm.nih.gov/gene/6643) · UniProt [O60749](https://www.uniprot.org/uniprotkb/O60749) · Ensembl [ENSG00000205302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205302)

## Data

Gene col 12965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12965); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12965]; `tensor/DDL_lfc|DDL_z.npy` [12965]; `embed/gene_vectors.npy` [12965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12965 or target_col == 12965). Every well: [[SNX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
