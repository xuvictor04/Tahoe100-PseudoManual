---
symbol: "NELFA"
type: "gene"
col: 11616
ensembl_id: "ENSG00000185049"
name: "negative elongation factor complex member A"
location: "4p16.3"
module: 146
arm: "+"
pooled_cpm: 29.72
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# NELFA

*negative elongation factor complex member A* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.57× (z +10.0, q 8e-21, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.538× (z -13.3, q 1e-37, down in 27 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -6.9, q 1e-09, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LOX-IMVI 0.232×, C-33 A 0.200×, HCT15 0.150×, A549 0.177×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.137×, NCI-H23 0.215×, SW480 0.364×, HS-578T 0.219×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.123×, A-427 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.457×); [[Orlistat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.150×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP3]] (+0.65, fdr 7e-06), [[NISCH]] (+0.65, fdr 1e-05), [[POLDIP3]] (+0.64, fdr 1e-05); moves opposite to [[BZW1]] (-0.58, fdr 1e-05), [[ACTR2]] (-0.57, fdr 3e-05), [[XRCC5]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 146]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +10.0 | 8e-21 | 30/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +7.4 | 4e-11 | 26/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.6 | 8e-09 | 25/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +5.3 | 1e-05 | 16/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.3 | 1e-05 | 21/46 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +5.1 | 3e-05 | 23/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.4 | 7e-04 | 18/47 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.20× | +3.9 | 0.006 | 17/48 (NCI-H460, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.8 | 0.011 | 11/48 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.12× | +3.6 | 0.017 | 13/48 (A-172, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.021 | 10/46 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.021 | 15/46 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.023 | 16/47 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.023 | 16/48 (SW48, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.18× | +3.4 | 0.023 | 12/48 (H4, CFPAC-1, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.040 | 13/47 (NCI-H460, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11616.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LOX-IMVI 0.232×, C-33 A 0.200×, HCT15 0.150×, A549 0.177×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.137×, NCI-H23 0.215×, SW480 0.364×, HS-578T 0.219×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.123×, A-427 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.457×); [[Orlistat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.150×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -13.3 | 1e-37 | 27/38 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.615×** | -10.8 | 6e-25 | 32/45 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -6.9 | 1e-09 | 26/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -5.0 | 9e-05 | 16/48 (SNU-1, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.806×** | -4.5 | 9e-04 | 22/42 (C-33 A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -4.3 | 0.002 | 14/47 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.861× | -3.4 | 0.063 | 5/48 (A498, COLO 205, …) | rises with dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.862× | -3.3 | 0.063 | 12/48 (SW 1088, NCI-H2030, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.10 | 8/48 (KATO III, SW48, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.10 | 8/48 (H4, COLO 205, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.10 | 4/48 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.872× | -3.1 | 0.10 | 7/48 (HEC-1-A, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 26.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 42.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.38× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -14.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 47.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.6) |
| [[A-427 (line)]] | wt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[C-33 A (line)]] | alt | 73.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 42.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.5) | — |
| [[SW480 (line)]] | alt | 31.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -13.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -11.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -10.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.150× (z -10.1) |
| [[LoVo (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 35.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.91× (z +9.0) | — |
| [[A498 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP3]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NISCH]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[POLDIP3]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TADA1]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ZNF14]] | +0.60 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[SAT2]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[DUSP12]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 | pathway: HIV Infection |
| [[LAMTOR4]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[ACVR1B]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ZNF592]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BZW1]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ACTR2]] | -0.57 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.56 | -0.42 / -0.62 | both halves | 4e-05 | pathway: HIV Infection |
| [[ASPH]] | -0.54 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[TPM4]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PTPN11]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ARPC5]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GALNT1]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 | same gene group |
| [[KPNA4]] | -0.52 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[SCYL2]] | -0.51 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[UGGT1]] | -0.51 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[FAM91A1]] | -0.50 | -0.30 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.3, -4.8); signed map (-25.4, -11.7). **Vector** length 84.1, 16.2% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.8 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +3.5 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +3.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.9 | -10.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | negative elongation factor complex member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,982,717-2,041,903 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NELF-A; previously WHSC2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Negative elongation factor complex members |
| Reactome | 25 pathways, smallest: Abortive elongation of HIV-1 transcript in the absence of Tat; Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3P2](https://www.uniprot.org/uniprotkb/Q9H3P2) (Negative elongation factor A):

> Essential component of the NELF complex, a complex that negatively regulates the elongation of transcription by RNA polymerase II. The NELF complex, which acts via an association with the DSIF complex and causes transcriptional pausing, is counteracted by the P-TEFb kinase complex.; (Microbial infection) The NELF complex is involved in HIV-1 latency possibly involving recruitment of PCF11 to paused RNA polymerase II.

**Summary**, from NCBI Gene [7469](https://www.ncbi.nlm.nih.gov/gene/7469):

> This gene is expressed ubiquitously with higher levels in fetal than in adult tissues. It encodes a protein sharing 93% sequence identity with the mouse protein. Wolf-Hirschhorn syndrome (WHS) is a malformation syndrome associated with a hemizygous deletion of the distal short arm of chromosome 4. This gene is mapped to the 165 kb WHS critical region, and may play a role in the phenotype of the WHS or Pitt-Rogers-Danks syndrome. The encoded protein is found to be capable of reacting with …

**Accessions** — [HGNC:12768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12768) · Entrez [7469](https://www.ncbi.nlm.nih.gov/gene/7469) · UniProt [Q9H3P2](https://www.uniprot.org/uniprotkb/Q9H3P2) · Ensembl [ENSG00000185049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185049)

## Data

Gene col 11616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11616); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11616]; `tensor/DDL_lfc|DDL_z.npy` [11616]; `embed/gene_vectors.npy` [11616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11616 or target_col == 11616). Every well: [[NELFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NELFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
