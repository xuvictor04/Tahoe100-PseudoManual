---
symbol: "UQCRC2"
type: "gene"
col: 6446
ensembl_id: "ENSG00000140740"
name: "ubiquinol-cytochrome c reductase core protein 2"
location: "16p12.2"
module: 207
arm: "+"
pooled_cpm: 98.63
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# UQCRC2

*ubiquinol-cytochrome c reductase core protein 2* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +11.8, q 3e-29, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.267×, COLO 205 0.363×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HCT15 0.351×, AsPC-1 0.445×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0948×); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.103×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.261×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC39A9]] (+0.59, fdr 1e-05), [[INTS8]] (+0.56, fdr 1e-05), [[VDAC1P8]] (+0.54, fdr 3e-05); moves opposite to [[CENPB]] (-0.50, fdr 6e-05), [[GPR153]] (-0.50, fdr 4e-05), [[PPM1G]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 207]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +11.8 | 3e-29 | 40/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +9.6 | 3e-19 | 30/48 (PANC-1, NCI-H2030, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.43×** | +7.7 | 3e-12 | 32/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +7.4 | 1e-11 | 29/49 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 9e-09 | 33/48 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.3 | 2e-08 | 35/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +6.0 | 1e-07 | 34/49 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.30×** | +5.2 | 2e-05 | 30/48 (BT-474, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.1 | 2e-05 | 31/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +5.0 | 3e-05 | 28/48 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 4e-05 | 31/48 (Hs 766T, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.26×** | +4.8 | 6e-05 | 26/48 (PANC-1, SNU-1, …) | top dose only | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.47×** | +4.4 | 5e-04 | 23/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 7e-04 | 22/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.003 | 21/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.004 | 5/49 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.007 | 24/48 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.013 | 17/48 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.013 | 15/48 (J82, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.016 | 13/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.017 | 15/48 (SNU-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.033 | 16/48 (SNU-1, C32, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.267×, COLO 205 0.363×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HCT15 0.351×, AsPC-1 0.445×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0948×); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.103×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.261×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.840× | -3.9 | 0.065 | 18/49 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.852× | -3.6 | 0.11 | 18/47 (COLO 205, A549, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.861× | -3.2 | 0.22 | 16/47 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.862× | -3.1 | 0.22 | 11/48 (SW 900, HT-29, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.871× | -3.1 | 0.22 | 12/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.872× | -3.0 | 0.22 | 9/48 (NCI-H1573, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 90.8 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +15.3) | — |
| [[KATO III (line)]] | alt | 146 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +16.0) | — |
| [[PANC-1 (line)]] | alt | 115 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 148 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.9) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 137 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 153 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 74.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.4) ⚠ cell-cycle shift, explains ~15% of this change | [[Lonafarnib (drug)]] 5 µM 0.198× (z -9.1) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 79.8 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0948× (z -10.0) |
| [[A498 (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 73.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.3) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[HOP62 (line)]] | alt | 55.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 140 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 73.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.7) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.261× (z -9.4) |
| [[J82 (line)]] | alt | 93.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.6) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[LOX-IMVI (line)]] | wt | 95.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 140 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 69.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.3) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[NCI-H2030 (line)]] | alt | 96.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 98.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.101× (z -8.8) |
| [[SW480 (line)]] | alt | 98.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.5) | — |
| [[A-172 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A9]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[INTS8]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[VDAC1P8]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[NDUFB5]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 976 |
| [[PDHX]] | +0.53 | +0.45 / +0.47 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[EMC1-AS1]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[GTF2B]] | +0.52 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ECD]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[EIF2A]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MRPL30]] | +0.52 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[POLR2A]] | +0.51 | +0.50 / +0.40 | both halves | 4e-05 |  |
| [[EPHX1]] | +0.51 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPB]] | -0.50 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[GPR153]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PPM1G]] | -0.49 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[ARHGAP23]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ACOT9]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[LUZP1]] | -0.47 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[LYSMD4]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[CELF1]] | -0.46 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[ZNF212]] | -0.46 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[CAB39]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[CLCF1]] | -0.46 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | -0.46 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-20.0, 17.8); signed map (-2.1, 3.9). **Vector** length 94.2, 24.1% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +5.4 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.6 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +5.1 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.9 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.6 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase core protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:21,953,288-21,983,660 (+) |
| Ensembl biotype | protein_coding |
| Also known as | QCR2, UQCR2 |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits; M16 metallopeptidases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Complex III assembly; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P22695](https://www.uniprot.org/uniprotkb/P22695) (Cytochrome b-c1 complex subunit 2, mitochondrial):

> Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular …

**Summary**, from NCBI Gene [7385](https://www.ncbi.nlm.nih.gov/gene/7385):

> The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:12586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12586) · Entrez [7385](https://www.ncbi.nlm.nih.gov/gene/7385) · UniProt [P22695](https://www.uniprot.org/uniprotkb/P22695) · Ensembl [ENSG00000140740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140740)

## Data

Gene col 6446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6446); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6446]; `tensor/DDL_lfc|DDL_z.npy` [6446]; `embed/gene_vectors.npy` [6446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6446 or target_col == 6446). Every well: [[UQCRC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCRC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
