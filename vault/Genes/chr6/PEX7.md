---
symbol: "PEX7"
type: "gene"
col: 3362
ensembl_id: "ENSG00000112357"
name: "peroxisomal biogenesis factor 7"
location: "6q23.3"
module: 33
arm: "+"
pooled_cpm: 20.93
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PEX7

*peroxisomal biogenesis factor 7* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM: 1.40× (z +5.5, q 2e-05, up in 23 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 1.24× (z +3.6, q 0.044, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.375× (z -16.1, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANGEL1]] (+0.65, fdr 7e-06), [[ORC5]] (+0.64, fdr 7e-06), [[ZNF485]] (+0.63, fdr 1e-05); moves opposite to [[LASP1]] (-0.51, fdr 2e-05), [[GPR137C]] (-0.51, fdr 2e-04), [[LNC-LBCS]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSEN2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.40×** | +5.5 | 2e-05 | 23/46 (SK-MEL-2, COLO 205, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.22×** | +4.6 | 1e-03 | 19/47 (RKO, LS 180, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.31×** | +4.5 | 0.001 | 17/46 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.044 | 12/46 (J82, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.5 | 0.044 | 13/47 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +3.5 | 0.044 | 8/46 (SW480, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.12 | 13/47 (LS 180, NCI-H1792, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3362.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.375×** | -16.1 | 0e+00 | 38/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.395×** | -15.2 | 0e+00 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -13.1 | 1e-36 | 38/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.503×** | -10.8 | 3e-25 | 33/44 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -9.9 | 5e-21 | 29/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.534×** | -9.5 | 2e-19 | 24/38 (SW480, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.586×** | -8.7 | 2e-16 | 32/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.606×** | -8.2 | 2e-14 | 24/42 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.725×** | -7.4 | 7e-12 | 28/46 (NCI-H23, C32, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.646×** | -7.1 | 5e-11 | 27/46 (AN3 CA, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.653×** | -6.7 | 1e-09 | 27/47 (NCI-H460, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.683×** | -6.0 | 1e-07 | 13/28 (LS 180, SNU-423, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.735×** | -5.0 | 2e-05 | 21/46 (PANC-1, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.766×** | -4.3 | 6e-04 | 16/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.002 | 19/47 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.015 | 5/47 (CHP-212, NCI-H2030, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.023 | 8/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.025 | 6/47 (BT-474, SW48, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.833×** | -3.0 | 0.071 | 11/45 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -16.7) |
| [[SW480 (line)]] | alt | 29.8 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -17.6) |
| [[PANC-1 (line)]] | alt | 30.0 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -19.0) |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.9) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -12.8) |
| [[COLO 205 (line)]] | alt | 81.8 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -11.1) |
| [[LoVo (line)]] | wt | 26.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.343× (z -9.3) |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 3 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0668× (z -10.5) |
| [[C32 (line)]] | wt | 22.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.4) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.228× (z -9.3) |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -9.3) |
| [[KATO III (line)]] | alt | 33.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -15.5) |
| [[A-427 (line)]] | wt | 20.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -9.4) |
| [[A498 (line)]] | wt | 9.56 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.0) ⚠ cell-cycle shift, explains ~85% of this change |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.221× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -9.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.155× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.236× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.243× (z -8.9) |
| [[RKO (line)]] | wt | 23.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.165× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.148× (z -12.8) |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -10.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.6) |
| [[A-172 (line)]] | wt | 14.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.189× (z -9.2) |
| [[A549 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -11.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.259× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 25.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.342× (z -9.3) |
| [[J82 (line)]] | alt | 15.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.229× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.9) ⚠ cell-cycle shift, explains ~85% of this change |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -10.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0782× (z -12.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[AsPC-1 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL1]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ORC5]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.61 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[KAT14]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MTFMT]] | +0.58 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[DHX57]] | +0.58 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[MRPL15]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[THEM4]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MECR]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BORCS5]] | +0.57 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LASP1]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[GPR137C]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[LNC-LBCS]] | -0.49 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSEN2]] | C | TSEN2 activity raises PEX7's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without TSEN2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.9, -43.3); signed map (-16.8, -22.6). **Vector** length 74.8, 14.5% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.4 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +3.8 | +4.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -16.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -10.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -2.7 | -7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:136,822,564-136,913,934 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTS2R, RD |
| Gene groups (HGNC) | WD repeat domain containing; Peroxins |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Peroxisomal protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O00628](https://www.uniprot.org/uniprotkb/O00628) (Peroxisomal targeting signal 2 receptor):

> Receptor required for the peroxisomal import of proteins containing an N-terminal PTS2-type peroxisomal targeting signal. Specifically binds to cargo proteins containing a PTS2 peroxisomal targeting signal in the cytosol. Cargo protein-binding triggers interaction with PEX5 and formation of a ternary complex composed of PEX5 and PEX7 along with PTS2-containing cargo proteins, which is translocated into peroxisomes by passing through the PEX13-PEX14 docking complex.

**Summary**, from NCBI Gene [5191](https://www.ncbi.nlm.nih.gov/gene/5191):

> This gene encodes the cytosolic receptor for the set of peroxisomal matrix enzymes targeted to the organelle by the peroxisome targeting signal 2 (PTS2). Defects in this gene cause peroxisome biogenesis disorders (PBDs), which are characterized by multiple defects in peroxisome function. There are at least 14 complementation groups for PBDs, with more than one phenotype being observed in cases falling into particular complementation groups. Although the clinical features of PBD patients vary, …

**Accessions** — [HGNC:8860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8860) · Entrez [5191](https://www.ncbi.nlm.nih.gov/gene/5191) · UniProt [O00628](https://www.uniprot.org/uniprotkb/O00628) · Ensembl [ENSG00000112357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112357)

## Data

Gene col 3362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3362); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3362]; `tensor/DDL_lfc|DDL_z.npy` [3362]; `embed/gene_vectors.npy` [3362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3362 or target_col == 3362). Every well: [[PEX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
