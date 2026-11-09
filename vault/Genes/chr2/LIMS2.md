---
symbol: "LIMS2"
type: "gene"
col: 1009
ensembl_id: "ENSG00000072163"
name: "LIM zinc finger domain containing 2"
location: "2q14.3"
module: 35
arm: "+"
pooled_cpm: 2.78
n_lines_expressing: 33
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# LIMS2

*LIM zinc finger domain containing 2* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.81× (z +10.6, q 3e-23, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +9.0, q 6e-17, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.506× (z -5.6, q 9e-06, down in 13 of 27 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.597× (z -4.3, q 0.002, down in 10 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0380×, A-172 0.0976×; ⚠ cell-cycle shift, explains ~91% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.114×, MIA PaCa-2 0.0844×; ⚠ cell-cycle shift, explains ~65% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (A-172 0.170×, MIA PaCa-2 0.127×; ⚠ cell-cycle shift, explains ~89% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (SW480 0.0612×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALM]] (+0.58, fdr 1e-05), [[TMEM72-AS1]] (+0.54, fdr 5e-05), [[DYSF]] (+0.54, fdr 3e-05); moves opposite to [[HS2ST1]] (-0.47, fdr 3e-05), [[KIAA1958]] (-0.46, fdr 1e-04), [[TXNDC17]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[SYNC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +10.6 | 3e-23 | 2/6 (HT-29, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +9.0 | 6e-17 | 10/21 (A498, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +8.8 | 3e-16 | 2/7 (HT-29, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +7.5 | 6e-12 | 9/23 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +6.6 | 4e-09 | 4/14 (HT-29, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.56×** | +5.1 | 3e-05 | 4/26 (LoVo, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +4.6 | 3e-04 | 4/23 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.4 | 6e-04 | 1/14 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.64×** | +4.1 | 0.003 | 5/23 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.62×** | +4.0 | 0.004 | 3/16 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.013 | 8/21 (NCI-H460, A-172, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.015 | 3/20 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.019 | 4/25 (NCI-H460, A-172, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.019 | 1/17 (A498) | inconsistent across doses |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.57×** | +3.3 | 0.031 | 1/17 (NCI-H460) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.035 | 0/20 | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.035 | 3/21 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.056 | 1/27 (RPMI-7951) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.072 | 5/23 (NCI-H460, HS-578T, …) | two highest doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1009.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0380×, A-172 0.0976×; ⚠ cell-cycle shift, explains ~91% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.114×, MIA PaCa-2 0.0844×; ⚠ cell-cycle shift, explains ~65% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (A-172 0.170×, MIA PaCa-2 0.127×; ⚠ cell-cycle shift, explains ~89% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (SW480 0.0612×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.506×** | -5.6 | 9e-06 | 13/27 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.513×** | -5.5 | 9e-06 | 15/27 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.527×** | -5.3 | 2e-05 | 15/23 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.574×** | -4.6 | 6e-04 | 9/27 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.597×** | -4.3 | 0.002 | 10/27 (A-172, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.598×** | -4.3 | 0.002 | 12/24 (A-172, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.643×** | -3.7 | 0.020 | 10/28 (MIA PaCa-2, A-172, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.658×** | -3.5 | 0.037 | 12/22 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.667×** | -3.4 | 0.050 | 18/25 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.774× | -3.0 | 0.15 | 6/24 (A498, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 9.25 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0380× (z -13.6) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A-172 (line)]] | wt | 28.7 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0976× (z -12.5) ⚠ cell-cycle shift, explains ~91% of this change |
| [[NCI-H460 (line)]] | wt | 2.80 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0656× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 5.77 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0459× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 2.27 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0612× (z -9.3) |
| [[A-427 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.868 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.404 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALM]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TMEM72-AS1]] | +0.54 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[DYSF]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SORBS3]] | +0.54 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[RUSC1-AS1]] | +0.53 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[TEK]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[CCDC3]] | +0.52 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ANXA8]] | +0.52 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[MRAS]] | +0.52 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[LINC00863]] | +0.51 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[TBKBP1]] | +0.51 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[PARP3]] | +0.50 | +0.45 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS2ST1]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[KIAA1958]] | -0.46 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[TXNDC17]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ATP5MC1]] | -0.43 | -0.28 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LIMS2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC2A9]] | B | SLC2A9 activity lowers LIMS2's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.89× higher at baseline in the lines without SLC2A9 | 0.097 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNC]] | B | LIMS2 activity raises SYNC's level | lines that do not express LIMS2 (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without LIMS2 | 0.047 | ⚠ within organs, on part of the lines; also absent: PALM, FHL1, ZNF469 |
| [[HVCN1]] | B | LIMS2 activity raises HVCN1's level | lines that do not express LIMS2 (17) vs lines expressing it (33) | 1.42× lower at baseline in the lines without LIMS2 | 0.062 | ⚠ within organs, on part of the lines; also absent: PALM, FHL1, ZNF469 |
| [[BMP1]] | B | LIMS2 activity raises BMP1's level | lines that do not express LIMS2 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without LIMS2 | 0.097 | ⚠ within organs, on part of the lines; also absent: PALM, FHL1, ZNF469 |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (16.5, 14.3); signed map (25.2, 10.6). **Vector** length 49.6, 9.72% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.3 | -5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -1.7 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.5 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.5 | -5.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | LIM zinc finger domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,638,381-127,681,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PINCH2, PINCH-2 |
| Gene groups (HGNC) | LIMS zinc finger family; ILK-PINCH-Parvin complex subunits |
| Reactome | 3 pathways, smallest: Cell-extracellular matrix interactions; Cell junction organization; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4I7](https://www.uniprot.org/uniprotkb/Q7Z4I7) (LIM and senescent cell antigen-like-containing domain protein 2):

> Adapter protein in a cytoplasmic complex linking beta-integrins to the actin cytoskeleton, bridges the complex to cell surface receptor tyrosine kinases and growth factor receptors. Plays a role in modulating cell spreading and migration.

**Summary**, from NCBI Gene [55679](https://www.ncbi.nlm.nih.gov/gene/55679):

> This gene encodes a member of a small family of focal adhesion proteins which interacts with ILK (integrin-linked kinase), a protein which effects protein-protein interactions with the extraceullar matrix. The encoded protein has five LIM domains, each domain forming two zinc fingers, which permit interactions which regulate cell shape and migration. A pseudogene of this gene is located on chromosome 4. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:16084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16084) · Entrez [55679](https://www.ncbi.nlm.nih.gov/gene/55679) · UniProt [Q7Z4I7](https://www.uniprot.org/uniprotkb/Q7Z4I7) · Ensembl [ENSG00000072163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072163)

## Data

Gene col 1009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1009); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1009]; `tensor/DDL_lfc|DDL_z.npy` [1009]; `embed/gene_vectors.npy` [1009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1009 or target_col == 1009). Every well: [[LIMS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
