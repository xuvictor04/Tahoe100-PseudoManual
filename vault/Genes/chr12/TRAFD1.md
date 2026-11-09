---
symbol: "TRAFD1"
type: "gene"
col: 5661
ensembl_id: "ENSG00000135148"
name: "TRAF-type zinc finger domain containing 1"
location: "12q24.13"
module: 70
arm: "+"
pooled_cpm: 23.29
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 10
n_dd_up_clean: 33
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TRAFD1

*TRAF-type zinc finger domain containing 1* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +24.4, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.620× (z -8.3, q 7e-14, down in 26 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.696× (z -6.8, q 3e-09, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX58]] (+0.69, fdr 7e-06), [[IRF7]] (+0.67, fdr 7e-06), [[FBXO6]] (+0.66, fdr 1e-05); moves opposite to [[AHCY]] (-0.64, fdr 1e-05), [[ARHGAP4]] (-0.60, fdr 1e-05), [[LYPLA1]] (-0.57, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 4 with an alert ⚠; shown: the 15 strongest. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +24.4 | 0e+00 | 44/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.66×** | +18.4 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.60×** | +18.0 | 0e+00 | 41/45 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +16.5 | 0e+00 | 44/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.40×** | +15.8 | 0e+00 | 45/48 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +14.7 | 0e+00 | 42/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +10.0 | 1e-21 | 30/46 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +9.8 | 5e-21 | 34/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +7.2 | 3e-11 | 26/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +7.0 | 1e-10 | 27/47 (A549, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.9 | 2e-10 | 25/48 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.7 | 1e-09 | 25/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.6 | 1e-09 | 23/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +6.5 | 5e-09 | 23/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 2e-07 | 22/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -8.3 | 7e-14 | 26/38 (SW1417, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -6.8 | 3e-09 | 29/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -5.9 | 7e-07 | 24/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.741×** | -5.6 | 3e-06 | 24/42 (LS 180, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -5.5 | 4e-06 | 19/48 (C32, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.786×** | -4.5 | 7e-04 | 21/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.785×** | -4.4 | 0.001 | 19/34 (BT-474, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.796×** | -4.3 | 0.001 | 19/48 (BT-474, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.828×** | -3.5 | 0.027 | 18/47 (NCI-H460, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.3 | 0.053 | 16/47 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.883× | -3.3 | 0.056 | 12/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.726×** | -3.1 | 0.082 | 10/30 (A-427, BT-474, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.2 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.5) | [[Digitoxin (drug)]] 0.5 µM 0.389× (z -8.9) |
| [[A498 (line)]] | wt | 45.4 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 18.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.3) | [[Digitoxin (drug)]] 0.5 µM 0.252× (z -13.0) |
| [[PANC-1 (line)]] | alt | 23.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.6) | — |
| [[A-172 (line)]] | wt | 35.0 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.07× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 15.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +14.5) | — |
| [[LoVo (line)]] | wt | 17.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 3 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.82× (z +13.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +9.4) | — |
| [[A549 (line)]] | wt | 23.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 60.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 22.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 35.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 23.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.93× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 16.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 25.8 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.24× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 20.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +11.1) | — |
| [[KATO III (line)]] | alt | 20.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX58]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IRF7]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[FBXO6]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[WHAMM]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ASB8]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GBP2]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[EMC9]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[BTN3A1]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PSMB9]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[NMI]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIH1]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRIM5]] | +0.62 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHCY]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[LYPLA1]] | -0.57 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[NUDT3]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SEH1L]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[CPSF6]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[GART]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRAFD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ETV7]] | B | ETV7 activity raises TRAFD1's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.18× lower at baseline in the lines without ETV7 | 0.069 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises TRAFD1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without GBP4 | 0.082 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[TMEM140]] | B | TMEM140 activity raises TRAFD1's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without TMEM140 | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFIT1]] | C | IFIT1 activity raises TRAFD1's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without IFIT1 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[IFT74]] | C | IFT74 activity lowers TRAFD1's level | lines that do not express IFT74 (3) vs lines expressing it (47) | 1.65× higher at baseline in the lines without IFT74 | 0.091 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.8, 49.4); signed map (62.1, 27.4). **Vector** length 104, 27.0% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Non-canonical inflammasome activation* (reactome, mean cos +0.60 to 4); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.55 to 4); *CASP4 inflammasome assembly* (reactome, mean cos +0.60 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +18.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +24.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +7.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.7 | +5.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | +2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TRAF-type zinc finger domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,125,538-112,153,604 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLN29 |
| Gene groups (HGNC) | Zinc fingers TRAF-type |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [O14545](https://www.uniprot.org/uniprotkb/O14545) (TRAF-type zinc finger domain-containing protein 1):

> Negative feedback regulator that controls excessive innate immune responses. Regulates both Toll-like receptor 4 (TLR4) and DDX58/RIG1-like helicases (RLH) pathways. May inhibit the LTR pathway by direct interaction with TRAF6 and attenuation of NF-kappa-B activation. May negatively regulate the RLH pathway downstream from MAVS and upstream of NF-kappa-B and IRF3 (By similarity).

**Summary**, from NCBI Gene [10906](https://www.ncbi.nlm.nih.gov/gene/10906):

> The innate immune system confers host defense against viral and microbial infection, and TRAFD1 is a negative feedback regulator that controls excessive immune responses (Sanada et al., 2008 [PubMed 18849341]).[supplied by OMIM, Dec 2009]

**Accessions** — [HGNC:24808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24808) · Entrez [10906](https://www.ncbi.nlm.nih.gov/gene/10906) · UniProt [O14545](https://www.uniprot.org/uniprotkb/O14545) · Ensembl [ENSG00000135148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135148)

## Data

Gene col 5661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5661); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5661]; `tensor/DDL_lfc|DDL_z.npy` [5661]; `embed/gene_vectors.npy` [5661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5661 or target_col == 5661). Every well: [[TRAFD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAFD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
