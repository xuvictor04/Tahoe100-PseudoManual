---
symbol: "MED1"
type: "gene"
col: 4643
ensembl_id: "ENSG00000125686"
name: "mediator complex subunit 1"
location: "17q12"
module: 168
arm: "-"
pooled_cpm: 93.77
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# MED1

*mediator complex subunit 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +36.4, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.165×, A-427 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.152×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.529×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SON]] (+0.78, fdr 7e-06), [[CDK12]] (+0.78, fdr 7e-06, ⚠ same locus), [[TAF2]] (+0.77, fdr 7e-06), [[ZNF629]] (+0.74, fdr 7e-06); moves opposite to [[HSPB11]] (-0.71, fdr 7e-06), [[SEC11A]] (-0.70, fdr 7e-06), [[SRP54-AS1]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 22 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +36.4 | 0e+00 | 48/48 (BT-474, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.04×** | +28.3 | 0e+00 | 48/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +23.9 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.18×** | +20.6 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +18.1 | 0e+00 | 45/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.12×** | +15.7 | 0e+00 | 43/49 (BT-474, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +14.1 | 2e-43 | 36/49 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +12.7 | 2e-35 | 45/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.59×** | +12.2 | 2e-32 | 44/48 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.52×** | +11.1 | 8e-27 | 37/48 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +10.9 | 4e-26 | 39/48 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +10.8 | 1e-25 | 39/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +10.0 | 4e-22 | 42/48 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +8.7 | 2e-16 | 43/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +8.7 | 2e-16 | 36/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +8.3 | 3e-15 | 34/48 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +8.1 | 2e-14 | 28/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +6.5 | 3e-09 | 26/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +5.7 | 2e-07 | 29/48 (LOX-IMVI, HT-29, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.165×, A-427 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.152×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.529×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 801 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +36.5) | — |
| [[LoVo (line)]] | wt | 71.6 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +16.7) | — |
| [[NCI-H460 (line)]] | wt | 90.9 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +22.3) | — |
| [[SW480 (line)]] | alt | 107 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +22.0) | — |
| [[HEC-1-A (line)]] | alt | 104 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +21.1) | — |
| [[HOP62 (line)]] | alt | 72.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +19.0) | — |
| [[NCI-H1573 (line)]] | alt | 64.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +23.4) | — |
| [[COLO 205 (line)]] | alt | 90.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +17.8) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.153× (z -10.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 64.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +19.8) | — |
| [[NCI-H2347 (line)]] | alt | 52.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +21.9) | — |
| [[A549 (line)]] | wt | 79.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +27.7) | — |
| [[CFPAC-1 (line)]] | alt | 97.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +19.4) | — |
| [[KATO III (line)]] | alt | 96.0 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[LS 180 (line)]] | wt | 66.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.0) | — |
| [[AsPC-1 (line)]] | alt | 38.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +15.8) | — |
| [[C32 (line)]] | wt | 60.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +17.8) | — |
| [[HS-578T (line)]] | alt | 60.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +19.2) | — |
| [[HT-29 (line)]] | alt | 74.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +20.8) | — |
| [[LOX-IMVI (line)]] | wt | 85.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.6) | — |
| [[Panc 03.27 (line)]] | alt | 88.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.2) | [[Lonafarnib (drug)]] 5 µM 0.152× (z -11.2) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 67.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +26.8) | — |
| [[RKO (line)]] | wt | 121 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 62.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +17.7) | — |
| [[SNU-1 (line)]] | wt | 74.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 81.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.7) | — |
| [[A-427 (line)]] | wt | 119 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.413× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.529× (z -9.6) |
| [[A498 (line)]] | wt | 82.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +20.9) | — |
| [[Hs 766T (line)]] | wt | 49.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 89.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 124 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +18.1) | — |
| [[RPMI-7951 (line)]] | alt | 71.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 65.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +20.6) | — |
| [[SW48 (line)]] | wt | 91.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 100 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.5) | — |
| [[H4 (line)]] | wt | 65.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.1) | — |
| [[J82 (line)]] | alt | 85.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 144 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +17.8) | — |
| [[SW1417 (line)]] | alt | 81.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 63.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 59.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SON]] | +0.78 | +0.82 / +0.63 | both halves | 7e-06 | STRING 455 |
| [[CDK12]] | +0.78 | +0.78 / +0.67 | both halves | 7e-06 | STRING 548; ⚠ same locus (10.2 kb: neighbours can correlate without regulation) |
| [[TAF2]] | +0.77 | +0.81 / +0.64 | both halves | 7e-06 | STRING 862 |
| [[ZNF629]] | +0.74 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[ERCC6L2]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[ASXL2]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[NSD1]] | +0.73 | +0.68 / +0.61 | both halves | 7e-06 | STRING 423 |
| [[DNAJC11]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 | pathway: Mitochondrial biogenesis |
| [[CHD8]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[ZBTB40]] | +0.70 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[THUMPD3]] | +0.70 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB11]] | -0.71 | -0.70 / -0.62 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[SEC11A]] | -0.70 | -0.68 / -0.69 | both halves | 7e-06 | pathway: Respiratory Syncytial Virus Infection Pathway |
| [[SRP54-AS1]] | -0.69 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.68 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[KCTD7]] | -0.67 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[AHDC1]] | -0.67 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[LINC00674]] | -0.65 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[SCAI]] | -0.65 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[CBLB]] | -0.64 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.64 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[PPP1R2]] | -0.64 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[SGK3]] | -0.63 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MED1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM102A]] | C | FAM102A activity lowers MED1's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 1.38× higher at baseline in the lines without FAM102A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **-** arm (projection on the module's main direction -0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-22.1, 11.2); signed map (13.8, -29.5). **Vector** length 111, 34.2% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.4 | +20.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.6 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +28.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +23.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.6 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +10.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +5.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.0 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -3.4 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,404,285-39,451,272 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PBP, TRAP220, RB18A, DRIP230, CRSP200, CRSP1; previously TRIP2, PPARGBP, PPARBP |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 32 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression; Expression of BMAL (ARNTL), CLOCK, and NPAS2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15648](https://www.uniprot.org/uniprotkb/Q15648) (Mediator of RNA polymerase II transcription subunit 1):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [5469](https://www.ncbi.nlm.nih.gov/gene/5469):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. …

**Accessions** — [HGNC:9234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9234) · Entrez [5469](https://www.ncbi.nlm.nih.gov/gene/5469) · UniProt [Q15648](https://www.uniprot.org/uniprotkb/Q15648) · Ensembl [ENSG00000125686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125686)

## Data

Gene col 4643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4643); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4643]; `tensor/DDL_lfc|DDL_z.npy` [4643]; `embed/gene_vectors.npy` [4643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4643 or target_col == 4643). Every well: [[MED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
