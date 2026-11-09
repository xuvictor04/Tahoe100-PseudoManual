---
symbol: "TPGS2"
type: "gene"
col: 5604
ensembl_id: "ENSG00000134779"
name: "tubulin polyglutamylase complex subunit 2"
location: "18q12.2"
module: 11
arm: "-"
pooled_cpm: 54.4
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TPGS2

*tubulin polyglutamylase complex subunit 2* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.91× (z +12.8, q 5e-35, up in 44 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-427 3.19×, A498 2.76×, KATO III 3.37×, PANC-1 2.26×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 2.75×, A498 2.89×, NCI-H1573 2.72×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.222× (z -42.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYH10]] (+0.59, fdr 1e-05), [[CPNE3]] (+0.59, fdr 1e-05), [[PGRMC1]] (+0.59, fdr 1e-05); moves opposite to [[ZNF593]] (-0.64, fdr 1e-05), [[PRPF38B]] (-0.63, fdr 7e-06), [[IWS1]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5604.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-427 3.19×, A498 2.76×, KATO III 3.37×, PANC-1 2.26×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 2.75×, A498 2.89×, NCI-H1573 2.72×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +12.8 | 5e-35 | 44/47 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +12.1 | 3e-31 | 37/41 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +5.7 | 2e-06 | 30/42 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.23 | 13/48 (KATO III, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.222×** | -42.0 | 0e+00 | 46/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.267×** | -26.0 | 0e+00 | 45/48 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.392×** | -17.8 | 0e+00 | 45/48 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.542×** | -12.1 | 2e-31 | 45/48 (HCT15, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -11.9 | 1e-30 | 40/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -9.6 | 7e-20 | 40/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.632×** | -9.0 | 1e-17 | 37/48 (NCI-H1573, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.648×** | -8.6 | 8e-16 | 38/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -8.1 | 3e-14 | 38/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -7.6 | 2e-12 | 36/49 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.691×** | -7.3 | 2e-11 | 30/48 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -6.9 | 2e-10 | 31/48 (NCI-H1573, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.731×** | -6.2 | 3e-08 | 31/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.724×** | -5.9 | 2e-07 | 27/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.826×** | -5.3 | 4e-06 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -3.9 | 0.002 | 20/48 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -3.9 | 0.003 | 16/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.050 | 17/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.858× | -2.9 | 0.083 | 16/48 (SK-MEL-2, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 75.7 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0955× (z -22.6) |
| [[SNU-423 (line)]] | alt | 64.9 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -27.9) |
| [[A-172 (line)]] | wt | 120 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -22.8) |
| [[NCI-H1573 (line)]] | alt | 48.9 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -27.6) |
| [[SW480 (line)]] | alt | 30.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -19.7) |
| [[C32 (line)]] | wt | 56.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -25.0) |
| [[LoVo (line)]] | wt | 32.4 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -26.7) |
| [[NCI-H460 (line)]] | wt | 49.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -33.6) |
| [[Panc 03.27 (line)]] | alt | 89.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -23.1) |
| [[AsPC-1 (line)]] | alt | 39.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -25.9) |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -19.0) |
| [[CFPAC-1 (line)]] | alt | 63.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -33.4) |
| [[NCI-H1792 (line)]] | alt | 97.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -41.3) |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.2) |
| [[A-427 (line)]] | wt | 65.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -32.7) |
| [[HCT15 (line)]] | alt | 70.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -19.6) |
| [[Hs 766T (line)]] | wt | 57.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -26.4) |
| [[HS-578T (line)]] | alt | 77.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -25.4) |
| [[KATO III (line)]] | alt | 39.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.3) |
| [[NCI-H2347 (line)]] | alt | 52.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.9) |
| [[PANC-1 (line)]] | alt | 49.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -23.2) |
| [[A498 (line)]] | wt | 35.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.6) |
| [[A549 (line)]] | wt | 45.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -22.2) |
| [[H4 (line)]] | wt | 81.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.7) |
| [[HOP62 (line)]] | alt | 60.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -29.0) |
| [[J82 (line)]] | alt | 78.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -24.1) |
| [[LOX-IMVI (line)]] | wt | 56.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.0) |
| [[NCI-H23 (line)]] | alt | 57.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -27.6) |
| [[RKO (line)]] | wt | 39.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 57.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -26.8) |
| [[SK-MEL-2 (line)]] | alt | 72.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -26.7) |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0478× (z -21.2) |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0646× (z -14.2) |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -21.6) |
| [[LS 180 (line)]] | wt | 44.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 20.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.1) |
| [[SW48 (line)]] | wt | 44.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -9.0) |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.116× (z -8.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.9) |
| [[SW 1271 (line)]] | alt | 81.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.8) |
| [[AN3 CA (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH10]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CPNE3]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PGRMC1]] | +0.59 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[YWHAQ]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.58 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CRTAP]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GNS]] | +0.57 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[VAMP3]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[CRYZ]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[BPNT2]] | +0.57 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ESYT1]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CNPY3]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | -0.64 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[PRPF38B]] | -0.63 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[IWS1]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SCAND1]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZNF768]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.59 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[MED18]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[EID2]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.57 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.57 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[NIFK]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.6, 0.8); signed map (-22.9, -36.3). **Vector** length 92.8, 25.6% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.3 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.0 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -26.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | tubulin polyglutamylase complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:36,777,647-36,829,216 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586M1523, HsT3006, PGs2; previously C18orf10 |
| Gene groups (HGNC) | Tubulin polyglutamylase complex subunits |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CL5](https://www.uniprot.org/uniprotkb/Q68CL5) (Tubulin polyglutamylase complex subunit 2):

> Subunit of the tubulin polyglutamylase complex (TPGC). The complex mediates cilia and flagella polyglutamylation which is essential for their biogenesis and motility.

**Summary**, from NCBI Gene [25941](https://www.ncbi.nlm.nih.gov/gene/25941):

> This gene encodes a protein that is a component of the neuronal polyglutamylase complex, which plays a role in post-translational addition of glutamate residues to C-terminal tubulin tails. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:24561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24561) · Entrez [25941](https://www.ncbi.nlm.nih.gov/gene/25941) · UniProt [Q68CL5](https://www.uniprot.org/uniprotkb/Q68CL5) · Ensembl [ENSG00000134779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134779)

## Data

Gene col 5604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5604); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5604]; `tensor/DDL_lfc|DDL_z.npy` [5604]; `embed/gene_vectors.npy` [5604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5604 or target_col == 5604). Every well: [[TPGS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPGS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
