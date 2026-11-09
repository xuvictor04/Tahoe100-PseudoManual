---
symbol: "ATIC"
type: "gene"
col: 6159
ensembl_id: "ENSG00000138363"
name: "5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase"
location: "2q35"
module: 4
arm: "+"
pooled_cpm: 38.29
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ATIC

*5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.27× (z +18.8, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.72× (z +8.5, q 1e-15, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.666× (z -9.2, q 3e-17, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FARSB]] (+0.85, fdr 7e-06), [[RUVBL1]] (+0.82, fdr 7e-06), [[C1QBP]] (+0.79, fdr 7e-06); moves opposite to [[SELENOK]] (-0.76, fdr 7e-06), [[AAMDC]] (-0.72, fdr 7e-06), [[GABARAPL2]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KRT7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.27×** | +18.8 | 0e+00 | 44/45 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +16.3 | 0e+00 | 39/41 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +11.8 | 9e-30 | 38/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +8.8 | 3e-16 | 44/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +8.5 | 1e-15 | 35/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.8 | 5e-07 | 27/47 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +5.8 | 5e-07 | 27/47 (NCI-H1792, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 6e-06 | 29/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.40×** | +5.2 | 1e-05 | 25/47 (NCI-H1573, RPMI-7951, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.86×** | +5.2 | 1e-05 | 24/47 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.38×** | +4.9 | 6e-05 | 22/48 (H4, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +4.5 | 3e-04 | 27/48 (NCI-H460, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.19× | +3.9 | 0.003 | 23/48 (A549, PANC-1, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.003 | 16/46 (MIA PaCa-2, J82, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.9 | 0.003 | 0/48 | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.004 | 18/47 (NCI-H460, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.007 | 21/47 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.012 | 11/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.015 | 17/47 (Panc 03.27, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.017 | 15/47 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lopinavir (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.017 | 11/47 (CFPAC-1, PANC-1, …) | rises with dose | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.040 | 8/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.085 | 16/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -9.2 | 3e-17 | 36/48 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.772×** | -4.3 | 0.004 | 20/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.771×** | -4.1 | 0.006 | 19/47 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.776×** | -3.9 | 0.014 | 17/47 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.656×** | -3.5 | 0.051 | 17/46 (HCT15, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.060 | 18/48 (SW48, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | 0.687× | -3.1 | 0.13 | 13/48 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.13 | 15/48 (NCI-H23, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | 0.821× | -3.0 | 0.14 | 13/47 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.875× | -3.0 | 0.14 | 16/48 (KATO III, NCI-H1792, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 53.0 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -12.8) |
| [[HOP62 (line)]] | alt | 18.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 62.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +10.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.9) |
| [[RKO (line)]] | wt | 56.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -18.0) |
| [[SNU-1 (line)]] | wt | 54.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.334× (z -11.2) |
| [[SW480 (line)]] | alt | 62.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +13.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.454× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +13.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 41.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +14.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 22.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +11.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 47.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 26.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +8.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0626× (z -18.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.40× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 60.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.85× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 76.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 19.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.49× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 76.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -9.0) |
| [[A-172 (line)]] | wt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 69.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0738× (z -8.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.12× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.71× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +8.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | +0.85 | +0.83 / +0.89 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.82 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[C1QBP]] | +0.79 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[SF3B3]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[PFAS]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 | same gene group; pathway: Metabolism of nucleotides; STRING 819 |
| [[RIOX2]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.76 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.76 | +0.72 / +0.85 | both halves | 7e-06 |  |
| [[NAA15]] | +0.76 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.75 | +0.70 / +0.80 | both halves | 7e-06 | STRING 998 |
| [[MAK16]] | +0.75 | +0.72 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.76 | -0.61 / -0.78 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.72 | -0.64 / -0.70 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.71 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[BSDC1]] | -0.71 | -0.64 / -0.73 | both halves | 7e-06 |  |
| [[SIRT2]] | -0.70 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[RABAC1]] | -0.70 | -0.68 / -0.70 | both halves | 7e-06 |  |
| [[STX5]] | -0.69 | -0.70 / -0.66 | both halves | 7e-06 |  |
| [[PHF1]] | -0.68 | -0.66 / -0.74 | both halves | 7e-06 |  |
| [[ULK1]] | -0.67 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.66 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.66 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[KLC4]] | -0.66 | -0.58 / -0.73 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT7]] | B | KRT7 activity lowers ATIC's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.45× higher at baseline in the lines without KRT7 | 0.011 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[NUP210]] | B | NUP210 activity raises ATIC's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without NUP210 | 0.031 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers ATIC's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without HLA-F-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[KRT7]] | B | KRT7 activity strengthens ATIC's drug response | lines that do not express KRT7 (34) vs lines expressing it (14) | the lines without KRT7 respond 0.78× as strongly (z diff +0.62); strongest at Homoharringtonine 0.5 µM: 1.34x vs 2.22x (z diff +3.1) | 0.086 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.850). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.4, -34.9); signed map (-6.8, -45.7). **Vector** length 122, 36.8% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.59 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.56 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +8.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:215,311,956-215,349,773 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PURH, AICARFT, IMPCHASE |
| Gene groups (HGNC) | Purinosome |
| Reactome | 6 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Signaling by ALK fusions and activated point mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P31939](https://www.uniprot.org/uniprotkb/P31939) (Bifunctional purine biosynthesis protein ATIC):

> Bifunctional enzyme that catalyzes the last two steps of purine biosynthesis. Acts as a transformylase that incorporates a formyl group to the AMP analog AICAR (5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide) to produce the intermediate formyl-AICAR (FAICAR). Can use both 10-formyldihydrofolate and 10-formyltetrahydrofolate as the formyl donor in this reaction. Also catalyzes the cyclization of FAICAR to inosine monophosphate (IMP). Is able to convert thio-AICAR to 6-mercaptopurine …

**Summary**, from NCBI Gene [471](https://www.ncbi.nlm.nih.gov/gene/471):

> This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:794) · Entrez [471](https://www.ncbi.nlm.nih.gov/gene/471) · UniProt [P31939](https://www.uniprot.org/uniprotkb/P31939) · Ensembl [ENSG00000138363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138363)

## Data

Gene col 6159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6159); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6159]; `tensor/DDL_lfc|DDL_z.npy` [6159]; `embed/gene_vectors.npy` [6159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6159 or target_col == 6159). Every well: [[ATIC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATIC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
