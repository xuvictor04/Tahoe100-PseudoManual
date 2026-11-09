---
symbol: "RABGGTB"
type: "gene"
col: 6098
ensembl_id: "ENSG00000137955"
name: "Rab geranylgeranyltransferase subunit beta"
location: "1p31.1"
module: 4
arm: "+"
pooled_cpm: 43.58
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 30
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RABGGTB

*Rab geranylgeranyltransferase subunit beta* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.34× (z +11.5, q 1e-27, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.635× (z -8.8, q 1e-15, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LoVo 0.338×, RKO 0.346×, NCI-H23 0.428×, SNU-1 0.361×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.190×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.211×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0936×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL3]] (+0.69, fdr 7e-06), [[AGK]] (+0.68, fdr 1e-05), [[PRPF19]] (+0.67, fdr 7e-06); moves opposite to [[ARID4A]] (-0.67, fdr 2e-05), [[DLEU2]] (-0.65, fdr 8e-06), [[CDK19]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +11.5 | 1e-27 | 43/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +11.3 | 3e-27 | 44/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.26×** | +11.0 | 1e-25 | 46/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.13×** | +9.6 | 1e-19 | 40/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +8.7 | 3e-16 | 43/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +8.7 | 4e-16 | 38/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +8.3 | 9e-15 | 43/49 (A498, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +8.0 | 1e-13 | 38/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.89×** | +7.5 | 5e-12 | 38/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +7.1 | 7e-11 | 40/47 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +6.8 | 7e-10 | 32/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.65×** | +6.7 | 8e-10 | 35/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +6.1 | 4e-08 | 37/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.0 | 7e-08 | 31/47 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.9 | 1e-07 | 34/43 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +5.7 | 4e-07 | 27/48 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.69×** | +5.0 | 1e-05 | 34/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.03×** | +5.0 | 2e-05 | 33/48 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.01×** | +4.9 | 3e-05 | 35/48 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +4.7 | 6e-05 | 25/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6098.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LoVo 0.338×, RKO 0.346×, NCI-H23 0.428×, SNU-1 0.361×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.190×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.211×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0936×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -8.8 | 1e-15 | 37/48 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.724×** | -4.4 | 0.003 | 30/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.794× | -3.2 | 0.29 | 20/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 80.9 | 3 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.83× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.70× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 30.5 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 36.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.15× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 41.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.53× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 53.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 56.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.13× (z +8.9) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 60.1 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.41× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 51.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0936× (z -9.4) |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.5) |
| [[C-33 A (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 46.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.211× (z -9.9) |
| [[HOP62 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.05× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 43.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.21× (z +9.1) | — |
| [[KATO III (line)]] | alt | 30.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.17× (z +10.1) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 35.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.59× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.28× (z +10.5) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 55.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +10.2) | — |
| [[RKO (line)]] | wt | 75.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.7) |
| [[SNU-1 (line)]] | wt | 59.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.7) |
| [[A-172 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 80.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL3]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 | same gene group |
| [[AGK]] | +0.68 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[PRPF19]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[DLAT]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[FKTN]] | +0.66 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[FIRRE]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CCT2]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[STARD7]] | +0.63 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[CLPB]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NLE1]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4A]] | -0.67 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[DLEU2]] | -0.65 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[CDK19]] | -0.62 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[CRAMP1]] | -0.61 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.60 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[STX5]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.59 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[TESK2]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ING2]] | -0.58 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[GCC2]] | -0.56 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[UBXN7]] | -0.55 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[TOM1L2]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.0, -40.4); signed map (-11.7, -48.6). **Vector** length 97.6, 26.7% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.1 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.5 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.1 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +8.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.7 |
|  | [[Sodium Salicylate (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | Rab geranylgeranyltransferase subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:75,786,197-75,795,086 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Rab geranylgeranyltransferase subunits; Protein geranylgeranyltransferase type III subunits |
| Reactome | 4 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; TP53 Regulates Transcription of Cell Death Genes; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P53611](https://www.uniprot.org/uniprotkb/P53611) (Geranylgeranyl transferase type-2 subunit beta):

> Catalyzes the transfer of a geranylgeranyl moiety from geranylgeranyl diphosphate to both cysteines of Rab proteins with the C-terminal sequence -XXCC, -XCXC and -CCXX, such as RAB1A, RAB3A, RAB5A and RAB7A. Catalytic subunit of the geranylgeranyl transferase type 3 (GGTase-3) complex. The GGTase-3 complex geranylgeranylates and targets FBXL2 to the cellular membranes, where FBXL2 forms part of the E3 ubiquitin-protein ligase complex SCF(FBXL2) that mediates the degradation of membrane-anchored …

**Summary**, from NCBI Gene [5876](https://www.ncbi.nlm.nih.gov/gene/5876):

> This gene encodes the beta-subunit of the enzyme Rab geranylgeranyl-transferase (RabGGTase), which belongs to the protein prenyltransferase family. RabGGTase catalyzes the post-translational addition of geranylgeranyl groups to C-terminal cysteine residues of Rab GTPases. Three small nucleolar RNA genes are present in the intronic regions of this gene. Alternately spliced transcript variants have been observed for this gene. A pseudogene associated with this gene is located on chromosome 3. …

**Accessions** — [HGNC:9796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9796) · Entrez [5876](https://www.ncbi.nlm.nih.gov/gene/5876) · UniProt [P53611](https://www.uniprot.org/uniprotkb/P53611) · Ensembl [ENSG00000137955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137955)

## Data

Gene col 6098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6098); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6098]; `tensor/DDL_lfc|DDL_z.npy` [6098]; `embed/gene_vectors.npy` [6098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6098 or target_col == 6098). Every well: [[RABGGTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABGGTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
