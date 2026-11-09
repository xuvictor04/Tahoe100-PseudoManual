---
symbol: "GOLGA5"
type: "gene"
col: 829
ensembl_id: "ENSG00000066455"
name: "golgin A5"
location: "14q32.12"
module: 41
arm: "+"
pooled_cpm: 65.52
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# GOLGA5

*golgin A5* — 14q32.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.323× (z -21.2, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.364× (z -18.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF5]] (+0.78, fdr 7e-06), [[OSBP]] (+0.76, fdr 7e-06), [[ACBD3]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.4 | 0.44 | 0/49 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.323×** | -21.2 | 0e+00 | 46/48 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.364×** | -18.9 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.526×** | -17.0 | 0e+00 | 39/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.466×** | -14.3 | 2e-44 | 41/49 (HCT15, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.448×** | -13.9 | 5e-42 | 43/44 (LS 180, NCI-H1573, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.481×** | -13.8 | 5e-41 | 44/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.518×** | -12.3 | 4e-33 | 44/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.505×** | -12.3 | 5e-33 | 42/48 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.542×** | -11.0 | 1e-26 | 35/40 (HCT15, NCI-H1573, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.608×** | -9.3 | 6e-19 | 37/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.608×** | -9.0 | 1e-17 | 36/47 (H4, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.623×** | -8.9 | 3e-17 | 37/48 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -7.5 | 2e-12 | 36/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.685×** | -7.1 | 5e-11 | 34/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.700×** | -6.7 | 8e-10 | 35/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -6.1 | 4e-08 | 26/47 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.757×** | -5.2 | 6e-06 | 26/48 (J82, CFPAC-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -4.9 | 2e-05 | 23/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.761×** | -4.8 | 3e-05 | 21/47 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -4.4 | 2e-04 | 24/48 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -3.9 | 0.002 | 18/48 (HOP62, SW 1271, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.674×** | -3.9 | 0.002 | 23/48 (CFPAC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.016 | 16/48 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.717×** | -3.3 | 0.020 | 12/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.9 | 0 | 13 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -20.7) |
| [[H4 (line)]] | wt | 81.2 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0990× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 88.0 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 84.8 | 0 | 10 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -16.6) |
| [[SW 900 (line)]] | alt | 81.2 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.252× (z -13.5) |
| [[HOP62 (line)]] | alt | 66.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -18.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 93.5 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -20.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.404× (z -11.0) |
| [[A549 (line)]] | wt | 72.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.427× (z -9.0) |
| [[HS-578T (line)]] | alt | 48.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -12.1) |
| [[PANC-1 (line)]] | alt | 53.8 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 59.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 93.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.427× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 71.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -17.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -14.5) |
| [[LoVo (line)]] | wt | 78.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -10.1) |
| [[SW1417 (line)]] | alt | 66.0 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -15.3) |
| [[J82 (line)]] | alt | 54.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -17.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -10.7) |
| [[LS 180 (line)]] | wt | 65.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0998× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -13.6) |
| [[SW48 (line)]] | wt | 61.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -11.1) |
| [[A-172 (line)]] | wt | 49.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -10.8) |
| [[KATO III (line)]] | alt | 96.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0817× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -10.6) |
| [[SHP-77 (line)]] | alt | 46.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -12.7) |
| [[SNU-423 (line)]] | alt | 49.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -9.6) |
| [[SW480 (line)]] | alt | 67.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -19.2) |
| [[HCT15 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0556× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Hs 766T (line)]] | wt | 74.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -14.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 69.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.322× (z -9.4) |
| [[C32 (line)]] | wt | 45.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 53.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 35.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 94.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -11.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 91.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[RKO (line)]] | wt | 48.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 62.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -20.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 43.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.145× (z -9.2) |
| [[BT-474 (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.263× (z -12.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[COLO 205 (line)]] | alt | 93.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SNU-1 (line)]] | wt | 62.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -18.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 1088 (line)]] | alt | 82.1 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0901× (z -8.5) |
| [[CHP-212 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF5]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[OSBP]] | +0.76 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.75 | +0.79 / +0.72 | both halves | 7e-06 | STRING 466 |
| [[COPB1]] | +0.75 | +0.80 / +0.69 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 636 |
| [[SRP54]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 | STRING 483 |
| [[SPTY2D1]] | +0.74 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[COPB2]] | +0.74 | +0.82 / +0.64 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 459 |
| [[COG3]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 892 |
| [[SLC33A1]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ERLEC1]] | +0.74 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[RUSF1]] | +0.73 | +0.82 / +0.64 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.828). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (12.2, -36.7); signed map (-52.5, 12.8). **Vector** length 103, 31.7% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.54 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.57 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +2.5 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -1.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.9 | +1.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -21.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.7 | -13.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.2 | -18.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.9 | -13.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -4.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -0.8 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | golgin A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:92,794,305-92,839,947 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ret-II, golgin-84, rfg5, GOLIM5 |
| Gene groups (HGNC) | Golgins |
| Reactome | 4 pathways, smallest: Intra-Golgi traffic; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBA6](https://www.uniprot.org/uniprotkb/Q8TBA6) (Golgin subfamily A member 5):

> Involved in maintaining Golgi structure. Stimulates the formation of Golgi stacks and ribbons. Involved in intra-Golgi retrograde transport.

**Summary**, from NCBI Gene [9950](https://www.ncbi.nlm.nih.gov/gene/9950):

> The Golgi apparatus, which participates in glycosylation and transport of proteins and lipids in the secretory pathway, consists of a series of stacked cisternae (flattened membrane sacs). Interactions between the Golgi and microtubules are thought to be important for the reorganization of the Golgi after it fragments during mitosis. This gene encodes one of the golgins, a family of proteins localized to the Golgi. This protein is a coiled-coil membrane protein that has been postulated to play …

**Accessions** — [HGNC:4428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4428) · Entrez [9950](https://www.ncbi.nlm.nih.gov/gene/9950) · UniProt [Q8TBA6](https://www.uniprot.org/uniprotkb/Q8TBA6) · Ensembl [ENSG00000066455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066455)

## Data

Gene col 829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 829); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 829]; `tensor/DDL_lfc|DDL_z.npy` [829]; `embed/gene_vectors.npy` [829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 829 or target_col == 829). Every well: [[GOLGA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
