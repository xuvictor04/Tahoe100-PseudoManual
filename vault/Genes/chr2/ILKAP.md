---
symbol: "ILKAP"
type: "gene"
col: 5298
ensembl_id: "ENSG00000132323"
name: "ILK associated serine/threonine phosphatase"
location: "2q37.3"
module: 163
arm: "+"
pooled_cpm: 56.71
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# ILKAP

*ILK associated serine/threonine phosphatase* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +10.2, q 9e-22, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.493× (z -9.5, q 1e-18, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.768× (z -3.5, q 0.058, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-172 0.221×, NCI-H2347 0.253×, C32 0.222×, J82 0.319×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2347 0.222×, SNU-1 0.175×, NCI-H2030 0.225×, NCI-H1573 0.245×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.252×, HEC-1-A 0.304×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.178×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61A2]] (+0.62, fdr 7e-06), [[RNF38]] (+0.61, fdr 1e-05), [[PTPRA]] (+0.60, fdr 1e-05); moves opposite to [[PPP1R10]] (-0.59, fdr 1e-05), [[CSNK1A1]] (-0.55, fdr 1e-05), [[RLIM]] (-0.55, fdr 2e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTNR1A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +10.2 | 9e-22 | 39/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.93×** | +8.8 | 5e-16 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +8.3 | 3e-14 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +7.3 | 3e-11 | 41/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +7.0 | 3e-10 | 40/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +6.1 | 1e-07 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.4 | 4e-06 | 36/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 1e-04 | 26/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.6 | 3e-04 | 30/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.008 | 25/50 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.015 | 23/48 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.6 | 0.015 | 21/37 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.043 | 24/48 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.089 | 17/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +3.0 | 0.090 | 19/48 (HT-29, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5298.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-172 0.221×, NCI-H2347 0.253×, C32 0.222×, J82 0.319×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2347 0.222×, SNU-1 0.175×, NCI-H2030 0.225×, NCI-H1573 0.245×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.252×, HEC-1-A 0.304×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.178×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.493×** | -9.5 | 1e-18 | 39/49 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -7.5 | 2e-11 | 33/43 (NCI-H2347, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.763×** | -3.6 | 0.054 | 25/48 (SW 1271, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.768×** | -3.5 | 0.058 | 29/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.773×** | -3.5 | 0.063 | 19/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.784× | -3.3 | 0.10 | 23/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.793× | -3.1 | 0.14 | 21/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | 0.793× | -3.1 | 0.14 | 21/49 (CFPAC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.797× | -3.0 | 0.14 | 19/47 (A498, LS 180, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.798× | -3.0 | 0.14 | 22/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +18.2) | — |
| [[SW480 (line)]] | alt | 51.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +13.6) | — |
| [[LoVo (line)]] | wt | 47.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 61.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.43× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 52.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.70× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +10.5) | — |
| [[A-172 (line)]] | wt | 80.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 62.0 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.31× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +11.1) | — |
| [[A-427 (line)]] | wt | 46.6 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.5) | — |
| [[A498 (line)]] | wt | 82.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 79.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 46.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 54.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 75.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 97.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[H4 (line)]] | wt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 72.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 58.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 67.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 77.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.6) | — |
| [[A549 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RNF38]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PTPRA]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MFSD14CP]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RNF138]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[UBP1]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SMG1P5]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SCAF4]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LSM8]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TBC1D12]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R10]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[CSNK1A1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RLIM]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[FOS]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SUPT6H]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[RABL3]] | -0.50 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZFPM2-AS1]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[AFF4]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[JUN]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[SKP1]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[BCL10]] | -0.49 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NUBP1]] | -0.49 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTNR1A]] | B | MTNR1A activity lowers ILKAP's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 1.21× higher at baseline in the lines without MTNR1A | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.5, -6.3); signed map (-41.3, -0.8). **Vector** length 96.8, 28.9% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +3.1 | +0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.9 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.0 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ILK associated serine/threonine phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:238,170,402-238,203,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434J2031, FLJ10181, PPM1O |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0C8](https://www.uniprot.org/uniprotkb/Q9H0C8) (Integrin-linked kinase-associated serine/threonine phosphatase 2C):

> Protein phosphatase that may play a role in regulation of cell cycle progression via dephosphorylation of its substrates whose appropriate phosphorylation states might be crucial for cell proliferation. Selectively associates with integrin linked kinase (ILK), to modulate cell adhesion and growth factor signaling. Inhibits the ILK-GSK3B signaling axis and may play an important role in inhibiting oncogenic transformation.

**Summary**, from NCBI Gene [80895](https://www.ncbi.nlm.nih.gov/gene/80895):

> The protein encoded by this gene is a protein serine/threonine phosphatase of the PP2C family. This protein can interact with integrin-linked kinase (ILK/ILK1), a regulator of integrin mediated signaling, and regulate the kinase activity of ILK. Through the interaction with ILK, this protein may selectively affect the signaling process of ILK-mediated glycogen synthase kinase 3 beta (GSK3beta), and thus participate in Wnt signaling pathway. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15566) · Entrez [80895](https://www.ncbi.nlm.nih.gov/gene/80895) · UniProt [Q9H0C8](https://www.uniprot.org/uniprotkb/Q9H0C8) · Ensembl [ENSG00000132323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132323)

## Data

Gene col 5298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5298); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5298]; `tensor/DDL_lfc|DDL_z.npy` [5298]; `embed/gene_vectors.npy` [5298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5298 or target_col == 5298). Every well: [[ILKAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILKAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
