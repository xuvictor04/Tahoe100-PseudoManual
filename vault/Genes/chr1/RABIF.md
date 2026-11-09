---
symbol: "RABIF"
type: "gene"
col: 11375
ensembl_id: "ENSG00000183155"
name: "RAB interacting factor"
location: "1q32.1"
module: 3
arm: "+"
pooled_cpm: 9.97
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RABIF

*RAB interacting factor* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.78× (z +8.0, q 7e-13, up in 26 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.36× (z +4.4, q 0.003, up in 8 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.579× (z -11.2, q 2e-26, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNQ]] (+0.60, fdr 1e-05), [[MAP1S]] (+0.60, fdr 3e-05), [[POP7]] (+0.59, fdr 2e-05); moves opposite to [[TOP2B]] (-0.62, fdr 1e-05), [[PAPOLA]] (-0.60, fdr 1e-04), [[TMEM123]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +8.0 | 7e-13 | 26/39 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 0.003 | 8/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.029 | 8/46 (BT-474, A549, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.036 | 8/47 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.036 | 8/43 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.036 | 5/41 (A549, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.067 | 8/44 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.067 | 5/44 (SHP-77, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.14 | 5/43 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.579×** | -11.2 | 2e-26 | 30/45 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -6.4 | 4e-08 | 23/46 (A-427, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.674×** | -5.7 | 2e-06 | 19/33 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -5.6 | 2e-06 | 21/47 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -5.1 | 3e-05 | 20/41 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.523×** | -4.9 | 8e-05 | 20/46 (RPMI-7951, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -4.6 | 4e-04 | 6/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.749×** | -4.2 | 0.002 | 18/43 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | **0.830×** | -3.8 | 0.008 | 15/44 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.010 | 17/45 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.786×** | -3.5 | 0.023 | 12/47 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.781×** | -3.3 | 0.041 | 5/47 (C32, A498, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.658×** | -3.2 | 0.064 | 6/48 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.8 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -10.8) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -13.8) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A549 (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.2) |
| [[HT-29 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0437× (z -16.9) ⚠ cell-cycle shift, explains ~2% of this change |
| [[J82 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -10.3) ⚠ cell-cycle shift, explains ~1% of this change |
| [[PANC-1 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -8.7) |
| [[A498 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNQ]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MAP1S]] | +0.60 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[POP7]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[VPS37C]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC4]] | +0.58 | +0.36 / +0.65 | both halves | 9e-05 | STRING 550 |
| [[YRDC]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NOP10]] ⚠ | +0.57 | +0.47 / +0.60 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF611]] | +0.57 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[CCDC127]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[DUSP18]] | +0.56 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[MTF1]] | +0.56 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[EMC6]] | +0.55 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[ZXDC]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP2B]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PAPOLA]] | -0.60 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[TMEM123]] | -0.57 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[MATR3]] | -0.56 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[CNOT1]] | -0.55 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[SH3BGRL]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PCM1]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[CUL4B]] | -0.54 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[RHOBTB3]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[LMBRD2]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[UBR5]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[COL12A1]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RABIF's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.0, -23.9); signed map (-33.3, 3.2). **Vector** length 66.0, 10.4% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | -4.3 | -2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB interacting factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,878,282-202,889,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mss4; previously RASGRF3 |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [P47224](https://www.uniprot.org/uniprotkb/P47224) (Guanine nucleotide exchange factor MSS4):

> Guanine-nucleotide-releasing protein that acts on members of the SEC4/YPT1/RAB subfamily. Stimulates GDP release from both YPT1, RAB3A and RAB10, but is less active on these proteins than on the SEC4 protein. Might play a general role in vesicular transport.

**Summary**, from NCBI Gene [5877](https://www.ncbi.nlm.nih.gov/gene/5877):

> This gene encodes a member of the SCE4/YPT1/RAB family of small GTP-binding proteins that are involved in the regulation of intracellular vesicular transport. This protein stimulates GTP-GDP exchange in SEC4, and to a lesser extent in YPT1 and RAB3A, and may play a general role in vesicular transport. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:9797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9797) · Entrez [5877](https://www.ncbi.nlm.nih.gov/gene/5877) · UniProt [P47224](https://www.uniprot.org/uniprotkb/P47224) · Ensembl [ENSG00000183155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183155)

## Data

Gene col 11375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11375); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11375]; `tensor/DDL_lfc|DDL_z.npy` [11375]; `embed/gene_vectors.npy` [11375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11375 or target_col == 11375). Every well: [[RABIF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABIF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
