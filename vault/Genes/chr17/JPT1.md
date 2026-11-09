---
symbol: "JPT1"
type: "gene"
col: 12097
ensembl_id: "ENSG00000189159"
name: "Jupiter microtubule associated homolog 1"
location: "17q25.1"
module: 3
arm: "+"
pooled_cpm: 97.83
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# JPT1

*Jupiter microtubule associated homolog 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.47× (z +15.4, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 4.14× (z +14.6, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIK]] (+0.64, fdr 1e-05), [[CDKN2D]] (+0.64, fdr 2e-05), [[LGALS1]] (+0.61, fdr 3e-05); moves opposite to [[MAPKAPK5]] (-0.65, fdr 2e-05), [[PEX26]] (-0.59, fdr 3e-05), [[MRRF]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **4.47×** | +15.4 | 0e+00 | 48/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.14×** | +14.6 | 0e+00 | 48/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.79×** | +13.7 | 1e-40 | 48/48 (SW480, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **2.03×** | +10.3 | 6e-23 | 41/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.7 | 4e-16 | 44/49 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.11×** | +7.7 | 1e-12 | 47/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.10×** | +7.7 | 1e-12 | 44/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +6.5 | 7e-09 | 43/48 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.86×** | +6.2 | 4e-08 | 40/48 (COLO 205, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.76×** | +5.9 | 3e-07 | 41/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.63×** | +5.0 | 3e-05 | 39/48 (A-427, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.62×** | +5.0 | 3e-05 | 31/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.1 | 0.002 | 30/47 (NCI-H2030, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.52×** | +3.9 | 0.004 | 31/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.013 | 29/49 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.078 | 23/48 (hTERT-HPNE, HOP62, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 47.0 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.48× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 65.5 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +15.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.96× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 111 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.60× (z +16.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.23× (z +16.3) | — |
| [[A-172 (line)]] | wt | 129 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.07× (z +14.3) | — |
| [[KATO III (line)]] | alt | 151 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.35× (z +13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.33× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 133 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.33× (z +10.8) | — |
| [[SW480 (line)]] | alt | 124 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +16.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.63× (z +14.6) | — |
| [[A498 (line)]] | wt | 80.9 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.15× (z +12.2) | — |
| [[A549 (line)]] | wt | 88.9 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.18× (z +13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.91× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 68.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +15.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.91× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 47.0 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.9× (z +13.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 10.7× (z +13.2) | — |
| [[LoVo (line)]] | wt | 65.4 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.70× (z +12.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.90× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 85.5 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.68× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.49× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 83.4 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.15× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 97.7 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.87× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 47.9 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.48× (z +14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 7.28× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 77.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +12.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.65× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 76.4 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.50× (z +14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.31× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.41× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 49.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.41× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 77.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 154 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.62× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.10× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 73.8 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.70× (z +15.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 7.55× (z +15.4) | — |
| [[A-427 (line)]] | wt | 115 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.13× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 100 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.24× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[CFPAC-1 (line)]] | alt | 131 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.57× (z +8.7) | — |
| [[H4 (line)]] | wt | 93.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 107 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.38× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 79.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 43.6 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.43× (z +12.1) | — |
| [[J82 (line)]] | alt | 111 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.46× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 202 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +12.1) | — |
| [[RKO (line)]] | wt | 72.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.95× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 78.8 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +11.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.57× (z +10.9) | — |
| [[C-33 A (line)]] | alt | 129 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[C32 (line)]] | wt | 70.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.5) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[CHP-212 (line)]] | wt | 202 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HCT15 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW48 (line)]] | wt | 82.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.07× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIK]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.64 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LGALS1]] | +0.61 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CDCA2]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[PTTG1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[MYO1E]] | +0.60 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TXNDC17]] | +0.59 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[CARHSP1]] | +0.59 | +0.21 / +0.60 | both halves | 7e-04 |  |
| [[ABCB9]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TUBB4B]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC25A4]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.65 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[PEX26]] | -0.59 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[MRRF]] | -0.57 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[C8orf44-SGK3]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[VPS33A]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[UNC50]] | -0.54 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[EIF3F]] | -0.54 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PSME3IP1]] | -0.54 | -0.21 / -0.52 | both halves | 6e-04 |  |
| [[NAA50]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ZMPSTE24]] | -0.53 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[DVL3]] | -0.53 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[SSU72]] | -0.53 | -0.29 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.9, 28.2); signed map (0.9, 25.3). **Vector** length 97.7, 38.3% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +7.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.9 | +13.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.9 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.5 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | Jupiter microtubule associated homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,135,248-75,168,281 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARM2, HN1A; previously HN1 |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK76](https://www.uniprot.org/uniprotkb/Q9UK76) (Jupiter microtubule associated homolog 1):

> Modulates negatively AKT-mediated GSK3B signaling. Induces CTNNB1 'Ser-33' phosphorylation and degradation through the suppression of the inhibitory 'Ser-9' phosphorylation of GSK3B, which represses the function of the APC:CTNNB1:GSK3B complex and the interaction with CDH1/E-cadherin in adherent junctions. Plays a role in the regulation of cell cycle and cell adhesion. Has an inhibitory role on AR-signaling pathway through the induction of receptor proteasomal degradation.

**Summary**, from NCBI Gene [51155](https://www.ncbi.nlm.nih.gov/gene/51155):

> Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14569) · Entrez [51155](https://www.ncbi.nlm.nih.gov/gene/51155) · UniProt [Q9UK76](https://www.uniprot.org/uniprotkb/Q9UK76) · Ensembl [ENSG00000189159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189159)

## Data

Gene col 12097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12097); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12097]; `tensor/DDL_lfc|DDL_z.npy` [12097]; `embed/gene_vectors.npy` [12097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12097 or target_col == 12097). Every well: [[JPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
