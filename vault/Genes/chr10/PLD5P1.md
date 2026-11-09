---
symbol: "PLD5P1"
type: "gene"
col: 16042
ensembl_id: "ENSG00000283930"
name: "PLD5 pseudogene 1"
location: "10p11.1"
module: 37
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PLD5P1

*PLD5 pseudogene 1* — 10p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +14.0, q 8e-42, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.562× (z -7.7, q 6e-12, down in 23 of 45 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.639× (z -6.2, q 1e-07, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (SNU-1 0.0982×; ⚠ cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.294×; ⚠ cell-cycle shift, would explain all of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SW480 0.129×); [[Drospirenone (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0775×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR49]] (+0.73, fdr 7e-06), [[NPHP3-ACAD11]] (+0.70, fdr 1e-05), [[PXDNL]] (+0.70, fdr 1e-05); moves opposite to [[WDR7]] (-0.60, fdr 2e-04), [[COMMD2]] (-0.56, fdr 2e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KAZN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +14.0 | 8e-42 | 34/43 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.0 | 3e-13 | 22/42 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.6 | 7e-09 | 19/43 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.1 | 2e-07 | 17/45 (A-172, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.8 | 8e-07 | 7/19 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.80×** | +4.3 | 0.001 | 6/44 (NCI-H23, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.003 | 6/47 (HOP62, LS 180, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.018 | 3/47 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.067 | 2/45 (NCI-H2030, C32) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.067 | 12/45 (SW48, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16042.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (SNU-1 0.0982×; ⚠ cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.294×; ⚠ cell-cycle shift, would explain all of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SW480 0.129×); [[Drospirenone (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0775×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.562×** | -7.7 | 6e-12 | 23/45 (SNU-1, HOP62, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -6.2 | 1e-07 | 22/46 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.666×** | -5.7 | 3e-06 | 18/47 (NCI-H460, BT-474, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.714×** | -4.7 | 4e-04 | 15/47 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.791×** | -4.6 | 5e-04 | 19/43 (SNU-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.741×** | -4.2 | 0.002 | 13/41 (SNU-1, SW48, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.741×** | -4.2 | 0.002 | 12/47 (hTERT-HPNE, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.750×** | -4.0 | 0.004 | 14/42 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.750×** | -4.0 | 0.004 | 13/45 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.788×** | -3.3 | 0.051 | 15/44 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.052 | 10/45 (SHP-77, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | 0.660× | -3.0 | 0.11 | 5/40 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 76.7 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0982× (z -15.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 21.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 8.85 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 8.84 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +10.5) | — |
| [[A498 (line)]] | wt | 4.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 6.35 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0775× (z -10.0) |
| [[SW480 (line)]] | alt | 5.38 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.129× (z -10.8) |
| [[A-172 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR49]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[NPHP3-ACAD11]] | +0.70 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[PXDNL]] | +0.70 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.69 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LINC01482]] | +0.69 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[LINC02680]] | +0.69 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SNX31]] | +0.66 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[FRZB]] | +0.66 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[APTX]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[DRC1]] | +0.65 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CCDC62]] | +0.64 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.60 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[COMMD2]] | -0.56 | -0.31 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KAZN]] | B | KAZN activity raises PLD5P1's level | lines that do not express KAZN (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without KAZN | 0.048 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PLD5P1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LYG1]] | B | LYG1 activity raises PLD5P1's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without LYG1 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PLD5P1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, -16.7); signed map (12.7, 3.7). **Vector** length 62.1, 8.51% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +14.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +5.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.0 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.3 | -7.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.7 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.3 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | PLD5 pseudogene 1 |
| Locus type | pseudogene |
| Location | 10p11.1 — chr10:38,094,368-38,360,098 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100420618](https://www.ncbi.nlm.nih.gov/gene/100420618):

> Predicted to be involved in regulation of DNA-templated transcription. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:55072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55072) · Entrez [100420618](https://www.ncbi.nlm.nih.gov/gene/100420618) · Ensembl [ENSG00000283930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283930)

## Data

Gene col 16042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16042); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16042]; `tensor/DDL_lfc|DDL_z.npy` [16042]; `embed/gene_vectors.npy` [16042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16042 or target_col == 16042). Every well: [[PLD5P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLD5P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
