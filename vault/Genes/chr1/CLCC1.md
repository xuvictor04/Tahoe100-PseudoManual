---
symbol: "CLCC1"
type: "gene"
col: 4308
ensembl_id: "ENSG00000121940"
name: "chloride channel CLIC like 1"
location: "1p13.3"
module: 162
arm: "+"
pooled_cpm: 71.05
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# CLCC1

*chloride channel CLIC like 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +14.2, q 3e-43, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.667× (z -8.2, q 1e-13, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.556× (z -6.5, q 3e-08, down in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 5 lines (A-172 0.267×, SK-MEL-2 0.314×, J82 0.421×, SNU-423 0.320×, …; ⚠ cell-cycle shift, explains ~52% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 0.453×, H4 0.309×, HS-578T 0.480×, A549 0.475×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.117×, NCI-H23 0.270×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (CHP-212 0.0883×); [[Lidocaine (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.203×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC15]] (+0.67, fdr 1e-05), [[DDX59]] (+0.60, fdr 2e-05), [[RNF14]] (+0.60, fdr 3e-05); moves opposite to [[HES1]] (-0.68, fdr 7e-06), [[NR4A1]] (-0.59, fdr 1e-05), [[TMEM251]] (-0.57, fdr 2e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +14.2 | 3e-43 | 43/49 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +8.3 | 2e-14 | 37/48 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +8.1 | 1e-13 | 36/48 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.40×** | +6.7 | 2e-09 | 30/48 (Panc 03.27, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.5 | 9e-09 | 34/48 (HS-578T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.9 | 3e-07 | 23/43 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.6 | 3e-04 | 27/50 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.23×** | +3.9 | 0.008 | 20/50 (A-427, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.012 | 12/49 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.6 | 0.020 | 9/48 (CFPAC-1, hTERT-HPNE, …) | top dose only | low cells (technical?) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.2 | 0.060 | 10/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.094 | 20/48 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.15× | +3.1 | 0.094 | 14/48 (C32, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4308.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 5 lines (A-172 0.267×, SK-MEL-2 0.314×, J82 0.421×, SNU-423 0.320×, …; ⚠ cell-cycle shift, explains ~52% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 0.453×, H4 0.309×, HS-578T 0.480×, A549 0.475×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.117×, NCI-H23 0.270×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (CHP-212 0.0883×); [[Lidocaine (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.203×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.667×** | -8.2 | 1e-13 | 31/48 (A-172, SK-MEL-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.556×** | -6.5 | 3e-08 | 34/49 (HS-578T, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.761×** | -5.8 | 2e-06 | 28/48 (HS-578T, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.792×** | -4.9 | 1e-04 | 22/48 (SW480, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -4.8 | 2e-04 | 27/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.803×** | -4.6 | 4e-04 | 25/48 (C32, LS 180, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.832×** | -3.9 | 0.009 | 20/48 (BT-474, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.847× | -3.5 | 0.034 | 20/48 (SHP-77, SNU-1, …) | all doses, flat |  |
| [[Thymol (drug)]] 5 µM |  | 0.890× | -3.5 | 0.034 | 8/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.850× | -3.4 | 0.034 | 17/49 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.891× | -3.4 | 0.034 | 20/48 (A-172, H4, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | 0.852× | -3.2 | 0.056 | 15/47 (A-172, J82, …) | top dose only |  |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | 0.862× | -3.1 | 0.078 | 8/48 (C-33 A, KATO III, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.864× | -3.1 | 0.088 | 15/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.866× | -3.0 | 0.098 | 8/47 (SK-MEL-2, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 109 | 2 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 65.4 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.267× (z -14.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HEC-1-A (line)]] | alt | 91.3 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.09× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.460× (z -10.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[LoVo (line)]] | wt | 61.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.6) | — |
| [[A-427 (line)]] | wt | 73.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) | — |
| [[A498 (line)]] | wt | 82.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 73.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 50.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.90× (z +9.2) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0775× (z -12.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 56.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 83.4 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.32× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 57.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 65.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.2) | — |
| [[RKO (line)]] | wt | 108 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 45.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.3) | [[Harringtonine (drug)]] 5 µM 0.320× (z -10.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 50.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +12.7) | — |
| [[C-33 A (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 53.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0883× (z -9.1) |
| [[H4 (line)]] | wt | 80.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 87.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.9) | — |
| [[J82 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.421× (z -10.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 61.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 82.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 97.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.314× (z -11.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SNU-1 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -19.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.203× (z -8.8) |
| [[SW 900 (line)]] | alt | 42.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.3) | — |
| [[SW480 (line)]] | alt | 47.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC15]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DDX59]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RNF14]] | +0.60 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[SETD7]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.59 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[ORMDL1]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ECPAS]] | +0.57 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[NAPB]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TIAL1]] | +0.57 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[SNHG22]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CIZ1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[NR4A1]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TMEM251]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MAML2]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[IER2]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MIDN]] | -0.55 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[NR4A3]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[GDF11]] | -0.53 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[DUSP2]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[TCF7L2]] | -0.52 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[CSRNP1]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ATP7A]] | -0.52 | -0.51 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLCC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NR4A3]] | B | NR4A3 activity raises CLCC1's level | lines that do not express NR4A3 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without NR4A3 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC4A7, SLC16A1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CLCC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CHST11]] | B | CHST11 activity lowers CLCC1's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 1.15× higher at baseline in the lines without CHST11 | 0.084 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |
| [[PSMB5]] | B | PSMB5 activity lowers CLCC1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAML2]] | B | MAML2 activity lowers CLCC1's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 1.52× higher at baseline in the lines without MAML2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction -0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.8, 18.3); signed map (-33.8, -22.4). **Vector** length 123, 33.4% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +14.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.5 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.8 | -8.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.3 | -4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.6 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -2.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | chloride channel CLIC like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:108,881,885-108,963,527 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCLC |
| Gene groups (HGNC) | Tetraspan junctional complex superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S66](https://www.uniprot.org/uniprotkb/Q96S66) (Chloride channel CLIC-like protein 1):

> Anion-selective channel with Ca(2+)-dependent and voltage-independent gating. Permeable to small monovalent anions with selectivity for bromide > chloride > nitrate > fluoride (By similarity). Operates in the endoplasmic reticulum (ER) membrane where it mediates chloride efflux to compensate for the loss of positive charges from the ER lumen upon Ca(2+) release. Contributes to the maintenance of ER Ca(2+) pools and activation of unfolded protein response to prevent accumulation of misfolded …

**Summary**, from NCBI Gene [23155](https://www.ncbi.nlm.nih.gov/gene/23155):

> Enables chloride channel activity. Involved in endoplasmic reticulum calcium ion homeostasis. Located in endoplasmic reticulum membrane and mitochondria-associated endoplasmic reticulum membrane contact site. Implicated in retinitis pigmentosa 32. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29675) · Entrez [23155](https://www.ncbi.nlm.nih.gov/gene/23155) · UniProt [Q96S66](https://www.uniprot.org/uniprotkb/Q96S66) · Ensembl [ENSG00000121940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121940)

## Data

Gene col 4308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4308); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4308]; `tensor/DDL_lfc|DDL_z.npy` [4308]; `embed/gene_vectors.npy` [4308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4308 or target_col == 4308). Every well: [[CLCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
