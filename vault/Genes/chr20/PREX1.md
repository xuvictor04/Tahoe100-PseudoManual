---
symbol: "PREX1"
type: "gene"
col: 4483
ensembl_id: "ENSG00000124126"
name: "phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 1"
location: "20q13.13"
module: 100
arm: "+"
pooled_cpm: 12.83
n_lines_expressing: 32
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# PREX1

*phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.63× (z +22.9, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.776× (z -4.1, q 0.013, down in 7 of 25 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 2 lines (H4 0.0811×, HS-578T 0.182×; ⚠ cell-cycle shift, explains ~11% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H23 0.149×, SW480 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.193×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.335×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.144×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNN3]] (+0.54, fdr 3e-05), [[RNF157]] (+0.53, fdr 5e-05), [[SNTG2]] (+0.53, fdr 5e-05); moves opposite to [[DDX59]] (-0.50, fdr 1e-04), [[RABL2A]] (-0.46, fdr 0.002, ⚠ one half only (not replicated)), [[RABL2B]] (-0.45, fdr 0.002, ⚠ one half only (not replicated)), [[URM1]] (-0.44, fdr 1e-04), [[NUP133]] (-0.44, fdr 2e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PADI2]] → it (grade B ⚠); 3 go from it, the strongest it → [[SLAIN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.63×** | +22.9 | 0e+00 | 28/30 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.20×** | +19.5 | 0e+00 | 25/30 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +18.4 | 0e+00 | 22/30 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +16.4 | 0e+00 | 22/29 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.60×** | +16.0 | 0e+00 | 23/30 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.53×** | +15.6 | 0e+00 | 23/27 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.37×** | +14.4 | 3e-45 | 25/30 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +12.0 | 2e-31 | 21/28 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.63×** | +8.5 | 1e-15 | 20/29 (LOX-IMVI, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.4 | 2e-15 | 9/28 (Hs 766T, A549, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +8.4 | 2e-15 | 14/30 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.57×** | +7.5 | 3e-12 | 8/21 (BT-474, A549, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +6.8 | 6e-10 | 14/27 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.5 | 4e-09 | 14/25 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.4 | 8e-09 | 10/19 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 4e-06 | 13/28 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.31×** | +4.5 | 2e-04 | 5/30 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.002 | 8/29 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4483.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 2 lines (H4 0.0811×, HS-578T 0.182×; ⚠ cell-cycle shift, explains ~11% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H23 0.149×, SW480 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.193×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.335×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.776×** | -4.1 | 0.013 | 7/25 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.1 | 0.013 | 11/29 (SNU-423, H4, …) | top dose only | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | 0.692× | -3.3 | 0.18 | 8/27 (H4, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.827× | -3.2 | 0.18 | 3/28 (hTERT-HPNE, SK-MEL-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.833× | -3.1 | 0.20 | 0/29 | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.824× | -3.0 | 0.20 | 4/27 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.825× | -3.0 | 0.20 | 5/29 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 15.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.01× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 4 | 0 | [[Belinostat (drug)]] 5 µM 5.51× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 37.3 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.21× (z +17.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 3.69× (z +13.7) | — |
| [[SW480 (line)]] | alt | 19.7 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.65× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 16.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.9) | [[Selinexor (drug)]] 0.5 µM 0.182× (z -9.4) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.198× (z -8.6) |
| [[SNU-423 (line)]] | alt | 24.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.311× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +14.2) | — |
| [[A-427 (line)]] | wt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -12.3) |
| [[Hs 766T (line)]] | wt | 12.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.5) | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.144× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 6.55 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -8.8) ⚠ toxic |
| [[A498 (line)]] | wt | 29.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +8.6) | — |
| [[H4 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0811× (z -11.1) ⚠ cell-cycle shift, explains ~11% of this change |
| [[hTERT-HPNE (line)]] | wt | 4.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +9.1) | — |
| [[J82 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.3) | — |
| [[KATO III (line)]] | alt | 3.33 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.3× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +14.3) | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNN3]] | +0.54 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[RNF157]] | +0.53 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[SNTG2]] | +0.53 | +0.40 / +0.61 | both halves | 5e-05 | same gene group |
| [[SEMA6B]] | +0.52 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[SUSD4]] | +0.51 | +0.37 / +0.60 | both halves | 7e-05 |  |
| [[LYPD6B]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[VAT1L]] | +0.50 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[SEMA4D]] | +0.49 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[FBLN2]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[AIF1L]] | +0.49 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[PRKAR2B]] | +0.49 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[ADGRB2]] | +0.48 | +0.31 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX59]] | -0.50 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[RABL2A]] | -0.46 | -0.11 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[RABL2B]] | -0.45 | -0.14 / -0.50 | ⚠ one half (not replicated) | 0.002 |  |
| [[URM1]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[NUP133]] | -0.44 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.44 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[SYNRG]] | -0.44 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[TCTN3]] | -0.44 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[ASTE1]] | -0.43 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[PAAF1]] | -0.43 | -0.20 / -0.44 | both halves | 7e-04 |  |
| [[DCAF10]] | -0.43 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[PCF11-AS1]] | -0.42 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[GPALPP1]] | -0.42 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[RBKS]] | -0.42 | -0.25 / -0.39 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PADI2]] | B | PADI2 activity raises PREX1's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without PADI2 | 0.034 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[OAF]] | C | OAF activity lowers PREX1's level | lines that do not express OAF (4) vs lines expressing it (46) | 5.59× higher at baseline in the lines without OAF | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLAIN1]] | B | PREX1 activity raises SLAIN1's level | lines that do not express PREX1 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without PREX1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, SOGA3, PCBP3 |
| [[RABL2B]] | B | PREX1 activity raises RABL2B's level | lines that do not express PREX1 (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without PREX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, SOGA3, PCBP3 |
| [[SUSD4]] | B | PREX1 activity raises SUSD4's level | lines that do not express PREX1 (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without PREX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, SOGA3, PCBP3 |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.453). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.2, 40.7); signed map (30.7, 26.6). **Vector** length 64.8, 13.2% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +22.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +15.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +14.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.8 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -1.7 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.6 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:48,624,252-48,827,999 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1415, P-REX1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; PDZ domain containing; DEP domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 20 pathways, smallest: RHOJ GTPase cycle; NRAGE signals death through JNK; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCU6](https://www.uniprot.org/uniprotkb/Q8TCU6) (Phosphatidylinositol 3,4,5-trisphosphate-dependent Rac exchanger 1 protein):

> Functions as a RAC guanine nucleotide exchange factor (GEF), which activates the Rac proteins by exchanging bound GDP for free GTP. Its activity is synergistically activated by phosphatidylinositol 3,4,5-trisphosphate and the beta gamma subunits of heterotrimeric G protein. May function downstream of heterotrimeric G proteins in neutrophils.

**Summary**, from NCBI Gene [57580](https://www.ncbi.nlm.nih.gov/gene/57580):

> The protein encoded by this gene acts as a guanine nucleotide exchange factor for the RHO family of small GTP-binding proteins (RACs). It has been shown to bind to and activate RAC1 by exchanging bound GDP for free GTP. The encoded protein, which is found mainly in the cytoplasm, is activated by phosphatidylinositol-3,4,5-trisphosphate and the beta-gamma subunits of heterotrimeric G proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:32594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32594) · Entrez [57580](https://www.ncbi.nlm.nih.gov/gene/57580) · UniProt [Q8TCU6](https://www.uniprot.org/uniprotkb/Q8TCU6) · Ensembl [ENSG00000124126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124126)

## Data

Gene col 4483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4483); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4483]; `tensor/DDL_lfc|DDL_z.npy` [4483]; `embed/gene_vectors.npy` [4483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4483 or target_col == 4483). Every well: [[PREX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PREX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
