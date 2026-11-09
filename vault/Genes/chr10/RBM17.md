---
symbol: "RBM17"
type: "gene"
col: 5563
ensembl_id: "ENSG00000134453"
name: "RNA binding motif protein 17"
location: "10p15.1"
module: 4
arm: "+"
pooled_cpm: 80.22
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RBM17

*RNA binding motif protein 17* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.84× (z +11.2, q 2e-26, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.01× (z +6.7, q 3e-09, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.809× (z -3.9, q 0.056, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.224×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM98B]] (+0.66, fdr 7e-06), [[SSRP1]] (+0.64, fdr 7e-06), [[U2SURP]] (+0.62, fdr 7e-06); moves opposite to [[BBIP1]] (-0.59, fdr 1e-05), [[STX5]] (-0.55, fdr 2e-05), [[SMIM4]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.84×** | +11.2 | 2e-26 | 48/49 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.83×** | +10.7 | 3e-24 | 35/44 (A-427, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.72×** | +9.2 | 6e-18 | 37/45 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +6.7 | 3e-09 | 40/49 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.44×** | +6.5 | 1e-08 | 35/47 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.1 | 8e-08 | 36/48 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.38×** | +6.0 | 2e-07 | 28/47 (HT-29, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +5.8 | 4e-07 | 30/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 7e-07 | 33/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +5.5 | 2e-06 | 32/48 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.3 | 5e-06 | 29/48 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.20×** | +4.9 | 6e-05 | 25/48 (A498, A549, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.4 | 4e-04 | 26/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.0 | 0.003 | 18/37 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.9 | 0.003 | 20/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.004 | 22/48 (Panc 03.27, NCI-H23, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.008 | 22/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.011 | 23/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.036 | 13/48 (NCI-H1792, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.076 | 8/49 (NCI-H460, A549, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.078 | 13/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.085 | 16/48 (NCI-H1792, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5563.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.224×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.9 | 0.056 | 24/48 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.825× | -3.5 | 0.11 | 16/49 (AN3 CA, NCI-H2122, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.882× | -3.3 | 0.21 | 7/48 (A498, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 72.3 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 88.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 2.63× (z +8.9) | — |
| [[SW480 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.56× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 90.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 86.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 85.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.224× (z -9.8) |
| [[Hs 766T (line)]] | wt | 54.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 86.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 84.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H23 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H460 (line)]] | wt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 67.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[PANC-1 (line)]] | alt | 55.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW 900 (line)]] | alt | 58.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 157 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM98B]] | +0.66 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SSRP1]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[U2SURP]] | +0.62 | +0.64 / +0.69 | both halves | 7e-06 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 995 |
| [[PAIP1]] | +0.61 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[BRD7]] | +0.60 | +0.60 / +0.65 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[SMARCE1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[SAAL1]] | +0.58 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[HDAC2]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[DICER1]] | +0.57 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SMG7]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[HNRNPR]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBIP1]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[STX5]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SMIM4]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[C16orf46]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CCNYL1]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[WDR26]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ERO1B]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[RABGEF1]] | -0.50 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ATG2A]] | -0.50 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[TOB2]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CATSPERG]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[POLR2A]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.466). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.8, -37.0); signed map (-18.4, -45.1). **Vector** length 81.4, 21.0% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.8 | +9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +3.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:6,089,034-6,117,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPF45, MGC14439 |
| Gene groups (HGNC) | G-patch domain containing; RNA binding motif containing; Spliceosomal A complex |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I25](https://www.uniprot.org/uniprotkb/Q96I25) (Splicing factor 45):

> Splice factor that binds to the single-stranded 3'AG at the exon/intron border and promotes its utilization in the second catalytic step. Involved in the regulation of alternative splicing and the utilization of cryptic splice sites. Promotes the utilization of a cryptic splice site created by the beta-110 mutation in the HBB gene. The resulting frameshift leads to sickle cell anemia.

**Summary**, from NCBI Gene [84991](https://www.ncbi.nlm.nih.gov/gene/84991):

> This gene encodes an RNA binding protein. The encoded protein is part of the spliceosome complex and functions in the second catalytic step of mRNA splicing. Alternatively spliced transcript variants have been described. Related pseudogenes exist on chromosomes 9 and 15. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:16944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16944) · Entrez [84991](https://www.ncbi.nlm.nih.gov/gene/84991) · UniProt [Q96I25](https://www.uniprot.org/uniprotkb/Q96I25) · Ensembl [ENSG00000134453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134453)

## Data

Gene col 5563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5563); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5563]; `tensor/DDL_lfc|DDL_z.npy` [5563]; `embed/gene_vectors.npy` [5563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5563 or target_col == 5563). Every well: [[RBM17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
