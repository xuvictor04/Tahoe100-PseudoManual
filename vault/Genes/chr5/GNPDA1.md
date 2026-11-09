---
symbol: "GNPDA1"
type: "gene"
col: 3471
ensembl_id: "ENSG00000113552"
name: "glucosamine-6-phosphate deaminase 1"
location: "5q31.3"
module: 124
arm: "+"
pooled_cpm: 34.51
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# GNPDA1

*glucosamine-6-phosphate deaminase 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.60× (z +26.5, q 0e+00, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.119×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.416×; ⚠ cell-cycle shift, explains ~0% of this change); [[AT7519 (drug)]] 5 µM in 1 line (SNU-1 0.0644×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM126B]] (+0.67, fdr 7e-06), [[VPS13C]] (+0.65, fdr 7e-06), [[HPS1]] (+0.65, fdr 1e-05); moves opposite to [[ZMYND19]] (-0.54, fdr 3e-05), [[SIVA1]] (-0.53, fdr 2e-05), [[THOC3]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NNT-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.60×** | +26.5 | 0e+00 | 43/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +15.2 | 0e+00 | 41/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +14.4 | 1e-44 | 29/37 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +13.0 | 1e-36 | 45/47 (PANC-1, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +12.0 | 2e-31 | 39/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.20×** | +11.5 | 9e-29 | 39/48 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.18×** | +11.0 | 4e-26 | 41/48 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.96×** | +9.9 | 4e-21 | 33/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.90×** | +9.4 | 4e-19 | 43/47 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +8.8 | 8e-17 | 39/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +8.5 | 1e-15 | 35/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +8.2 | 1e-14 | 33/47 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +7.8 | 3e-13 | 36/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +7.6 | 1e-12 | 28/44 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.46×** | +6.9 | 2e-10 | 39/48 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 7e-08 | 35/48 (LoVo, HT-29, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +5.9 | 1e-07 | 27/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.2 | 6e-06 | 25/48 (SNU-1, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.42×** | +4.9 | 3e-05 | 28/48 (PANC-1, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 6e-05 | 23/47 (J82, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +4.4 | 2e-04 | 25/47 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3471.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.119×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.416×; ⚠ cell-cycle shift, explains ~0% of this change); [[AT7519 (drug)]] 5 µM in 1 line (SNU-1 0.0644×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.613× | -3.7 | 0.11 | 13/47 (A498, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +17.8) | — |
| [[A-172 (line)]] | wt | 30.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +26.8) | — |
| [[J82 (line)]] | alt | 43.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +22.2) | — |
| [[NCI-H460 (line)]] | wt | 29.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +31.2) | — |
| [[A498 (line)]] | wt | 29.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +16.4) | — |
| [[COLO 205 (line)]] | alt | 40.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +20.6) | — |
| [[HEC-1-A (line)]] | alt | 41.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.86× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 13.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +18.6) | — |
| [[Hs 766T (line)]] | wt | 45.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +21.2) | — |
| [[KATO III (line)]] | alt | 25.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 20.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 36.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +18.3) | — |
| [[RKO (line)]] | wt | 102 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 22.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 15.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +18.7) | — |
| [[LoVo (line)]] | wt | 37.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 57.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +25.1) | — |
| [[SW480 (line)]] | alt | 31.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.7) | — |
| [[A549 (line)]] | wt | 20.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 44.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.39× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +16.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 77.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +17.7) | — |
| [[NCI-H1573 (line)]] | alt | 44.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +17.7) | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +15.1) | — |
| [[A-427 (line)]] | wt | 64.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +15.2) | — |
| [[C32 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +8.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +14.9) | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +13.3) | — |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 1 | — | [[AT7519 (drug)]] 5 µM 0.0644× (z -9.0) |
| [[AN3 CA (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM126B]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[VPS13C]] | +0.65 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[HPS1]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[DUSP3]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GTF2H1]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ATP6V1C1]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RRAGB]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[OSTM1]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[RRAGC-DT]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[HS1BP3]] | +0.60 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[CRYM]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LYRM2]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND19]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[SIVA1]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[THOC3]] | -0.52 | -0.59 / -0.40 | both halves | 4e-05 |  |
| [[GLRX5]] | -0.52 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[CMC2]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[WDFY2]] | -0.50 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[RNF121]] | -0.50 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[MED26]] | -0.50 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[UHRF2]] | -0.50 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[C2CD2L]] | -0.49 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[RECQL4]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[MYCBP]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT-AS1]] | B | NNT-AS1 activity lowers GNPDA1's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.71× higher at baseline in the lines without NNT-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.342). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-17.9, 13.5); signed map (15.5, -14.6). **Vector** length 110, 32.6% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.9 | +13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +12.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +26.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.2 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Afatinib (drug)]] 5 µM |  | +3.8 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | glucosamine-6-phosphate deaminase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,991,749-142,013,041 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GNPDA, HLN, GPI, KIAA0060; previously GNPI |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P46926](https://www.uniprot.org/uniprotkb/P46926) (Glucosamine-6-phosphate deaminase 1):

> Catalyzes the reversible conversion of alpha-D-glucosamine 6-phosphate (GlcN-6P) into beta-D-fructose 6-phosphate (Fru-6P) and ammonium ion, a regulatory reaction step in de novo uridine diphosphate-N-acetyl-alpha-D-glucosamine (UDP-GlcNAc) biosynthesis via hexosamine pathway. Deamination is coupled to aldo-keto isomerization mediating the metabolic flux from UDP-GlcNAc toward Fru-6P. At high ammonium level can drive amination and isomerization of Fru-6P toward hexosamines and UDP-GlcNAc …

**Summary**, from NCBI Gene [10007](https://www.ncbi.nlm.nih.gov/gene/10007):

> Glucosamine-6-phosphate deaminase (EC 3.5.99.6) is an allosteric enzyme that catalyzes the reversible conversion of D-glucosamine-6-phosphate into D-fructose-6-phosphate and ammonium (Arreola et al., 2003 [PubMed 12965206]).[supplied by OMIM, Jan 2010]

**Accessions** — [HGNC:4417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4417) · Entrez [10007](https://www.ncbi.nlm.nih.gov/gene/10007) · UniProt [P46926](https://www.uniprot.org/uniprotkb/P46926) · Ensembl [ENSG00000113552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113552)

## Data

Gene col 3471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3471); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3471]; `tensor/DDL_lfc|DDL_z.npy` [3471]; `embed/gene_vectors.npy` [3471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3471 or target_col == 3471). Every well: [[GNPDA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNPDA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
