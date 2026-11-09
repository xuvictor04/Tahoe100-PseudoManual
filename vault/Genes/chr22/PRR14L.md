---
symbol: "PRR14L"
type: "gene"
col: 11416
ensembl_id: "ENSG00000183530"
name: "proline rich 14 like"
location: "22q12.2"
module: 7
arm: "+"
pooled_cpm: 85.8
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PRR14L

*proline rich 14 like* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.7, q 7e-06, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.522× (z -11.6, q 1e-28, down in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.831× (z -4.6, q 2e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK12]] (+0.66, fdr 7e-06), [[WAPL]] (+0.64, fdr 1e-05), [[IREB2]] (+0.62, fdr 1e-05); moves opposite to [[FOXO6]] (-0.63, fdr 1e-05), [[HMGN3]] (-0.62, fdr 5e-05), [[THRA]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYB5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 7e-06 | 33/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.9 | 3e-04 | 35/48 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.16× | +3.9 | 0.020 | 18/49 (C32, Hs 766T, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.053 | 23/48 (NCI-H1573, SW 1088, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.20×** | +3.4 | 0.084 | 20/48 (RKO, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -11.6 | 1e-28 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.571×** | -10.0 | 3e-21 | 39/49 (A-427, HCT15, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.678×** | -9.8 | 2e-20 | 36/48 (hTERT-HPNE, NCI-H1792, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -9.6 | 8e-20 | 42/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.560×** | -9.6 | 8e-20 | 36/45 (RKO, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.603×** | -9.1 | 1e-17 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.663×** | -7.1 | 1e-10 | 36/48 (hTERT-HPNE, A-427, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.680×** | -6.6 | 2e-09 | 30/44 (A-427, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.761×** | -4.9 | 6e-05 | 30/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.605×** | -4.7 | 2e-04 | 23/38 (BT-474, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -4.6 | 2e-04 | 25/48 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.002 | 25/49 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~85% of this change | **0.816×** | -3.6 | 0.013 | 22/48 (RPMI-7951, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.763×** | -3.4 | 0.024 | 26/47 (CHP-212, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.826×** | -3.3 | 0.040 | 21/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift |
| [[Radotinib (drug)]] 5 µM |  | 0.885× | -3.1 | 0.076 | 10/48 (PANC-1, CHP-212, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.831×** | -3.0 | 0.076 | 18/47 (C-33 A, LS 180, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.083 | 17/48 (NCI-H2030, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 86.8 | 0 | 10 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 92.6 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -18.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 67.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[KATO III (line)]] | alt | 136 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -18.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 67.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 100 | 0 | 3 (2 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.312× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 78.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LoVo (line)]] | wt | 108 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 75.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[RKO (line)]] | wt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -21.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 88.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW48 (line)]] | wt | 98.3 | 0 | 3 (3 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0792× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 72.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.488× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 59.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 76.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.209× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 90.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -10.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 94.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -14.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 89.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.472× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 71.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 81.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 73.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -9.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A498 (line)]] | wt | 86.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.344× (z -10.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.364× (z -9.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -9.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LS 180 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.429× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 96.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 84.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.393× (z -10.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.359× (z -9.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 106 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK12]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[WAPL]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[IREB2]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[BAG5]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TRAPPC12]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PSMB5]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ALG8]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FAM120B]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ACAD9]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[METTL13]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[DDX56]] | +0.56 | +0.51 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO6]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.62 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[THRA]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[BCAM]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[IL11RA]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[PNKD]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[AMOT]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CYB5A]] | -0.55 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[MPP7]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ARHGAP12]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[STARD5]] | -0.55 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SPTB]] | -0.55 | -0.38 / -0.56 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYB5A]] | B | CYB5A activity raises PRR14L's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without CYB5A | 0.035 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[AMOT]] | B | AMOT activity raises PRR14L's level | lines that do not express AMOT (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without AMOT | 0.079 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-15.7, 17.7); signed map (-4.9, -22.3). **Vector** length 98.5, 27.8% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +4.2 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.1 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +0.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.8 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -4.6 | -10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -4.4 | -6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.9 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 14 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,676,256-31,750,140 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC50372; previously C22orf30 |
| Matched by | ensembl_id |

UniProt [Q5THK1](https://www.uniprot.org/uniprotkb/Q5THK1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28738) · Entrez [253143](https://www.ncbi.nlm.nih.gov/gene/253143) · UniProt [Q5THK1](https://www.uniprot.org/uniprotkb/Q5THK1) · Ensembl [ENSG00000183530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183530)

## Data

Gene col 11416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11416); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11416]; `tensor/DDL_lfc|DDL_z.npy` [11416]; `embed/gene_vectors.npy` [11416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11416 or target_col == 11416). Every well: [[PRR14L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR14L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
