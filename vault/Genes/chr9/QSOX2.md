---
symbol: "QSOX2"
type: "gene"
col: 9160
ensembl_id: "ENSG00000165661"
name: "quiescin sulfhydryl oxidase 2"
location: "9q34.3"
module: 18
arm: "+"
pooled_cpm: 23.69
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# QSOX2

*quiescin sulfhydryl oxidase 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.40× (z +16.3, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0877×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.463×; ⚠ cell-cycle shift, explains ~62% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0849×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (H4 0.0760×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAD]] (+0.78, fdr 7e-06), [[CHID1]] (+0.74, fdr 7e-06), [[POFUT1]] (+0.72, fdr 7e-06); moves opposite to [[MPHOSPH8]] (-0.58, fdr 1e-05), [[RSRC2]] (-0.57, fdr 3e-05), [[SNRPB2]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.40×** | +16.3 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.29×** | +15.5 | 0e+00 | 44/48 (KATO III, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +12.7 | 2e-34 | 31/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +12.3 | 2e-32 | 37/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.91×** | +12.0 | 4e-31 | 38/48 (LS 180, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.90×** | +12.0 | 5e-31 | 40/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.88×** | +11.7 | 7e-30 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +11.7 | 1e-29 | 40/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.78×** | +10.4 | 2e-23 | 24/36 (LS 180, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +9.8 | 1e-20 | 37/47 (HT-29, Hs 766T, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.56×** | +7.9 | 1e-13 | 30/46 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +7.0 | 1e-10 | 34/48 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.43×** | +6.7 | 9e-10 | 27/45 (HS-578T, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +6.7 | 9e-10 | 27/47 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +6.0 | 7e-08 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 5e-06 | 23/47 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +4.9 | 3e-05 | 17/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.002 | 15/46 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.002 | 11/47 (J82, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.020 | 4/47 (AsPC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.030 | 13/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.036 | 6/48 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.062 | 6/48 (AsPC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9160.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0877×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.463×; ⚠ cell-cycle shift, explains ~62% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0849×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (H4 0.0760×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entrectinib (drug)]] 5 µM |  | 0.833× | -3.5 | 0.27 | 11/47 (NCI-H2347, A-427, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.846× | -3.2 | 0.35 | 8/48 (C32, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | 0.851× | -3.1 | 0.38 | 12/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 14.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 15.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.92× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 45.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0849× (z -9.8) |
| [[H4 (line)]] | wt | 23.1 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0760× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[NCI-H2347 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 24.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +9.4) | — |
| [[RKO (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0877× (z -11.1) |
| [[SHP-77 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0980× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.101× (z -9.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAD]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[CHID1]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[POFUT1]] | +0.72 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[PFAS]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[XPO5]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[POLD2]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[NOC2L]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MDN1]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[RFT1]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.64 | +0.57 / +0.68 | both halves | 8e-06 |  |
| [[EMC1]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH8]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[RSRC2]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SNRPB2]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[GPBP1]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SNRNP27]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MSX1]] | -0.54 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[FRG1]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PPP1R12A]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[NRBF2]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[IFRD1]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[UBB]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.8, -36.6); signed map (-7.9, -47.6). **Vector** length 76.5, 15.1% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +16.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.6 | +11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.6 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.6 | +10.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.5 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | quiescin sulfhydryl oxidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,206,333-136,245,812 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SOXN, DKFZp762A2013; previously QSCN6L1 |
| Gene groups (HGNC) | Flavoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZRP7](https://www.uniprot.org/uniprotkb/Q6ZRP7) (Sulfhydryl oxidase 2):

> Sulfhydryl oxidase that catalyzes the oxidation of protein thiol groups to form disulfide bonds, with the reduction of oxygen to hydrogen peroxide (By similarity). May contribute to disulfide bond formation in secreted proteins (By similarity). May play a role in regulating the sensitization of neuroblastoma cells for interferon-gamma-induced apoptosis. Required for normal ovarian function (By similarity).

**Summary**, from NCBI Gene [169714](https://www.ncbi.nlm.nih.gov/gene/169714):

> QSOX2 is a member of the sulfhydryl oxidase/quiescin-6 (Q6) family (QSOX1; MIM 603120) that regulates the sensitization of neuroblastoma cells for IFN-gamma (IFNG; MIM 147570)-induced cell death (Wittke et al., 2003 [PubMed 14633699]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:30249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30249) · Entrez [169714](https://www.ncbi.nlm.nih.gov/gene/169714) · UniProt [Q6ZRP7](https://www.uniprot.org/uniprotkb/Q6ZRP7) · Ensembl [ENSG00000165661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165661)

## Data

Gene col 9160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9160); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9160]; `tensor/DDL_lfc|DDL_z.npy` [9160]; `embed/gene_vectors.npy` [9160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9160 or target_col == 9160). Every well: [[QSOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QSOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
