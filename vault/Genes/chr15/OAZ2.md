---
symbol: "OAZ2"
type: "gene"
col: 11096
ensembl_id: "ENSG00000180304"
name: "ornithine decarboxylase antizyme 2"
location: "15q22.31"
module: 29
arm: "+"
pooled_cpm: 26.2
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# OAZ2

*ornithine decarboxylase antizyme 2* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.98× (z +14.5, q 4e-45, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.193×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1B2]] (+0.58, fdr 3e-05), [[VWA5A]] (+0.58, fdr 3e-05), [[DCTN1]] (+0.57, fdr 2e-05); moves opposite to [[CDR2]] (-0.60, fdr 2e-05), [[SCLY]] (-0.58, fdr 3e-05), [[KCNJ14]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TUBA1A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +14.5 | 4e-45 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +13.7 | 4e-40 | 45/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +13.1 | 7e-37 | 43/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +11.8 | 7e-30 | 33/43 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +11.7 | 1e-29 | 39/48 (LoVo, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +9.4 | 3e-19 | 23/41 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +8.9 | 6e-17 | 23/35 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +8.0 | 6e-14 | 33/48 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.30×** | +8.0 | 1e-13 | 30/47 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +6.7 | 1e-09 | 25/48 (NCI-H460, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.4 | 6e-09 | 27/48 (hTERT-HPNE, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +6.3 | 1e-08 | 28/48 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **1.34×** | +6.3 | 2e-08 | 21/46 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 4e-07 | 21/48 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.4 | 3e-06 | 25/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +5.2 | 9e-06 | 20/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.001 | 8/48 (NCI-H2347, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.001 | 9/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 14/47 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.002 | 9/48 (A-172, BT-474, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.011 | 6/48 (SW480, HepG2/C3A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11096.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.193×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.859× | -3.2 | 0.66 | 7/48 (C32, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.20× (z +9.5) | — |
| [[A498 (line)]] | wt | 26.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +8.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1B2]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[VWA5A]] | +0.58 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[DCTN1]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CLSTN1]] | +0.56 | +0.28 / +0.60 | both halves | 3e-04 |  |
| [[ZMYM3]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MAPK3]] | +0.56 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[KIDINS220]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[GCOM1]] | +0.55 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[TMEM9]] | +0.54 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[DLD]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |
| [[FKBP8]] | +0.54 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[SLC44A2]] | +0.54 | +0.36 / +0.58 | both halves | 1e-04 | pathway: Metabolism of amino acids and derivatives |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDR2]] | -0.60 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[SCLY]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |
| [[KCNJ14]] | -0.57 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[MYO19]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[HIRA]] | -0.49 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[TOP3A]] | -0.48 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[TMEM11-DT]] | -0.48 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[ATR]] | -0.48 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[LIN52]] | -0.48 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[ANKMY1]] | -0.48 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[TMEM267]] | -0.48 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[ATP6V0A2]] | -0.47 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUBA1A]] | B | TUBA1A activity raises OAZ2's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.26× lower at baseline in the lines without TUBA1A | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.356). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.0, -10.3); signed map (-4.1, 17.0). **Vector** length 73.3, 12.9% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.2 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +8.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.6 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +5.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.7 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.2 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.2 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ornithine decarboxylase antizyme 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,687,573-64,703,281 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ornithine decarboxylase antizyme family |
| Reactome | 3 pathways, smallest: Regulation of ornithine decarboxylase (ODC); Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O95190](https://www.uniprot.org/uniprotkb/O95190) (Ornithine decarboxylase antizyme 2):

> Ornithine decarboxylase (ODC) antizyme protein that negatively regulates ODC activity and intracellular polyamine biosynthesis and uptake in response to increased intracellular polyamine levels. Binds to ODC monomers, inhibiting the assembly of the functional ODC homodimers. Does not target the ODC monomers for degradation, which allows a protein synthesis-independent restoration of ODC activity. Involved in the translocation of AZIN2 from ER-Golgi intermediate compartment (ERGIC) to the …

**Summary**, from NCBI Gene [4947](https://www.ncbi.nlm.nih.gov/gene/4947):

> The protein encoded by this gene belongs to the ornithine decarboxylase antizyme family, which plays a role in cell growth and proliferation by regulating intracellular polyamines. Expression of antizymes requires +1 ribosomal frameshifting, which is enhanced by high levels of polyamines. Antizymes in turn bind to and inhibit ornithine decarboxylase (ODC), the key enzyme in polyamine biosynthesis; thus, completing the auto-regulatory circuit. This gene encodes antizyme 2, the second member of …

**Accessions** — [HGNC:8096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8096) · Entrez [4947](https://www.ncbi.nlm.nih.gov/gene/4947) · UniProt [O95190](https://www.uniprot.org/uniprotkb/O95190) · Ensembl [ENSG00000180304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180304)

## Data

Gene col 11096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11096); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11096]; `tensor/DDL_lfc|DDL_z.npy` [11096]; `embed/gene_vectors.npy` [11096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11096 or target_col == 11096). Every well: [[OAZ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OAZ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
