---
symbol: "CFAP298"
type: "gene"
col: 8213
ensembl_id: "ENSG00000159079"
name: "cilia and flagella associated protein 298"
location: "21q22.11"
module: 1
arm: "+"
pooled_cpm: 37.59
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CFAP298

*cilia and flagella associated protein 298* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.50× (z +10.0, q 1e-20, up in 32 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.27× (z +3.6, q 0.018, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.692× (z -4.1, q 0.020, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.154×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM28]] (+0.63, fdr 1e-05), [[MPHOSPH6]] (+0.58, fdr 1e-05), [[MAK16]] (+0.57, fdr 8e-06); moves opposite to [[GNAS]] (-0.56, fdr 1e-05), [[PSAP]] (-0.52, fdr 2e-05), [[SAP30-DT]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.50×** | +10.0 | 1e-20 | 32/40 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.66×** | +9.4 | 1e-18 | 42/46 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.82×** | +6.2 | 8e-08 | 31/43 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.5 | 4e-06 | 40/46 (CFPAC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.58×** | +5.0 | 8e-05 | 34/48 (LS 180, HEC-1-A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.46×** | +4.2 | 0.003 | 25/47 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.39×** | +3.7 | 0.017 | 24/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.018 | 22/48 (A-172, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.27×** | +3.6 | 0.018 | 24/48 (NCI-H2030, COLO 205, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +3.6 | 0.018 | 28/47 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +3.3 | 0.041 | 22/48 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.34×** | +3.3 | 0.041 | 21/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.041 | 24/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.079 | 22/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.31×** | +3.1 | 0.082 | 20/48 (J82, HS-578T, …) | all doses, flat | position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.082 | 19/48 (Hs 766T, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8213.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.154×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.020 | 27/48 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -3.8 | 0.043 | 31/48 (RKO, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.736× | -3.3 | 0.17 | 20/47 (LS 180, SNU-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.820× | -3.0 | 0.29 | 21/48 (PANC-1, HT-29, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW480 (line)]] | alt | 60.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AsPC-1 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HEC-1-A (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 46.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM28]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MAK16]] | +0.57 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[ZNHIT6]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[BMS1]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RRS1]] | +0.54 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DDX10]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[YLPM1]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[EIF2B3]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RUVBL1]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 | STRING 443 |
| [[SMARCAD1]] | +0.51 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[AGGF1]] | +0.51 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[PSAP]] | -0.52 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[SAP30-DT]] | -0.52 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[FAM229A]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMEM72-AS1]] | -0.49 | -0.16 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[HCG27]] | -0.48 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[TAGAP-AS1]] | -0.47 | -0.26 / -0.39 | both halves | 3e-04 |  |
| [[MICA]] | -0.46 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[B3GNT4]] | -0.45 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[SEC24B-AS1]] | -0.45 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[FEM1C]] | -0.45 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RDH5]] | -0.45 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[ATG9A]] | -0.45 | -0.37 / -0.52 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.3, -39.6); signed map (-2.4, -42.1). **Vector** length 69.5, 16.7% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.6 | +5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.5 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.4 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.2 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | +1.1 | -1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -3.8 | +6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -1.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.0 | -0.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 298 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:32,592,079-32,612,603 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20467, FBB18, CILD26, Kur, DNAAF16; previously C21orf48, C21orf59 |
| Gene groups (HGNC) | Cilia and flagella associated; Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P57076](https://www.uniprot.org/uniprotkb/P57076) (Cilia- and flagella-associated protein 298):

> Plays a role in motile cilium function, possibly by acting on outer dynein arm assembly. Seems to be important for initiation rather than maintenance of cilium motility (By similarity). Required for correct positioning of the cilium at the apical cell surface, suggesting an additional role in the planar cell polarity (PCP) pathway (By similarity). May suppress canonical Wnt signaling activity (By similarity).

**Summary**, from NCBI Gene [56683](https://www.ncbi.nlm.nih.gov/gene/56683):

> This gene encodes a protein that plays a critical role in dynein arm assembly and motile cilia function. Mutations in this gene result in primary ciliary dyskinesia. Naturally occuring readthrough transcription occurs from this locus to the downstream t-complex 10 like (TCP10L) gene. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:1301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1301) · Entrez [56683](https://www.ncbi.nlm.nih.gov/gene/56683) · UniProt [P57076](https://www.uniprot.org/uniprotkb/P57076) · Ensembl [ENSG00000159079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159079)

## Data

Gene col 8213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8213); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8213]; `tensor/DDL_lfc|DDL_z.npy` [8213]; `embed/gene_vectors.npy` [8213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8213 or target_col == 8213). Every well: [[CFAP298 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP298.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
