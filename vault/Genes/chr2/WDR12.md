---
symbol: "WDR12"
type: "gene"
col: 6177
ensembl_id: "ENSG00000138442"
name: "WD repeat domain 12"
location: "2q33.2"
module: 18
arm: "+"
pooled_cpm: 38.51
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# WDR12

*WD repeat domain 12* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +19.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.772× (z -5.9, q 2e-06, down in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~16% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.827× (z -4.5, q 0.001, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.506×, SW480 0.601×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.261×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (AN3 CA 0.165×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX33]] (+0.73, fdr 7e-06), [[ADAT2]] (+0.71, fdr 7e-06), [[HEATR1]] (+0.70, fdr 7e-06); moves opposite to [[DCTN3]] (-0.54, fdr 4e-05), [[CDKN2D]] (-0.54, fdr 4e-05), [[OAZ1]] (-0.53, fdr 7e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LTBR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +19.5 | 0e+00 | 43/48 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.99×** | +16.5 | 0e+00 | 36/45 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +14.8 | 0e+00 | 33/41 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +13.7 | 2e-40 | 40/47 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +9.6 | 1e-19 | 33/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +9.3 | 2e-18 | 34/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +8.7 | 2e-16 | 29/48 (NCI-H2347, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.44×** | +8.1 | 4e-14 | 28/45 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.83×** | +7.5 | 3e-12 | 36/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +7.4 | 9e-12 | 23/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.31×** | +6.2 | 3e-08 | 27/47 (A-172, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +6.2 | 3e-08 | 24/48 (LOX-IMVI, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +6.2 | 3e-08 | 23/47 (J82, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +6.0 | 7e-08 | 24/47 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.27×** | +5.8 | 3e-07 | 22/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +5.4 | 2e-06 | 19/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +5.1 | 1e-05 | 18/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.9 | 3e-05 | 22/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +4.6 | 1e-04 | 18/47 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +4.4 | 2e-04 | 16/48 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +4.2 | 7e-04 | 12/47 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.004 | 7/48 (NCI-H460, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.010 | 9/48 (NCI-H460, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.011 | 10/48 (NCI-H1792, H4, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6177.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.506×, SW480 0.601×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.261×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (AN3 CA 0.165×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.772×** | -5.9 | 2e-06 | 21/47 (LOX-IMVI, NCI-H661, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -5.2 | 5e-05 | 1/48 (SW 1271) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.827×** | -4.5 | 0.001 | 15/47 (SW480, HCT15, …) | rises with dose | low cells (technical?) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.894× | -3.8 | 0.024 | 9/49 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.859× | -3.6 | 0.034 | 7/47 (LoVo, LS 180, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.900× | -3.5 | 0.039 | 11/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.886× | -3.4 | 0.057 | 12/48 (A-427, AN3 CA, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.0 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +20.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 20.9 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +13.5) | — |
| [[A-172 (line)]] | wt | 23.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.0) | — |
| [[SW480 (line)]] | alt | 60.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 20.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.0) | — |
| [[J82 (line)]] | alt | 34.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 26.7 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.23× (z +9.8) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 53.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 46.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.3) | — |
| [[A498 (line)]] | wt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 29.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 57.0 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.165× (z -9.2) |
| [[C-33 A (line)]] | alt | 55.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.261× (z -10.5) |
| [[C32 (line)]] | wt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 37.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +14.5) | — |
| [[Hs 766T (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.03× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.8) | — |
| [[A-427 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX33]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.70 | +0.71 / +0.76 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 908 |
| [[MDN1]] | +0.69 | +0.74 / +0.73 | both halves | 7e-06 | STRING 994 |
| [[MRPS25]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[DTD2]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ECHDC1]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[CTTN-DT]] | +0.65 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[TUBGCP4]] | +0.64 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[PUM3]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 | STRING 875 |
| [[ANAPC1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DDX31]] | +0.62 | +0.65 / +0.67 | both halves | 7e-06 | STRING 874 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN3]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CDKN2D]] | -0.54 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[OAZ1]] | -0.53 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBR]] | B | LTBR activity lowers WDR12's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.54× higher at baseline in the lines without LTBR | 0.029 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[TOP2A]] | B | TOP2A activity lowers WDR12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TUBA1A]] | B | TUBA1A activity raises WDR12's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without TUBA1A | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[SLC9B2]] | C | SLC9B2 activity raises WDR12's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.38× lower at baseline in the lines without SLC9B2 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.0, -37.0); signed map (-3.7, -51.3). **Vector** length 95.7, 23.0% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +13.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +19.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +9.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.5 | -5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:202,874,261-203,014,798 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YTM1, FLJ10881 |
| Gene groups (HGNC) | WD repeat domain containing; PeBoW complex |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZL7](https://www.uniprot.org/uniprotkb/Q9GZL7) (Ribosome biogenesis protein WDR12):

> Component of the PeBoW complex, which is required for maturation of 28S and 5.8S ribosomal RNAs and formation of the 60S ribosome.

**Summary**, from NCBI Gene [55759](https://www.ncbi.nlm.nih.gov/gene/55759):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This protein is highly similar to the mouse WD repeat domain 12 protein at …

**Accessions** — [HGNC:14098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14098) · Entrez [55759](https://www.ncbi.nlm.nih.gov/gene/55759) · UniProt [Q9GZL7](https://www.uniprot.org/uniprotkb/Q9GZL7) · Ensembl [ENSG00000138442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138442)

## Data

Gene col 6177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6177); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6177]; `tensor/DDL_lfc|DDL_z.npy` [6177]; `embed/gene_vectors.npy` [6177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6177 or target_col == 6177). Every well: [[WDR12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
