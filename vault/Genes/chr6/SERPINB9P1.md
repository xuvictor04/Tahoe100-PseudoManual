---
symbol: "SERPINB9P1"
type: "gene"
col: 13748
ensembl_id: "ENSG00000230438"
name: "serpin family B member 9 pseudogene 1"
location: "6p25.2"
module: 80
arm: "+"
pooled_cpm: 6.49
n_lines_expressing: 31
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# SERPINB9P1

*serpin family B member 9 pseudogene 1* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +11.7, q 6e-29, up in 18 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.476× (z -7.7, q 1e-11, down in 20 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIVEP2-DT]] (+0.65, fdr 1e-05), [[TRIM69]] (+0.63, fdr 2e-05), [[SIAH2-AS1]] (+0.63, fdr 5e-05); moves opposite to [[BRF1]] (-0.58, fdr 6e-05), [[FAM118A]] (-0.56, fdr 1e-04), [[BRAT1]] (-0.55, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[WFDC10B]] → it (grade B ⚠); 5 go from it, the strongest it → [[SPATS2L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +11.7 | 6e-29 | 18/26 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.3 | 7e-11 | 18/29 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.6 | 7e-09 | 3/18 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +6.5 | 1e-08 | 3/12 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +5.6 | 3e-06 | 10/27 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.0 | 5e-05 | 3/16 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.60×** | +4.6 | 3e-04 | 11/27 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.6 | 3e-04 | 10/28 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 0.001 | 14/27 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.003 | 13/24 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Acetohexamide (drug)]] 5 µM |  | 1.23× | +3.0 | 0.13 | 3/29 (HEC-1-A, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.476×** | -7.7 | 1e-11 | 20/29 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.489×** | -7.4 | 4e-11 | 22/29 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -6.9 | 7e-10 | 18/29 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.514×** | -6.9 | 8e-10 | 16/27 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.592×** | -5.4 | 7e-06 | 17/29 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -4.9 | 1e-04 | 14/27 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.633×** | -4.7 | 2e-04 | 18/29 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.639×** | -4.6 | 2e-04 | 18/24 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.452×** | -4.3 | 0.001 | 8/28 (SW1417, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.664×** | -4.2 | 0.001 | 14/26 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.664×** | -4.1 | 0.002 | 12/28 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.004 | 13/28 (PANC-1, AsPC-1, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.694×** | -3.8 | 0.007 | 7/29 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.700×** | -3.7 | 0.009 | 9/27 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.709×** | -3.6 | 0.014 | 9/29 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.021 | 11/28 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.724×** | -3.3 | 0.027 | 6/29 (A498, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.030 | 15/29 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.2) |
| [[A498 (line)]] | wt | 17.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -11.4) |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0978× (z -9.6) |
| [[J82 (line)]] | alt | 9.12 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -9.4) |
| [[SW480 (line)]] | alt | 7.39 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0894× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 3.94 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.0× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0782× (z -9.1) |
| [[LoVo (line)]] | wt | 3.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.55 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0665× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 9.74 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0799× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 6.71 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2-DT]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TRIM69]] | +0.63 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SIAH2-AS1]] | +0.63 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[LINC02068]] | +0.63 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[BCL10-AS1]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PKD1L1]] | +0.62 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ZFHX2-AS1]] | +0.62 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | +0.62 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[UBE2D3-AS1]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[LINC01829]] | +0.61 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[LINC00880]] | +0.60 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[PIPOX]] | +0.60 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRF1]] | -0.58 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[FAM118A]] | -0.56 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[BRAT1]] | -0.55 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.54 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[PRKRA]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[UBE2Q2P2]] | -0.53 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[TXNL4A]] | -0.53 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[BCKDHB]] | -0.53 | -0.37 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC10B]] | B | WFDC10B activity raises SERPINB9P1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without WFDC10B | 0.003 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[WFDC3]] | B | WFDC3 activity raises SERPINB9P1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without WFDC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[RBPMS]] | B | RBPMS activity raises SERPINB9P1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without RBPMS | 0.032 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[TOP2A]] | B | TOP2A activity lowers SERPINB9P1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZHX2]] | B | ZHX2 activity raises SERPINB9P1's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without ZHX2 | 0.047 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[MXRA5]] | B | MXRA5 activity raises SERPINB9P1's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 1.56× lower at baseline in the lines without MXRA5 | 0.051 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476 |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises SERPINB9P1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.83× lower at baseline in the lines without ZNF341-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[SLFN5]] | B | SLFN5 activity raises SERPINB9P1's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without SLFN5 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers SERPINB9P1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC02086]] | C | LINC02086 activity raises SERPINB9P1's level | lines that do not express LINC02086 (24) vs lines expressing it (26) | 2.92× lower at baseline in the lines without LINC02086 | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MIR4713HG, SERPINB9, PRSS3; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATS2L]] | B | SERPINB9P1 activity raises SPATS2L's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without SERPINB9P1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9 |
| [[C17orf67]] | B | SERPINB9P1 activity raises C17orf67's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without SERPINB9P1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9 |
| [[CEACAM16-AS1]] | B | SERPINB9P1 activity raises CEACAM16-AS1's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without SERPINB9P1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9 |
| [[LY6E-DT]] | B | SERPINB9P1 activity raises LY6E-DT's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without SERPINB9P1 | 0.084 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9 |
| [[LINC02086]] | C | SERPINB9P1 activity raises LINC02086's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 4.27× lower at baseline in the lines without SERPINB9P1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9; co-absent with the target |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, 11.9); signed map (22.8, -4.4). **Vector** length 66.6, 14.8% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.5 | -7.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.7 | -4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 9 pseudogene 1 |
| Locus type | pseudogene |
| Location | 6p25.2 — chr6:2,851,230-2,881,407 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MGC39372 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28590) · Entrez [221756](https://www.ncbi.nlm.nih.gov/gene/221756) · Ensembl [ENSG00000230438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230438)

## Data

Gene col 13748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13748); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13748]; `tensor/DDL_lfc|DDL_z.npy` [13748]; `embed/gene_vectors.npy` [13748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13748 or target_col == 13748). Every well: [[SERPINB9P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB9P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
