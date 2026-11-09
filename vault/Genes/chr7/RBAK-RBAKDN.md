---
symbol: "RBAK-RBAKDN"
type: "gene"
col: 15752
ensembl_id: "ENSG00000272968"
name: "RBAK-RBAKDN readthrough"
location: "7p22.1"
module: 49
arm: "+"
pooled_cpm: 86.83
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RBAK-RBAKDN

*RBAK-RBAKDN readthrough* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.39× (z +8.2, q 1e-13, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 9 lines (RKO 3.52×, SW48 2.95×, HT-29 2.97×, HOP62 2.20×, …).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.348× (z -37.6, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.71, fdr 1e-05), [[ATG4B]] (+0.68, fdr 1e-05), [[RNF216P1]] (+0.68, fdr 8e-06, ⚠ same locus), [[NAT9]] (+0.68, fdr 1e-05); moves opposite to [[TAPBP]] (-0.70, fdr 1e-05), [[HMGN2]] (-0.69, fdr 1e-05), [[BAZ2B]] (-0.69, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15752.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 9 lines (RKO 3.52×, SW48 2.95×, HT-29 2.97×, HOP62 2.20×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +8.2 | 1e-13 | 29/48 (RKO, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.20× | +4.3 | 0.006 | 20/48 (RKO, LoVo, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.044 | 15/49 (SNU-1, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.044 | 15/49 (A498, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -37.6 | 0e+00 | 44/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.389×** | -22.8 | 0e+00 | 45/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -20.7 | 0e+00 | 40/44 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.457×** | -19.7 | 0e+00 | 42/49 (NCI-H23, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -18.4 | 0e+00 | 41/49 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.494×** | -17.7 | 0e+00 | 42/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.494×** | -16.4 | 0e+00 | 41/45 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -15.3 | 0e+00 | 42/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.577×** | -13.8 | 2e-41 | 39/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -12.4 | 1e-33 | 36/50 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.710×** | -12.2 | 3e-32 | 42/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -11.0 | 2e-26 | 38/47 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -10.7 | 4e-25 | 34/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -9.7 | 8e-21 | 36/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.691×** | -9.3 | 7e-19 | 34/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.852× | -4.0 | 0.002 | 21/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.913× | -3.2 | 0.034 | 8/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.918× | -3.0 | 0.058 | 6/48 (HOP62, NCI-H1792, …) | top dose only |  |
| [[venetoclax (drug)]] 0.05 µM |  | 0.884× | -2.9 | 0.080 | 8/49 (Panc 03.27, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 181 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -40.7) |
| [[NCI-H460 (line)]] | wt | 82.9 | 0 | 15 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -21.0) |
| [[HOP62 (line)]] | alt | 82.9 | 1 | 13 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.20× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -30.5) |
| [[H4 (line)]] | wt | 255 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -21.7) |
| [[HEC-1-A (line)]] | alt | 146 | 0 | 12 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.365× (z -20.2) |
| [[BT-474 (line)]] | alt | 108 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -15.0) |
| [[C32 (line)]] | wt | 102 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -25.2) |
| [[HS-578T (line)]] | alt | 96.1 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -34.8) |
| [[SW 900 (line)]] | alt | 80.7 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.4) |
| [[A498 (line)]] | wt | 139 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -29.2) |
| [[hTERT-HPNE (line)]] | wt | 80.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -18.3) |
| [[LoVo (line)]] | wt | 127 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -15.6) |
| [[J82 (line)]] | alt | 63.0 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -29.4) |
| [[MIA PaCa-2 (line)]] | alt | 95.8 | 1 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.98× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -15.8) |
| [[PANC-1 (line)]] | alt | 70.2 | 1 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.88× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -28.0) |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.8) |
| [[SW480 (line)]] | alt | 98.4 | 1 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.60× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.521× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.532× (z -11.7) |
| [[A549 (line)]] | wt | 95.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 74.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -28.6) |
| [[NCI-H2347 (line)]] | alt | 50.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -19.9) |
| [[SW1417 (line)]] | alt | 85.6 | 1 | 6 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.95× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.477× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 64.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -20.0) |
| [[AN3 CA (line)]] | alt | 108 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0521× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0719× (z -18.5) |
| [[Hs 766T (line)]] | wt | 61.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -18.2) |
| [[KATO III (line)]] | alt | 110 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 39.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 97.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -30.6) |
| [[SNU-423 (line)]] | alt | 64.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -23.5) |
| [[SW48 (line)]] | wt | 154 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.95× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 71.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -16.6) |
| [[A-427 (line)]] | wt | 61.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 48.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -20.1) |
| [[CHP-212 (line)]] | wt | 67.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0744× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.1) |
| [[RKO (line)]] | wt | 69.0 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.52× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.2) |
| [[SHP-77 (line)]] | alt | 97.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -28.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 84.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -14.2) |
| [[C-33 A (line)]] | alt | 83.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -16.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 43.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.97× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 76.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.22× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.6) |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.8) |
| [[HCT15 (line)]] | alt | 62.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 58.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.71 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.68 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RNF216P1]] | +0.68 | +0.67 / +0.58 | both halves | 8e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NAT9]] | +0.68 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[RNF216]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ANKS3]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[EIF4EBP1]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SEC13]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[BICD2]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TMEM243]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[LPCAT1]] | +0.66 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[LINC02693]] | +0.66 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GPR89B]] | +0.66 | +0.37 / +0.68 | both halves | 8e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPBP]] | -0.70 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.69 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.69 | -0.72 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.68 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[DECR1]] | -0.66 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[RAP2C]] | -0.66 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TIA1]] | -0.66 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[CASD1]] | -0.65 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.63 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.63 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[FMR1]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NFKB1]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RBAK-RBAKDN's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM111A]] | C | FAM111A activity strengthens RBAK-RBAKDN's drug response | lines that do not express FAM111A (3) vs lines expressing it (47) | the lines without FAM111A respond 0.47× as strongly (z diff +2.48); strongest at Ouabain (Octahydrate) 5 µM: 0.84x vs 0.48x (z diff +5.6) | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.5, 0.7); signed map (-43.8, -0.5). **Vector** length 117, 36.4% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.9 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.0 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.6 | -22.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.3 | -17.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -9.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -37.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -12.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RBAK-RBAKDN readthrough |
| Locus type | readthrough (other) |
| Location | 7p22.1 — chr7:4,983,718-5,073,221 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100533952](https://www.ncbi.nlm.nih.gov/gene/100533952):

> This locus represents naturally occurring read-through transcription between the neighboring RBAK (RB-associated KRAB zinc finger) and LOC389458 (hypothetical LOC389458) genes on chromosome 7. The read-through transcript encodes a protein that shares sequence identity with the upstream gene product but its C-terminal region is distinct due to frameshifts relative to the downstream gene. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:42971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42971) · Entrez [100533952](https://www.ncbi.nlm.nih.gov/gene/100533952) · Ensembl [ENSG00000272968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272968)

## Data

Gene col 15752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15752); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15752]; `tensor/DDL_lfc|DDL_z.npy` [15752]; `embed/gene_vectors.npy` [15752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15752 or target_col == 15752). Every well: [[RBAK-RBAKDN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBAK-RBAKDN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
