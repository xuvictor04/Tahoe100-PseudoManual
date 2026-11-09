---
symbol: "BMS1P20"
type: "gene"
col: 15742
ensembl_id: "ENSG00000272779"
name: "BMS1 pseudogene 20"
location: "22q11.22"
module: 25
arm: "+"
pooled_cpm: 15.64
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# BMS1P20

*BMS1 pseudogene 20* — 22q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.58× (z +16.0, q 0e+00, up in 37 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.51× (z +7.0, q 5e-10, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.800× (z -3.8, q 0.044, down in 16 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 0.5 µM: 0.737× (z -3.7, q 0.044, down in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 3 lines (NCI-H460 0.260×, A-427 0.177×, SHP-77 0.122×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (SNU-423 0.0544×); [[Bestatin (drug)]] 0.05 µM in 1 line (SNU-423 0.0507×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTLC1]] (+0.63, fdr 2e-05), [[EIF3C]] (+0.61, fdr 3e-05), [[KLC2]] (+0.60, fdr 2e-05); moves opposite to [[TMEM60]] (-0.57, fdr 1e-05), [[FOXA2]] (-0.52, fdr 2e-04), [[DBF4]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.58×** | +16.0 | 0e+00 | 37/39 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.51×** | +14.9 | 0e+00 | 26/28 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.96×** | +10.5 | 2e-23 | 29/33 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +7.0 | 5e-10 | 31/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.6 | 4e-09 | 26/47 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +6.1 | 1e-07 | 25/43 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.39×** | +5.6 | 2e-06 | 24/48 (SW480, LS 180, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.36×** | +5.2 | 2e-05 | 20/47 (LS 180, AsPC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.1 | 2e-05 | 22/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 4e-04 | 17/47 (NCI-H2030, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.5 | 4e-04 | 18/48 (SW480, HEC-1-A, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.4 | 6e-04 | 19/48 (SW1417, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.30×** | +4.2 | 0.001 | 14/41 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.1 | 0.001 | 8/22 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 13/47 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.6 | 0.010 | 7/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.011 | 9/48 (NCI-H1792, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.013 | 8/46 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.015 | 11/46 (MIA PaCa-2, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.040 | 4/47 (SK-MEL-2, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Clofarabine (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.043 | 8/46 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.061 | 1/48 (PANC-1) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.061 | 6/45 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Menadione (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.074 | 4/46 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 5 µM |  | 1.13× | +2.8 | 0.077 | 2/48 (A498, J82) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15742.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 3 lines (NCI-H460 0.260×, A-427 0.177×, SHP-77 0.122×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (SNU-423 0.0544×); [[Bestatin (drug)]] 0.05 µM in 1 line (SNU-423 0.0507×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.800×** | -3.8 | 0.044 | 16/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.737×** | -3.7 | 0.044 | 16/45 (A-427, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.806×** | -3.7 | 0.044 | 10/47 (SW1417, HCT15, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.824× | -3.3 | 0.13 | 8/47 (H4, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.829× | -3.2 | 0.13 | 13/46 (SW 900, NCI-H1573, …) | two highest doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 0.830× | -3.2 | 0.13 | 13/44 (NCI-H460, A-427, …) | inconsistent across doses | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.831× | -3.1 | 0.13 | 7/48 (HT-29, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 11.0 | 0 | 2 (1 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.177× (z -9.7) |
| [[LoVo (line)]] | wt | 13.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Thymol (drug)]] 0.5 µM 0.260× (z -10.0) |
| [[SNU-423 (line)]] | alt | 7.69 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0544× (z -12.0) |
| [[HOP62 (line)]] | alt | 7.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.195× (z -8.9) |
| [[PANC-1 (line)]] | alt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0909× (z -9.6) |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.122× (z -9.5) |
| [[SW480 (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC1]] | +0.63 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[EIF3C]] | +0.61 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[KLC2]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[DHFR]] | +0.60 | +0.29 / +0.65 | both halves | 2e-04 |  |
| [[EIF4H]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[RPN1]] | +0.57 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[DCTN1]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[THOC5]] | +0.57 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ELMOD2]] | +0.57 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[CDK9]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[GPN1]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[DYNC1LI2]] | +0.56 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM60]] | -0.57 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[DBF4]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[POLR2L]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD12]] | -0.50 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SUMO4]] | -0.49 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[NBPF19]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RRAGC]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TGIF2]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TXNIP]] | -0.48 | -0.48 / -0.32 | both halves | 1e-04 |  |
| [[IRS2]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[SLC25A37]] | -0.48 | -0.27 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.4, -24.0); signed map (-20.5, -35.6). **Vector** length 56.7, 7.61% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.6 | +16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.3 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.9 | +10.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.0 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +7.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | +4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.7 | +1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | BMS1 pseudogene 20 |
| Locus type | pseudogene |
| Location | 22q11.22 — chr22:22,303,224-22,310,401 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [96610](https://www.ncbi.nlm.nih.gov/gene/96610):

> This locus appears to be a transcribed pseudogene of the BMS1 homolog of yeast ribosome assembly protein on chromosome 10 that has arisen from duplication of the 3' half of the parent gene. Frameshifts and premature stop codons are present in this pseudogene compared to the parent gene. This gene lies in the immunoglobulin lambda gene cluster on chromosome 22q11.21.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:49153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49153) · Entrez [96610](https://www.ncbi.nlm.nih.gov/gene/96610) · Ensembl [ENSG00000272779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272779)

## Data

Gene col 15742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15742); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15742]; `tensor/DDL_lfc|DDL_z.npy` [15742]; `embed/gene_vectors.npy` [15742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15742 or target_col == 15742). Every well: [[BMS1P20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMS1P20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
