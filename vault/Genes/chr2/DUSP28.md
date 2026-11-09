---
symbol: "DUSP28"
type: "gene"
col: 12021
ensembl_id: "ENSG00000188542"
name: "dual specificity phosphatase 28"
location: "2q37.3"
module: 35
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# DUSP28

*dual specificity phosphatase 28* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +16.8, q 0e+00, up in 33 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.851× (z -7.1, q 8e-10, down in 16 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.645× (z -5.6, q 8e-06, down in 16 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALY-AS1]] (+0.71, fdr 7e-06), [[USP34-DT]] (+0.68, fdr 1e-05), [[CPEB2-DT]] (+0.68, fdr 2e-05); moves opposite to [[PARP1]] (-0.55, fdr 2e-04), [[SHROOM2]] (-0.53, fdr 1e-04), [[SORT1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +16.8 | 0e+00 | 33/36 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +8.7 | 1e-15 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +8.5 | 5e-15 | 14/34 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +7.9 | 4e-13 | 4/8 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +7.6 | 3e-12 | 14/45 (A-172, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.9 | 4e-10 | 8/24 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.89×** | +5.8 | 4e-07 | 7/23 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +5.7 | 8e-07 | 12/36 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.7 | 8e-07 | 7/20 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.9 | 6e-05 | 9/30 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.8 | 9e-05 | 4/20 (SK-MEL-2, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.3 | 8e-04 | 7/42 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 6/43 (H4, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.010 | 6/34 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.061 | 7/42 (SW480, A-172, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.068 | 0/41 | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12021.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.851× | -7.1 | 8e-10 | 16/47 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -5.6 | 8e-06 | 16/43 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.665×** | -5.2 | 4e-05 | 15/46 (C-33 A, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -4.7 | 3e-04 | 13/41 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.755×** | -3.6 | 0.041 | 10/42 (NCI-H1573, SNU-423, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -3.5 | 0.041 | 6/45 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.775×** | -3.2 | 0.091 | 12/43 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.775×** | -3.2 | 0.091 | 7/45 (A-427, SW 1271, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.623× | -3.1 | 0.10 | 9/35 (HOP62, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.74 | 0 | 2 | — | [[Erlotinib (drug)]] 5 µM 0.0763× (z -8.9) |
| [[HOP62 (line)]] | alt | 3.36 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (drug)]] 0.05 µM 0.0763× (z -9.1) |
| [[KATO III (line)]] | alt | 4.68 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.0957× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 8.00 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.117× (z -9.1) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 2.92 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0803× (z -8.5) |
| [[SW 900 (line)]] | alt | 5.00 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0765× (z -8.8) |
| [[A-427 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALY-AS1]] | +0.71 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[USP34-DT]] | +0.68 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SPATA1]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[LINC00863]] | +0.65 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[C14orf28]] | +0.65 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[GSK3B-DT]] | +0.65 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PTPN23-DT]] | +0.65 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CCT6B]] | +0.65 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[ZNF213-AS1]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.65 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LCA5L]] | +0.64 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP1]] | -0.55 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[SHROOM2]] | -0.53 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[SORT1]] | -0.53 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DUSP28's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TOP2A]] | B | TOP2A activity lowers DUSP28's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01829]] | C | LINC01829 activity raises DUSP28's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 1.45× lower at baseline in the lines without LINC01829 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.3, 21.1); signed map (28.9, -2.9). **Vector** length 48.4, 5.53% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +16.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +5.8 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.6 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.2 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -2.1 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,560,054-240,565,256 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VHP, DUSP26 |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0W2](https://www.uniprot.org/uniprotkb/Q4G0W2) (Dual specificity phosphatase 28):

> Has phosphatase activity with the synthetic substrate 6,8-difluoro-4-methylumbelliferyl phosphate (in vitro). Has almost no detectable activity with phosphotyrosine, even less activity with phosphothreonine and displays complete lack of activity with phosphoserine. The poor activity with phosphotyrosine may be due to steric hindrance by bulky amino acid sidechains that obstruct access to the active site.

**Summary**, from NCBI Gene [285193](https://www.ncbi.nlm.nih.gov/gene/285193):

> Enables phosphatase activity. Involved in dephosphorylation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33237) · Entrez [285193](https://www.ncbi.nlm.nih.gov/gene/285193) · UniProt [Q4G0W2](https://www.uniprot.org/uniprotkb/Q4G0W2) · Ensembl [ENSG00000188542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188542)

## Data

Gene col 12021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12021); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12021]; `tensor/DDL_lfc|DDL_z.npy` [12021]; `embed/gene_vectors.npy` [12021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12021 or target_col == 12021). Every well: [[DUSP28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
