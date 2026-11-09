---
symbol: "MRPS31"
type: "gene"
col: 2264
ensembl_id: "ENSG00000102738"
name: "mitochondrial ribosomal protein S31"
location: "13q14.11"
module: 12
arm: "+"
pooled_cpm: 36.02
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MRPS31

*mitochondrial ribosomal protein S31* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.03× (z +15.1, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.515× (z -13.6, q 3e-39, down in 27 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.716× (z -7.1, q 1e-10, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2347 0.0959×, Panc 03.27 0.0908×, RPMI-7951 0.0904×, LOX-IMVI 0.136×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.120×, NCI-H2347 0.261×, KATO III 0.298×, HepG2/C3A 0.164×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 3 lines (LS 180 0.224×, NCI-H460 0.392×, COLO 205 0.379×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.310×); [[OTS514 (drug)]] 5 µM in 1 line (HCT15 0.0921×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf131]] (+0.79, fdr 7e-06), [[EBAG9]] (+0.76, fdr 7e-06), [[NKAP]] (+0.74, fdr 7e-06); moves opposite to [[ATP2A2]] (-0.67, fdr 7e-06), [[SMG1P3]] (-0.65, fdr 1e-05), [[TXNDC5]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +15.1 | 0e+00 | 47/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +12.4 | 1e-32 | 40/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +10.1 | 8e-22 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +9.2 | 6e-18 | 37/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +6.9 | 7e-10 | 31/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +6.6 | 4e-09 | 24/48 (HT-29, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +5.8 | 4e-07 | 24/48 (HEC-1-A, LS 180, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +5.7 | 1e-06 | 25/48 (LS 180, COLO 205, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +5.7 | 1e-06 | 19/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +5.3 | 7e-06 | 24/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 12/48 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.9 | 0.005 | 12/48 (COLO 205, RKO, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.20× | +3.7 | 0.009 | 11/48 (HepG2/C3A, HEC-1-A, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +3.3 | 0.043 | 5/48 (A498, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | 1.17× | +3.2 | 0.053 | 18/47 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.056 | 12/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2264.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2347 0.0959×, Panc 03.27 0.0908×, RPMI-7951 0.0904×, LOX-IMVI 0.136×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.120×, NCI-H2347 0.261×, KATO III 0.298×, HepG2/C3A 0.164×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 3 lines (LS 180 0.224×, NCI-H460 0.392×, COLO 205 0.379×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.310×); [[OTS514 (drug)]] 5 µM in 1 line (HCT15 0.0921×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -13.6 | 3e-39 | 27/38 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.574×** | -10.9 | 2e-25 | 31/43 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.606×** | -10.7 | 3e-24 | 36/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -7.4 | 3e-11 | 2/48 (SW48, SW 1088) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.716×** | -7.1 | 1e-10 | 31/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -6.2 | 6e-08 | 28/47 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.770×** | -5.6 | 2e-06 | 22/48 (LS 180, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -5.0 | 5e-05 | 21/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.894× | -3.4 | 0.049 | 9/48 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.900× | -3.2 | 0.089 | 1/48 (Hs 766T) | rises with dose |  |
| [[Quinestrol (drug)]] 0.5 µM |  | 0.864× | -3.1 | 0.095 | 6/48 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.1 | 0.095 | 17/48 (LS 180, SNU-1, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 40.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.224× (z -13.8) |
| [[KATO III (line)]] | alt | 48.7 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -17.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 75.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.379× (z -8.7) |
| [[SW480 (line)]] | alt | 56.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.519× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -22.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 46.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 21.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 43.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0959× (z -25.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.392× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 61.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0908× (z -24.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 57.0 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0921× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -11.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -15.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0988× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0904× (z -18.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf131]] | +0.79 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[NKAP]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[RP9]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[LEO1]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PHAX]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ASB8]] | +0.71 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CEPT1]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[COIL]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2A2]] | -0.67 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.65 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.62 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[AKT1]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SELENON]] | -0.61 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[CAPZB]] | -0.60 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ARHGAP4]] | -0.60 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[CTSZ]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.60 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[EIF4EBP2]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MRPS31's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-39.0, -9.3); signed map (-14.7, -7.8). **Vector** length 103, 24.0% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +15.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +10.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.4 | -10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -13.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.1 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Cinacalcet (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:40,729,128-40,771,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMOGN38, mS31 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q92665](https://www.uniprot.org/uniprotkb/Q92665) carries no function annotation.

**Summary**, from NCBI Gene [10240](https://www.ncbi.nlm.nih.gov/gene/10240):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16632) · Entrez [10240](https://www.ncbi.nlm.nih.gov/gene/10240) · UniProt [Q92665](https://www.uniprot.org/uniprotkb/Q92665) · Ensembl [ENSG00000102738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102738)

## Data

Gene col 2264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2264); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2264]; `tensor/DDL_lfc|DDL_z.npy` [2264]; `embed/gene_vectors.npy` [2264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2264 or target_col == 2264). Every well: [[MRPS31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
