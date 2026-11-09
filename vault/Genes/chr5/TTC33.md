---
symbol: "TTC33"
type: "gene"
col: 3485
ensembl_id: "ENSG00000113638"
name: "tetratricopeptide repeat domain 33"
location: "5p13.1"
module: 39
arm: "+"
pooled_cpm: 46.08
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TTC33

*tetratricopeptide repeat domain 33* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +16.5, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.759× (z -5.8, q 3e-06, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 0.732× (z -3.4, q 0.082, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.146×, A549 0.139×, HepG2/C3A 0.0824×, HCT15 0.177×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.153×, A549 0.237×, C32 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (BT-474 0.0829×, A-427 0.220×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0908×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM151B]] (+0.77, fdr 9e-06), [[LINC02955]] (+0.76, fdr 1e-05), [[NQO1-DT]] (+0.72, fdr 4e-05); moves opposite to [[FAM118A]] (-0.62, fdr 3e-04), [[BRAT1]] (-0.60, fdr 2e-04), [[PSMD9]] (-0.59, fdr 8e-05).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +16.5 | 0e+00 | 37/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +14.4 | 2e-44 | 37/48 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +8.1 | 1e-13 | 32/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.0 | 2e-13 | 31/48 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.2 | 7e-11 | 34/48 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +7.2 | 7e-11 | 28/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +5.8 | 6e-07 | 28/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.5 | 2e-06 | 24/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +5.2 | 2e-05 | 25/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +5.0 | 3e-05 | 25/48 (A498, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 21/49 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.005 | 12/48 (SW480, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.005 | 12/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.005 | 18/48 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.027 | 16/48 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.042 | 4/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.043 | 15/47 (A549, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3485.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.146×, A549 0.139×, HepG2/C3A 0.0824×, HCT15 0.177×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.153×, A549 0.237×, C32 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (BT-474 0.0829×, A-427 0.220×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0908×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.759×** | -5.8 | 3e-06 | 27/48 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.774×** | -5.4 | 2e-05 | 31/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.826×** | -3.9 | 0.018 | 22/47 (BT-474, A-427, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.732×** | -3.4 | 0.082 | 20/48 (PANC-1, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 0.862× | -3.2 | 0.15 | 19/48 (SW 1271, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.857× | -3.1 | 0.15 | 18/48 (LoVo, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.864× | -3.1 | 0.15 | 12/48 (SW480, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 50.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.9) | [[Lonafarnib (drug)]] 5 µM 0.0919× (z -11.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 41.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +13.5) | — |
| [[A-427 (line)]] | wt | 74.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[A498 (line)]] | wt | 46.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 40.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.3) | — |
| [[LoVo (line)]] | wt | 52.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.2) | — |
| [[NCI-H1573 (line)]] | alt | 39.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[NCI-H1792 (line)]] | alt | 52.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 81.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +21.0) | — |
| [[A549 (line)]] | wt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[AsPC-1 (line)]] | alt | 37.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0829× (z -17.5) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 42.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LOX-IMVI (line)]] | wt | 39.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 38.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +15.6) | — |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 41.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 78.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0908× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0824× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.107× (z -8.7) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 34.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 55.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 37.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 44.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.57× (z +8.9) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[SW480 (line)]] | alt | 48.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.30× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM151B]] | +0.77 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[LINC02955]] | +0.76 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[NQO1-DT]] | +0.72 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[AEBP2]] | +0.71 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[USP50]] | +0.71 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.70 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[YIPF7]] | +0.70 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.70 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.68 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[LINC00880]] | +0.68 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[SLC6A13]] | +0.68 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[LINC01934]] | +0.68 | +0.62 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.62 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[BRAT1]] | -0.60 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[PSMD9]] | -0.59 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[ANTKMT]] | -0.59 | -0.53 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.5, -11.5); signed map (20.3, 3.2). **Vector** length 98.4, 22.6% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +8.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +6.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +14.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +8.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.5 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -7.6 | -5.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.2 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -6.8 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -2.8 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:40,512,333-40,755,963 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OSRF |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q6PID6](https://www.uniprot.org/uniprotkb/Q6PID6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29959) · Entrez [23548](https://www.ncbi.nlm.nih.gov/gene/23548) · UniProt [Q6PID6](https://www.uniprot.org/uniprotkb/Q6PID6) · Ensembl [ENSG00000113638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113638)

## Data

Gene col 3485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3485); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3485]; `tensor/DDL_lfc|DDL_z.npy` [3485]; `embed/gene_vectors.npy` [3485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3485 or target_col == 3485). Every well: [[TTC33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
