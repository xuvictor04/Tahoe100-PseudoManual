---
symbol: "FLCN"
type: "gene"
col: 7840
ensembl_id: "ENSG00000154803"
name: "folliculin"
location: "17p11.2"
module: 59
arm: "+"
pooled_cpm: 36.93
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# FLCN

*folliculin* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.22× (z +23.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.459× (z -11.0, q 2e-25, down in 39 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (C32 0.0780×, MIA PaCa-2 0.181×, SNU-423 0.206×, A-427 0.181×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-423 0.142×, MIA PaCa-2 0.154×, HCT15 0.0911×, HT-29 0.131×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HT-29 0.0579×, RPMI-7951 0.0708×, NCI-H1792 0.142×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAGC]] (+0.76, fdr 7e-06), [[UAP1L1]] (+0.73, fdr 7e-06), [[NEU1]] (+0.72, fdr 7e-06); moves opposite to [[MACROH2A1]] (-0.59, fdr 1e-05), [[PSMD2]] (-0.57, fdr 1e-05), [[ILF2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.22×** | +23.3 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.17×** | +16.3 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +11.7 | 2e-29 | 42/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +11.3 | 1e-27 | 42/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +10.5 | 1e-23 | 35/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.97×** | +9.5 | 2e-19 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +7.4 | 8e-12 | 36/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.4 | 1e-08 | 39/48 (A498, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +5.5 | 2e-06 | 32/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 2e-05 | 26/48 (Hs 766T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.41×** | +4.8 | 7e-05 | 30/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +4.3 | 7e-04 | 26/49 (NCI-H460, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.78×** | +4.2 | 1e-03 | 22/48 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.001 | 24/48 (H4, J82, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.005 | 23/48 (A498, SW480, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.039 | 20/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.039 | 18/48 (HCT15, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7840.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (C32 0.0780×, MIA PaCa-2 0.181×, SNU-423 0.206×, A-427 0.181×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-423 0.142×, MIA PaCa-2 0.154×, HCT15 0.0911×, HT-29 0.131×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HT-29 0.0579×, RPMI-7951 0.0708×, NCI-H1792 0.142×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -11.0 | 2e-25 | 39/47 (C32, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.476×** | -9.7 | 8e-20 | 31/41 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -6.7 | 3e-09 | 27/38 (HT-29, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.8 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +25.8) | — |
| [[PANC-1 (line)]] | alt | 30.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +19.3) | — |
| [[COLO 205 (line)]] | alt | 62.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 49.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.1 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -14.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 84.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -11.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +17.4) | — |
| [[HS-578T (line)]] | alt | 37.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 32.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.0579× (z -20.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 49.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 98.3 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -15.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 46.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +14.9) | — |
| [[H4 (line)]] | wt | 35.3 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.10× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -11.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 48.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 34.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +15.1) | — |
| [[J82 (line)]] | alt | 40.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 45.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 50.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.0708× (z -18.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 34.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 32.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0780× (z -14.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -13.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 37.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[LoVo (line)]] | wt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +16.3) | — |
| [[RKO (line)]] | wt | 38.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +14.4) | — |
| [[SW480 (line)]] | alt | 36.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +18.4) | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGC]] | +0.76 | +0.79 / +0.73 | both halves | 7e-06 | pathway: Amino acids regulate mTORC1; STRING 999 |
| [[UAP1L1]] | +0.73 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[NEU1]] | +0.72 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[TSC1]] | +0.71 | +0.75 / +0.57 | both halves | 1e-05 | STRING 498 |
| [[TRPM7]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[RRAGC-DT]] | +0.69 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[SAT2]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[FNIP1]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 | same gene group; pathway: Amino acids regulate mTORC1; STRING 999 |
| [[LRRC37B]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[RBM5]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[HPS1]] | +0.61 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TOLLIP]] | +0.61 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PSMD2]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ILF2]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PSMD14]] | -0.57 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[STRAP]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PAFAH1B2]] | -0.56 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[GMPS]] | -0.56 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[TCP1]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NUP93]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.56 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[KIF2A]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.685). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.0, -31.8); signed map (-5.2, 0.4). **Vector** length 118, 35.3% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.4 | +16.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.4 | +5.1 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.3 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.8 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.9 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -9.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -0.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | folliculin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,212,212-17,237,188 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BHD, MGC17998, MGC23445, DENND8B |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFG4](https://www.uniprot.org/uniprotkb/Q8NFG4) (Folliculin):

> Multi-functional protein, involved in both the cellular response to amino acid availability and in the regulation of glycolysis. GTPase-activating protein that plays a key role in the cellular response to amino acid availability through regulation of the non-canonical mTORC1 signaling cascade controlling the MiT/TFE factors TFEB and TFE3. Activates mTORC1 by acting as a GTPase-activating protein: specifically stimulates GTP hydrolysis by RagC/RRAGC or RagD/RRAGD, promoting the conversion to the …

**Summary**, from NCBI Gene [201163](https://www.ncbi.nlm.nih.gov/gene/201163):

> This gene is located within the Smith-Magenis syndrome region on chromosome 17. Mutations in this gene are associated with Birt-Hogg-Dube syndrome, which is characterized by fibrofolliculomas, renal tumors, lung cysts, and pneumothorax. Alternative splicing of this gene results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:27310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27310) · Entrez [201163](https://www.ncbi.nlm.nih.gov/gene/201163) · UniProt [Q8NFG4](https://www.uniprot.org/uniprotkb/Q8NFG4) · Ensembl [ENSG00000154803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154803)

## Data

Gene col 7840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7840); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7840]; `tensor/DDL_lfc|DDL_z.npy` [7840]; `embed/gene_vectors.npy` [7840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7840 or target_col == 7840). Every well: [[FLCN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLCN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
