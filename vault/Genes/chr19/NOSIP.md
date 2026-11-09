---
symbol: "NOSIP"
type: "gene"
col: 6631
ensembl_id: "ENSG00000142546"
name: "nitric oxide synthase interacting protein"
location: "19q13.33"
module: 25
arm: "-"
pooled_cpm: 31.41
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# NOSIP

*nitric oxide synthase interacting protein* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.51× (z +21.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.674× (z -6.1, q 5e-07, down in 25 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.788× (z -3.9, q 0.016, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.112×, Panc 03.27 0.302×, COLO 205 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.0743×, A549 0.196×, KATO III 0.252×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.0852×, SW1417 0.207×, HepG2/C3A 0.147×; ⚠ toxic; transcription drop); [[Hesperidin (drug)]] 5 µM in 1 line (AN3 CA 0.0872×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGP1]] (+0.76, fdr 7e-06), [[ATG4B]] (+0.66, fdr 3e-05), [[RAB5A]] (+0.65, fdr 1e-05); moves opposite to [[MTHFD1]] (-0.67, fdr 7e-06), [[RNASEH2B]] (-0.66, fdr 1e-05), [[SMG7]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.51×** | +21.1 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.16×** | +19.3 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.08×** | +18.9 | 0e+00 | 46/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +11.0 | 4e-26 | 37/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +9.0 | 2e-17 | 34/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +8.0 | 8e-14 | 34/48 (SW480, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.0 | 1e-13 | 34/47 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.9 | 3e-07 | 28/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.1 | 2e-05 | 29/45 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +5.1 | 2e-05 | 28/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 7e-05 | 26/47 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.5 | 3e-04 | 19/48 (KATO III, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 22/48 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.003 | 21/49 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.027 | 12/48 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.045 | 12/48 (SW480, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.070 | 10/47 (HCT15, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.112×, Panc 03.27 0.302×, COLO 205 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.0743×, A549 0.196×, KATO III 0.252×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.0852×, SW1417 0.207×, HepG2/C3A 0.147×; ⚠ toxic; transcription drop); [[Hesperidin (drug)]] 5 µM in 1 line (AN3 CA 0.0872×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.674×** | -6.1 | 5e-07 | 25/40 (hTERT-HPNE, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -4.8 | 4e-04 | 24/47 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -3.9 | 0.016 | 20/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.016 | 21/48 (HS-578T, A-427, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.783×** | -3.8 | 0.016 | 16/48 (NCI-H2347, AN3 CA, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.6 | 0.025 | 16/35 (hTERT-HPNE, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.10 | 14/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.827× | -3.1 | 0.15 | 13/47 (SW 1271, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.829× | -3.0 | 0.15 | 9/47 (NCI-H460, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 46.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 29.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.77× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 34.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.26× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.65× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 24.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.71× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 27.9 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.57× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 49.1 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.07× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +12.5) | — |
| [[A-427 (line)]] | wt | 28.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.4) | — |
| [[A498 (line)]] | wt | 19.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 36.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 21.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 31.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 45.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +11.3) | — |
| [[J82 (line)]] | alt | 26.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 46.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 19.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 21.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.6) | — |
| [[SW480 (line)]] | alt | 38.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +18.3) | — |
| [[AsPC-1 (line)]] | alt | 29.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 39.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0743× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +10.2) | — |
| [[RKO (line)]] | wt | 26.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.71× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 41.9 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0872× (z -10.2) |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 30.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.11× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 75.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.27× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 34.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 24.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGP1]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[ATG4B]] | +0.66 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[RAB5A]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ESCO1]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[CTR9]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SIRT6]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ASL]] | +0.65 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ARID3A]] | +0.64 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[PMM1]] | +0.64 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[BTG1]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[AFMID]] | +0.63 | +0.44 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD1]] | -0.67 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[RNASEH2B]] | -0.66 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[SMG7]] | -0.66 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.65 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[IPO5]] | -0.65 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[NCKAP1]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.64 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[UBQLN4]] | -0.64 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NAA50]] | -0.62 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.62 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.62 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[VMA21]] | -0.61 | -0.54 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.3, -30.5); signed map (-26.6, 13.0). **Vector** length 92.2, 21.8% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +18.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +21.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +19.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +8.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.1 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.2 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nitric oxide synthase interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,555,468-49,590,262 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-25 |
| Gene groups (HGNC) | U-box domain containing; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 1 pathways, smallest: Metabolism of nitric oxide: NOS3 activation and regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y314](https://www.uniprot.org/uniprotkb/Q9Y314) (Nitric oxide synthase-interacting protein):

> E3 ubiquitin-protein ligase that is essential for proper development of the forebrain, the eye, and the face. Catalyzes monoubiquitination of serine/threonine-protein phosphatase 2A (PP2A) catalytic subunit PPP2CA/PPP2CB (By similarity). Negatively regulates nitric oxide production by inducing NOS1 and NOS3 translocation to actin cytoskeleton and inhibiting their enzymatic activity.

**Summary**, from NCBI Gene [51070](https://www.ncbi.nlm.nih.gov/gene/51070):

> The protein encoded by this gene may modulate the activity and localization of nitric oxide synthase (endothelial and neuronal) and thus nitric oxide production. Alternative splicing results in multiple transcript variants that encode the same protein. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:17946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17946) · Entrez [51070](https://www.ncbi.nlm.nih.gov/gene/51070) · UniProt [Q9Y314](https://www.uniprot.org/uniprotkb/Q9Y314) · Ensembl [ENSG00000142546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142546)

## Data

Gene col 6631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6631); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6631]; `tensor/DDL_lfc|DDL_z.npy` [6631]; `embed/gene_vectors.npy` [6631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6631 or target_col == 6631). Every well: [[NOSIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOSIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
