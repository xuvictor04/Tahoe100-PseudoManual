---
symbol: "SCAMP1"
type: "gene"
col: 1422
ensembl_id: "ENSG00000085365"
name: "secretory carrier membrane protein 1"
location: "5q14.1"
module: 76
arm: "+"
pooled_cpm: 104.49
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 40
n_dd_up_clean: 0
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# SCAMP1

*secretory carrier membrane protein 1* — 5q14.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.278× (z -47.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXI1]] (+0.64, fdr 7e-06), [[RALBP1]] (+0.61, fdr 1e-05), [[VPS35]] (+0.61, fdr 1e-05); moves opposite to [[EME2]] (-0.52, fdr 4e-04), [[NOP56]] (-0.51, fdr 4e-05), [[GABPB1-AS1]] (-0.50, fdr 7e-04).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.19× | +4.4 | 0.005 | 19/47 (H4, A-172, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.3 | 0.005 | 0/50 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.11× | +4.1 | 0.008 | 0/48 | all doses, stronger at high dose |  |
| [[Pentagastrin (drug)]] 5 µM |  | 1.11× | +4.0 | 0.008 | 1/48 (HCT15) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +4.0 | 0.008 | 18/47 (SNU-423, H4, …) | rises with dose | low cells (technical?) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.9 | 0.011 | 6/48 (KATO III, BT-474, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.278×** | -47.8 | 0e+00 | 48/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.374×** | -26.0 | 0e+00 | 46/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -25.2 | 0e+00 | 46/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.379×** | -24.6 | 0e+00 | 47/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.425×** | -22.6 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -19.0 | 0e+00 | 41/49 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.512×** | -17.0 | 0e+00 | 44/47 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.567×** | -15.0 | 0e+00 | 46/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -14.2 | 3e-44 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -12.9 | 3e-36 | 43/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -12.6 | 6e-35 | 43/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -11.8 | 3e-30 | 41/48 (SNU-423, A-427, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.641×** | -11.3 | 8e-28 | 34/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -11.2 | 2e-27 | 42/48 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.655×** | -11.2 | 2e-27 | 39/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -10.4 | 1e-23 | 38/49 (A-172, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.687×** | -9.9 | 2e-21 | 33/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -8.1 | 2e-14 | 36/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.589×** | -7.3 | 6e-12 | 38/48 (HEC-1-A, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.754×** | -7.0 | 5e-11 | 35/48 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.614×** | -6.7 | 3e-10 | 35/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.7 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -34.9) |
| [[HOP62 (line)]] | alt | 128 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -29.1) |
| [[A-172 (line)]] | wt | 171 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -34.6) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -27.4) |
| [[LoVo (line)]] | wt | 110 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -24.3) |
| [[SW480 (line)]] | alt | 86.3 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -24.7) |
| [[HS-578T (line)]] | alt | 126 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -23.2) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -34.5) |
| [[NCI-H1573 (line)]] | alt | 75.1 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -23.5) |
| [[PANC-1 (line)]] | alt | 113 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -32.4) |
| [[A549 (line)]] | wt | 133 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -27.4) |
| [[Hs 766T (line)]] | wt | 96.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -24.4) |
| [[AsPC-1 (line)]] | alt | 94.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -23.9) |
| [[C32 (line)]] | wt | 77.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -28.0) |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -20.7) |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -31.2) |
| [[NCI-H1792 (line)]] | alt | 142 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -20.8) |
| [[NCI-H2347 (line)]] | alt | 140 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -29.4) |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -23.3) |
| [[SNU-1 (line)]] | wt | 99.5 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.172× (z -15.3) |
| [[SW 900 (line)]] | alt | 114 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -19.8) |
| [[A498 (line)]] | wt | 94.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -24.0) |
| [[J82 (line)]] | alt | 93.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -32.3) |
| [[NCI-H2030 (line)]] | alt | 73.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -19.5) |
| [[RKO (line)]] | wt | 96.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -20.3) |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -26.7) |
| [[HEC-1-A (line)]] | alt | 89.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -21.3) |
| [[KATO III (line)]] | alt | 79.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 81.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -20.8) |
| [[SK-MEL-2 (line)]] | alt | 95.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -27.9) |
| [[SW1417 (line)]] | alt | 51.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.5) |
| [[A-427 (line)]] | wt | 116 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -19.5) |
| [[BT-474 (line)]] | alt | 75.7 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.319× (z -11.2) |
| [[COLO 205 (line)]] | alt | 93.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -21.0) |
| [[LS 180 (line)]] | wt | 95.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -19.5) |
| [[RPMI-7951 (line)]] | alt | 96.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -34.3) |
| [[AN3 CA (line)]] | alt | 142 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.7) |
| [[H4 (line)]] | wt | 97.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.8) |
| [[HCT15 (line)]] | alt | 107 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 75.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.2) |
| [[HT-29 (line)]] | alt | 72.0 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.300× (z -14.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.390× (z -11.5) |
| [[SHP-77 (line)]] | alt | 87.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.451× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.3) |
| [[SW 1088 (line)]] | alt | 160 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.113× (z -10.4) |
| [[SW48 (line)]] | wt | 87.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.1) |
| [[C-33 A (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H661 (line)]] | alt | 52.1 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0587× (z -11.7) |
| [[SW 1271 (line)]] | alt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.7) |
| [[CHP-212 (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXI1]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RALBP1]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[VPS35]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[APPL1]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[GPN3]] | +0.60 | +0.26 / +0.46 | both halves | 3e-04 |  |
| [[RBL2]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[DHX40]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[MARCHF8]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[FBXO25]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ARL3]] | +0.57 | +0.62 / +0.27 | both halves | 3e-04 |  |
| [[ANKIB1]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EME2]] | -0.52 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[NOP56]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[GABPB1-AS1]] | -0.50 | -0.53 / -0.20 | both halves | 7e-04 |  |
| [[BFSP1]] | -0.49 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ADCK1]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[ASMTL-AS1]] | -0.48 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[MSANTD2]] | -0.48 | -0.40 / -0.23 | both halves | 6e-04 |  |
| [[CUEDC1]] | -0.48 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[LINC00106]] | -0.48 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[SRSF1]] | -0.48 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[ST7L]] | -0.47 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[MBD3]] | -0.47 | -0.52 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.3, -52.2); signed map (-20.3, 9.2). **Vector** length 69.6, 18.8% of its response variance represented; |z| ≥ 3 in 1,602 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.5 | -9.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.0 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.8 | -15.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.6 | -11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | +2.6 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -0.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.6 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.1 | -17.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | secretory carrier membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:78,360,611-78,480,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCAMP37 |
| Gene groups (HGNC) | Secretory carrier membrane proteins |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O15126](https://www.uniprot.org/uniprotkb/O15126) (Secretory carrier-associated membrane protein 1):

> Functions in post-Golgi recycling pathways. Acts as a recycling carrier to the cell surface.

**Summary**, from NCBI Gene [9522](https://www.ncbi.nlm.nih.gov/gene/9522):

> This gene product belongs to the SCAMP family of proteins, which are secretory carrier membrane proteins. They function as carriers to the cell surface in post-golgi recycling pathways. Different family members are highly related products of distinct genes, and are usually expressed together. These findings suggest that these protein family members may function at the same site during vesicular transport rather than in separate pathways. A pseudogene of this gene has been defined on chromosome …

**Accessions** — [HGNC:10563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10563) · Entrez [9522](https://www.ncbi.nlm.nih.gov/gene/9522) · UniProt [O15126](https://www.uniprot.org/uniprotkb/O15126) · Ensembl [ENSG00000085365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085365)

## Data

Gene col 1422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1422); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1422]; `tensor/DDL_lfc|DDL_z.npy` [1422]; `embed/gene_vectors.npy` [1422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1422 or target_col == 1422). Every well: [[SCAMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
