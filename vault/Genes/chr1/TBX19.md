---
symbol: "TBX19"
type: "gene"
col: 6691
ensembl_id: "ENSG00000143178"
name: "T-box transcription factor 19"
location: "1q24.2"
module: 37
arm: "+"
pooled_cpm: 15.26
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TBX19

*T-box transcription factor 19* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +11.5, q 6e-28, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.489× (z -12.2, q 2e-31, down in 33 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 0.630× (z -4.1, q 0.003, down in 12 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 0.141×, Hs 766T 0.119×, SK-MEL-2 0.215×, HT-29 0.122×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 0.0579×, SK-MEL-2 0.0829×, A498 0.151×, KATO III 0.148×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0713×, HEC-1-A 0.135×, Hs 766T 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Pralsetinib (drug)]] 5 µM in 1 line (C32 0.0398×); [[Thymol (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.112×); [[Raltitrexed (drug)]] 0.5 µM in 1 line (NCI-H1792 0.190×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMYA5]] (+0.71, fdr 7e-06), [[LINC02680]] (+0.67, fdr 7e-06), [[LINC00640]] (+0.66, fdr 1e-05); moves opposite to [[PPP5C]] (-0.57, fdr 3e-05), [[CTPS1]] (-0.54, fdr 2e-05), [[IDH3A]] (-0.53, fdr 1e-04).
> It is in [[Module 037]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +11.5 | 6e-28 | 30/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +9.3 | 6e-18 | 30/45 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.46×** | +9.0 | 3e-17 | 29/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.28×** | +7.3 | 3e-11 | 26/47 (A498, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +6.7 | 3e-09 | 22/48 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.5 | 8e-09 | 23/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.38×** | +5.4 | 5e-06 | 15/48 (RPMI-7951, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.38×** | +5.4 | 5e-06 | 19/46 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.3 | 9e-06 | 17/45 (HOP62, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +5.1 | 2e-05 | 16/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +4.8 | 1e-04 | 10/43 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **1.29×** | +4.3 | 7e-04 | 5/48 (A498, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.1 | 0.002 | 18/41 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 14/48 (A498, Hs 766T, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.17× | +3.7 | 0.007 | 5/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.013 | 8/45 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.013 | 8/47 (H4, Hs 766T, …) | two highest doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.013 | 8/47 (LoVo, SW480, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.013 | 4/48 (C32, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.017 | 6/48 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.023 | 8/48 (NCI-H460, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6691.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 0.141×, Hs 766T 0.119×, SK-MEL-2 0.215×, HT-29 0.122×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 0.0579×, SK-MEL-2 0.0829×, A498 0.151×, KATO III 0.148×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0713×, HEC-1-A 0.135×, Hs 766T 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Pralsetinib (drug)]] 5 µM in 1 line (C32 0.0398×); [[Thymol (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.112×); [[Raltitrexed (drug)]] 0.5 µM in 1 line (NCI-H1792 0.190×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.489×** | -12.2 | 2e-31 | 33/39 (A-172, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.504×** | -10.8 | 1e-24 | 26/34 (SK-MEL-2, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.533×** | -10.3 | 1e-22 | 24/30 (A-172, Hs 766T, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.693×** | -6.3 | 6e-08 | 26/47 (LOX-IMVI, SW480, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.723×** | -5.5 | 3e-06 | 22/45 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.744×** | -5.0 | 4e-05 | 22/45 (CFPAC-1, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.778×** | -4.3 | 0.001 | 17/47 (A-172, SW480, …) | two highest doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.630×** | -4.1 | 0.003 | 12/45 (C32, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -3.8 | 0.007 | 4/48 (A-427, NCI-H661, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.801×** | -3.8 | 0.008 | 14/47 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.858× | -3.7 | 0.011 | 3/48 (A498, LS 180, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.825×** | -3.1 | 0.087 | 6/47 (hTERT-HPNE, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.3 | 3 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 21.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[C32 (line)]] | wt | 38.0 | 0 | 3 (2 ⚠) | — | [[Pralsetinib (drug)]] 5 µM 0.0398× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 64.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0829× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 25.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0579× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 26.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Raltitrexed (drug)]] 0.5 µM 0.190× (z -8.8) |
| [[A549 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 9.06 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.158× (z -9.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.112× (z -9.2) |
| [[KATO III (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 9.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMYA5]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[LINC02680]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.66 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[KLRD1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TEX29]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SNX31]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RSBN1]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[COLEC11]] | +0.61 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[TMEM269]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[WDR49]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SOS1]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LINC02641]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP5C]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[CTPS1]] | -0.54 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[IDH3A]] | -0.53 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SSX2IP]] | -0.52 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[GFM1]] | -0.52 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[UQCC2]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SLX4]] | -0.52 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[AKIRIN1]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[POFUT1]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SAE1]] | -0.51 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[NCBP1]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[TEX2]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, -18.3); signed map (10.1, 4.6). **Vector** length 93.6, 19.4% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.4 | +9.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.3 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +11.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -3.4 | -12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.9 | -10.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -2.9 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.5 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.4 | -6.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:168,280,877-168,314,426 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dj747L4.1, TPIT |
| Gene groups (HGNC) | T-box transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O60806](https://www.uniprot.org/uniprotkb/O60806) (T-box transcription factor TBX19):

> Transcriptional regulator involved in developmental processes. Can activate POMC gene expression and repress the alpha glycoprotein subunit and thyroid-stimulating hormone beta promoters.

**Summary**, from NCBI Gene [9095](https://www.ncbi.nlm.nih.gov/gene/9095):

> This gene is a member of a phylogenetically conserved family of genes that share a common DNA-binding domain, the T-box. T-box genes encode transcription factors involved in the regulation of developmental processes. Mutations in this gene were found in patients with isolated deficiency of pituitary POMC-derived ACTH, suggesting an essential role for this gene in differentiation of the pituitary POMC lineage. ACTH deficiency is characterized by adrenal insufficiency symptoms such as weight …

**Accessions** — [HGNC:11596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11596) · Entrez [9095](https://www.ncbi.nlm.nih.gov/gene/9095) · UniProt [O60806](https://www.uniprot.org/uniprotkb/O60806) · Ensembl [ENSG00000143178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143178)

## Data

Gene col 6691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6691); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6691]; `tensor/DDL_lfc|DDL_z.npy` [6691]; `embed/gene_vectors.npy` [6691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6691 or target_col == 6691). Every well: [[TBX19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBX19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
