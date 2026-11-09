---
symbol: "TBC1D32"
type: "gene"
col: 7084
ensembl_id: "ENSG00000146350"
name: "TBC1 domain family member 32"
location: "6q22.31"
module: 17
arm: "+"
pooled_cpm: 98.83
n_lines_expressing: 46
n_dd_up: 4
n_dd_down: 42
n_dd_up_clean: 3
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TBC1D32

*TBC1 domain family member 32* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.36× (z +4.7, q 0.002, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.276× (z -28.4, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H12B]] (+0.54, fdr 1e-04), [[SPATA6]] (+0.53, fdr 1e-05), [[CCDC7]] (+0.52, fdr 3e-05); moves opposite to [[MGLL]] (-0.50, fdr 5e-05), [[TLNRD1]] (-0.48, fdr 5e-05), [[CAB39]] (-0.48, fdr 7e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 3 go from it, the strongest it → [[SPATA6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.7 | 0.002 | 28/43 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 0.004 | 23/45 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.005 | 25/43 (C32, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.25×** | +3.5 | 0.077 | 21/46 (NCI-H596, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.12 | 12/44 (A-427, SK-MEL-2, …) | all doses, flat |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.14 | 15/45 (C-33 A, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.18 | 16/45 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.18 | 14/44 (LS 180, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.276×** | -28.4 | 0e+00 | 43/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.251×** | -21.6 | 0e+00 | 43/44 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.269×** | -20.5 | 0e+00 | 43/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.309×** | -18.4 | 0e+00 | 43/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.318×** | -17.2 | 0e+00 | 43/44 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.340×** | -16.9 | 0e+00 | 43/44 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.377×** | -15.2 | 0e+00 | 42/44 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -13.7 | 5e-41 | 36/45 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.414×** | -13.2 | 3e-38 | 39/43 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.411×** | -12.8 | 7e-36 | 36/41 (PANC-1, A-427, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.477×** | -11.5 | 4e-29 | 35/44 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.463×** | -11.4 | 2e-28 | 39/45 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -11.2 | 1e-27 | 43/45 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.477×** | -11.1 | 4e-27 | 36/40 (A-427, H4, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.479×** | -11.0 | 9e-27 | 36/44 (HEC-1-A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.505×** | -10.1 | 1e-22 | 36/44 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.520×** | -9.8 | 3e-21 | 37/46 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.543×** | -9.5 | 5e-20 | 38/44 (SW480, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.570×** | -8.8 | 5e-17 | 37/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -7.5 | 1e-12 | 36/44 (LOX-IMVI, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.2 | 0 | 21 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -26.5) |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 20 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -19.8) |
| [[MIA PaCa-2 (line)]] | alt | 146 | 0 | 20 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -24.6) |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 19 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -20.0) |
| [[H4 (line)]] | wt | 85.2 | 0 | 17 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0599× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0924× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 156 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -46.1) |
| [[HEC-1-A (line)]] | alt | 90.9 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -23.5) |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -18.7) |
| [[PANC-1 (line)]] | alt | 213 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -22.9) |
| [[SNU-423 (line)]] | alt | 122 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -19.9) |
| [[SW480 (line)]] | alt | 75.0 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0809× (z -23.8) |
| [[A-172 (line)]] | wt | 75.1 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.205× (z -13.7) |
| [[Hs 766T (line)]] | wt | 127 | 0 | 11 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.196× (z -14.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 80.8 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -18.5) |
| [[HOP62 (line)]] | alt | 75.1 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.179× (z -16.2) |
| [[LS 180 (line)]] | wt | 68.8 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.245× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 135 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -28.3) |
| [[SW 900 (line)]] | alt | 73.2 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.6) |
| [[A-427 (line)]] | wt | 258 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0371× (z -39.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -13.2) |
| [[A549 (line)]] | wt | 55.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -21.8) |
| [[C32 (line)]] | wt | 74.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -19.0) |
| [[LoVo (line)]] | wt | 96.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -21.9) |
| [[NCI-H23 (line)]] | alt | 161 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -24.7) |
| [[SNU-1 (line)]] | wt | 164 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.279× (z -11.7) |
| [[A498 (line)]] | wt | 85.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -25.9) |
| [[COLO 205 (line)]] | alt | 50.7 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -15.3) |
| [[HS-578T (line)]] | alt | 88.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -17.3) |
| [[HT-29 (line)]] | alt | 76.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.9) |
| [[J82 (line)]] | alt | 71.4 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.8) |
| [[RKO (line)]] | wt | 55.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.7) |
| [[C-33 A (line)]] | alt | 487 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 77.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -10.2) |
| [[HCT15 (line)]] | alt | 89.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.1) |
| [[SW1417 (line)]] | alt | 45.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -16.9) |
| [[BT-474 (line)]] | alt | 77.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.0) |
| [[SHP-77 (line)]] | alt | 64.4 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.260× (z -11.8) |
| [[SW48 (line)]] | wt | 84.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.3) |
| [[AN3 CA (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0735× (z -13.4) |
| [[SW 1088 (line)]] | alt | 146 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0687× (z -10.5) |
| [[CHP-212 (line)]] | wt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.0) |
| [[SW 1271 (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0858× (z -12.5) ⚠ transcription drop; cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -9.6) |
| [[NCI-H596 (line)]] | alt | 97.2 | 1 | 0 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 2.13× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H12B]] | +0.54 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[SPATA6]] | +0.53 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CCDC7]] | +0.52 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TMEM67]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 | STRING 506 |
| [[CDC73]] | +0.50 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[MAGEA3-DT]] | +0.50 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[DYNC2H1]] | +0.50 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[WDPCP]] | +0.49 | +0.43 / +0.48 | both halves | 3e-05 | STRING 653 |
| [[POT1]] | +0.49 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[BABAM2]] | +0.48 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[MBD5]] | +0.48 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LINC01473]] | +0.48 | +0.37 / +0.53 | both halves | 9e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGLL]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TLNRD1]] | -0.48 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[CAB39]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 | same gene group |
| [[TRIM8]] | -0.46 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[RAPH1]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RASSF3]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[DUSP22]] | -0.43 | -0.21 / -0.48 | both halves | 6e-04 |  |
| [[TEP1]] | -0.43 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[LTO1]] | -0.43 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[PDCD6P1]] | -0.43 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[TTC9]] | -0.43 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[RUBCN]] | -0.43 | -0.38 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TBC1D32's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CCDC102B]] | B | CCDC102B activity raises TBC1D32's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 2.65× lower at baseline in the lines without CCDC102B | 0.042 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers TBC1D32's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[GXYLT2]] | B | GXYLT2 activity raises TBC1D32's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without GXYLT2 | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[PRKN]] | B | PRKN activity raises TBC1D32's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without PRKN | 0.078 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[CCDC171]] | C | CCDC171 activity raises TBC1D32's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA6]] | C | TBC1D32 activity raises SPATA6's level | lines that do not express TBC1D32 (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without TBC1D32 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ACOT12, ENSG00000271590, ENSG00000288545; co-absent with the target; its own permutation p |
| [[RPGRIP1L]] | C | TBC1D32 activity raises RPGRIP1L's level | lines that do not express TBC1D32 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without TBC1D32 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ACOT12, ENSG00000271590, ENSG00000288545 |
| [[SDR16C5]] | C | TBC1D32 activity lowers SDR16C5's level | lines that do not express TBC1D32 (4) vs lines expressing it (46) | 3.55× higher at baseline in the lines without TBC1D32 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ACOT12, ENSG00000271590, ENSG00000288545 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.351). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.5, 32.7); signed map (-27.1, -10.8). **Vector** length 72.4, 24.1% of its response variance represented; |z| ≥ 3 in 1,655 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.6 | -21.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | -0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -13.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.0 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -3.3 | -11.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.2 | -5.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.0 | -5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:121,079,494-121,334,745 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30899, dJ310J6.1, FLJ34235, bA57L9.1, BROMI; previously C6orf171, C6orf170 |
| Gene groups (HGNC) | Armadillo like helical domain containing; TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NH3](https://www.uniprot.org/uniprotkb/Q96NH3) (Protein broad-minded):

> Required for high-level Shh responses in the developing neural tube. Together with CDK20, controls the structure of the primary cilium by coordinating assembly of the ciliary membrane and axoneme, allowing GLI2 to be properly activated in response to Shh signaling (By similarity).

**Summary**, from NCBI Gene [221322](https://www.ncbi.nlm.nih.gov/gene/221322):

> This gene encodes a TBC-domain containing protein. Studies of a similar protein in mouse and zebrafish suggest that the encoded protein is involved in sonic hedgehog signaling, and that it interacts with and stabilizes cell cycle-related kinase. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:21485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21485) · Entrez [221322](https://www.ncbi.nlm.nih.gov/gene/221322) · UniProt [Q96NH3](https://www.uniprot.org/uniprotkb/Q96NH3) · Ensembl [ENSG00000146350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146350)

## Data

Gene col 7084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7084); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7084]; `tensor/DDL_lfc|DDL_z.npy` [7084]; `embed/gene_vectors.npy` [7084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7084 or target_col == 7084). Every well: [[TBC1D32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
