---
symbol: "DPF2"
type: "gene"
col: 5485
ensembl_id: "ENSG00000133884"
name: "double PHD fingers 2"
location: "11q13.1"
module: 12
arm: "+"
pooled_cpm: 34.54
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DPF2

*double PHD fingers 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +17.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.599× (z -10.3, q 4e-22, down in 22 of 36 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.168×, SW48 0.243×, HepG2/C3A 0.202×, SNU-1 0.237×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 0.115×, LoVo 0.187×, HEC-1-A 0.298×, SNU-423 0.340×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H1792 0.170×, LOX-IMVI 0.354×, HT-29 0.280×, CFPAC-1 0.382×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COIL]] (+0.72, fdr 7e-06), [[TBCC]] (+0.71, fdr 7e-06), [[THAP3]] (+0.70, fdr 7e-06); moves opposite to [[SMG1P3]] (-0.61, fdr 1e-05), [[HNRNPA3]] (-0.61, fdr 1e-05), [[RBBP7]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +17.8 | 0e+00 | 45/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +14.0 | 3e-42 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +11.9 | 3e-30 | 36/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.3 | 2e-27 | 40/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +8.8 | 2e-16 | 30/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +7.7 | 2e-12 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +7.4 | 1e-11 | 31/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.5 | 7e-09 | 27/46 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 20/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.8 | 1e-04 | 23/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +4.3 | 9e-04 | 23/47 (HOP62, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.001 | 18/48 (PANC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.22×** | +4.2 | 0.001 | 20/46 (SW1417, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.002 | 14/47 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.003 | 19/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.005 | 18/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.7 | 0.006 | 16/48 (LoVo, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.022 | 16/48 (PANC-1, SW48, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.030 | 13/46 (NCI-H460, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5485.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.168×, SW48 0.243×, HepG2/C3A 0.202×, SNU-1 0.237×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 0.115×, LoVo 0.187×, HEC-1-A 0.298×, SNU-423 0.340×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H1792 0.170×, LOX-IMVI 0.354×, HT-29 0.280×, CFPAC-1 0.382×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -10.3 | 4e-22 | 22/36 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.641×** | -9.3 | 4e-18 | 29/43 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -9.0 | 4e-17 | 29/43 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.6 | 0.044 | 2/48 (SW 1088, SW 1271) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.903× | -3.0 | 0.28 | 9/48 (SHP-77, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +21.0) | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -10.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 22.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -16.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 31.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 81.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -12.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.6) | — |
| [[A-427 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -16.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -9.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.6) | — |
| [[J82 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.541× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COIL]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[TBCC]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[THAP3]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MED18]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ZSWIM1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[EID2]] | +0.68 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[NAA30]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[GFER]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[KBTBD4]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.67 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P3]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.59 | -0.48 / -0.56 | both halves | 2e-05 | pathway: ATP-dependent chromatin remodelers |
| [[TXNDC5]] | -0.58 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[TFDP1]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[FAM20B]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.2, 4.7); signed map (0.4, -13.3). **Vector** length 89.6, 19.2% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +17.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +14.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.2 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.6 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -9.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -2.7 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -0.2 |
|  | [[venetoclax (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -0.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | double PHD fingers 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,333,843-65,354,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ubi-d4, BAF45d, SMARCG2; previously REQ |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PHD finger proteins; BAF complex subunits |
| Reactome | 16 pathways, smallest: Formation of the canonical BAF (cBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex; Formation of neuronal progenitor and neuronal BAF (npBAF and nBAF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92785](https://www.uniprot.org/uniprotkb/Q92785) (Zinc finger protein ubi-d4):

> Plays an active role in transcriptional regulation by binding modified histones H3 and H4. Is a negative regulator of myeloid differentiation of hematopoietic progenitor cells. Might also have a role in the development and maturation of lymphoid cells (By similarity). Involved in the regulation of non-canonical NF-kappa-B pathway.

**Summary**, from NCBI Gene [5977](https://www.ncbi.nlm.nih.gov/gene/5977):

> The protein encoded by this gene is a member of the d4 domain family, characterized by a zinc finger-like structural motif. This protein functions as a transcription factor which is necessary for the apoptotic response following deprivation of survival factors. It likely serves a regulatory role in rapid hematopoietic cell growth and turnover. This gene is considered a candidate gene for multiple endocrine neoplasia type I, an inherited cancer syndrome involving multiple parathyroid, …

**Accessions** — [HGNC:9964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9964) · Entrez [5977](https://www.ncbi.nlm.nih.gov/gene/5977) · UniProt [Q92785](https://www.uniprot.org/uniprotkb/Q92785) · Ensembl [ENSG00000133884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133884)

## Data

Gene col 5485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5485); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5485]; `tensor/DDL_lfc|DDL_z.npy` [5485]; `embed/gene_vectors.npy` [5485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5485 or target_col == 5485). Every well: [[DPF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
