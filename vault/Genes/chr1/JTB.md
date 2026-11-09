---
symbol: "JTB"
type: "gene"
col: 6765
ensembl_id: "ENSG00000143543"
name: "jumping translocation breakpoint"
location: "1q21.3"
module: 24
arm: "+"
pooled_cpm: 34.98
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# JTB

*jumping translocation breakpoint* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +9.0, q 9e-17, up in 41 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.17×, NCI-H1792 7.33×, NCI-H460 5.03×, PANC-1 4.04×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HOP62 3.83×, A-172 2.75×, SNU-423 3.30×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 5.05×, SW480 4.23×, NCI-H1792 5.49×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.415× (z -3.6, q 0.090, down in 29 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.281×, NCI-H2347 0.370×, AsPC-1 0.353×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.271×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX14]] (+0.62, fdr 3e-05), [[RPAIN]] (+0.61, fdr 1e-05), [[ALKBH7]] (+0.60, fdr 3e-04); moves opposite to [[BZW1]] (-0.50, fdr 1e-04), [[KPNA4]] (-0.48, fdr 3e-05), [[GLO1]] (-0.47, fdr 7e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6765.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.17×, NCI-H1792 7.33×, NCI-H460 5.03×, PANC-1 4.04×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HOP62 3.83×, A-172 2.75×, SNU-423 3.30×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 5.05×, SW480 4.23×, NCI-H1792 5.49×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +9.0 | 9e-17 | 41/45 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +7.8 | 2e-12 | 32/37 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +5.0 | 1e-04 | 31/40 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.7 | 3e-04 | 14/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.64×** | +4.0 | 0.007 | 35/45 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.4 | 0.056 | 26/46 (CFPAC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | 1.48× | +3.0 | 0.20 | 23/47 (A549, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6765.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.281×, NCI-H2347 0.370×, AsPC-1 0.353×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.271×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -3.6 | 0.090 | 29/46 (HOP62, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.639×** | -3.6 | 0.090 | 25/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.665× | -3.3 | 0.19 | 27/48 (BT-474, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.33× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 59.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -8.6) |
| [[SW480 (line)]] | alt | 33.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 43.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.05× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 20 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX14]] | +0.62 | +0.43 / +0.77 | both halves | 3e-05 |  |
| [[RPAIN]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.60 | +0.27 / +0.78 | both halves | 3e-04 |  |
| [[MRPS24]] | +0.59 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[WDR83OS]] ⚠ | +0.58 | +0.36 / +0.70 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CNPY2]] | +0.56 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[SNHG9]] | +0.56 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[SELENOM]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[APOC1]] | +0.55 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[MRPL23]] | +0.55 | +0.33 / +0.66 | both halves | 1e-04 |  |
| [[CDK13]] | +0.55 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[PPARA]] | +0.54 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[EAF2]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BZW1]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[KPNA4]] | -0.48 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[GLO1]] | -0.47 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[TRDMT1]] | -0.47 | -0.11 / -0.58 | ⚠ one half (not replicated) | 0.002 |  |
| [[PCNX2]] | -0.47 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[ODC1]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[YWHAZ]] | -0.47 | -0.25 / -0.56 | both halves | 4e-04 |  |
| [[MAPRE1]] | -0.47 | -0.15 / -0.65 | ⚠ one half (not replicated) | 0.001 |  |
| [[TAF1B]] | -0.46 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[NT5E]] | -0.46 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[NES]] | -0.46 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[CD59]] | -0.46 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[CAPN2]] | -0.45 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[GGACT]] | -0.45 | -0.38 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.6, -25.1); signed map (-28.2, 8.0). **Vector** length 58.9, 16.4% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +2.6 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.1 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +0.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.0 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | jumping translocation breakpoint |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,974,269-153,977,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hJT, PAR |
| Matched by | ensembl_id |

**Function**, from UniProt [O76095](https://www.uniprot.org/uniprotkb/O76095) (Protein JTB):

> Required for normal cytokinesis during mitosis. Plays a role in the regulation of cell proliferation. May be a component of the chromosomal passenger complex (CPC), a complex that acts as a key regulator of mitosis. The CPC complex has essential functions at the centromere in ensuring correct chromosome alignment and segregation and is required for chromatin-induced microtubule stabilization and spindle assembly. Increases AURKB activity. Inhibits apoptosis induced by TGFB1 (By similarity). …

**Summary**, from NCBI Gene [10899](https://www.ncbi.nlm.nih.gov/gene/10899):

> Enables protein kinase binding activity. Involved in mitotic cytokinesis and positive regulation of protein kinase activity. Located in cytoplasm; microtubule cytoskeleton; and midbody. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6201) · Entrez [10899](https://www.ncbi.nlm.nih.gov/gene/10899) · UniProt [O76095](https://www.uniprot.org/uniprotkb/O76095) · Ensembl [ENSG00000143543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143543)

## Data

Gene col 6765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6765); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6765]; `tensor/DDL_lfc|DDL_z.npy` [6765]; `embed/gene_vectors.npy` [6765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6765 or target_col == 6765). Every well: [[JTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
