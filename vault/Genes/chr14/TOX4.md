---
symbol: "TOX4"
type: "gene"
col: 1695
ensembl_id: "ENSG00000092203"
name: "TOX high mobility group box family member 4"
location: "14q11.2"
module: 18
arm: "-"
pooled_cpm: 58.71
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TOX4

*TOX high mobility group box family member 4* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +14.9, q 0e+00, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.770× (z -6.8, q 6e-09, down in 28 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.859× (z -5.6, q 4e-06, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 4 lines (HOP62 0.0816×, Panc 03.27 0.197×, BT-474 0.166×, hTERT-HPNE 0.111×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.121×, CFPAC-1 0.459×, RPMI-7951 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.103×, NCI-H1573 0.321×, SW 900 0.343×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM5A]] (+0.64, fdr 7e-06), [[GOLGB1]] (+0.62, fdr 7e-06), [[NKIRAS2]] (+0.61, fdr 1e-05); moves opposite to [[UCK2]] (-0.67, fdr 7e-06), [[TMTC4]] (-0.64, fdr 1e-05), [[PALS2]] (-0.59, fdr 7e-06).
> It sits in the **-** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +14.9 | 0e+00 | 43/49 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +14.8 | 0e+00 | 41/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +13.4 | 2e-38 | 39/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +12.0 | 3e-31 | 40/48 (HEC-1-A, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +11.4 | 3e-28 | 38/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +11.1 | 8e-27 | 36/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +10.8 | 2e-25 | 39/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +10.3 | 4e-23 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +10.2 | 1e-22 | 35/48 (LoVo, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +9.3 | 1e-18 | 32/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +8.6 | 6e-16 | 36/48 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +8.4 | 2e-15 | 30/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.6 | 2e-12 | 31/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +6.3 | 1e-08 | 25/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 6e-08 | 28/48 (SW480, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1695.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 4 lines (HOP62 0.0816×, Panc 03.27 0.197×, BT-474 0.166×, hTERT-HPNE 0.111×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.121×, CFPAC-1 0.459×, RPMI-7951 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.103×, NCI-H1573 0.321×, SW 900 0.343×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -6.8 | 6e-09 | 28/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.787×** | -6.0 | 6e-07 | 27/47 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -5.6 | 4e-06 | 18/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.804×** | -5.4 | 8e-06 | 21/42 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -4.6 | 4e-04 | 19/48 (NCI-H2347, CHP-212, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains <1% of this change | 0.838× | -4.4 | 8e-04 | 19/47 (RPMI-7951, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.844× | -4.4 | 8e-04 | 18/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -4.3 | 0.001 | 19/48 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.754×** | -3.8 | 0.008 | 17/38 (HOP62, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.867× | -3.7 | 0.012 | 12/48 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 0.877× | -3.2 | 0.083 | 17/45 (RKO, H4, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.797×** | -3.1 | 0.095 | 14/48 (A549, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.798×** | -3.1 | 0.095 | 16/48 (SW48, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.884× | -3.0 | 0.095 | 8/47 (NCI-H2347, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 72.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.4 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 51.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.0) | [[Lonafarnib (drug)]] 5 µM 0.0816× (z -15.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 37.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -23.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 51.0 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 68.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.481× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 54.4 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +11.8) | — |
| [[A-427 (line)]] | wt | 46.7 | 2 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.78× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[BT-474 (line)]] | alt | 83.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.5) | [[Lonafarnib (drug)]] 5 µM 0.166× (z -10.4) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 39.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +10.0) | — |
| [[A549 (line)]] | wt | 60.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[MIA PaCa-2 (line)]] | alt | 63.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +11.5) | — |
| [[RKO (line)]] | wt | 56.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.62× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[RPMI-7951 (line)]] | alt | 75.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[A498 (line)]] | wt | 43.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 70.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 39.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +9.5) | — |
| [[H4 (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[HT-29 (line)]] | alt | 39.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.111× (z -10.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 56.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 70.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 83.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.197× (z -10.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 59.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5A]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GOLGB1]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[NKIRAS2]] | +0.61 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[SNIP1]] | +0.61 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[CCNK]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[YIPF3]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TMUB2]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[USP8]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[SUPT6H]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZNF791]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[KIN]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[SLU7]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCK2]] | -0.67 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[TMTC4]] | -0.64 | -0.74 / -0.49 | both halves | 1e-05 |  |
| [[PALS2]] | -0.59 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[PMS1]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[CAD]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MEMO1]] | -0.57 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[FXN]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[KLHL2]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GPR63]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TARBP1]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ASB13]] | -0.54 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.53 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **-** arm (projection on the module's main direction -0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-5.3, -47.6); signed map (-4.9, -6.8). **Vector** length 107, 28.2% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +14.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +13.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +6.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +4.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains <1% of this change | -6.7 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.3 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -4.8 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TOX high mobility group box family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,476,597-21,499,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LCP1; previously C14orf92, KIAA0737 |
| Gene groups (HGNC) | thymocyte selection associated high mobility group box family |
| Matched by | ensembl_id |

**Function**, from UniProt [O94842](https://www.uniprot.org/uniprotkb/O94842) (TOX high mobility group box family member 4):

> Transcription factor that modulates cell fate reprogramming from the somatic state to the pluripotent and neuronal fate (By similarity). In liver, controls the expression of hormone-regulated gluconeogenic genes such as G6PC1 and PCK1 (By similarity). This regulation is independent of the insulin receptor activation (By similarity). Also acts as a regulatory component of protein phosphatase 1 (PP1) complexes. Component of the PNUTS-PP1 protein phosphatase complex, a PP1 complex that regulates …

**Summary**, from NCBI Gene [9878](https://www.ncbi.nlm.nih.gov/gene/9878):

> Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and chromatin DNA binding activity. Involved in RNA polymerase II promoter clearance and positive regulation of transcription elongation by RNA polymerase II. Located in chromatin and chromosome, telomeric region. Part of PTW/PP1 phosphatase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20161) · Entrez [9878](https://www.ncbi.nlm.nih.gov/gene/9878) · UniProt [O94842](https://www.uniprot.org/uniprotkb/O94842) · Ensembl [ENSG00000092203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092203)

## Data

Gene col 1695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1695); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1695]; `tensor/DDL_lfc|DDL_z.npy` [1695]; `embed/gene_vectors.npy` [1695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1695 or target_col == 1695). Every well: [[TOX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
