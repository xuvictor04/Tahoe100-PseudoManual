---
symbol: "SLC25A3"
type: "gene"
col: 1119
ensembl_id: "ENSG00000075415"
name: "solute carrier family 25 member 3"
location: "12q23.1"
module: 43
arm: "+"
pooled_cpm: 142.95
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# SLC25A3

*solute carrier family 25 member 3* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +8.2, q 1e-13, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.39× (z +3.6, q 0.020, up in 34 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.350×, NCI-H2030 0.400×, AN3 CA 0.340×, C-33 A 0.474×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.325×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.513×; ⚠ cell-cycle shift, explains ~46% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL5]] (+0.59, fdr 1e-05), [[RPL17]] (+0.58, fdr 1e-05), [[RPL7]] (+0.57, fdr 1e-05); moves opposite to [[ZNF436]] (-0.59, fdr 2e-05), [[ZNF252P]] (-0.53, fdr 1e-04), [[CDC42EP1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.11×** | +8.2 | 1e-13 | 46/49 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.80×** | +6.4 | 3e-08 | 44/48 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.75×** | +5.9 | 7e-07 | 31/44 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.74×** | +5.8 | 8e-07 | 43/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.6 | 2e-06 | 44/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.59×** | +4.7 | 2e-04 | 34/45 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.52×** | +4.6 | 3e-04 | 39/48 (COLO 205, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.020 | 34/48 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.38×** | +3.6 | 0.024 | 30/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | **1.36×** | +3.4 | 0.037 | 30/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.34×** | +3.3 | 0.059 | 26/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.067 | 38/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.74×** | +3.1 | 0.074 | 36/48 (C-33 A, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.1 | 0.077 | 28/47 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.82×** | +3.1 | 0.081 | 33/47 (NCI-H1792, C32, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.350×, NCI-H2030 0.400×, AN3 CA 0.340×, C-33 A 0.474×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.325×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.513×; ⚠ cell-cycle shift, explains ~46% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 206 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 82.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A498 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 147 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AN3 CA (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 300 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[MIA PaCa-2 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2030 (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RKO (line)]] | wt | 193 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SHP-77 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SNU-1 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.73× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SNU-423 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AsPC-1 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 102 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 230 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL5]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 | same gene group |
| [[RPL17]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 | same gene group |
| [[RPL7]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RPL9]] ⚠ | +0.57 | +0.54 / +0.54 | both halves | 1e-05 | STRING 477; ⚠ in the vector space only through flagged drug-doses |
| [[RPS3]] ⚠ | +0.57 | +0.52 / +0.54 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; ⚠ in the vector space only through flagged drug-doses |
| [[SLC25A5]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 860 |
| [[RPS14]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[RPL23]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 | same gene group |
| [[RPS17]] ⚠ | +0.54 | +0.48 / +0.56 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL13A]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[UQCRH]] | +0.54 | +0.46 / +0.55 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[RPS10]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[COX7C]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 444 |
| [[RPL35A]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[COX6C]] | +0.53 | +0.42 / +0.55 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF436]] | -0.59 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZNF252P]] | -0.53 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[CDC42EP1]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ZNF620]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ZNF641]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[LIG4]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[RIMOC1]] | -0.49 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[ARCN1]] | -0.48 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[VEZF1]] | -0.48 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[LGALS8]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ARMT1]] | -0.48 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[CGGBP1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-48.3, -28.8); signed map (-60.2, -2.1). **Vector** length 74.4, 28.1% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +1.9 | +3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | +0.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -3.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 25 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:98,593,591-98,606,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PiC, PTP; previously PHC |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Solute carrier family 25 |
| Hallmark sets | MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00325](https://www.uniprot.org/uniprotkb/Q00325) (Solute carrier family 25 member 3):

> Inorganic ion transporter that transports phosphate or copper ions across the mitochondrial inner membrane into the matrix compartment (By similarity). Mediates proton-coupled symport of phosphate ions necessary for mitochondrial oxidative phosphorylation of ADP to ATP (By similarity). Transports copper ions probably in the form of anionic copper(I) complexes to maintain mitochondrial matrix copper pool and to supply copper for cytochrome C oxidase complex assembly. May also play a role in …

**Summary**, from NCBI Gene [5250](https://www.ncbi.nlm.nih.gov/gene/5250):

> The protein encoded by this gene catalyzes the transport of phosphate into the mitochondrial matrix, either by proton cotransport or in exchange for hydroxyl ions. The protein contains three related segments arranged in tandem which are related to those found in other characterized members of the mitochondrial carrier family. Both the N-terminal and C-terminal regions of this protein protrude toward the cytosol. Multiple alternatively spliced transcript variants have been isolated. [provided by …

**Accessions** — [HGNC:10989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10989) · Entrez [5250](https://www.ncbi.nlm.nih.gov/gene/5250) · UniProt [Q00325](https://www.uniprot.org/uniprotkb/Q00325) · Ensembl [ENSG00000075415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075415)

## Data

Gene col 1119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1119); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1119]; `tensor/DDL_lfc|DDL_z.npy` [1119]; `embed/gene_vectors.npy` [1119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1119 or target_col == 1119). Every well: [[SLC25A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC25A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
