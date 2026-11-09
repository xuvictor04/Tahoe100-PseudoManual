---
symbol: "RHOT1"
type: "gene"
col: 4773
ensembl_id: "ENSG00000126858"
name: "ras homolog family member T1"
location: "17q11.2"
module: 30
arm: "+"
pooled_cpm: 80.72
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# RHOT1

*ras homolog family member T1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.36× (z +9.3, q 6e-18, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.599× (z -15.7, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP14]] (+0.73, fdr 7e-06), [[EHMT2]] (+0.73, fdr 7e-06), [[CRYZL1]] (+0.69, fdr 8e-06); moves opposite to [[DUSP5-DT]] (-0.62, fdr 1e-05), [[MSRA]] (-0.60, fdr 3e-05), [[AP3B2]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HLA-K]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +9.3 | 6e-18 | 37/48 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +8.5 | 4e-15 | 37/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +8.0 | 2e-13 | 35/49 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +7.6 | 3e-12 | 29/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +6.4 | 1e-08 | 25/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +6.2 | 5e-08 | 23/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +5.9 | 2e-07 | 23/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +5.8 | 4e-07 | 16/48 (AsPC-1, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.5 | 2e-06 | 20/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +5.3 | 6e-06 | 21/49 (HT-29, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.16× | +4.8 | 6e-05 | 16/50 (AsPC-1, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +4.2 | 0.001 | 12/48 (HEC-1-A, AsPC-1, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.9 | 0.005 | 12/49 (C32, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.010 | 11/49 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.10× | +3.6 | 0.011 | 6/48 (AsPC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.12× | +3.5 | 0.018 | 13/48 (HOP62, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.08× | +3.3 | 0.034 | 3/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.599×** | -15.7 | 0e+00 | 41/48 (C32, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -12.9 | 7e-36 | 32/49 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.705×** | -10.7 | 2e-24 | 35/48 (AN3 CA, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -10.7 | 2e-24 | 27/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -10.6 | 6e-24 | 26/44 (CHP-212, SW1417, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.711×** | -9.6 | 5e-20 | 28/45 (A-427, A549, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.824×** | -8.4 | 5e-15 | 25/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.762×** | -8.3 | 8e-15 | 30/49 (NCI-H460, A-427, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.819×** | -5.9 | 3e-07 | 23/50 (A-172, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.823×** | -5.7 | 6e-07 | 22/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.831×** | -5.7 | 8e-07 | 22/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | 0.841× | -5.3 | 6e-06 | 23/48 (A-172, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 0.865× | -4.4 | 4e-04 | 18/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | 0.870× | -4.1 | 0.002 | 16/47 (NCI-H460, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.883× | -3.8 | 0.005 | 14/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.819×** | -3.8 | 0.006 | 16/47 (hTERT-HPNE, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Futibatinib (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.065 | 9/46 (Hs 766T, RKO, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.825×** | -2.9 | 0.098 | 11/48 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.9 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -12.5) |
| [[C32 (line)]] | wt | 98.2 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -18.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -15.6) |
| [[A-172 (line)]] | wt | 136 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 56.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -20.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 90.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -10.9) |
| [[SW 1271 (line)]] | alt | 94.7 | 0 | 4 | — | [[Harringtonine (drug)]] 0.05 µM 0.0503× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 114 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.522× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 98.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -11.7) |
| [[PANC-1 (line)]] | alt | 90.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -15.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.493× (z -12.4) |
| [[A-427 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 96.6 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.118× (z -11.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.384× (z -10.5) |
| [[C-33 A (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 96.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 73.4 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.570× (z -11.3) |
| [[RKO (line)]] | wt | 72.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 58.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 92.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 81.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.452× (z -10.0) |
| [[SW1417 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.468× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 73.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -10.7) |
| [[A498 (line)]] | wt | 78.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -10.0) |
| [[A549 (line)]] | wt | 95.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -12.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -16.5) |
| [[CHP-212 (line)]] | wt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 114 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.425× (z -11.7) |
| [[J82 (line)]] | alt | 72.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.593× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 63.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.523× (z -8.8) |
| [[LS 180 (line)]] | wt | 72.7 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 87.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 84.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP14]] | +0.73 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.69 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[MRPS34]] | +0.68 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ATRN]] | +0.68 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.66 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.66 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[CROT]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[RWDD1]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.65 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[MLLT10]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[IRAK1BP1]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP5-DT]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[MSRA]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[AP3B2]] | -0.59 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[DDX5]] | -0.58 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[USP11]] | -0.58 | -0.51 / -0.43 | both halves | 3e-05 | pathway: Deubiquitination |
| [[ATXN1L]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[LINC01829]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SSUH2]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | -0.57 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[PARD6G-AS1]] | -0.57 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SERPINB8]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CDK6-AS1]] | -0.57 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-K]] | B | HLA-K activity lowers RHOT1's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.30× higher at baseline in the lines without HLA-K | 0.030 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[TOP2A]] | B | TOP2A activity raises RHOT1's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.6, -9.2); signed map (-28.0, -10.2). **Vector** length 115, 30.2% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +6.8 | +5.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.4 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -15.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.7 | -10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.8 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member T1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:32,142,454-32,253,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIRO-1, FLJ11040, MIRO1; previously ARHT1 |
| Gene groups (HGNC) | Miro like atypical Rho GTPases; EF-hand domain containing |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: RHOT1 GTPase cycle; Miro GTPase Cycle; Ub-specific processing proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXI2](https://www.uniprot.org/uniprotkb/Q8IXI2) (Mitochondrial Rho GTPase 1):

> Atypical mitochondrial nucleoside-triphosphatase (NTPase) involved in mitochondrial trafficking. Probably involved in control of anterograde transport of mitochondria and their subcellular distribution. Promotes mitochondrial fission during high calcium conditions. Can hydrolyze GTP, ATP and UTP.

**Summary**, from NCBI Gene [55288](https://www.ncbi.nlm.nih.gov/gene/55288):

> Enables guanyl ribonucleotide binding activity; metal ion binding activity; and ribonucleoside triphosphate phosphatase activity. Involved in several processes, including mitochondrial outer membrane permeabilization; mitochondrion transport along microtubule; and regulation of mitochondrion organization. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21168) · Entrez [55288](https://www.ncbi.nlm.nih.gov/gene/55288) · UniProt [Q8IXI2](https://www.uniprot.org/uniprotkb/Q8IXI2) · Ensembl [ENSG00000126858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126858)

## Data

Gene col 4773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4773); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4773]; `tensor/DDL_lfc|DDL_z.npy` [4773]; `embed/gene_vectors.npy` [4773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4773 or target_col == 4773). Every well: [[RHOT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
