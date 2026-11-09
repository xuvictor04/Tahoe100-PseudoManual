---
symbol: "ZBTB40"
type: "gene"
col: 11566
ensembl_id: "ENSG00000184677"
name: "zinc finger and BTB domain containing 40"
location: "1p36.12"
module: 7
arm: "+"
pooled_cpm: 38.99
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZBTB40

*zinc finger and BTB domain containing 40* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.69× (z +20.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.673× (z -7.7, q 7e-12, down in 25 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.190×, A549 0.306×, SW 900 0.285×, H4 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.175×, A-427 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.270×, SW480 0.458×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (BT-474 0.104×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0802×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (SW 1271 0.0714×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED1]] (+0.70, fdr 1e-05), [[ZNF24]] (+0.70, fdr 1e-05), [[ZC3HC1]] (+0.67, fdr 1e-05); moves opposite to [[PPP1R2]] (-0.63, fdr 1e-05), [[IDH2]] (-0.60, fdr 2e-05), [[APAF1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CARD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.69×** | +20.8 | 0e+00 | 46/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +19.3 | 0e+00 | 39/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.16×** | +16.2 | 0e+00 | 45/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.03×** | +14.9 | 0e+00 | 47/48 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +13.1 | 3e-37 | 41/47 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +12.5 | 4e-34 | 41/48 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +12.2 | 2e-32 | 37/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +9.7 | 2e-20 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +8.4 | 3e-15 | 32/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +8.3 | 5e-15 | 40/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +8.2 | 1e-14 | 32/48 (SNU-423, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +7.6 | 1e-12 | 32/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +7.5 | 4e-12 | 38/48 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +7.2 | 3e-11 | 31/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +7.1 | 5e-11 | 29/48 (LoVo, KATO III, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +6.6 | 2e-09 | 33/47 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +6.2 | 2e-08 | 30/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11566.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.190×, A549 0.306×, SW 900 0.285×, H4 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.175×, A-427 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.270×, SW480 0.458×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (BT-474 0.104×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0802×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (SW 1271 0.0714×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -7.7 | 7e-12 | 25/44 (RKO, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.739×** | -6.4 | 5e-08 | 27/47 (SNU-1, A549, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Erythromycin (drug)]] 5 µM |  | 0.861× | -3.2 | 0.30 | 9/48 (HEC-1-A, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.2 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[NCI-H460 (line)]] | wt | 41.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +19.0) | — |
| [[BT-474 (line)]] | alt | 28.7 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.86× (z +11.7) | [[Oxaprozin (drug)]] 0.5 µM 0.104× (z -15.1) |
| [[KATO III (line)]] | alt | 42.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[PANC-1 (line)]] | alt | 51.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -8.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 69.3 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -16.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 67.9 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 4.12× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 28.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +13.9) | — |
| [[LoVo (line)]] | wt | 37.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +14.9) | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 54.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.64× (z +16.4) | — |
| [[H4 (line)]] | wt | 39.8 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 33.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +13.1) | — |
| [[SNU-1 (line)]] | wt | 44.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 29.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.2) | — |
| [[A549 (line)]] | wt | 34.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -10.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +14.5) | — |
| [[J82 (line)]] | alt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 40.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.1) | — |
| [[A-427 (line)]] | wt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -15.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 45.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.131× (z -12.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 41.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 58.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.8) | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0802× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 30.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.9) | — |
| [[SW 1271 (line)]] | alt | 49.6 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0714× (z -9.1) |
| [[SW 900 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 37.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +8.5) | — |
| [[SW48 (line)]] | wt | 45.7 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.273× (z -8.6) |
| [[AN3 CA (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | +0.70 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[ZNF24]] | +0.70 | +0.63 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZC3HC1]] | +0.67 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ASXL2]] | +0.67 | +0.72 / +0.45 | both halves | 3e-05 | STRING 434 |
| [[C11orf58]] | +0.67 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[TAF7]] | +0.65 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[ATXN10]] | +0.65 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[WDR82]] | +0.65 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[MRM3]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 | same gene group |
| [[SON]] | +0.64 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[SMCR8]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R2]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[IDH2]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[APAF1]] | -0.60 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CARD19]] | -0.59 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[PRRC1]] | -0.58 | -0.69 / -0.26 | both halves | 4e-04 |  |
| [[GMCL1]] | -0.58 | -0.54 / -0.49 | both halves | 1e-05 | same gene group |
| [[ARL3]] | -0.57 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MED26]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CBLB]] | -0.57 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[POGLUT2]] | -0.57 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[TMEM50B]] | -0.56 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[ETHE1]] | -0.56 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD6]] | B | CARD6 activity lowers ZBTB40's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.33× higher at baseline in the lines without CARD6 | 0.037 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises ZBTB40's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.66× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-30.0, 12.5); signed map (5.0, -28.4). **Vector** length 94.7, 23.3% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.4 | +16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +12.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.0 | +20.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.5 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +8.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | +6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:22,428,838-22,531,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0478, ZNF923 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUA8](https://www.uniprot.org/uniprotkb/Q9NUA8) (Zinc finger and BTB domain-containing protein 40):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [9923](https://www.ncbi.nlm.nih.gov/gene/9923):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific. Involved in DNA damage response. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29045) · Entrez [9923](https://www.ncbi.nlm.nih.gov/gene/9923) · UniProt [Q9NUA8](https://www.uniprot.org/uniprotkb/Q9NUA8) · Ensembl [ENSG00000184677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184677)

## Data

Gene col 11566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11566); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11566]; `tensor/DDL_lfc|DDL_z.npy` [11566]; `embed/gene_vectors.npy` [11566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11566 or target_col == 11566). Every well: [[ZBTB40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
