---
symbol: "ZSCAN12"
type: "gene"
col: 8181
ensembl_id: "ENSG00000158691"
name: "zinc finger and SCAN domain containing 12"
location: "6p22.1"
module: 16
arm: "+"
pooled_cpm: 6.39
n_lines_expressing: 36
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZSCAN12

*zinc finger and SCAN domain containing 12* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.53× (z +24.4, q 0e+00, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.795× (z -4.4, q 0.005, down in 17 of 31 measured lines) ⚠ cell-cycle shift, explains ~11% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 0.144×, Panc 03.27 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.253×, SK-MEL-2 0.294×; ⚠ cell-cycle shift, explains ~11% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.0863×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Brimonidine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0843×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.236×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF780A]] (+0.77, fdr 7e-06), [[ZNF772]] (+0.75, fdr 7e-06), [[ZNF620]] (+0.73, fdr 7e-06); moves opposite to [[SENP5]] (-0.66, fdr 7e-06), [[CD81]] (-0.64, fdr 1e-05), [[FBXW7]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZSCAN23]] → it (grade B ⚠); 12 go from it, the strongest it → [[MSANTD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.53×** | +24.4 | 0e+00 | 26/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.68×** | +13.5 | 7e-39 | 26/29 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.49×** | +12.0 | 7e-31 | 27/32 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.08×** | +10.0 | 2e-21 | 26/32 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.83×** | +8.3 | 2e-14 | 17/32 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +8.2 | 3e-14 | 13/34 (A-172, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 3e-06 | 12/32 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.8 | 1e-04 | 9/33 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.8 | 0.008 | 5/21 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.020 | 13/31 (NCI-H1792, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.031 | 4/32 (KATO III, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.3 | 0.053 | 4/23 (NCI-H2347, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.064 | 8/32 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.079 | 6/28 (RPMI-7951, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.17× | +3.1 | 0.079 | 4/34 (HT-29, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8181.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 0.144×, Panc 03.27 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.253×, SK-MEL-2 0.294×; ⚠ cell-cycle shift, explains ~11% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.0863×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Brimonidine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0843×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.236×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.795×** | -4.4 | 0.005 | 17/31 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 0.767× | -3.5 | 0.12 | 5/25 (CHP-212, SHP-77, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.784× | -3.3 | 0.12 | 12/30 (CHP-212, MIA PaCa-2, …) | rises with dose |  |
| [[Talc (drug)]] 0.5 µM |  | 0.785× | -3.3 | 0.12 | 5/32 (A-427, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.843× | -3.3 | 0.12 | 8/33 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.732× | -3.0 | 0.18 | 10/28 (CHP-212, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.800× | -3.0 | 0.18 | 6/33 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.794× | -3.0 | 0.18 | 8/32 (hTERT-HPNE, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 14.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -10.6) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.236× (z -8.6) |
| [[A-172 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0863× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.118× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0843× (z -9.3) |
| [[J82 (line)]] | alt | 2.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 1.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 4.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 7.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.3) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF780A]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | same gene group |
| [[ZNF772]] | +0.75 | +0.74 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZNF620]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 | same gene group |
| [[ZNF317]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 | same gene group |
| [[ZNF480]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 | same gene group |
| [[ZBED9]] | +0.72 | +0.76 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZNF155]] | +0.72 | +0.78 / +0.60 | both halves | 7e-06 | same gene group |
| [[ZSCAN26]] | +0.70 | +0.74 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZNF391]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 | same gene group |
| [[METTL18]] | +0.70 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[ZNF221]] | +0.69 | +0.74 / +0.62 | both halves | 7e-06 | same gene group |
| [[DCLRE1A]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | -0.66 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[CD81]] | -0.64 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[FBXW7]] | -0.62 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[VPS53]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[GNB2]] | -0.60 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[MFN1]] | -0.60 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[MLEC]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN23]] | B | ZSCAN23 activity raises ZSCAN12's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 2.80× lower at baseline in the lines without ZSCAN23 | 0.018 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[ZNF502]] | B | ZNF502 activity raises ZSCAN12's level | lines that do not express ZNF502 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without ZNF502 | 0.025 | ⚠ within organs, on part of the lines; also absent: CXCR4, LINC01611, ZNF506 |
| [[ARMCX1]] | B | ARMCX1 activity raises ZSCAN12's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 2.60× lower at baseline in the lines without ARMCX1 | 0.039 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[ZNF525]] | B | ZNF525 activity raises ZSCAN12's level | lines that do not express ZNF525 (10) vs lines expressing it (40) | 2.27× lower at baseline in the lines without ZNF525 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF331, ZNF577, ZNF83 |
| [[SPART]] | B | SPART activity raises ZSCAN12's level | lines that do not express SPART (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without SPART | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC169, SPART-AS1, FIGN |
| [[ZBED9]] | B | ZBED9 activity raises ZSCAN12's level | lines that do not express ZBED9 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without ZBED9 | 0.092 | ⚠ within organs, on part of the lines; also absent: TDRP, ZNF583, POPDC3 |
| [[ZNF829]] | B | ZNF829 activity raises ZSCAN12's level | lines that do not express ZNF829 (20) vs lines expressing it (30) | 2.37× lower at baseline in the lines without ZNF829 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF568, ZNF880, ZNF625 |
| [[ZNF711]] | B | ZNF711 activity raises ZSCAN12's level | lines that do not express ZNF711 (15) vs lines expressing it (35) | 1.66× lower at baseline in the lines without ZNF711 | 0.094 | ⚠ within organs, on part of the lines; also absent: FRMPD3, RPS6KA6, MIR9-3HG |
| [[SOGA3]] | C | SOGA3 activity raises ZSCAN12's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.91× lower at baseline in the lines without SOGA3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1; co-absent with the target |
| [[KIAA0408]] | C | KIAA0408 activity raises ZSCAN12's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without KIAA0408 | 0.038 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSANTD4]] | B | ZSCAN12 activity raises MSANTD4's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without ZSCAN12 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[IL4I1]] | B | ZSCAN12 activity raises IL4I1's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.05× lower at baseline in the lines without ZSCAN12 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[SRGAP2C]] | B | ZSCAN12 activity raises SRGAP2C's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without ZSCAN12 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[TMEM126B]] | B | ZSCAN12 activity raises TMEM126B's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without ZSCAN12 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[DUSP15]] | B | ZSCAN12 activity raises DUSP15's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without ZSCAN12 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[TTC7A]] | B | ZSCAN12 activity raises TTC7A's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.44× lower at baseline in the lines without ZSCAN12 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[ZNF222]] | B | ZSCAN12 activity raises ZNF222's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.60× lower at baseline in the lines without ZSCAN12 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[RFLNB]] | B | ZSCAN12 activity raises RFLNB's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without ZSCAN12 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[ZNF284]] | B | ZSCAN12 activity raises ZNF284's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.96× lower at baseline in the lines without ZSCAN12 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[XPO1]] | B | ZSCAN12 activity raises XPO1's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.07× lower at baseline in the lines without ZSCAN12 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[CPEB1]] | B | ZSCAN12 activity raises CPEB1's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without ZSCAN12 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[RNF214]] | B | ZSCAN12 activity raises RNF214's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.14× lower at baseline in the lines without ZSCAN12 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.2, 9.9); signed map (2.0, -26.5). **Vector** length 56.1, 9.76% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +24.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +13.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +8.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.2 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.9 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,378,955-28,399,747 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0426, ZNF29K1, ZFP96, dJ29K1.2; previously ZNF305, ZNF96 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43309](https://www.uniprot.org/uniprotkb/O43309) (Zinc finger and SCAN domain-containing protein 12):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [9753](https://www.ncbi.nlm.nih.gov/gene/9753):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13172) · Entrez [9753](https://www.ncbi.nlm.nih.gov/gene/9753) · UniProt [O43309](https://www.uniprot.org/uniprotkb/O43309) · Ensembl [ENSG00000158691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158691)

## Data

Gene col 8181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8181); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8181]; `tensor/DDL_lfc|DDL_z.npy` [8181]; `embed/gene_vectors.npy` [8181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8181 or target_col == 8181). Every well: [[ZSCAN12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
