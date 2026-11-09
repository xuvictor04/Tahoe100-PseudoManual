---
symbol: "EID2B"
type: "gene"
col: 10713
ensembl_id: "ENSG00000176401"
name: "EP300 interacting inhibitor of differentiation 2B"
location: "19q13.2"
module: 178
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 37
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 24
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# EID2B

*EP300 interacting inhibitor of differentiation 2B* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.67× (z +10.7, q 9e-24, up in 14 of 14 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.41× (z +7.5, q 2e-11, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Berberine (chloride hydrate) (drug)]] 5 µM: 0.732× (z -3.8, q 0.092, down in 7 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 5 µM in 1 line (A-172 0.0766×); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.410×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.345×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53TG1]] (+0.73, fdr 1e-05), [[PRMT9]] (+0.69, fdr 1e-05), [[MINCR]] (+0.65, fdr 3e-05); moves opposite to [[NPIPB4]] (-0.61, fdr 4e-05), [[DOCK1]] (-0.57, fdr 4e-05), [[ELK4]] (-0.57, fdr 3e-05).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DLL3]] → it (grade B ⚠); 24 go from it, the strongest it → [[MHENCR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.67×** | +10.7 | 9e-24 | 14/14 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +7.5 | 2e-11 | 21/32 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.32×** | +6.9 | 1e-09 | 0/3 | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +6.7 | 3e-09 | 4/5 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +6.4 | 2e-08 | 15/32 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +6.2 | 4e-08 | 13/33 (A-427, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.90×** | +5.5 | 3e-06 | 15/34 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.75×** | +4.8 | 1e-04 | 4/17 (A549, SHP-77, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +4.3 | 0.001 | 7/24 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +4.1 | 0.002 | 7/34 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.3 | 0.055 | 3/27 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +3.2 | 0.056 | 5/23 (PANC-1, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10713.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 5 µM in 1 line (A-172 0.0766×); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.410×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.345×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.732×** | -3.8 | 0.092 | 7/34 (hTERT-HPNE, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.698× | -3.1 | 0.61 | 8/34 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.60× (z +10.3) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -8.9) |
| [[A-172 (line)]] | wt | 6.07 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0766× (z -10.5) |
| [[A-427 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53TG1]] | +0.73 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.69 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[MINCR]] | +0.65 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[FAM182B]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.64 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | +0.64 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[C12orf76]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CLN8-AS1]] | +0.62 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[MHENCR]] | +0.62 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[MED17]] | +0.62 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[KIAA2013]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB4]] | -0.61 | -0.40 / -0.60 | both halves | 4e-05 |  |
| [[DOCK1]] | -0.57 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ELK4]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NUP188]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[DESI1]] | -0.55 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[PIEZO1]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[NEK10]] | -0.54 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[THOC6]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NPIPB5]] | -0.53 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[CYFIP1]] | -0.53 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[RBM19]] | -0.53 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLL3]] | B | DLL3 activity raises EID2B's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without DLL3 | 0.026 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[HDAC6]] | B | HDAC6 activity lowers EID2B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 24, C 0. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MHENCR]] | B | EID2B activity raises MHENCR's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without EID2B | 0.006 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[PEPD]] | B | EID2B activity raises PEPD's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without EID2B | 0.010 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[ZNF232-AS1]] | B | EID2B activity raises ZNF232-AS1's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without EID2B | 0.010 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[ZFAND2A-DT]] | B | EID2B activity raises ZFAND2A-DT's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without EID2B | 0.011 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[WRAP53]] | B | EID2B activity raises WRAP53's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without EID2B | 0.012 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[FAM182B]] | B | EID2B activity raises FAM182B's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without EID2B | 0.023 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[FAM229B]] | B | EID2B activity raises FAM229B's level | lines that do not express EID2B (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without EID2B | 0.030 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | EID2B activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express EID2B (13) vs lines expressing it (35) | the lines without EID2B: 1.27× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[MALSU1]] | B | EID2B activity raises MALSU1's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without EID2B | 0.036 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[FAM104B]] | B | EID2B activity raises FAM104B's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without EID2B | 0.040 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[TRIM7-AS2]] | B | EID2B activity raises TRIM7-AS2's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without EID2B | 0.042 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[ZNF358]] | B | EID2B activity raises ZNF358's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without EID2B | 0.055 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.6, -10.3); signed map (-30.2, -10.4). **Vector** length 39.8, 5.86% of its response variance represented; |z| ≥ 3 in 532 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +10.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -1.2 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | +2.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Cinacalcet (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | EP300 interacting inhibitor of differentiation 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,530,987-39,532,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EID-3, FLJ38944 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D98](https://www.uniprot.org/uniprotkb/Q96D98) (EP300-interacting inhibitor of differentiation 2B):

> Acts as a repressor of MYOD-dependent transcription, glucocorticoid receptor-dependent transcription, and muscle differentiation.

**Summary**, from NCBI Gene [126272](https://www.ncbi.nlm.nih.gov/gene/126272):

> Enables identical protein binding activity. Involved in negative regulation of DNA-templated transcription and negative regulation of myoblast differentiation. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26796) · Entrez [126272](https://www.ncbi.nlm.nih.gov/gene/126272) · UniProt [Q96D98](https://www.uniprot.org/uniprotkb/Q96D98) · Ensembl [ENSG00000176401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176401)

## Data

Gene col 10713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10713); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10713]; `tensor/DDL_lfc|DDL_z.npy` [10713]; `embed/gene_vectors.npy` [10713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10713 or target_col == 10713). Every well: [[EID2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EID2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
