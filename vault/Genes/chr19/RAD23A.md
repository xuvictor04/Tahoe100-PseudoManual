---
symbol: "RAD23A"
type: "gene"
col: 11015
ensembl_id: "ENSG00000179262"
name: "RAD23 nucleotide excision repair protein A"
location: "19p13.13"
module: 12
arm: "+"
pooled_cpm: 65.71
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RAD23A

*RAD23 nucleotide excision repair protein A* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.51× (z +10.6, q 2e-23, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +4.2, q 0.004, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (HOP62 4.78×, NCI-H460 4.69×, SK-MEL-2 5.22×, A549 5.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HOP62 5.72×, NCI-H1792 7.43×, NCI-H460 5.58×, A549 6.78×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -5.8, q 5e-06, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (CHP-212 0.115×, MIA PaCa-2 0.258×, H4 0.241×, LoVo 0.372×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.394×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP290]] (+0.57, fdr 5e-05), [[RNF214]] (+0.56, fdr 3e-05), [[ATP9B]] (+0.55, fdr 2e-05); moves opposite to [[FUCA1]] (-0.57, fdr 1e-05), [[SMARCD2]] (-0.53, fdr 1e-05), [[LYPLA2]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11015.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (HOP62 4.78×, NCI-H460 4.69×, SK-MEL-2 5.22×, A549 5.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HOP62 5.72×, NCI-H1792 7.43×, NCI-H460 5.58×, A549 6.78×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +10.6 | 2e-23 | 42/43 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +10.0 | 3e-21 | 47/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +7.6 | 4e-12 | 40/45 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.004 | 36/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.53×** | +3.6 | 0.038 | 32/47 (A549, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.49×** | +3.5 | 0.041 | 30/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.3 | 0.067 | 32/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.092 | 29/48 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.29×** | +3.2 | 0.097 | 33/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.44× | +3.1 | 0.12 | 31/48 (NCI-H1792, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11015.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (CHP-212 0.115×, MIA PaCa-2 0.258×, H4 0.241×, LoVo 0.372×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.394×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -5.8 | 5e-06 | 38/48 (CHP-212, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.518× | -3.0 | 0.45 | 32/48 (C-33 A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.710× | -3.0 | 0.45 | 32/48 (SW480, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 72.1 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -12.9) |
| [[A549 (line)]] | wt | 41.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.76× (z +10.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 109 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -12.9) |
| [[HOP62 (line)]] | alt | 52.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +11.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 77.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 56.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 36.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.94× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 37.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 35.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.43× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 48.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 99.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 76.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 58.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 73.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.3) |
| [[A498 (line)]] | wt | 98.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +8.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.35× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 48.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 68.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -14.0) |
| [[HCT15 (line)]] | alt | 85.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 67.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.5) |
| [[LS 180 (line)]] | wt | 77.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 70.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 96.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP290]] | +0.57 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[RNF214]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ATP9B]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TTC1]] | +0.54 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[NMT1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[RPAP3]] | +0.53 | +0.54 / +0.23 | both halves | 5e-04 |  |
| [[WDR70]] | +0.53 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[JPX]] | +0.53 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[METTL2A]] | +0.53 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[MRPS9]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[NEK1]] | +0.52 | +0.56 / +0.26 | both halves | 3e-04 |  |
| [[DCTN6]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUCA1]] | -0.57 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.53 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[LYPLA2]] | -0.50 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[CDIPT]] | -0.48 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[OXR1-AS1]] | -0.48 | -0.07 / -0.40 | ⚠ not reproduced | 0.004 |  |
| [[NIPBL-DT]] | -0.48 | -0.13 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[PIGX]] | -0.48 | -0.20 / -0.46 | both halves | 7e-04 |  |
| [[WDR20]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 | pathway: Deubiquitination |
| [[CXCR4]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[CDK2AP1]] | -0.47 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[SP3]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GUCD1]] | -0.47 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[CST3]] | -0.47 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[BCL2L2]] | -0.46 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[GTPBP1]] | -0.46 | -0.38 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-22.0, -0.3); signed map (-19.5, -25.5). **Vector** length 54.9, 16.8% of its response variance represented; |z| ≥ 3 in 555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.1 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | -0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.1 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.0 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RAD23 nucleotide excision repair protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,945,855-12,953,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HHR23A, MGC111083 |
| Gene groups (HGNC) | Nucleotide excision repair; RAD23 nucleotide excision repair protein family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 7 pathways, smallest: Josephin domain DUBs; DNA Damage Recognition in GG-NER; Formation of Incision Complex in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [P54725](https://www.uniprot.org/uniprotkb/P54725) (Lysine-specific demethylase RAD23A):

> Multifunctional protein that participates in histone H4K20 demethylation, DNA repair, ubiquitin-dependent protein degradation, transcriptional regulation, and viral replication. Specifically demethylates mono-, di- and trimethylated 'Lys-20' of histone H4 (H4K20me1, H4K20me2, H4K20me3, respectively) into unmethylated forms. Activates the transcription of coding genes by demethylating H4K20me1 and the transcription of repetitive elements by demethylating H4K20me3. Involved in modulation of …

**Summary**, from NCBI Gene [5886](https://www.ncbi.nlm.nih.gov/gene/5886):

> The protein encoded by this gene is one of two human homologs of Saccharomyces cerevisiae Rad23, a protein involved in nucleotide excision repair. Proteins in this family have a modular domain structure consisting of an ubiquitin-like domain (UbL), ubiquitin-associated domain 1 (UbA1), XPC-binding domain and UbA2. The protein encoded by this gene plays an important role in nucleotide excision repair and also in delivery of polyubiquitinated proteins to the proteasome. Alternative splicing …

**Accessions** — [HGNC:9812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9812) · Entrez [5886](https://www.ncbi.nlm.nih.gov/gene/5886) · UniProt [P54725](https://www.uniprot.org/uniprotkb/P54725) · Ensembl [ENSG00000179262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179262)

## Data

Gene col 11015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11015); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11015]; `tensor/DDL_lfc|DDL_z.npy` [11015]; `embed/gene_vectors.npy` [11015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11015 or target_col == 11015). Every well: [[RAD23A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD23A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
