---
symbol: "INTS2"
type: "gene"
col: 2955
ensembl_id: "ENSG00000108506"
name: "integrator complex subunit 2"
location: "17q23.2"
module: 148
arm: "+"
pooled_cpm: 51.83
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# INTS2

*integrator complex subunit 2* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.18× (z +31.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.756× (z -5.4, q 4e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (C-33 A 0.103×, HEC-1-A 0.310×, NCI-H460 0.410×, PANC-1 0.444×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.206×, MIA PaCa-2 0.262×, NCI-H460 0.400×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.0894×, LS 180 0.348×; ⚠ toxic; transcription drop); [[OTS514 (drug)]] 5 µM in 1 line (H4 0.0692×); [[Thymol (drug)]] 0.5 µM in 1 line (Hs 766T 0.316×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX18]] (+0.69, fdr 1e-05), [[MRPL30]] (+0.66, fdr 3e-05), [[ICE2]] (+0.65, fdr 2e-05); moves opposite to [[SNN]] (-0.61, fdr 5e-05), [[CYTH3]] (-0.56, fdr 1e-04), [[SGPP1]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF675]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.18×** | +31.3 | 0e+00 | 47/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +14.3 | 5e-44 | 44/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +11.2 | 1e-26 | 45/48 (J82, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.0 | 1e-13 | 29/48 (HepG2/C3A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +7.3 | 4e-11 | 29/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 1e-05 | 26/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 4e-04 | 28/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.003 | 23/48 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.004 | 22/48 (LoVo, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.012 | 18/47 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.1 | 0.093 | 12/44 (HS-578T, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.11 | 8/48 (C-33 A, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2955.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (C-33 A 0.103×, HEC-1-A 0.310×, NCI-H460 0.410×, PANC-1 0.444×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.206×, MIA PaCa-2 0.262×, NCI-H460 0.400×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.0894×, LS 180 0.348×; ⚠ toxic; transcription drop); [[OTS514 (drug)]] 5 µM in 1 line (H4 0.0692×); [[Thymol (drug)]] 0.5 µM in 1 line (Hs 766T 0.316×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.756×** | -5.4 | 4e-05 | 28/48 (A549, CHP-212, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.776×** | -4.9 | 3e-04 | 25/49 (A-427, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -4.4 | 0.002 | 21/48 (LOX-IMVI, HOP62, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.831×** | -3.6 | 0.050 | 18/47 (hTERT-HPNE, HS-578T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.5 | 0.051 | 18/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.827×** | -3.4 | 0.066 | 22/45 (C-33 A, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.843× | -3.3 | 0.069 | 13/48 (KATO III, SW1417, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.837× | -3.3 | 0.069 | 19/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.891× | -3.2 | 0.10 | 8/48 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.777× | -3.0 | 0.14 | 13/48 (A-427, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.4 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +27.1) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 32.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.15× (z +26.4) | — |
| [[LoVo (line)]] | wt | 38.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +25.4) | — |
| [[HEC-1-A (line)]] | alt | 67.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.9) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -12.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 49.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +22.8) | — |
| [[J82 (line)]] | alt | 46.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.431× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 51.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +24.9) | [[Lonafarnib (drug)]] 5 µM 0.0813× (z -12.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 65.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +27.6) | — |
| [[PANC-1 (line)]] | alt | 54.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +26.3) | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +26.0) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 72.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +22.0) | [[Digitoxin (drug)]] 5 µM 0.494× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 50.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +18.0) | — |
| [[A-427 (line)]] | wt | 59.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0894× (z -23.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 45.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +29.0) | — |
| [[C-33 A (line)]] | alt | 99.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -20.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 47.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +20.3) | — |
| [[CFPAC-1 (line)]] | alt | 53.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.3) | — |
| [[H4 (line)]] | wt | 73.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +11.7) | [[OTS514 (drug)]] 5 µM 0.0692× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 50.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 54.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +22.4) | — |
| [[Hs 766T (line)]] | wt | 35.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.6) | [[Thymol (drug)]] 0.5 µM 0.316× (z -8.9) |
| [[LS 180 (line)]] | wt | 54.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 78.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +19.7) | — |
| [[NCI-H2030 (line)]] | alt | 43.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +24.0) | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.4) | — |
| [[SW 900 (line)]] | alt | 44.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.3) | — |
| [[A549 (line)]] | wt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.7) | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +16.6) | — |
| [[HCT15 (line)]] | alt | 68.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +15.4) | — |
| [[KATO III (line)]] | alt | 70.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 58.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +21.2) | — |
| [[NCI-H2347 (line)]] | alt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[RKO (line)]] | wt | 51.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 44.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +24.6) | — |
| [[SW48 (line)]] | wt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX18]] | +0.69 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[MRPL30]] | +0.66 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[ICE2]] | +0.65 | +0.70 / +0.46 | both halves | 2e-05 | pathway: RNA polymerase II transcribes snRNA genes |
| [[C17orf75]] | +0.64 | +0.70 / +0.37 | both halves | 8e-05 |  |
| [[FUNDC1]] | +0.61 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[INTS14]] | +0.59 | +0.64 / +0.39 | both halves | 6e-05 | same gene group; pathway: RNA polymerase II transcribes snRNA genes; STRING 965 |
| [[GUF1]] | +0.59 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[MCCC2]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[SLC16A9]] | +0.58 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[MIX23]] | +0.58 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[ERAL1]] | +0.58 | +0.66 / +0.30 | both halves | 2e-04 |  |
| [[DCPS]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNN]] | -0.61 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[CYTH3]] | -0.56 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[SGPP1]] | -0.54 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[RPS6KA5]] | -0.52 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[TPST2]] | -0.52 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[GNB2]] | -0.51 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[MFSD12]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CORO7]] | -0.50 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[TSPAN17]] | -0.50 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[STRN]] | -0.50 | -0.58 / -0.20 | both halves | 7e-04 |  |
| [[OTUD7A]] | -0.50 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[LMTK2]] | -0.49 | -0.50 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises INTS2's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.62× lower at baseline in the lines without ZNF675 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-18.9, 7.6); signed map (10.0, -29.1). **Vector** length 106, 26.3% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.6 | +31.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.7 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +14.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.6 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | -0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.0 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:61,865,367-61,928,016 (-) |
| Ensembl biotype | protein_coding |
| Also known as | INT2; previously KIAA1287 |
| Gene groups (HGNC) | Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0H0](https://www.uniprot.org/uniprotkb/Q9H0H0) (Integrator complex subunit 2):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [57508](https://www.ncbi.nlm.nih.gov/gene/57508):

> INTS2 is a subunit of the Integrator complex, which associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690) (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29241) · Entrez [57508](https://www.ncbi.nlm.nih.gov/gene/57508) · UniProt [Q9H0H0](https://www.uniprot.org/uniprotkb/Q9H0H0) · Ensembl [ENSG00000108506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108506)

## Data

Gene col 2955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2955); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2955]; `tensor/DDL_lfc|DDL_z.npy` [2955]; `embed/gene_vectors.npy` [2955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2955 or target_col == 2955). Every well: [[INTS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
