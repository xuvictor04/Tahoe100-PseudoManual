---
symbol: "IARS2"
type: "gene"
col: 867
ensembl_id: "ENSG00000067704"
name: "isoleucyl-tRNA synthetase 2, mitochondrial"
location: "1q41"
module: 57
arm: "+"
pooled_cpm: 106.17
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# IARS2

*isoleucyl-tRNA synthetase 2, mitochondrial* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +13.3, q 1e-37, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 2.99×, NCI-H1792 3.60×, LoVo 3.14×, NCI-H2030 2.53×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 3.13×, NCI-H460 2.62×, MIA PaCa-2 2.65×, HT-29 3.18×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -28.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEBP1]] (+0.69, fdr 7e-06), [[KDM1A]] (+0.68, fdr 7e-06), [[ERMP1]] (+0.67, fdr 7e-06); moves opposite to [[IER5]] (-0.63, fdr 1e-05), [[TUT7]] (-0.59, fdr 1e-05), [[MOB3C]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAH17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 867.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 2.99×, NCI-H1792 3.60×, LoVo 3.14×, NCI-H2030 2.53×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 3.13×, NCI-H460 2.62×, MIA PaCa-2 2.65×, HT-29 3.18×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +13.3 | 1e-37 | 45/49 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +11.6 | 8e-29 | 38/44 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +7.3 | 5e-11 | 36/45 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.60×** | +5.0 | 6e-05 | 35/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.0 | 6e-05 | 0/50 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.6 | 0.027 | 13/48 (HS-578T, AsPC-1, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.371×** | -28.5 | 0e+00 | 48/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.471×** | -14.7 | 0e+00 | 46/48 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -9.5 | 5e-19 | 41/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -7.4 | 2e-11 | 35/48 (C32, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.695×** | -5.3 | 1e-05 | 31/48 (J82, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.773×** | -5.2 | 2e-05 | 27/48 (SW 900, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.779×** | -5.1 | 3e-05 | 27/48 (SW 900, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.784×** | -4.9 | 6e-05 | 25/48 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.778×** | -4.9 | 6e-05 | 30/47 (SHP-77, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.795×** | -4.6 | 2e-04 | 25/48 (SNU-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.811×** | -4.2 | 0.001 | 25/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.814×** | -4.2 | 0.001 | 22/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.816×** | -4.1 | 0.002 | 28/48 (J82, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.004 | 21/48 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.705×** | -3.7 | 0.008 | 19/45 (HEC-1-A, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **0.831×** | -3.6 | 0.010 | 20/48 (NCI-H2030, A498, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.852× | -3.2 | 0.035 | 21/48 (LS 180, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 159 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -27.7) |
| [[BT-474 (line)]] | alt | 71.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 161 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -26.6) |
| [[SNU-1 (line)]] | wt | 124 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -17.8) |
| [[SW 900 (line)]] | alt | 148 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -26.2) |
| [[A549 (line)]] | wt | 108 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -14.4) |
| [[C32 (line)]] | wt | 138 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -22.5) |
| [[A-172 (line)]] | wt | 133 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -25.8) |
| [[HEC-1-A (line)]] | alt | 118 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -18.4) |
| [[LS 180 (line)]] | wt | 95.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -19.4) |
| [[PANC-1 (line)]] | alt | 115 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -16.7) |
| [[A498 (line)]] | wt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.602× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 72.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.9) |
| [[Hs 766T (line)]] | wt | 120 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -23.5) |
| [[HT-29 (line)]] | alt | 63.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.2) |
| [[KATO III (line)]] | alt | 82.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 85.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 87.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 119 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -21.6) |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -20.1) |
| [[SHP-77 (line)]] | alt | 118 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.63× (z +10.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.425× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.4) |
| [[A-427 (line)]] | wt | 130 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -11.5) |
| [[COLO 205 (line)]] | alt | 59.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -16.2) |
| [[HS-578T (line)]] | alt | 57.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -12.7) |
| [[J82 (line)]] | alt | 90.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -25.7) |
| [[NCI-H1792 (line)]] | alt | 93.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.330× (z -12.4) |
| [[SNU-423 (line)]] | alt | 96.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -21.6) |
| [[SW480 (line)]] | alt | 86.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -12.5) |
| [[C-33 A (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 93.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -22.6) |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.5) |
| [[HCT15 (line)]] | alt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 91.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -15.4) |
| [[HOP62 (line)]] | alt | 96.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -23.5) |
| [[hTERT-HPNE (line)]] | wt | 76.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 91.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 95.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 83.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.8) |
| [[SW1417 (line)]] | alt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -10.9) |
| [[SW48 (line)]] | wt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.3) |
| [[AN3 CA (line)]] | alt | 123 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEBP1]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[KDM1A]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MDH1]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[LNPK]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[BBS2]] | +0.63 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[MIGA1]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ATP5F1A]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 | pathway: Mitochondrial protein degradation; STRING 491 |
| [[ERLIN1]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LANCL1]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[RNPEP]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[TUT7]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MOB3C]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CACNG8]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CLCF1]] | -0.57 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[CDK3]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZNF274]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MIDN]] | -0.55 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[ISG20]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CEACAM19]] | -0.54 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[MATN1-AS1]] | -0.54 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[FMNL1-DT]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH17]] | B | DNAH17 activity lowers IARS2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.13× higher at baseline in the lines without DNAH17 | 0.070 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.3, -12.4); signed map (-36.3, -15.5). **Vector** length 116, 36.5% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.0 | +3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.0 | +5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +0.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.2 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -28.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -4.9 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -9.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -1.2 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | isoleucyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:220,094,132-220,148,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10326 |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 4 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSE4](https://www.uniprot.org/uniprotkb/Q9NSE4) (Isoleucine--tRNA ligase, mitochondrial):

> Aminoacyl-tRNA synthetase that catalyzes the specific attachment of isoleucine to its cognate tRNA (tRNA(Ile)).

**Summary**, from NCBI Gene [55699](https://www.ncbi.nlm.nih.gov/gene/55699):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes the mitochondrial isoleucine-tRNA synthetase which belongs to the class-I aminoacyl-tRNA synthetase …

**Accessions** — [HGNC:29685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29685) · Entrez [55699](https://www.ncbi.nlm.nih.gov/gene/55699) · UniProt [Q9NSE4](https://www.uniprot.org/uniprotkb/Q9NSE4) · Ensembl [ENSG00000067704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067704)

## Data

Gene col 867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 867); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 867]; `tensor/DDL_lfc|DDL_z.npy` [867]; `embed/gene_vectors.npy` [867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 867 or target_col == 867). Every well: [[IARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
