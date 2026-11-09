---
symbol: "MYADM"
type: "gene"
col: 11057
ensembl_id: "ENSG00000179820"
name: "myeloid associated differentiation marker"
location: "19q13.42"
module: 161
arm: "+"
pooled_cpm: 138.07
n_lines_expressing: 47
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# MYADM

*myeloid associated differentiation marker* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.09× (z +8.3, q 6e-14, up in 40 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 3.08×, SW480 3.43×, KATO III 4.49×, J82 2.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 2.69×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.330× (z -17.6, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAI2]] (+0.67, fdr 2e-05), [[CALM1]] (+0.62, fdr 2e-05), [[VIM]] (+0.60, fdr 1e-05); moves opposite to [[SMAD1]] (-0.60, fdr 5e-05), [[QRSL1]] (-0.57, fdr 4e-05), [[MTHFSD]] (-0.56, fdr 1e-04).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LGALS1]] → it (grade B ⚠); 7 go from it, the strongest it → [[RPS6KA5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 3.08×, SW480 3.43×, KATO III 4.49×, J82 2.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 2.69×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +8.3 | 6e-14 | 40/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.7 | 5e-09 | 34/40 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +4.5 | 0.001 | 26/42 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 1.35× | +3.2 | 0.17 | 32/45 (SW1417, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.330×** | -17.6 | 0e+00 | 42/44 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.305×** | -13.4 | 3e-38 | 43/44 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -10.8 | 1e-24 | 39/45 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.452×** | -8.9 | 6e-17 | 44/45 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.463×** | -8.2 | 4e-14 | 42/45 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -7.9 | 3e-13 | 39/46 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.514×** | -7.5 | 7e-12 | 41/45 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -6.9 | 4e-10 | 37/45 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.565×** | -6.4 | 9e-09 | 36/45 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.347×** | -6.2 | 3e-08 | 33/42 (H4, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.609×** | -5.6 | 1e-06 | 30/45 (NCI-H23, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.637×** | -5.1 | 2e-05 | 31/45 (A-172, PANC-1, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -5.0 | 3e-05 | 31/45 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.633×** | -4.9 | 3e-05 | 36/46 (SW 1088, SNU-423, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.661×** | -4.6 | 1e-04 | 27/45 (NCI-H23, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.627×** | -3.7 | 0.006 | 33/45 (NCI-H460, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.014 | 31/45 (NCI-H23, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -3.4 | 0.018 | 23/45 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.030 | 21/45 (A-172, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.762×** | -3.0 | 0.057 | 21/45 (A-172, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 517 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0544× (z -38.7) |
| [[H4 (line)]] | wt | 169 | 0 | 14 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -14.1) |
| [[HOP62 (line)]] | alt | 138 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -24.6) |
| [[HS-578T (line)]] | alt | 211 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.0) |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 200 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -22.0) |
| [[PANC-1 (line)]] | alt | 203 | 2 (2 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -15.3) |
| [[J82 (line)]] | alt | 138 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.6) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 180 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.5) |
| [[A549 (line)]] | wt | 297 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 94.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -22.8) |
| [[SNU-423 (line)]] | alt | 129 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.7) |
| [[SW 1088 (line)]] | alt | 256 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.4) |
| [[A-427 (line)]] | wt | 114 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -15.9) |
| [[A498 (line)]] | wt | 283 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -18.4) |
| [[HCT15 (line)]] | alt | 112 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 159 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.4) |
| [[Hs 766T (line)]] | wt | 184 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.250× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 194 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 74.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -21.1) |
| [[RKO (line)]] | wt | 72.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -11.2) |
| [[SW 900 (line)]] | alt | 140 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -9.6) |
| [[SW480 (line)]] | alt | 91.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 131 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.2) |
| [[KATO III (line)]] | alt | 125 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.3) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.210× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.1) |
| [[RPMI-7951 (line)]] | alt | 188 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -12.8) |
| [[AN3 CA (line)]] | alt | 42.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.104× (z -9.3) |
| [[C-33 A (line)]] | alt | 81.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.1) |
| [[HT-29 (line)]] | alt | 157 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 83.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.0) |
| [[SNU-1 (line)]] | wt | 81.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 34.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | +0.67 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[CALM1]] | +0.62 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[VIM]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.59 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[PLP2]] | +0.58 | +0.64 / +0.44 | both halves | 3e-05 | same gene group |
| [[CRIP2]] | +0.58 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[TGFB1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EFHC1]] | +0.56 | +0.42 / +0.30 | both halves | 2e-04 |  |
| [[ECE1]] | +0.56 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[APLP2]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[OSBPL8]] | +0.55 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[RALY]] | +0.55 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD1]] | -0.60 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[QRSL1]] | -0.57 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[MTHFSD]] | -0.56 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[NSMAF]] | -0.54 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[DHRS4]] | -0.53 | -0.46 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[ACTR3C]] | -0.52 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[PSMA3]] | -0.51 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[MIX23]] | -0.51 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[TRAPPC13]] | -0.50 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[LRRC61]] | -0.50 | -0.48 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[KEAP1]] | -0.50 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[SART3]] | -0.50 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[DNAJC11]] | -0.50 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[FAIM]] | -0.50 | -0.50 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS1]] | B | LGALS1 activity raises MYADM's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.42× lower at baseline in the lines without LGALS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[TOP2A]] | B | TOP2A activity raises MYADM's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SERPINE1]] | B | SERPINE1 activity raises MYADM's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.99× lower at baseline in the lines without SERPINE1 | 0.079 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS6KA5]] | C | MYADM activity lowers RPS6KA5's level | lines that do not express MYADM (3) vs lines expressing it (47) | 3.74× higher at baseline in the lines without MYADM | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5 |
| [[STXBP1]] | C | MYADM activity strengthens STXBP1's drug response | lines that do not express MYADM (3) vs lines expressing it (46) | the lines without MYADM respond 0.73× as strongly (z diff +1.84); strongest at Homoharringtonine 5 µM: 0.94x vs 0.46x (z diff +7.3) | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5; target measured in part of the lines; both ways; artifact flags |
| [[ZBED3]] | C | MYADM activity lowers ZBED3's level | lines that do not express MYADM (3) vs lines expressing it (47) | 3.67× higher at baseline in the lines without MYADM | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5 |
| [[GSEC]] | C | MYADM activity strengthens GSEC's drug response | lines that do not express MYADM (3) vs lines expressing it (41) | the lines without MYADM respond 1.19× as strongly (z diff -0.33); strongest at Dinaciclib 0.5 µM: 0.24x vs 1.38x (z diff +5.8) | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5; target measured in part of the lines; both ways; artifact flags |
| [[OGG1]] | C | MYADM's natural level strengthens OGG1's drug response | MYADM's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.34; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[EX229 (drug)]] 0.05 µM | C | MYADM activity lowers the cells' numbers under EX229 0.05 µM (makes them more sensitive) | lines that do not express MYADM (3) vs lines expressing it (45) | the lines without MYADM: 1.34× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5 |
| [[LGALS1]] | C | MYADM activity raises LGALS1's level | lines that do not express MYADM (3) vs lines expressing it (47) | 7.02× lower at baseline in the lines without MYADM | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5 |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.8, 1.7); signed map (-7.8, 41.1). **Vector** length 111, 39.0% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.1 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.0 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.0 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.5 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +0.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.3 | +2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.2 | +1.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.4 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -8.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.9 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | myeloid associated differentiation marker |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:53,864,763-53,876,435 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MARVEL domain containing |
| Matched by | ensembl_id |

UniProt [Q96S97](https://www.uniprot.org/uniprotkb/Q96S97) carries no function annotation.

**Summary**, from NCBI Gene [91663](https://www.ncbi.nlm.nih.gov/gene/91663):

> Involved in several processes, including negative regulation of actin filament polymerization; negative regulation of heterotypic cell-cell adhesion; and positive regulation of substrate adhesion-dependent cell spreading. Located in several cellular components, including cortical actin cytoskeleton; membrane raft; and ruffle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7544) · Entrez [91663](https://www.ncbi.nlm.nih.gov/gene/91663) · UniProt [Q96S97](https://www.uniprot.org/uniprotkb/Q96S97) · Ensembl [ENSG00000179820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179820)

## Data

Gene col 11057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11057); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11057]; `tensor/DDL_lfc|DDL_z.npy` [11057]; `embed/gene_vectors.npy` [11057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11057 or target_col == 11057). Every well: [[MYADM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYADM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
