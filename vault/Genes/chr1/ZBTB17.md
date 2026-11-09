---
symbol: "ZBTB17"
type: "gene"
col: 3842
ensembl_id: "ENSG00000116809"
name: "zinc finger and BTB domain containing 17"
location: "1p36.13"
module: 16
arm: "+"
pooled_cpm: 17.28
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZBTB17

*zinc finger and BTB domain containing 17* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.34× (z +17.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -9.7, q 2e-19, down in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LOX-IMVI 0.0984×, NCI-H2347 0.248×, PANC-1 0.281×, LS 180 0.197×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.119×, HS-578T 0.197×, NCI-H2347 0.311×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.137×); [[Allantoin (drug)]] 0.5 µM in 1 line (SNU-1 0.0941×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.436×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMAP1]] (+0.64, fdr 1e-05), [[RNF40]] (+0.61, fdr 1e-05), [[ZNF780A]] (+0.60, fdr 2e-05); moves opposite to [[GAN]] (-0.56, fdr 1e-05), [[SOS1]] (-0.52, fdr 1e-04), [[CDK13]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF260]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.34×** | +17.4 | 0e+00 | 44/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +17.1 | 0e+00 | 43/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.95×** | +13.1 | 4e-37 | 39/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +12.5 | 7e-34 | 43/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +10.1 | 5e-22 | 41/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +9.6 | 5e-20 | 36/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +8.0 | 9e-14 | 35/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +7.9 | 2e-13 | 32/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +7.3 | 1e-11 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +6.9 | 2e-10 | 32/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +5.8 | 3e-07 | 25/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +5.5 | 2e-06 | 18/37 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.3 | 5e-06 | 24/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.003 | 13/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.009 | 7/48 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.014 | 15/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.067 | 8/44 (COLO 205, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3842.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LOX-IMVI 0.0984×, NCI-H2347 0.248×, PANC-1 0.281×, LS 180 0.197×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.119×, HS-578T 0.197×, NCI-H2347 0.311×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.137×); [[Allantoin (drug)]] 0.5 µM in 1 line (SNU-1 0.0941×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.436×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -9.7 | 2e-19 | 34/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -7.7 | 3e-12 | 25/31 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.642×** | -7.0 | 6e-10 | 25/39 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -4.2 | 0.003 | 23/48 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | 0.813× | -3.3 | 0.13 | 15/47 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.2 | 0.15 | 9/48 (SW480, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.6 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 22.1 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.94× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 14.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +9.7) | — |
| [[SW480 (line)]] | alt | 19.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +10.9) | — |
| [[A-172 (line)]] | wt | 13.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 24.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 18.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 28.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -12.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +8.5) | — |
| [[A498 (line)]] | wt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +14.1) | — |
| [[A549 (line)]] | wt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0691× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -9.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.49× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0984× (z -13.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.2) | — |
| [[RKO (line)]] | wt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -13.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0941× (z -10.3) |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMAP1]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[RNF40]] | +0.61 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ZNF780A]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 | same gene group |
| [[ZNF211]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 | same gene group |
| [[ZNF180]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF527]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 | same gene group |
| [[C15orf39]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[HARS2]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ZSCAN26]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 | same gene group |
| [[DEDD]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KAT5]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TNKS1BP1]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAN]] | -0.56 | -0.53 / -0.63 | both halves | 1e-05 | same gene group |
| [[SOS1]] | -0.52 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[CDK13]] | -0.52 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[METTL21A]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ZCCHC7]] | -0.51 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[WDR49]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ORMDL1]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MIB1]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[C9orf153]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TPP2]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[FCHO2]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[CDK19]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF260]] | C | ZNF260 activity raises ZBTB17's level | lines that do not express ZNF260 (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without ZNF260 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF566, ZNF567 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.4, -2.3); signed map (-12.9, -27.9). **Vector** length 64.9, 11.2% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +17.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +17.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | +3.0 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.7 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | +0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:15,941,869-15,976,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIZ1, pHZ-67; previously ZNF151, ZNF60 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 9 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13105](https://www.uniprot.org/uniprotkb/Q13105) (Zinc finger and BTB domain-containing protein 17):

> Transcription factor that can function as an activator or repressor depending on its binding partners, and by targeting negative regulators of cell cycle progression. Plays a critical role in early lymphocyte development, where it is essential to prevent apoptosis in lymphoid precursors, allowing them to survive in response to IL7 and undergo proper lineage commitment. Has been shown to bind to the promoters of adenovirus major late protein and cyclin D1 and activate transcription. Required for …

**Summary**, from NCBI Gene [7709](https://www.ncbi.nlm.nih.gov/gene/7709):

> This gene encodes a zinc finger protein involved in the regulation of c-myc. The symbol MIZ1 has also been associated with PIAS2 which is a different gene located on chromosome 18. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12936) · Entrez [7709](https://www.ncbi.nlm.nih.gov/gene/7709) · UniProt [Q13105](https://www.uniprot.org/uniprotkb/Q13105) · Ensembl [ENSG00000116809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116809)

## Data

Gene col 3842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3842); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3842]; `tensor/DDL_lfc|DDL_z.npy` [3842]; `embed/gene_vectors.npy` [3842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3842 or target_col == 3842). Every well: [[ZBTB17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
