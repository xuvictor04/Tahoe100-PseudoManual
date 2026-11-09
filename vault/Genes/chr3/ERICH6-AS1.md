---
symbol: "ERICH6-AS1"
type: "gene"
col: 14226
ensembl_id: "ENSG00000240137"
name: "ERICH6 antisense RNA 1"
location: "3q25.1"
module: 10
arm: "+"
pooled_cpm: 3.05
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ERICH6-AS1

*ERICH6 antisense RNA 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +8.2, q 2e-13, up in 14 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.626× (z -5.2, q 1e-04, down in 14 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.681× (z -4.2, q 0.004, down in 15 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00466]] (+0.61, fdr 1e-05), [[ID2-AS1]] (+0.59, fdr 1e-05), [[AGBL2]] (+0.59, fdr 3e-05); moves opposite to [[ATP6V0A2]] (-0.50, fdr 5e-05), [[AFG3L2]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CACNA1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +8.2 | 2e-13 | 14/29 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +7.9 | 1e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +7.6 | 4e-12 | 12/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +5.9 | 4e-07 | 13/37 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +5.6 | 2e-06 | 14/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +5.6 | 2e-06 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.5 | 3e-06 | 2/15 (HEC-1-A, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.3 | 0.001 | 10/46 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.40×** | +3.7 | 0.012 | 7/37 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.5 | 0.026 | 2/16 (LoVo, C-33 A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.035 | 4/43 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +3.3 | 0.049 | 2/43 (A498, C32) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.2 | 0.049 | 2/14 (A-427, SW480) | rises with dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.049 | 2/19 (NCI-H2030, A549) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.056 | 8/46 (J82, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.060 | 10/40 (A-427, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -5.2 | 1e-04 | 14/25 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.636×** | -5.0 | 2e-04 | 16/47 (PANC-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -4.2 | 0.004 | 15/39 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -4.1 | 0.005 | 8/23 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.718×** | -3.7 | 0.028 | 6/37 (SNU-423, SHP-77, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.721×** | -3.6 | 0.028 | 12/39 (HEC-1-A, NCI-H23, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.724×** | -3.6 | 0.028 | 8/47 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.5 | 0.028 | 11/47 (HepG2/C3A, COLO 205, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -3.5 | 0.031 | 10/45 (HepG2/C3A, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.734×** | -3.4 | 0.036 | 8/44 (SW 1271, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.736×** | -3.4 | 0.036 | 11/41 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.067 | 7/43 (NCI-H1573, SW48, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.757×** | -3.1 | 0.091 | 14/44 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0552× (z -9.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HEC-1-A (line)]] | alt | 2.93 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0701× (z -8.8) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 3.08 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0440× (z -8.7) ⚠ transcription drop |
| [[NCI-H1573 (line)]] | alt | 6.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0901× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.45 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 4.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0870× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00466]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ID2-AS1]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 | same gene group |
| [[AGBL2]] | +0.59 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[SSPOP]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[LRRC36]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FAM66C]] | +0.57 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[TMEM139-AS1]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 | same gene group |
| [[LINC02175]] | +0.53 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[DOC2A]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.52 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[CFL1P1-1]] | +0.52 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[JPH3]] | +0.52 | +0.48 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0A2]] | -0.50 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[AFG3L2]] | -0.43 | -0.29 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1B]] | B | CACNA1B activity raises ERICH6-AS1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.52× lower at baseline in the lines without CACNA1B | 0.024 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[MYT1]] | B | MYT1 activity raises ERICH6-AS1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.40× lower at baseline in the lines without MYT1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.6, 29.7); signed map (37.4, -8.2). **Vector** length 41.9, 4.65% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.9 | -0.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.9 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.5 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.4 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -1.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ERICH6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q25.1 — chr3:150,703,486-150,723,005 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41205) · Entrez [101928085](https://www.ncbi.nlm.nih.gov/gene/101928085) · Ensembl [ENSG00000240137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240137)

## Data

Gene col 14226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14226); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14226]; `tensor/DDL_lfc|DDL_z.npy` [14226]; `embed/gene_vectors.npy` [14226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14226 or target_col == 14226). Every well: [[ERICH6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERICH6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
