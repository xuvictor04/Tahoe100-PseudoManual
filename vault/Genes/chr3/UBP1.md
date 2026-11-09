---
symbol: "UBP1"
type: "gene"
col: 7729
ensembl_id: "ENSG00000153560"
name: "upstream binding protein 1"
location: "3p22.3"
module: 163
arm: "+"
pooled_cpm: 88.5
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# UBP1

*upstream binding protein 1* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +10.9, q 6e-25, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.786× (z -4.3, q 0.010, down in 24 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SNU-1 0.0859×, SW48 0.179×, A-427 0.334×, SK-MEL-2 0.334×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.328×, SK-MEL-2 0.318×, AsPC-1 0.342×, A549 0.384×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.319×, C-33 A 0.322×, MIA PaCa-2 0.330×, A549 0.387×; ⚠ toxic; transcription drop); [[Flutamide (drug)]] 5 µM in 1 line (SW 1088 0.0841×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF4]] (+0.69, fdr 7e-06), [[MFSD14B]] (+0.66, fdr 7e-06), [[MTRR]] (+0.63, fdr 7e-06); moves opposite to [[FNIP1]] (-0.61, fdr 1e-05), [[BTG1]] (-0.53, fdr 1e-05), [[MRFAP1]] (-0.52, fdr 2e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Minodronic acid (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +10.9 | 6e-25 | 44/49 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +9.3 | 2e-18 | 46/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +9.3 | 2e-18 | 36/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +9.2 | 4e-18 | 43/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.2 | 2e-14 | 42/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +7.7 | 1e-12 | 38/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.0 | 1e-10 | 31/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 2e-08 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +5.6 | 1e-06 | 32/48 (A-172, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.5 | 2e-06 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +5.3 | 6e-06 | 29/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 1e-05 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +5.1 | 1e-05 | 31/48 (SNU-423, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 6e-05 | 26/48 (C32, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.002 | 23/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.017 | 22/48 (J82, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tadalafil (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.037 | 14/48 (LS 180, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7729.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SNU-1 0.0859×, SW48 0.179×, A-427 0.334×, SK-MEL-2 0.334×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.328×, SK-MEL-2 0.318×, AsPC-1 0.342×, A549 0.384×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.319×, C-33 A 0.322×, MIA PaCa-2 0.330×, A549 0.387×; ⚠ toxic; transcription drop); [[Flutamide (drug)]] 5 µM in 1 line (SW 1088 0.0841×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.786×** | -4.3 | 0.010 | 24/49 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.6 | 0.071 | 3/50 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.812×** | -3.6 | 0.071 | 20/44 (LOX-IMVI, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.833× | -3.3 | 0.16 | 17/47 (AN3 CA, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 63.7 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +14.4) | — |
| [[SW480 (line)]] | alt | 109 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +12.3) | — |
| [[KATO III (line)]] | alt | 52.0 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.20× (z +10.0) | — |
| [[LoVo (line)]] | wt | 67.6 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.95× (z +17.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 79.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 72.0 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 80.4 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +10.6) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.24× (z +9.5) | — |
| [[A-427 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 83.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -10.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 76.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.28× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 83.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0859× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 67.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 177 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.37× (z +9.4) | — |
| [[SW48 (line)]] | wt | 112 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.38× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -10.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.76× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 52.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.52× (z +10.2) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 84.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[RKO (line)]] | wt | 121 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.38× (z +8.9) | — |
| [[SW 1088 (line)]] | alt | 70.4 | 0 | 1 | — | [[Flutamide (drug)]] 5 µM 0.0841× (z -8.5) |
| [[A-172 (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 98.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 110 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF4]] | +0.69 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[MFSD14B]] | +0.66 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[MTRR]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.60 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[FAR1]] | +0.59 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[EIF4ENIF1]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ANP32A]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ILKAP]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[RNF138]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GMPS]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNIP1]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[BTG1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[MRFAP1]] | -0.52 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[THAP5]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[WBP2]] | -0.51 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[AFF4]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[FCF1]] | -0.51 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[OSGIN1]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[JUN]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[SRRD]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SQSTM1]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[GEM]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Minodronic acid (drug)]] 0.5 µM | C | UBP1's natural level lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | UBP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.038 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.6, -6.6); signed map (-41.7, -15.4). **Vector** length 89.4, 25.5% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.5 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.5 | +3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +8.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +2.5 | +3.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +0.1 |
|  | [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | +7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | upstream binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:33,388,336-33,441,371 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFCP2L5, LBP-1a |
| Gene groups (HGNC) | Transcription factor CP2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZI7](https://www.uniprot.org/uniprotkb/Q9NZI7) (Upstream-binding protein 1):

> Functions as a transcriptional activator in a promoter context-dependent manner. Modulates the placental expression of CYP11A1. Involved in regulation of the alpha-globin gene in erythroid cells. Activation of the alpha-globin promoter in erythroid cells is via synergistic interaction with TFCP2 (By similarity). Involved in regulation of the alpha-globin gene in erythroid cells. Binds strongly to sequences around the HIV-1 initiation site and weakly over the TATA-box. Represses HIV-1 …

**Summary**, from NCBI Gene [7342](https://www.ncbi.nlm.nih.gov/gene/7342):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in negative regulation of viral transcription and positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12507) · Entrez [7342](https://www.ncbi.nlm.nih.gov/gene/7342) · UniProt [Q9NZI7](https://www.uniprot.org/uniprotkb/Q9NZI7) · Ensembl [ENSG00000153560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153560)

## Data

Gene col 7729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7729); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7729]; `tensor/DDL_lfc|DDL_z.npy` [7729]; `embed/gene_vectors.npy` [7729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7729 or target_col == 7729). Every well: [[UBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
