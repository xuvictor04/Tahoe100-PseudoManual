---
symbol: "ZXDA"
type: "gene"
col: 12553
ensembl_id: "ENSG00000198205"
name: "zinc finger X-linked duplicated A"
location: "Xp11.21"
module: 135
arm: "+"
pooled_cpm: 3.0
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# ZXDA

*zinc finger X-linked duplicated A* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +6.1, q 5e-07, up in 20 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.228× (z -15.0, q 0e+00, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZXDB]] (+0.88, fdr 7e-06), [[ZNF181]] (+0.76, fdr 1e-05), [[ZNF747]] (+0.74, fdr 2e-05); moves opposite to [[PCMT1]] (-0.72, fdr 4e-05), [[SH3GL1]] (-0.70, fdr 2e-05), [[AP1S1]] (-0.70, fdr 7e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C1QL1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CCT6P3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +6.1 | 5e-07 | 20/32 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +5.1 | 1e-04 | 12/29 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.2 | 0.004 | 6/29 (SW1417, SHP-77, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.007 | 7/38 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.010 | 4/42 (BT-474, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.010 | 8/41 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +3.8 | 0.010 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.044 | 6/35 (SW480, A549, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.100 | 2/42 (NCI-H1573, A-427) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.23× | +3.0 | 0.13 | 5/41 (A-172, SW480, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.228×** | -15.0 | 0e+00 | 36/41 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.249×** | -14.1 | 1e-42 | 36/42 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.264×** | -13.5 | 3e-39 | 33/40 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.427×** | -8.6 | 1e-15 | 26/42 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.520×** | -6.6 | 4e-09 | 18/27 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.851× | -5.3 | 9e-06 | 21/43 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.636×** | -4.6 | 4e-04 | 15/34 (NCI-H23, A-427, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.649×** | -4.4 | 9e-04 | 15/42 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.642×** | -4.3 | 0.001 | 8/32 (A-172, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.459×** | -4.1 | 0.002 | 8/37 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -4.1 | 0.002 | 10/41 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.004 | 14/41 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.671×** | -3.9 | 0.005 | 8/20 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.692×** | -3.7 | 0.008 | 8/41 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.723×** | -3.3 | 0.041 | 17/38 (NCI-H460, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.729×** | -3.2 | 0.053 | 8/40 (A549, NCI-H460, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.727×** | -3.1 | 0.063 | 3/40 (C-33 A, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 6.50 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0804× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 5.05 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.193× (z -9.7) |
| [[LoVo (line)]] | wt | 2.42 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0671× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0911× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 4.56 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0455× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Oxaprozin (drug)]] 0.5 µM 0.0794× (z -8.7) |
| [[SW1417 (line)]] | alt | 2.83 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0333× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0348× (z -10.0) |
| [[SW480 (line)]] | alt | 2.80 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0879× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 3.78 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0662× (z -9.2) |
| [[A498 (line)]] | wt | 3.73 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0655× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0339× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 6.16 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.154 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.165 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | +0.88 | +0.84 / +0.79 | both halves | 7e-06 | same gene group |
| [[ZNF181]] | +0.76 | +0.72 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF747]] | +0.74 | +0.70 / +0.48 | both halves | 2e-05 | same gene group |
| [[ARL14EP]] | +0.74 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[POLR2M]] | +0.74 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ZNF391]] | +0.72 | +0.67 / +0.57 | both halves | 1e-05 | same gene group |
| [[C19orf54]] | +0.72 | +0.70 / +0.37 | both halves | 9e-05 |  |
| [[KICS2]] | +0.72 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[ZNF773]] | +0.72 | +0.68 / +0.44 | both halves | 3e-05 | same gene group |
| [[RIMOC1]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[MTHFSD]] | +0.71 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PEF1]] | +0.70 | +0.65 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.72 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[SH3GL1]] | -0.70 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[AP1S1]] | -0.70 | -0.70 / -0.37 | both halves | 7e-05 |  |
| [[METRN]] | -0.70 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.69 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[AP2S1]] | -0.69 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[COX6A1]] | -0.67 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[UQCRH]] | -0.67 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[ANAPC11]] | -0.67 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[KYAT1]] | -0.66 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.66 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[IGSF8]] | -0.66 | -0.57 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1QL1]] | B | C1QL1 activity raises ZXDA's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without C1QL1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[SYNE1]] | B | SYNE1 activity lowers ZXDA's level | lines that do not express SYNE1 (10) vs lines expressing it (40) | 1.35× higher at baseline in the lines without SYNE1 | 0.098 | ⚠ within organs, on part of the lines; also absent: DPYS, SGCE, SPX |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCT6P3]] | C | ZXDA activity raises CCT6P3's level | lines that do not express ZXDA (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without ZXDA | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MBOAT2; its own permutation p |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-17.9, 7.7); signed map (8.9, -28.9). **Vector** length 55.4, 7.66% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.0 | -15.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.8 | -14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -13.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -8.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.7 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger X-linked duplicated A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:57,905,430-57,910,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF896 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P98168](https://www.uniprot.org/uniprotkb/P98168) (Zinc finger X-linked protein ZXDA):

> Cooperates with CIITA to promote transcription of MHC class I and MHC class II genes.

**Summary**, from NCBI Gene [7789](https://www.ncbi.nlm.nih.gov/gene/7789):

> This gene encodes one of two duplicated zinc finger genes on chromosome Xp11. This gene is the telomeric copy; GeneID 158586 ZXDB is the more centromeric copy. The two genes have 98% nucleotide sequence similarity, and the predicted proteins contain 10 tandem zinc finger motifs. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:13198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13198) · Entrez [7789](https://www.ncbi.nlm.nih.gov/gene/7789) · UniProt [P98168](https://www.uniprot.org/uniprotkb/P98168) · Ensembl [ENSG00000198205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198205)

## Data

Gene col 12553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12553); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12553]; `tensor/DDL_lfc|DDL_z.npy` [12553]; `embed/gene_vectors.npy` [12553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12553 or target_col == 12553). Every well: [[ZXDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZXDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
