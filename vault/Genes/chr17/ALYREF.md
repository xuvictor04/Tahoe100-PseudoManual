---
symbol: "ALYREF"
type: "gene"
col: 11436
ensembl_id: "ENSG00000183684"
name: "Aly/REF export factor"
location: "17q25.3"
module: 157
arm: "+"
pooled_cpm: 14.11
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# ALYREF

*Aly/REF export factor* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.73× (z +11.1, q 1e-25, up in 37 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.44× (z +5.7, q 2e-06, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.832× (z -4.1, q 0.027, down in 28 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Larotrectinib (drug)]] 5 µM in 1 line (CHP-212 0.0913×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.148×; ⚠ cell-cycle shift, explains ~68% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMPD4BP]] (+0.65, fdr 7e-06), [[FIS1]] (+0.58, fdr 1e-05), [[NDOR1]] (+0.57, fdr 1e-05); moves opposite to [[DSG2]] (-0.49, fdr 2e-05), [[ENPP4]] (-0.47, fdr 5e-05), [[CAST]] (-0.46, fdr 1e-04).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **5.73×** | +11.1 | 1e-25 | 37/37 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **4.59×** | +9.3 | 4e-18 | 26/26 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.44×** | +7.8 | 8e-13 | 43/46 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.80×** | +6.7 | 3e-09 | 29/31 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +5.7 | 2e-06 | 34/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **2.28×** | +5.0 | 5e-05 | 34/42 (SK-MEL-2, NCI-H1573, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.14×** | +4.8 | 1e-04 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.0 | 0.005 | 23/41 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.69×** | +3.8 | 0.008 | 33/47 (NCI-H1573, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.83×** | +3.8 | 0.008 | 27/44 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.80×** | +3.7 | 0.010 | 27/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.17×** | +3.5 | 0.021 | 30/45 (SHP-77, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.70×** | +3.3 | 0.035 | 22/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.69×** | +3.3 | 0.037 | 23/46 (LoVo, SW1417, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.03×** | +3.2 | 0.050 | 24/46 (SK-MEL-2, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.00×** | +3.1 | 0.062 | 25/46 (SW480, SW48, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.99×** | +3.1 | 0.063 | 22/46 (NCI-H23, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.95×** | +3.0 | 0.076 | 18/46 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11436.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Larotrectinib (drug)]] 5 µM in 1 line (CHP-212 0.0913×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.148×; ⚠ cell-cycle shift, explains ~68% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.832×** | -4.1 | 0.027 | 28/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.582× | -3.4 | 0.11 | 25/47 (BT-474, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.655× | -3.4 | 0.11 | 29/48 (KATO III, A498, …) | rises with dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.618× | -3.1 | 0.25 | 24/47 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.619× | -3.1 | 0.25 | 23/48 (SW480, H4, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.06 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW480 (line)]] | alt | 16.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.38× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 9.96 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 16.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.78× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 12.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.54× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -8.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A498 (line)]] | wt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 1 | — | [[Larotrectinib (drug)]] 5 µM 0.0913× (z -9.0) |
| [[Hs 766T (line)]] | wt | 6.24 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 7.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.51× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 8.51 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 9.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.34× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4BP]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[FIS1]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[NDOR1]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[NDUFS6]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.55 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[SNHG10]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[HDAC7]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TIMM23B]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[AKT2]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PIDD1]] | +0.53 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SH2B1]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CCNL2]] | +0.53 | +0.54 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSG2]] | -0.49 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ENPP4]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CAST]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[PABPC1]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 | same gene group; STRING 774 |
| [[SCOC]] | -0.45 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ZBTB41]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CPNE3]] | -0.45 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[THNSL1]] | -0.44 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[SDCBP]] | -0.44 | -0.56 / -0.47 | both halves | 2e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[NAMPTP1]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[CTBS]] | -0.44 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[IQGAP1]] | -0.43 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.3, -35.8); signed map (-44.9, -25.5). **Vector** length 56.6, 13.0% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.6 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.5 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | +1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Aly/REF export factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,887,835-81,891,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALY, BEF, ALY/REF, REF; previously THOC4 |
| Gene groups (HGNC) | RNA binding motif containing; THO complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 14 pathways, smallest: Transport of the SLBP independent Mature mRNA; Transport of the SLBP Dependant Mature mRNA; Transport of Mature mRNA Derived from an Intronless Transcript |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V81](https://www.uniprot.org/uniprotkb/Q86V81) (THO complex subunit 4):

> Functions as an mRNA export adapter; component of the transcription/export (TREX) complex which is thought to couple mRNA transcription, processing and nuclear export, and specifically associates with spliced mRNA and not with unspliced pre-mRNA. TREX is recruited to spliced mRNAs by a transcription-independent mechanism, binds to mRNA upstream of the exon-junction complex (EJC) and is recruited in a splicing- and cap-dependent manner to a region near the 5' end of the mRNA where it functions …

**Summary**, from NCBI Gene [10189](https://www.ncbi.nlm.nih.gov/gene/10189):

> The protein encoded by this gene is a heat stable, nuclear protein and functions as a molecular chaperone. It is thought to regulate dimerization, DNA binding, and transcriptional activity of basic region-leucine zipper (bZIP) proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19071) · Entrez [10189](https://www.ncbi.nlm.nih.gov/gene/10189) · UniProt [Q86V81](https://www.uniprot.org/uniprotkb/Q86V81) · Ensembl [ENSG00000183684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183684)

## Data

Gene col 11436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11436); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11436]; `tensor/DDL_lfc|DDL_z.npy` [11436]; `embed/gene_vectors.npy` [11436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11436 or target_col == 11436). Every well: [[ALYREF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALYREF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
