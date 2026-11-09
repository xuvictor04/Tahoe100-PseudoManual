---
symbol: "MBTPS1"
type: "gene"
col: 6466
ensembl_id: "ENSG00000140943"
name: "membrane bound transcription factor peptidase, site 1"
location: "16q23.3-q24.1"
module: 76
arm: "+"
pooled_cpm: 77.65
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# MBTPS1

*membrane bound transcription factor peptidase, site 1* — 16q23.3-q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 1.73×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.475× (z -19.5, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.654× (z -15.7, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC28A]] (+0.65, fdr 1e-05), [[PLEKHM3]] (+0.63, fdr 2e-05), [[RBL2]] (+0.62, fdr 1e-05); moves opposite to [[LHFPL6]] (-0.49, fdr 6e-05), [[IL34]] (-0.49, fdr 1e-04), [[UBE2N]] (-0.47, fdr 8e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 1.73×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 5 µM |  | 1.14× | +3.4 | 0.41 | 3/48 (Panc 03.27, SW 900, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6466.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.475×** | -19.5 | 0e+00 | 47/48 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -15.7 | 0e+00 | 41/49 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.721×** | -12.0 | 4e-31 | 31/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -11.8 | 6e-30 | 41/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.647×** | -10.9 | 8e-26 | 36/48 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -10.4 | 3e-23 | 40/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.487×** | -9.8 | 6e-21 | 45/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.514×** | -9.1 | 6e-18 | 41/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -9.0 | 1e-17 | 1/50 (COLO 205) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.519×** | -9.0 | 2e-17 | 45/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.715×** | -8.8 | 1e-16 | 32/48 (HOP62, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.528×** | -8.7 | 1e-16 | 42/48 (KATO III, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.629×** | -8.6 | 2e-16 | 42/48 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.537×** | -8.5 | 7e-16 | 38/48 (NCI-H2030, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.698×** | -6.7 | 9e-10 | 41/49 (SW48, SNU-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -6.7 | 9e-10 | 22/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.789×** | -5.7 | 4e-07 | 24/47 (J82, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.7 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.409× (z -11.4) |
| [[HOP62 (line)]] | alt | 106 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -21.0) |
| [[RKO (line)]] | wt | 97.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.261× (z -14.2) |
| [[SW480 (line)]] | alt | 82.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -12.3) |
| [[A498 (line)]] | wt | 68.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 63.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -17.8) |
| [[J82 (line)]] | alt | 69.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -12.2) |
| [[LoVo (line)]] | wt | 60.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -14.7) |
| [[SNU-423 (line)]] | alt | 73.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -20.7) |
| [[A-427 (line)]] | wt | 68.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 83.0 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.412× (z -10.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.5) |
| [[C32 (line)]] | wt | 63.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.3) |
| [[HS-578T (line)]] | alt | 88.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.445× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 120 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.408× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 72.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 54.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.302× (z -13.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -11.9) |
| [[CHP-212 (line)]] | wt | 51.2 | 0 | 2 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.114× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.145× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -14.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -8.8) |
| [[Hs 766T (line)]] | wt | 73.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -11.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.1) |
| [[HT-29 (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -13.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -11.3) |
| [[KATO III (line)]] | alt | 85.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -13.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -20.4) |
| [[NCI-H23 (line)]] | alt | 79.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 63.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.374× (z -10.3) |
| [[PANC-1 (line)]] | alt | 75.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.453× (z -12.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.551× (z -9.4) |
| [[A-172 (line)]] | wt | 81.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -10.3) |
| [[AN3 CA (line)]] | alt | 90.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -11.5) |
| [[BT-474 (line)]] | alt | 87.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 50.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -9.0) |
| [[HCT15 (line)]] | alt | 72.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 68.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.448× (z -9.5) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 67.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.6) |
| [[SHP-77 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.448× (z -8.9) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 78.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 80.9 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0750× (z -9.3) |
| [[SW 1271 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -8.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SW 900 (line)]] | alt | 86.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.450× (z -8.9) |
| [[SW1417 (line)]] | alt | 71.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -8.8) |
| [[SW48 (line)]] | wt | 70.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -10.0) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC28A]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[PLEKHM3]] | +0.63 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[RBL2]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[FBXO25]] | +0.62 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[HACL1]] | +0.62 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TFDP2]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[AUH]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NIPAL3]] | +0.59 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[COQ8A]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[WIPI2]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[KIZ]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[WDR48]] | +0.57 | +0.35 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LHFPL6]] | -0.49 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[IL34]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[UBE2N]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[MYH15]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[RP1]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ENO3]] | -0.46 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[MZF1-AS1]] | -0.45 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[PLEKHA8P1]] | -0.45 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[LINC02966]] | -0.45 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[EPHA1-AS1]] | -0.44 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[NOP56]] | -0.44 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TMEM186]] | -0.44 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.1, -46.5); signed map (-19.4, 8.7). **Vector** length 111, 28.8% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.4 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | -2.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.5 | -19.5 |
|  | [[EX229 (drug)]] 5 µM |  | -7.4 | -8.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.3 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -11.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.9 | -9.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.8 | -9.0 |

## What is on record

|  |  |
|---|---|
| Name | membrane bound transcription factor peptidase, site 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3-q24.1 — chr16:84,053,761-84,116,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S1P, KIAA0091, SKI-1, PCSK8 |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Reactome | 15 pathways, smallest: ATF6B (ATF6-beta) activates chaperones; CREB3 factors activate genes; Assembly of active LPL and LIPC lipase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14703](https://www.uniprot.org/uniprotkb/Q14703) (Membrane-bound transcription factor site-1 protease):

> Serine protease that cleaves after hydrophobic or small residues, provided that Arg or Lys is in position P4: known substrates include SREBF1/SREBP1, SREBF2/SREBP2, BDNF, GNPTAB, ATF6, ATF6B and FAM20C. Cleaves substrates after Arg-Ser-Val-Leu (SREBP2), Arg-His-Leu-Leu (ATF6), Arg-Gly-Leu-Thr (BDNF) and its own propeptide after Arg-Arg-Leu-Leu. Catalyzes the first step in the proteolytic activation of the sterol regulatory element-binding proteins (SREBPs) SREBF1/SREBP1 and SREBF2/SREBP2. Also …

**Summary**, from NCBI Gene [8720](https://www.ncbi.nlm.nih.gov/gene/8720):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. The encoded protein undergoes an initial autocatalytic processing event in the ER to generate a heterodimer which exits the ER and sorts to the cis/medial-Golgi where a second autocatalytic event takes place and the catalytic activity is acquired. It encodes a type 1 …

**Accessions** — [HGNC:15456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15456) · Entrez [8720](https://www.ncbi.nlm.nih.gov/gene/8720) · UniProt [Q14703](https://www.uniprot.org/uniprotkb/Q14703) · Ensembl [ENSG00000140943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140943)

## Data

Gene col 6466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6466); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6466]; `tensor/DDL_lfc|DDL_z.npy` [6466]; `embed/gene_vectors.npy` [6466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6466 or target_col == 6466). Every well: [[MBTPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBTPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
