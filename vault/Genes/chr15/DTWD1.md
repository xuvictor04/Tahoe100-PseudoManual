---
symbol: "DTWD1"
type: "gene"
col: 2409
ensembl_id: "ENSG00000104047"
name: "DTW motif tRNA-uridine aminocarboxypropyltransferase 1"
location: "15q21.2"
module: 198
arm: "+"
pooled_cpm: 36.14
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# DTWD1

*DTW motif tRNA-uridine aminocarboxypropyltransferase 1* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.58× (z +8.9, q 2e-16, up in 38 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.38× (z +6.6, q 8e-09, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.635× (z -13.0, q 8e-36, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTPCR]] (+0.69, fdr 7e-06), [[ZNF383]] (+0.66, fdr 1e-05), [[TRIAP1]] (+0.66, fdr 1e-05); moves opposite to [[CTNNA1]] (-0.56, fdr 1e-05), [[ACLY]] (-0.55, fdr 1e-05), [[RCOR1]] (-0.55, fdr 1e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TUBB3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +8.9 | 2e-16 | 38/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.29×** | +7.4 | 4e-11 | 28/48 (A-427, RKO, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +6.6 | 8e-09 | 28/48 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.3 | 2e-05 | 23/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.16× | +4.4 | 0.001 | 13/48 (A549, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.24×** | +4.4 | 0.001 | 18/48 (A-427, Hs 766T, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.20× | +3.6 | 0.023 | 11/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.12× | +3.2 | 0.086 | 6/48 (Hs 766T, NCI-H1573, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.086 | 10/48 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.1 | 0.12 | 10/48 (HOP62, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -13.0 | 8e-36 | 36/48 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.656×** | -12.0 | 6e-31 | 28/47 (NCI-H460, NCI-H1792, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -9.6 | 2e-19 | 31/48 (C32, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -9.1 | 9e-18 | 35/48 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.635×** | -8.8 | 1e-16 | 33/47 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.680×** | -7.8 | 6e-13 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.670×** | -7.8 | 6e-13 | 29/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -7.4 | 1e-11 | 30/48 (hTERT-HPNE, SW48, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -7.2 | 5e-11 | 28/49 (SNU-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.705×** | -7.1 | 9e-11 | 28/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.706×** | -7.0 | 1e-10 | 26/46 (LoVo, NCI-H23, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.700×** | -6.8 | 5e-10 | 25/48 (CHP-212, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.740×** | -5.6 | 8e-07 | 20/41 (H4, C-33 A, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -5.4 | 3e-06 | 22/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -5.0 | 3e-05 | 4/49 (NCI-H2030, AN3 CA, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.674×** | -4.2 | 9e-04 | 17/47 (SNU-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.038 | 13/47 (HCT15, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.816×** | -2.9 | 0.079 | 6/48 (SW 1088, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.866× | -2.9 | 0.079 | 6/48 (AN3 CA, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.5 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -25.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -11.1) |
| [[PANC-1 (line)]] | alt | 41.7 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -14.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW480 (line)]] | alt | 38.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.362× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 48.2 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 58.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 68.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -19.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW 900 (line)]] | alt | 39.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 30.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.87× (z +9.4) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 27.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.8) |
| [[H4 (line)]] | wt | 39.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 35.7 | 0 | 2 (1 ⚠) | — | [[PF-06260933 (drug)]] 5 µM 0.0527× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -8.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.5) |
| [[LoVo (line)]] | wt | 45.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[LOX-IMVI (line)]] | wt | 46.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 54.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.236× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.261× (z -9.8) |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.6) |
| [[CHP-212 (line)]] | wt | 65.8 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0434× (z -15.1) |
| [[HOP62 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -10.2) |
| [[J82 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H23 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0746× (z -15.0) |
| [[SW48 (line)]] | wt | 37.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -9.4) |
| [[A-172 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTPCR]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ZNF383]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[TRIAP1]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[FBXL5]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[THAP6]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.62 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[PEX2]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[THUMPD2]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[XPA]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TAB1]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[COIL]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNA1]] | -0.56 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ACLY]] | -0.55 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[RCOR1]] | -0.55 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[HCN2]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[CTBP2]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[LARGE1]] | -0.52 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CHD4]] | -0.49 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[SFXN5]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[RALY]] | -0.48 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[MYLK2]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TCF7]] | -0.48 | -0.50 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUBB3]] | C | DTWD1's natural level strengthens TUBB3's drug response | DTWD1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.17; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.9, 2.9); signed map (-15.6, -14.6). **Vector** length 95.0, 22.4% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.6 | +8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +7.0 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.1 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.8 | +4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -13.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -9.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | DTW motif tRNA-uridine aminocarboxypropyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:49,621,037-49,656,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS009, MGC111207 |
| Gene groups (HGNC) | DTW motif tRNA-uridine aminocarboxypropyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5C7](https://www.uniprot.org/uniprotkb/Q8N5C7) (tRNA-uridine aminocarboxypropyltransferase 1):

> Catalyzes the formation of 3-(3-amino-3-carboxypropyl)uridine (acp3U) at position 20 in the D-loop of several cytoplasmic tRNAs (acp3U(20)).

**Summary**, from NCBI Gene [56986](https://www.ncbi.nlm.nih.gov/gene/56986):

> Enables tRNA-uridine aminocarboxypropyltransferase activity. Involved in tRNA modification. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30926) · Entrez [56986](https://www.ncbi.nlm.nih.gov/gene/56986) · UniProt [Q8N5C7](https://www.uniprot.org/uniprotkb/Q8N5C7) · Ensembl [ENSG00000104047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104047)

## Data

Gene col 2409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2409); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2409]; `tensor/DDL_lfc|DDL_z.npy` [2409]; `embed/gene_vectors.npy` [2409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2409 or target_col == 2409). Every well: [[DTWD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTWD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
