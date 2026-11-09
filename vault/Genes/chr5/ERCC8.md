---
symbol: "ERCC8"
type: "gene"
col: 544
ensembl_id: "ENSG00000049167"
name: "ERCC excision repair 8, CSA ubiquitin ligase complex subunit"
location: "5q12.1"
module: 4
arm: "+"
pooled_cpm: 46.62
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ERCC8

*ERCC excision repair 8, CSA ubiquitin ligase complex subunit* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.38× (z +19.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.844× (z -5.4, q 3e-05, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.265×, C-33 A 0.210×, AN3 CA 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (SHP-77 0.280×, J82 0.359×, PANC-1 0.484×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.234×, SW 1271 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.205×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0727×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF346]] (+0.66, fdr 7e-06), [[MRPS9]] (+0.65, fdr 7e-06), [[COX10]] (+0.64, fdr 7e-06); moves opposite to [[BMF]] (-0.56, fdr 2e-05), [[ING1]] (-0.56, fdr 1e-05), [[BCL2L11]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.38×** | +19.7 | 0e+00 | 45/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.31×** | +18.0 | 0e+00 | 44/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.95×** | +15.1 | 0e+00 | 41/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.56×** | +9.8 | 2e-20 | 34/47 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +9.1 | 1e-17 | 35/44 (LOX-IMVI, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +7.4 | 1e-11 | 35/48 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +7.1 | 8e-11 | 25/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.37×** | +7.1 | 1e-10 | 25/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +6.8 | 8e-10 | 27/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +6.7 | 1e-09 | 32/48 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +6.6 | 2e-09 | 30/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.6 | 2e-09 | 27/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.33×** | +6.5 | 3e-09 | 26/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +5.9 | 1e-07 | 26/49 (CFPAC-1, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +5.9 | 2e-07 | 24/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +4.5 | 2e-04 | 15/48 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.2 | 6e-04 | 10/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.001 | 12/48 (HT-29, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.001 | 15/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 12/48 (NCI-H2347, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.265×, C-33 A 0.210×, AN3 CA 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (SHP-77 0.280×, J82 0.359×, PANC-1 0.484×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.234×, SW 1271 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.205×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0727×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -5.4 | 3e-05 | 19/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.804×** | -4.8 | 6e-04 | 19/47 (LS 180, NCI-H2030, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.6 | 6e-04 | 0/48 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.814×** | -4.5 | 0.001 | 22/47 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.773×** | -4.2 | 0.004 | 16/48 (AN3 CA, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | 0.849× | -3.7 | 0.020 | 18/48 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.857× | -3.5 | 0.037 | 9/48 (AsPC-1, KATO III, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.759×** | -3.2 | 0.089 | 16/48 (HT-29, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 65.5 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 40.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.21× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 41.1 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 51.7 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.41× (z +15.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.484× (z -9.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 38.5 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.28× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 36.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.74× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 50.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.46× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 22.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.56× (z +11.3) | — |
| [[LoVo (line)]] | wt | 60.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 50.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.00× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 49.6 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -20.6) |
| [[A-427 (line)]] | wt | 56.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 49.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.4) | — |
| [[H4 (line)]] | wt | 36.7 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.04× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 35.6 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.38× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 34.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 55.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 66.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 37.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.81× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 95.0 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 62.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 81.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 38.5 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.64× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 30.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.45× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.37× (z +9.3) | — |
| [[J82 (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.359× (z -10.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 69.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.91× (z +9.3) | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0727× (z -9.2) |
| [[SW48 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF346]] | +0.66 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[MRPS9]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[COX10]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[LARS2]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TANGO6]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NAA25]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[GFM1]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[QRSL1]] | +0.63 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TOMM40L]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ALKBH8]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CLPB]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CWC27]] | +0.62 | +0.68 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMF]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ING1]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[BCL2L11]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LNX2]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TESK2]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[VASN]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TXNDC16]] | -0.51 | -0.42 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.6, -1.4); signed map (-18.5, -23.2). **Vector** length 115, 30.7% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.8 | +19.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.5 | +18.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.6 | +15.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +5.4 | +9.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.0 | +9.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +6.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 8, CSA ubiquitin ligase complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:60,866,454-60,945,073 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSA; previously CKN1 |
| Gene groups (HGNC) | WD repeat domain containing; ERCC excision repair associated |
| Hallmark sets | DNA_REPAIR |
| Reactome | 7 pathways, smallest: Formation of TC-NER Pre-Incision Complex; Gap-filling DNA repair synthesis and ligation in TC-NER; Dual incision in TC-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13216](https://www.uniprot.org/uniprotkb/Q13216) (DNA excision repair protein ERCC-8):

> Substrate-recognition component of the CSA complex, a DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex, involved in transcription-coupled nucleotide excision repair (TC-NER), a process during which RNA polymerase II-blocking lesions are rapidly removed from the transcribed strand of active genes. Following recruitment to lesion-stalled RNA polymerase II (Pol II), the CSA complex mediates ubiquitination of Pol II subunit POLR2A/RPB1 at 'Lys-1268', a critical TC-NER checkpoint, governing …

**Summary**, from NCBI Gene [1161](https://www.ncbi.nlm.nih.gov/gene/1161):

> This gene encodes a WD repeat protein, which interacts with Cockayne syndrome type B (CSB) protein and with p44 protein, a subunit of the RNA polymerase II transcription factor IIH. Mutations in this gene have been identified in patients with hereditary disease Cockayne syndrome (CS). CS cells are abnormally sensitive to ultraviolet radiation and are defective in the repair of transcriptionally active genes. Several transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:3439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3439) · Entrez [1161](https://www.ncbi.nlm.nih.gov/gene/1161) · UniProt [Q13216](https://www.uniprot.org/uniprotkb/Q13216) · Ensembl [ENSG00000049167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049167)

## Data

Gene col 544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 544); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 544]; `tensor/DDL_lfc|DDL_z.npy` [544]; `embed/gene_vectors.npy` [544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 544 or target_col == 544). Every well: [[ERCC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
